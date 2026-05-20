import json
import requests_mock
import unittest

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
    "buckets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.list_buckets(
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
    "enabled": True,
    "maximumFileSize": 100.0,
    "allowedFileExtensions": [],
    "compression": "gzip",
    "encryption": True,
    "antivirus": True,
    "transformations": True,
    "totalSize": 128.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.create_bucket(
            '<BUCKET_ID>',
            '<NAME>',
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
    "enabled": True,
    "maximumFileSize": 100.0,
    "allowedFileExtensions": [],
    "compression": "gzip",
    "encryption": True,
    "antivirus": True,
    "transformations": True,
    "totalSize": 128.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.get_bucket(
            '<BUCKET_ID>',
        )

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
    "enabled": True,
    "maximumFileSize": 100.0,
    "allowedFileExtensions": [],
    "compression": "gzip",
    "encryption": True,
    "antivirus": True,
    "transformations": True,
    "totalSize": 128.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.update_bucket(
            '<BUCKET_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_bucket(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.delete_bucket(
            '<BUCKET_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_files(self, m):
        data = {
    "total": 5.0,
    "files": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.list_files(
            '<BUCKET_ID>',
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
    "signature": "5d529fd02b544198ae075bd57c1762bb",
    "mimeType": "image\/png",
    "sizeOriginal": 17890.0,
    "sizeActual": 12345.0,
    "chunksTotal": 17890.0,
    "chunksUploaded": 17890.0,
    "encryption": True,
    "compression": "gzip"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.create_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
            InputFile.from_bytes(bytearray(), "example.file"),
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
    "signature": "5d529fd02b544198ae075bd57c1762bb",
    "mimeType": "image\/png",
    "sizeOriginal": 17890.0,
    "sizeActual": 12345.0,
    "chunksTotal": 17890.0,
    "chunksUploaded": 17890.0,
    "encryption": True,
    "compression": "gzip"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.get_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )

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
    "signature": "5d529fd02b544198ae075bd57c1762bb",
    "mimeType": "image\/png",
    "sizeOriginal": 17890.0,
    "sizeActual": 12345.0,
    "chunksTotal": 17890.0,
    "chunksUploaded": 17890.0,
    "encryption": True,
    "compression": "gzip"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.update_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_file(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.storage.delete_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_file_download(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.storage.get_file_download(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_file_preview(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.storage.get_file_preview(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_file_view(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.storage.get_file_view(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )

        self.assertEqual(response, data)

