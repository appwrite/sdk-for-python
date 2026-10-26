"""End-to-end checks against a real local server over real sockets.

The unit suite mocks at the transport layer, so it never exercises TCP, TLS,
keep-alive or real concurrency. These tests drive the SDK against a real
HTTP(S) server bound to 127.0.0.1 and assert on what actually went over the wire.
"""

import asyncio
import hashlib
import json
import shutil
import ssl
import subprocess
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from appwrite.client import Client
from appwrite.exception import AppwriteException
from appwrite.input_file import InputFile
from appwrite.services.storage import Storage


class _State:
    """Thread-safe counters describing what the server actually observed."""

    def __init__(self):
        self.lock = threading.Lock()
        self.reset()

    def reset(self):
        self.connections = 0
        self.requests = 0
        self.in_flight = 0
        self.peak_in_flight = 0
        self.chunks = []
        self.chunk_size = 0
        self.expected_total = 0
        self.file_id = 'file-1'

    def enter(self):
        with self.lock:
            self.in_flight += 1
            self.requests += 1
            self.peak_in_flight = max(self.peak_in_flight, self.in_flight)

    def leave(self):
        with self.lock:
            self.in_flight -= 1

    def record_chunk(self, index, payload, content_range, upload_id):
        with self.lock:
            self.chunks.append(
                {
                    'index': index,
                    'payload': payload,
                    'content_range': content_range,
                    'upload_id': upload_id,
                }
            )


def _multipart_parts(body, content_type):
    """Split a raw multipart body into (headers, payload) pairs."""
    boundary = None
    for piece in content_type.split(';')[1:]:
        key, _, value = piece.strip().partition('=')
        if key.lower() == 'boundary':
            boundary = value.strip('"')
    if not boundary:
        return []

    marker = ('--' + boundary).encode()
    parts = []
    for raw in body.split(marker)[1:]:
        if raw.startswith(b'--'):
            break
        if raw.startswith(b'\r\n'):
            raw = raw[2:]
        head, _, payload = raw.partition(b'\r\n\r\n')
        if payload.endswith(b'\r\n'):
            payload = payload[:-2]
        parts.append((head, payload))
    return parts


def _build_handler(state):
    class Handler(BaseHTTPRequestHandler):
        protocol_version = 'HTTP/1.1'

        def setup(self):
            super().setup()
            with state.lock:
                state.connections += 1
            self.connection_id = state.connections

        def log_message(self, *args):
            pass

        def _read_body(self):
            length = int(self.headers.get('Content-Length') or 0)
            return self.rfile.read(length) if length else b''

        def _send(self, status, body=b'', content_type='application/json', extra=None):
            if isinstance(body, str):
                body = body.encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(body)))
            for key, value in (extra or {}).items():
                self.send_header(key, value)
            self.end_headers()
            if body:
                self.wfile.write(body)

        def _send_json(self, status, payload, extra=None):
            self._send(status, json.dumps(payload), 'application/json', extra)

        def _route(self, path, query, body):
            if path == '/slow':
                time.sleep(float(query.get('delay', ['0.25'])[0]))
                self._send_json(200, {'ok': True, 'connection': self.connection_id})
                return

            if path == '/echo':
                parts = _multipart_parts(body, self.headers.get('Content-Type', ''))
                file_parts = [payload for head, payload in parts if b'filename=' in head]
                self._send_json(
                    200,
                    {
                        'method': self.command,
                        'path': path,
                        'query': query,
                        'body_len': len(body),
                        'body_text': body.decode('utf-8', 'replace'),
                        'body_sha256': hashlib.sha256(body).hexdigest(),
                        'content_range': self.headers.get('content-range'),
                        'x_appwrite_id': self.headers.get('x-appwrite-id'),
                        'file_sha256': hashlib.sha256(file_parts[0]).hexdigest() if file_parts else None,
                        'file_len': len(file_parts[0]) if file_parts else 0,
                    },
                )
                return

            if path == '/error':
                self._send_json(404, {'message': 'Resource not found', 'type': 'not_found', 'code': 404})
                return

            if path == '/text':
                self._send(200, 'plain text body', 'text/plain')
                return

            if path == '/binary':
                self._send(200, bytes(range(256)), 'application/octet-stream')
                return

            if path == '/location':
                self._send_json(200, {'ok': True}, {'Location': 'https://example.com/redirected'})
                return

            if path == '/redirect':
                self._send(302, b'', 'text/plain', {'Location': '/echo'})
                return

            if self.command == 'GET':
                # Resume probe for a chunked upload.
                total = (state.expected_total + state.chunk_size - 1) // max(state.chunk_size, 1)
                self._send_json(200, {'$id': state.file_id, 'chunksTotal': total, 'chunksUploaded': 0})
                return

            # Chunk upload.
            content_range = self.headers.get('content-range')
            start = int(content_range.split(' ')[1].split('-')[0]) if content_range else 0
            index = start // state.chunk_size if state.chunk_size else 0
            parts = _multipart_parts(body, self.headers.get('Content-Type', ''))
            file_parts = [payload for head, payload in parts if b'filename=' in head]
            state.record_chunk(
                index,
                file_parts[0] if file_parts else b'',
                content_range,
                self.headers.get('x-appwrite-id'),
            )

            total_chunks = (state.expected_total + state.chunk_size - 1) // max(state.chunk_size, 1)
            self._send_json(
                200,
                {
                    '$id': state.file_id,
                    'chunksTotal': total_chunks,
                    'chunksUploaded': len({chunk['index'] for chunk in state.chunks}),
                },
            )

        def _handle(self):
            parsed = urlparse(self.path)
            body = self._read_body()
            state.enter()
            try:
                self._route(parsed.path, parse_qs(parsed.query), body)
            finally:
                state.leave()

        do_GET = _handle
        do_POST = _handle
        do_PUT = _handle
        do_DELETE = _handle
        do_PATCH = _handle

    return Handler


class _Server:
    def __init__(self, tls=False):
        self.state = _State()
        self.httpd = ThreadingHTTPServer(('127.0.0.1', 0), _build_handler(self.state))
        self.httpd.daemon_threads = True
        self.certdir = None
        if tls:
            self.certdir = tempfile.mkdtemp(prefix='appwrite-tls-')
            self._make_cert()
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(self.certdir + '/cert.pem', self.certdir + '/key.pem')
            self.httpd.socket = context.wrap_socket(self.httpd.socket, server_side=True)
        self.port = self.httpd.server_address[1]
        self.scheme = 'https' if tls else 'http'
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def _make_cert(self):
        subprocess.run(
            [
                'openssl',
                'req',
                '-x509',
                '-newkey',
                'rsa:2048',
                '-keyout',
                self.certdir + '/key.pem',
                '-out',
                self.certdir + '/cert.pem',
                '-days',
                '1',
                '-nodes',
                '-subj',
                '/CN=localhost',
            ],
            check=True,
            capture_output=True,
        )

    @property
    def endpoint(self):
        return f'{self.scheme}://localhost:{self.port}'

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        if self.certdir:
            shutil.rmtree(self.certdir, ignore_errors=True)


class _LiveServerTest(unittest.IsolatedAsyncioTestCase):
    server = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.server = _Server()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.server.close()

    async def asyncSetUp(self):
        self.client = Client()
        self.client.set_endpoint(self.server.endpoint)
        self.state = self.server.state

    async def asyncTearDown(self):
        await self.client.aclose()


class TestRealRequests(_LiveServerTest):
    async def test_request_round_trips_over_a_real_socket(self):
        response = await self.client.call('get', '/echo', {}, {'probe': 'yes'})

        self.assertEqual(response['method'], 'GET')
        self.assertEqual(response['path'], '/echo')
        self.assertEqual(response['query'], {'probe': ['yes']})
        self.assertGreater(self.state.connections, 0)

    async def test_json_body_is_sent_and_parsed(self):
        body = {'name': 'Walter', 'active': True}
        response = await self.client.call('post', '/echo', {'content-type': 'application/json'}, body)

        self.assertEqual(response['method'], 'POST')
        self.assertEqual(response['body_text'], json.dumps(body))

    async def test_multipart_file_bytes_reach_the_server_intact(self):
        payload = b'\x00\x01\x02binary\xff' * 100
        response = await self.client.call(
            'post',
            '/echo',
            {'content-type': 'multipart/form-data'},
            {'file': InputFile.from_bytes(payload, 'blob.bin'), 'name': 'blob'},
        )

        self.assertEqual(response['file_len'], len(payload))
        self.assertEqual(response['file_sha256'], hashlib.sha256(payload).hexdigest())

    async def test_binary_response_is_returned_as_bytes(self):
        response = await self.client.call('get', '/binary')

        self.assertIsInstance(response, bytes)
        self.assertEqual(response, bytes(range(256)))

    async def test_text_response_is_decoded(self):
        response = await self.client.call('get', '/text', response_type='text')

        self.assertEqual(response, 'plain text body')

    async def test_location_response_type_returns_the_header(self):
        response = await self.client.call('get', '/location', response_type='location')

        self.assertEqual(response, 'https://example.com/redirected')

    async def test_error_response_raises_appwrite_exception(self):
        with self.assertRaises(AppwriteException) as context:
            await self.client.call('get', '/error')

        self.assertEqual(context.exception.code, 404)
        self.assertEqual(context.exception.message, 'Resource not found')
        self.assertEqual(context.exception.type, 'not_found')

    async def test_connection_refused_is_wrapped_in_appwrite_exception(self):
        client = Client()
        client.set_endpoint('http://127.0.0.1:1/v1')
        try:
            with self.assertRaises(AppwriteException):
                await client.call('get', '/echo')
        finally:
            await client.aclose()


class TestRealConcurrency(_LiveServerTest):
    async def test_requests_overlap_on_the_wire(self):
        """Sequential calls pay the delay every time; concurrent calls overlap."""
        count = 8
        delay = 0.25

        self.state.reset()
        started = time.perf_counter()
        for _ in range(count):
            await self.client.call('get', '/slow', {}, {'delay': str(delay)})
        sequential = time.perf_counter() - started

        self.state.reset()
        started = time.perf_counter()
        await asyncio.gather(*[self.client.call('get', '/slow', {}, {'delay': str(delay)}) for _ in range(count)])
        concurrent = time.perf_counter() - started

        self.assertGreater(sequential, delay * count * 0.9, 'sequential baseline should pay the delay every time')
        self.assertLess(concurrent, sequential / 3, 'concurrent calls should overlap instead of queueing')
        self.assertGreater(self.state.peak_in_flight, 1, 'the server never handled two requests at once')

    async def test_each_concurrent_request_gets_its_own_connection(self):
        count = 6
        self.state.reset()

        await asyncio.gather(*[self.client.call('get', '/slow', {}, {'delay': '0.2'}) for _ in range(count)])

        self.assertEqual(self.state.requests, count)
        self.assertEqual(self.state.connections, count, 'requests were serialised onto a single connection')

    async def test_connection_pool_is_reused_for_sequential_calls(self):
        self.state.reset()

        for _ in range(5):
            await self.client.call('get', '/echo')

        self.assertEqual(self.state.requests, 5)
        self.assertEqual(self.state.connections, 1, 'keep-alive should reuse a single connection')


class TestRealChunkedUpload(_LiveServerTest):
    async def test_chunks_arrive_intact_over_real_multipart(self):
        payload = bytes(range(256)) * 800  # 204800 bytes
        chunk_size = 51_200  # exactly 4 chunks
        self.state.reset()
        self.state.chunk_size = chunk_size
        self.state.expected_total = len(payload)
        self.state.file_id = 'file-1'

        self.client._chunk_size = chunk_size
        progress = []

        async def on_progress(update):
            progress.append(update)

        storage = Storage(self.client)
        result = await storage.create_file(
            bucket_id='bucket-1',
            file_id='file-1',
            file=InputFile.from_bytes(payload, 'blob.bin'),
            on_progress=on_progress,
        )

        self.assertEqual(result.id, 'file-1')

        chunks = sorted(self.state.chunks, key=lambda chunk: chunk['index'])
        self.assertEqual(len(chunks), 4)
        self.assertEqual(
            hashlib.sha256(b''.join(chunk['payload'] for chunk in chunks)).hexdigest(),
            hashlib.sha256(payload).hexdigest(),
            'the bytes that arrived on the wire differ from the bytes we sent',
        )
        self.assertEqual(
            sorted(chunk['content_range'] for chunk in chunks),
            [
                'bytes 0-51199/204800',
                'bytes 102400-153599/204800',
                'bytes 153600-204799/204800',
                'bytes 51200-102399/204800',
            ],
        )
        self.assertEqual([chunk['upload_id'] for chunk in chunks], ['file-1'] * 4)

        self.assertEqual(max(item['progress'] for item in progress), 100.0)
        self.assertEqual(sorted(item['chunksUploaded'] for item in progress), [1, 2, 3, 4])


class TestRealTls(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if shutil.which('openssl') is None:
            raise unittest.SkipTest('openssl is required to generate a self-signed certificate')
        cls.server = _Server(tls=True)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.server.close()

    async def test_self_signed_certificate_is_rejected_by_default(self):
        client = Client()
        client.set_endpoint(self.server.endpoint)
        try:
            with self.assertRaises(AppwriteException):
                await client.call('get', '/echo')
        finally:
            await client.aclose()

    async def test_self_signed_certificate_is_accepted_after_opt_in(self):
        async with Client() as client:
            client.set_endpoint(self.server.endpoint)
            client.set_self_signed()
            response = await client.call('get', '/echo')

        self.assertEqual(response['method'], 'GET')


class TestRealAppwriteCloud(unittest.IsolatedAsyncioTestCase):
    """Talks to the real Appwrite Cloud endpoint over real TLS."""

    async def test_cloud_endpoint_rejects_unauthenticated_call(self):
        async with Client() as client:
            client.set_endpoint('https://cloud.appwrite.io/v1')
            try:
                with self.assertRaises(AppwriteException) as context:
                    await asyncio.wait_for(client.call('get', '/health'), timeout=20)
            except TimeoutError:
                self.skipTest('Appwrite Cloud did not answer within 20s')

        if context.exception.code is None:
            self.skipTest(f'Appwrite Cloud is unreachable from this machine: {context.exception.message}')

        self.assertEqual(context.exception.code, 401)
        self.assertIn('missing scopes', context.exception.message)


if __name__ == '__main__':
    unittest.main()
