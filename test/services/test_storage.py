import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.storage import Storage


class StorageServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.storage = Storage(self.client)

    @requests_mock.Mocker()
    def test_list_buckets(self, m):
        data = {
            "total": 5.0,
            "buckets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.list_buckets(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_bucket(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "fileSecurity": True,
            "name": "Documents",
            "description": "Invoices and receipts uploaded by customers.",
            "enabled": True,
            "maximumFileSize": 100.0,
            "allowedFileExtensions": [],
            "compression": "gzip",
            "encryption": True,
            "antivirus": True,
            "transformations": True,
            "stripMetadata": True,
            "totalSize": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.create_bucket(
            '<BUCKET_ID>',
            '<NAME>',
            permissions=[],
            file_security=False,
            enabled=False,
            maximum_file_size=1,
            allowed_file_extensions=[],
            compression='none',
            encryption=False,
            antivirus=False,
            transformations=False,
            description='<DESCRIPTION>',
            strip_metadata=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'bucketId': '<BUCKET_ID>',
                'name': '<NAME>',
                'permissions': [],
                'fileSecurity': False,
                'enabled': False,
                'maximumFileSize': 1,
                'allowedFileExtensions': [],
                'compression': 'none',
                'encryption': False,
                'antivirus': False,
                'transformations': False,
                'description': '<DESCRIPTION>',
                'stripMetadata': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_bucket(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "fileSecurity": True,
            "name": "Documents",
            "description": "Invoices and receipts uploaded by customers.",
            "enabled": True,
            "maximumFileSize": 100.0,
            "allowedFileExtensions": [],
            "compression": "gzip",
            "encryption": True,
            "antivirus": True,
            "transformations": True,
            "stripMetadata": True,
            "totalSize": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.get_bucket(
            '<BUCKET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_bucket(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "fileSecurity": True,
            "name": "Documents",
            "description": "Invoices and receipts uploaded by customers.",
            "enabled": True,
            "maximumFileSize": 100.0,
            "allowedFileExtensions": [],
            "compression": "gzip",
            "encryption": True,
            "antivirus": True,
            "transformations": True,
            "stripMetadata": True,
            "totalSize": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.update_bucket(
            '<BUCKET_ID>',
            '<NAME>',
            permissions=[],
            file_security=False,
            enabled=False,
            maximum_file_size=1,
            allowed_file_extensions=[],
            compression='none',
            encryption=False,
            antivirus=False,
            transformations=False,
            description='<DESCRIPTION>',
            strip_metadata=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'permissions': [],
                'fileSecurity': False,
                'enabled': False,
                'maximumFileSize': 1,
                'allowedFileExtensions': [],
                'compression': 'none',
                'encryption': False,
                'antivirus': False,
                'transformations': False,
                'description': '<DESCRIPTION>',
                'stripMetadata': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_bucket(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.delete_bucket(
            '<BUCKET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_files(self, m):
        data = {
            "total": 5.0,
            "files": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.list_files(
            '<BUCKET_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_file(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "bucketId": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "name": "Pink.png",
            "folder": "photos\/2026\/",
            "key": "photos\/2026\/Pink.png",
            "signature": "5d529fd02b544198ae075bd57c1762bb",
            "mimeType": "image\/png",
            "sizeOriginal": 17890.0,
            "sizeActual": 12345.0,
            "chunksTotal": 17890.0,
            "chunksUploaded": 17890.0,
            "encryption": True,
            "compression": "gzip",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.create_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
            InputFile.from_bytes(bytearray(), "example.file"),
            permissions=[],
            folder='photos/2026',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files',
        )
        sent = dict(
            re.findall(
                r'form-data; name="([^"\[]+)[^\r\n]*\r\n(?:[^\r\n]+\r\n)*\r\n(.*?)\r\n--',
                request.body.decode('latin-1'),
                re.S,
            )
        )
        self.assertEqual(
            sent,
            {
                'fileId': '<FILE_ID>',
                'file': '',
                'folder': 'photos/2026',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_file(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "bucketId": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "name": "Pink.png",
            "folder": "photos\/2026\/",
            "key": "photos\/2026\/Pink.png",
            "signature": "5d529fd02b544198ae075bd57c1762bb",
            "mimeType": "image\/png",
            "sizeOriginal": 17890.0,
            "sizeActual": 12345.0,
            "chunksTotal": 17890.0,
            "chunksUploaded": 17890.0,
            "encryption": True,
            "compression": "gzip",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.get_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files/<FILE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_file(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "bucketId": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "name": "Pink.png",
            "folder": "photos\/2026\/",
            "key": "photos\/2026\/Pink.png",
            "signature": "5d529fd02b544198ae075bd57c1762bb",
            "mimeType": "image\/png",
            "sizeOriginal": 17890.0,
            "sizeActual": 12345.0,
            "chunksTotal": 17890.0,
            "chunksUploaded": 17890.0,
            "encryption": True,
            "compression": "gzip",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.update_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
            name='name',
            permissions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files/<FILE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': 'name',
                'permissions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_file(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.storage.delete_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files/<FILE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_file_download(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.storage.get_file_download(
            '<BUCKET_ID>',
            '<FILE_ID>',
            token='<TOKEN>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files/<FILE_ID>/download',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'token': ['<TOKEN>'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_file_preview(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.storage.get_file_preview(
            '<BUCKET_ID>',
            '<FILE_ID>',
            width=1,
            height=1,
            gravity='auto',
            quality=1,
            border_width=1,
            border_color='FFFFFF',
            border_radius=1,
            opacity=1.0,
            rotation=1,
            background='FFFFFF',
            output='jpg',
            token='<TOKEN>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files/<FILE_ID>/preview',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'width': ['1'],
                'height': ['1'],
                'gravity': ['auto'],
                'quality': ['1'],
                'borderWidth': ['1'],
                'borderColor': ['FFFFFF'],
                'borderRadius': ['1'],
                'opacity': ['1.0'],
                'rotation': ['1'],
                'background': ['FFFFFF'],
                'output': ['jpg'],
                'token': ['<TOKEN>'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_file_view(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.storage.get_file_view(
            '<BUCKET_ID>',
            '<FILE_ID>',
            token='<TOKEN>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/storage/buckets/<BUCKET_ID>/files/<FILE_ID>/view',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'token': ['<TOKEN>'],
            },
        )
        self.assertEqual(response, data)
