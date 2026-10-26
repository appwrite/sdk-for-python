import asyncio
import inspect
import json
import os
import platform
import sys
import httpx2
from .input_file import InputFile
from .exception import AppwriteException
from .encoders.value_class_encoder import ValueClassEncoder
from .query import Query

_ssl_context = None


def _default_ssl_context():
    """Build the TLS context once and reuse it across clients."""
    global _ssl_context
    if _ssl_context is None:
        _ssl_context = httpx2.create_ssl_context()
    return _ssl_context


class Client:
    def __init__(self):
        self._chunk_size = 5 * 1024 * 1024
        self._self_signed = False
        self._endpoint = 'https://cloud.appwrite.io/v1'
        self._global_headers = {
            'content-type': '',
            'user-agent': f'AppwritePythonSDK/26.0.0 ({platform.uname().system}; {platform.uname().version}; {platform.uname().machine})',
            'x-sdk-name': 'Python',
            'x-sdk-platform': 'server',
            'x-sdk-language': 'python',
            'x-sdk-version': '26.0.0',
            'X-Appwrite-Response-Format': '2.5.0',
        }
        self._config = {}
        self._http = self._new_http_client(verify=True)

    def _new_http_client(self, verify):
        context = _default_ssl_context() if verify else False
        return httpx2.AsyncClient(verify=context, timeout=None)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.aclose()

    async def aclose(self):
        """Close the underlying HTTP connection pool."""
        await self._http.aclose()

    def set_self_signed(self, status=True):
        """Accept self-signed TLS certificates."""
        self._self_signed = status
        previous = self._http
        self._http = self._new_http_client(verify=not status)
        self._dispose(previous)
        return self

    @staticmethod
    def _dispose(client):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            return
        loop.create_task(client.aclose())

    def set_endpoint(self, endpoint):
        if not endpoint.startswith('http://') and not endpoint.startswith('https://'):
            raise AppwriteException('Invalid endpoint URL: ' + endpoint)

        self._endpoint = endpoint
        return self

    def add_header(self, key, value):
        self._global_headers[key.lower()] = value
        return self

    def get_headers(self):
        return dict(self._global_headers)

    def get_config(self, key):
        return self._config.get(key, '')

    def set_project(self, value):
        """Your project ID"""

        self._config['project'] = value
        return self

    def set_key(self, value):
        """Your secret API key"""

        self._global_headers['x-appwrite-key'] = value
        self._config['key'] = value
        return self

    def set_organization(self, value):
        """Your organization ID"""

        self._global_headers['x-appwrite-organization'] = value
        self._config['organization'] = value
        return self

    def set_jwt(self, value):
        """Your secret JSON Web Token"""

        self._global_headers['x-appwrite-jwt'] = value
        self._config['jwt'] = value
        return self

    def set_bearer(self, value):
        """The OAuth access token to authenticate with"""

        self._global_headers['authorization'] = 'Bearer ' + value
        self._config['bearer'] = value
        return self

    def set_locale(self, value):
        self._global_headers['x-appwrite-locale'] = value
        self._config['locale'] = value
        return self

    def set_session(self, value):
        """The user session to authenticate with"""

        self._global_headers['x-appwrite-session'] = value
        self._config['session'] = value
        return self

    def set_forwarded_user_agent(self, value):
        """The user agent string of the client that made the request"""

        self._global_headers['x-forwarded-user-agent'] = value
        self._config['forwardeduseragent'] = value
        return self

    def set_cookie(self, value):
        """The user cookie to authenticate with. Used by SDKs that forward an incoming Cookie header in server-side runtimes."""

        self._global_headers['cookie'] = value
        self._config['cookie'] = value
        return self

    def set_impersonate_user_id(self, value):
        """Impersonate a user by ID"""

        self._global_headers['x-appwrite-impersonate-user-id'] = value
        self._config['impersonateuserid'] = value
        return self

    def set_impersonate_user_email(self, value):
        """Impersonate a user by email"""

        self._global_headers['x-appwrite-impersonate-user-email'] = value
        self._config['impersonateuseremail'] = value
        return self

    def set_impersonate_user_phone(self, value):
        """Impersonate a user by phone"""

        self._global_headers['x-appwrite-impersonate-user-phone'] = value
        self._config['impersonateuserphone'] = value
        return self

    async def call(self, method, path='', headers=None, params=None, response_type='json'):
        """Perform a single API request."""
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        params = {key: Query._flatten(value) for key, value in params.items()}

        data = {}
        files = {}
        content = None
        stringify = False

        headers = {**self._global_headers, **headers}

        if method != 'get':
            data = params
            params = {}

        if headers['content-type'].startswith('application/json'):
            content = json.dumps(data, cls=ValueClassEncoder)
            data = {}

        if headers['content-type'].startswith('multipart/form-data'):
            del headers['content-type']
            stringify = True
            for key in data.copy():
                if isinstance(data[key], InputFile):
                    payload = data[key].data
                    if isinstance(payload, str):
                        payload = payload.encode('utf-8')
                    elif not isinstance(payload, bytes):
                        payload = bytes(payload)
                    files[key] = (data[key].filename, payload)
                    del data[key]
            data = self.flatten(data, stringify=stringify)
            if not files and data:
                # Without a file, httpx2 would fall back to a URL-encoded body.
                files = {key: (None, value) for key, value in data.items()}
                data = {}
            elif not files:
                # With no parts at all, httpx2 would send a bare body, so close an empty multipart one.
                boundary = os.urandom(16).hex()
                headers['content-type'] = f'multipart/form-data; boundary={boundary}'
                content = f'--{boundary}--\r\n'

        response = None
        try:
            response = await self._http.request(  # call method dynamically https://stackoverflow.com/a/4246075/2299554
                method=method,
                url=self._endpoint + path,
                params=self.flatten(params, stringify=stringify),
                data=data or None,
                files=files or None,
                content=content,
                headers=headers,
                follow_redirects=False if response_type == 'location' else True,
            )

            response.raise_for_status()

            warnings = response.headers.get('x-appwrite-warning')
            if warnings:
                for warning in warnings.split(';'):
                    print(f'Warning: {warning}', file=sys.stderr)

            content_type = response.headers.get('Content-Type', '')

            if response_type == 'location':
                return response.headers.get('Location')

            if response_type == 'text':
                return response.content.decode('utf-8')

            if content_type.startswith('application/json'):
                return response.json()

            return response.content
        except Exception as e:
            if response != None:
                content_type = response.headers.get('Content-Type', '')
                if content_type.startswith('application/json'):
                    raise AppwriteException(
                        response.json()['message'], response.status_code, response.json().get('type'), response.text
                    )
                else:
                    raise AppwriteException(response.text, response.status_code, None, response.text)
            else:
                raise AppwriteException(e)

    async def chunked_upload(
        self,
        path,
        headers=None,
        params=None,
        param_name='',
        on_progress=None,
        upload_id='',
        response_type='json',
        method='post',
    ):
        """Upload a file in chunks, reporting progress as it goes."""
        if params.get(param_name) is None:
            return await self.call(method, path, headers, params, response_type=response_type)

        input_file = params[param_name]

        if input_file.source_type == 'path':
            size = os.stat(input_file.path).st_size
            input = None
        elif input_file.source_type == 'bytes':
            size = len(input_file.data)
            input = input_file.data

        if size <= self._chunk_size or response_type == 'text':
            if input_file.source_type == 'path':
                with open(input_file.path, 'rb') as input:
                    input_file.data = input.read()

            params[param_name] = input_file
            return await self.call(method, path, headers, params, response_type=response_type)

        offset = 0
        counter = 0

        if upload_id:
            try:
                result = await self.call('get', path + '/' + upload_id, headers)
                counter = result['chunksUploaded']
            except:
                pass

        if counter > 0:
            offset = counter * self._chunk_size

        total_chunks = (size + self._chunk_size - 1) // self._chunk_size
        chunks = []
        while offset < size:
            end = min(offset + self._chunk_size, size)
            chunks.append(
                {
                    'index': counter,
                    'start': offset,
                    'end': end,
                }
            )
            offset = end
            counter = counter + 1

        if not chunks:
            return result

        def read_chunk(start, end):
            if input_file.source_type == 'path':
                with open(input_file.path, 'rb') as chunk_file:
                    chunk_file.seek(start)
                    return chunk_file.read(end - start)
            return input[start:end]

        upload_id_header = upload_id
        completed_count = chunks[0]['index']
        uploaded_size = chunks[0]['start']
        last_result = None
        final_result = None

        def is_upload_complete(chunk_result):
            if not isinstance(chunk_result, dict):
                return False
            chunks_uploaded = chunk_result.get('chunksUploaded')
            if chunks_uploaded is None:
                return False
            chunks_total = chunk_result.get('chunksTotal', total_chunks)
            return int(chunks_uploaded) >= int(chunks_total)

        async def upload_chunk(chunk, current_upload_id):
            chunk_input = InputFile.from_bytes(
                await asyncio.to_thread(read_chunk, chunk['start'], chunk['end']),
                input_file.filename,
                getattr(input_file, 'mime_type', None),
            )
            chunk_params = {**params, param_name: chunk_input}
            chunk_headers = {**headers}
            chunk_headers["content-range"] = f"bytes {chunk['start']}-{chunk['end'] - 1}/{size}"
            if current_upload_id:
                chunk_headers["x-appwrite-id"] = current_upload_id

            return await self.call(
                method,
                path,
                chunk_headers,
                chunk_params,
                response_type=response_type,
            )

        result = await upload_chunk(chunks[0], upload_id_header)
        last_result = result
        if isinstance(result, dict) and "$id" in result:
            upload_id_header = result["$id"]

        completed_count = chunks[0]['index'] + 1
        uploaded_size = chunks[0]['end']

        await self._report_progress(
            on_progress,
            {
                "$id": result.get("$id") if isinstance(result, dict) else None,
                "progress": uploaded_size / size * 100,
                "sizeUploaded": uploaded_size,
                "chunksTotal": total_chunks,
                "chunksUploaded": completed_count,
            },
        )

        semaphore = asyncio.Semaphore(8)

        async def upload_remaining_chunk(chunk):
            nonlocal completed_count, uploaded_size, last_result, final_result
            async with semaphore:
                chunk_result = await upload_chunk(chunk, upload_id_header)
            completed_count = completed_count + 1
            uploaded_size = uploaded_size + (chunk['end'] - chunk['start'])
            last_result = chunk_result
            if is_upload_complete(chunk_result):
                final_result = chunk_result
            await self._report_progress(
                on_progress,
                {
                    "$id": upload_id_header,
                    "progress": uploaded_size / size * 100,
                    "sizeUploaded": uploaded_size,
                    "chunksTotal": total_chunks,
                    "chunksUploaded": completed_count,
                },
            )

        # Wait for every sibling chunk to settle before surfacing a failure, so the
        # caller never observes an error while other chunks are still being written.
        outcomes = await asyncio.gather(
            *(upload_remaining_chunk(chunk) for chunk in chunks[1:]),
            return_exceptions=True,
        )
        for outcome in outcomes:
            if isinstance(outcome, BaseException):
                raise outcome

        return final_result or last_result

    @staticmethod
    async def _report_progress(on_progress, payload):
        """Invoke the progress callback, awaiting it when it is a coroutine."""
        if on_progress is None:
            return
        result = on_progress(payload)
        if inspect.isawaitable(result):
            await result

    def flatten(self, data, prefix='', stringify=False):
        output = {}
        entries = data.items() if isinstance(data, dict) else enumerate(data)

        for key, value in entries:
            finalKey = f'{prefix}[{key}]' if prefix or isinstance(data, list) else key

            if isinstance(value, list) or isinstance(value, dict):
                output = {**output, **self.flatten(value, finalKey, stringify)}
            elif isinstance(value, bool):
                output[finalKey] = 'true' if value else 'false'
            else:
                if stringify:
                    output[finalKey] = str(value)
                else:
                    output[finalKey] = value

        return output
