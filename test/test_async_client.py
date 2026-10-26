import asyncio
import unittest

import httpx2
import respx

from appwrite.client import Client
from appwrite.exception import AppwriteException
from appwrite.input_file import InputFile
from appwrite.services.storage import Storage


class AsyncClientTest(unittest.IsolatedAsyncioTestCase):

    @respx.mock
    async def test_requests_are_served_concurrently(self):
        in_flight = 0
        peak = 0

        async def handler(request):
            nonlocal in_flight, peak
            in_flight += 1
            peak = max(peak, in_flight)
            await asyncio.sleep(0.05)
            in_flight -= 1
            return httpx2.Response(200, json={'$id': 'user-1'}, headers={'Content-Type': 'application/json'})

        respx.route().mock(side_effect=handler)

        async with Client() as client:
            responses = await asyncio.gather(
                *[client.call('get', f'/users/{index}', {'accept': 'application/json'}) for index in range(5)]
            )

        self.assertEqual(len(responses), 5)
        self.assertEqual(peak, 5)

    @respx.mock
    async def test_error_response_raises_appwrite_exception(self):
        respx.route().mock(
            return_value=httpx2.Response(
                404,
                json={'message': 'User not found', 'type': 'user_not_found'},
                headers={'Content-Type': 'application/json'},
            )
        )

        async with Client() as client:
            with self.assertRaises(AppwriteException) as context:
                await client.call('get', '/users/missing', {'accept': 'application/json'})

        self.assertEqual(context.exception.message, 'User not found')
        self.assertEqual(context.exception.code, 404)
        self.assertEqual(context.exception.type, 'user_not_found')

    @respx.mock
    async def test_context_manager_closes_the_connection_pool(self):
        async with Client() as client:
            http = client._http
            self.assertFalse(http.is_closed)

        self.assertTrue(http.is_closed)

    @respx.mock
    async def test_chunked_upload_reports_progress(self):
        total_chunks = 4
        received = 0
        ranges = []
        upload_ids = []

        async def handler(request):
            nonlocal received
            if request.method == 'GET':
                # Resume probe: the SDK asks whether an upload is already in progress.
                return httpx2.Response(
                    200,
                    json={'$id': 'file-1', 'chunksTotal': total_chunks, 'chunksUploaded': 0},
                    headers={'Content-Type': 'application/json'},
                )
            received += 1
            ranges.append(request.headers.get('content-range'))
            upload_ids.append(request.headers.get('x-appwrite-id'))
            return httpx2.Response(
                200,
                json={'$id': 'file-1', 'chunksTotal': total_chunks, 'chunksUploaded': received},
                headers={'Content-Type': 'application/json'},
            )

        respx.route().mock(side_effect=handler)

        progress = []

        async def on_progress(payload):
            progress.append(payload)

        async with Client() as client:
            client._chunk_size = 10
            storage = Storage(client)
            await storage.create_file(
                bucket_id='bucket-1',
                file_id='file-1',
                file=InputFile.from_bytes(b'x' * 40, 'test.txt'),
                on_progress=on_progress,
            )

        self.assertEqual(received, total_chunks)
        self.assertEqual(
            sorted(ranges),
            ['bytes 0-9/40', 'bytes 10-19/40', 'bytes 20-29/40', 'bytes 30-39/40'],
        )
        self.assertEqual(upload_ids, ['file-1'] * total_chunks)
        self.assertEqual(sorted(item['chunksUploaded'] for item in progress), [1, 2, 3, 4])
        self.assertEqual(max(item['progress'] for item in progress), 100.0)
        self.assertEqual(max(item['sizeUploaded'] for item in progress), 40)

    @respx.mock
    async def test_chunked_upload_waits_for_sibling_chunks_after_a_failure(self):
        total_chunks = 4
        in_flight = 0
        completed = 0

        async def handler(request):
            nonlocal in_flight, completed
            if request.method == 'GET':
                # Resume probe: the SDK asks whether an upload is already in progress.
                return httpx2.Response(
                    200,
                    json={'$id': 'file-1', 'chunksTotal': total_chunks, 'chunksUploaded': 0},
                    headers={'Content-Type': 'application/json'},
                )
            if request.headers.get('content-range', '').startswith('bytes 10-19'):
                # Reject one chunk straight away, while its siblings are still uploading.
                return httpx2.Response(
                    400,
                    json={'message': 'Chunk rejected', 'type': 'general_bad_request'},
                    headers={'Content-Type': 'application/json'},
                )
            in_flight += 1
            await asyncio.sleep(0.2)
            in_flight -= 1
            completed += 1
            return httpx2.Response(
                200,
                json={'$id': 'file-1', 'chunksTotal': total_chunks, 'chunksUploaded': 1},
                headers={'Content-Type': 'application/json'},
            )

        respx.route().mock(side_effect=handler)

        async with Client() as client:
            client._chunk_size = 10
            storage = Storage(client)
            with self.assertRaises(AppwriteException) as context:
                await storage.create_file(
                    bucket_id='bucket-1',
                    file_id='file-1',
                    file=InputFile.from_bytes(b'x' * 40, 'test.txt'),
                )

        self.assertEqual(context.exception.message, 'Chunk rejected')
        self.assertEqual(in_flight, 0, 'sibling chunk uploads were still running when the error surfaced')
        self.assertEqual(completed, 3, 'sibling chunk uploads did not run to completion')
