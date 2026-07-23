import io
import json
import os
import platform
import sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from .input_file import InputFile
from .exception import AppwriteException
from .encoders.value_class_encoder import ValueClassEncoder

class Client:
    def __init__(self):
        self._chunk_size = 5*1024*1024
        self._self_signed = False
        self._endpoint = 'https://cloud.appwrite.io/v1'
        self._global_headers = {
            'content-type': '',
            'user-agent' : f'AppwritePythonSDK/22.2.0 ({platform.uname().system}; {platform.uname().version}; {platform.uname().machine})',
            'x-sdk-name': 'Python',
            'x-sdk-platform': 'server',
            'x-sdk-language': 'python',
            'x-sdk-version': '22.2.0',
            'X-Appwrite-Response-Format' : '1.9.5',
        }
        self._config = {}

    def set_self_signed(self, status=True):
        self._self_signed = status
        return self

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

    def set_dev_key(self, value):
        """Your secret dev API key"""

        self._global_headers['x-appwrite-dev-key'] = value
        self._config['devkey'] = value
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

    def call(self, method, path='', headers=None, params=None, response_type='json'):
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        data = {}
        files = {}
        stringify = False

        headers = {**self._global_headers, **headers}

        if method != 'get':
            data = params
            params = {}

        if headers['content-type'].startswith('application/json'):
            data = json.dumps(data, cls=ValueClassEncoder)

        if headers['content-type'].startswith('multipart/form-data'):
            del headers['content-type']
            stringify = True
            for key in data.copy():
                if isinstance(data[key], InputFile):
                    files[key] = (data[key].filename, data[key].data)
                    del data[key]
            data = self.flatten(data, stringify=stringify)

        response = None
        try:
            response = requests.request(  # call method dynamically https://stackoverflow.com/a/4246075/2299554
                method=method,
                url=self._endpoint + path,
                params=self.flatten(params, stringify=stringify),
                data=data,
                files=files,
                headers=headers,
                verify=(not self._self_signed),
                allow_redirects=False if response_type == 'location' else True
            )

            response.raise_for_status()

            warnings = response.headers.get('x-appwrite-warning')
            if warnings:
                for warning in warnings.split(';'):
                    print(f'Warning: {warning}', file=sys.stderr)

            content_type = response.headers['Content-Type']

            if response_type == 'location':
                return response.headers.get('Location')

            if content_type.startswith('application/json'):
                return response.json()

            return response._content
        except Exception as e:
            if response != None:
                content_type = response.headers['Content-Type']
                if content_type.startswith('application/json'):
                    raise AppwriteException(response.json()['message'], response.status_code, response.json().get('type'), response.text)
                else:
                    raise AppwriteException(response.text, response.status_code, None, response.text)
            else:
                raise AppwriteException(e)

    def chunked_upload(
        self,
        path,
        headers = None,
        params = None,
        param_name = '',
        on_progress = None,
        upload_id = ''
    ):
        input_file = params[param_name]

        if input_file.source_type == 'path':
            size = os.stat(input_file.path).st_size
            input = None
        elif input_file.source_type == 'bytes':
            size = len(input_file.data)
            input = input_file.data

        if size < self._chunk_size:
            if input_file.source_type == 'path':
                with open(input_file.path, 'rb') as input:
                    input_file.data = input.read()

            params[param_name] = input_file
            return self.call(
                'post',
                path,
                headers,
                params
            )

        offset = 0
        counter = 0

        try:
            result = self.call('get', path + '/' + upload_id, headers)
            counter = result['chunksUploaded']
        except:
            pass

        if counter > 0:
            offset = counter * self._chunk_size

        total_chunks = (size + self._chunk_size - 1) // self._chunk_size
        chunks = []
        while offset < size:
            end = min(offset + self._chunk_size, size)
            chunks.append({
                'index': counter,
                'start': offset,
                'end': end,
            })
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
        progress_lock = Lock()
        last_result = None
        final_result = None

        def is_upload_complete(chunk_result):
            chunks_uploaded = chunk_result.get('chunksUploaded')
            if chunks_uploaded is None:
                return False
            chunks_total = chunk_result.get('chunksTotal', total_chunks)
            return int(chunks_uploaded) >= int(chunks_total)

        def upload_chunk(chunk, current_upload_id):
            chunk_input = InputFile.from_bytes(
                read_chunk(chunk['start'], chunk['end']),
                input_file.filename,
                getattr(input_file, 'mime_type', None)
            )
            chunk_params = {**params, param_name: chunk_input}
            chunk_headers = {**headers}
            chunk_headers["content-range"] = f"bytes {chunk['start']}-{chunk['end'] - 1}/{size}"
            if current_upload_id:
                chunk_headers["x-appwrite-id"] = current_upload_id

            return self.call(
                'post',
                path,
                chunk_headers,
                chunk_params,
            )

        result = upload_chunk(chunks[0], upload_id_header)
        last_result = result
        if "$id" in result:
            upload_id_header = result["$id"]

        completed_count = chunks[0]['index'] + 1
        uploaded_size = chunks[0]['end']

        if on_progress is not None:
            on_progress({
                "$id": result.get("$id"),
                "progress": uploaded_size / size * 100,
                "sizeUploaded": uploaded_size,
                "chunksTotal": total_chunks,
                "chunksUploaded": completed_count,
            })

        def upload_remaining_chunk(chunk):
            nonlocal completed_count, uploaded_size, last_result, final_result
            chunk_result = upload_chunk(chunk, upload_id_header)
            with progress_lock:
                completed_count = completed_count + 1
                uploaded_size = uploaded_size + (chunk['end'] - chunk['start'])
                last_result = chunk_result
                if is_upload_complete(chunk_result):
                    final_result = chunk_result
                if on_progress is not None:
                    on_progress({
                        "$id": upload_id_header,
                        "progress": uploaded_size / size * 100,
                        "sizeUploaded": uploaded_size,
                        "chunksTotal": total_chunks,
                        "chunksUploaded": completed_count,
                    })

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(upload_remaining_chunk, chunk) for chunk in chunks[1:]]
            for future in as_completed(futures):
                future.result()

        return final_result or last_result

    def flatten(self, data, prefix='', stringify=False):
        output = {}
        i = 0

        for key in data:
            value = data[key] if isinstance(data, dict) else key
            finalKey = prefix + '[' + key +']' if prefix else key
            finalKey = prefix + '[' + str(i) +']' if isinstance(data, list) else finalKey
            i += 1

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
