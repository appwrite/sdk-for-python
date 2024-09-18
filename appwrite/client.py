import json
import requests
from .payload import Payload
from .multipart import MultipartParser
from .exception import AppwriteException
from .encoders.value_class_encoder import ValueClassEncoder

class Client:
    def __init__(self):
        self._chunk_size = 5*1024*1024
        self._self_signed = False
        self._endpoint = 'https://cloud.appwrite.io/v1'
        self._global_headers = {
            'content-type': '',
            'user-agent' : 'AppwritePythonSDK/7.0.0-rc1 (${os.uname().sysname}; ${os.uname().version}; ${os.uname().machine})',
            'x-sdk-name': 'Python',
            'x-sdk-platform': 'server',
            'x-sdk-language': 'python',
            'x-sdk-version': '7.0.0-rc1',
            'X-Appwrite-Response-Format' : '1.6.0',
        }

    def set_self_signed(self, status=True):
        self._self_signed = status
        return self

    def set_endpoint(self, endpoint):
        self._endpoint = endpoint
        return self

    def add_header(self, key, value):
        self._global_headers[key.lower()] = value
        return self

    def set_project(self, value):
        """Your project ID"""

        self._global_headers['x-appwrite-project'] = value
        return self

    def set_key(self, value):
        """Your secret API key"""

        self._global_headers['x-appwrite-key'] = value
        return self

    def set_jwt(self, value):
        """Your secret JSON Web Token"""

        self._global_headers['x-appwrite-jwt'] = value
        return self

    def set_locale(self, value):
        self._global_headers['x-appwrite-locale'] = value
        return self

    def set_session(self, value):
        """The user session to authenticate with"""

        self._global_headers['x-appwrite-session'] = value
        return self

    def set_forwarded_user_agent(self, value):
        """The user agent string of the client that made the request"""

        self._global_headers['x-forwarded-user-agent'] = value
        return self

    def call(self, method, path='', headers=None, params=None, response_type='json'):
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        params = {k: v for k, v in params.items() if v is not None}  # Remove None values from params dictionary

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
            headers['accept'] = 'multipart/form-data'
            stringify = True
            for key in data.copy():
                if isinstance(data[key], Payload):
                    if data[key].filename:
                        files[key] = (data[key].filename, data[key].to_binary())
                    else:
                        data[key] = data[key].to_binary()
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
                    print(f'Warning: {warning}')

            content_type = response.headers['Content-Type']

            if response_type == 'location':
                return response.headers.get('Location')

            if content_type.startswith('application/json'):
                return response.json()

            if content_type.startswith('multipart/form-data'): 
                return MultipartParser(response.content, content_type).to_dict()

            return response._content
        except Exception as e:
            if response != None:
                content_type = response.headers['Content-Type']
                if content_type.startswith('application/json'):
                    raise AppwriteException(response.json()['message'], response.status_code, response.json().get('type'), response.json())
                else:
                    raise AppwriteException(response.text, response.status_code)
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
        payload = params[param_name]
        size = params[param_name].size

        if size < self._chunk_size:    
            return self.call(
                'post',
                path,
                headers,
                params
            )

        offset = 0
        counter = 0

        if upload_id != 'unique()':
            try:
                result = self.call('get', path + '/' + upload_id, headers)
                counter = result['chunksUploaded']
            except:
                pass

        if counter > 0:
            offset = counter * self._chunk_size
            input.seek(offset)

        while offset < size:
            params[param_name] = Payload.from_binary(
                payload.to_binary(offset, min(self._chunk_size, size - offset)),
                payload.filename
            )
            headers["content-range"] = f'bytes {offset}-{min((offset + self._chunk_size) - 1, size - 1)}/{size}'

            result = self.call(
                'post',
                path,
                headers,
                params,
            )
            
            offset = offset + self._chunk_size
            
            if "$id" in result: 
                headers["x-appwrite-id"] = result["$id"]

            if on_progress is not None:
                end = min((((counter * self._chunk_size) + self._chunk_size) - 1), size - 1)
                on_progress({
                    "$id": result["$id"],
                    "progress": min(offset, size)/size * 100,
                    "sizeUploaded": end+1,
                    "chunksTotal": result["chunksTotal"],
                    "chunksUploaded": result["chunksUploaded"],
                })

            counter = counter + 1

        return result

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
            else:
                if stringify:
                    output[finalKey] = str(value)
                else:
                    output[finalKey] = value

        return output

