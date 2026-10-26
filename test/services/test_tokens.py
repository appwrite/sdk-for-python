import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.tokens import Tokens


class TokensServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.tokens = Tokens(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list(self):
        data = {
            "total": 5.0,
            "tokens": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.tokens.list(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_file_token(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "resourceId": "5e5ea5c168bb8:5e5ea5c168bb8",
            "resourceType": "files",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.tokens.create_file_token(
            '<BUCKET_ID>',
            '<FILE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "resourceId": "5e5ea5c168bb8:5e5ea5c168bb8",
            "resourceType": "files",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.tokens.get(
            '<TOKEN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "resourceId": "5e5ea5c168bb8:5e5ea5c168bb8",
            "resourceType": "files",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.tokens.update(
            '<TOKEN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.tokens.delete(
            '<TOKEN_ID>',
        )
        self.assertEqual(response, data)
