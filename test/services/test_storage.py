import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.storage import Storage


class StorageServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.storage = Storage(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list_buckets(self):
        data = {
            "total": 5.0,
            "buckets": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.list_buckets()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_bucket(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.create_bucket(
            '<BUCKET_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_bucket(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.get_bucket(
            '<BUCKET_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_bucket(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.update_bucket(
            '<BUCKET_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_bucket(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.delete_bucket(
            '<BUCKET_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_files(self):
        data = {
            "total": 5.0,
            "files": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.list_files(
            '<BUCKET_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_file(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.create_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
            InputFile.from_bytes(bytearray(), "example.file"),
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_file(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.get_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_file(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.update_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_file(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.storage.delete_file(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_file_download(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.storage.get_file_download(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_file_preview(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.storage.get_file_preview(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_file_view(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.storage.get_file_view(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response, data)
