import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.avatars import Avatars


class AvatarsServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.avatars = Avatars(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_get_browser(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_browser(
            'aa',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_credit_card(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_credit_card(
            'amex',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_favicon(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_favicon(
            'https://example.com',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_flag(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_flag(
            'af',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_image(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_image(
            'https://example.com',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_initials(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_initials()
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_photo(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_photo()
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_photo(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "John Doe",
            "registration": "2020-10-15T06:38:00.000+00:00",
            "status": True,
            "labels": [],
            "passwordUpdate": "2020-10-15T06:38:00.000+00:00",
            "email": "john@appwrite.io",
            "phone": "+4930901820",
            "emailVerification": True,
            "phoneVerification": True,
            "mfa": True,
            "prefs": {},
            "targets": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.avatars.update_photo(
            InputFile.from_bytes(bytearray(), "example.file"),
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_photo(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.avatars.delete_photo()
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_qr(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_qr(
            '<TEXT>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_get_screenshot(self):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        respx.route().mock(
            return_value=httpx2.Response(200, content=bytes(data), headers=headers),
        )
        response = await self.avatars.get_screenshot(
            'https://example.com',
        )
        self.assertEqual(response, data)
