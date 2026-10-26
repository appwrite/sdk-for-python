import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.webhooks import Webhooks


class WebhooksServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.webhooks = Webhooks(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list(self):
        data = {
            "total": 5.0,
            "webhooks": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.webhooks.list()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Webhook",
            "description": "Notifies the billing service about new users.",
            "url": "https:\/\/example.com\/webhook",
            "events": [],
            "tls": True,
            "authUsername": "username",
            "authPassword": "webhook-password",
            "secret": "ad3d581ca230e2b7059c545e5a",
            "enabled": True,
            "logs": "Failed to connect to remote server.",
            "attempts": 10.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.webhooks.create(
            '<WEBHOOK_ID>',
            'https://example.com/webhook',
            '<NAME>',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Webhook",
            "description": "Notifies the billing service about new users.",
            "url": "https:\/\/example.com\/webhook",
            "events": [],
            "tls": True,
            "authUsername": "username",
            "authPassword": "webhook-password",
            "secret": "ad3d581ca230e2b7059c545e5a",
            "enabled": True,
            "logs": "Failed to connect to remote server.",
            "attempts": 10.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.webhooks.get(
            '<WEBHOOK_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Webhook",
            "description": "Notifies the billing service about new users.",
            "url": "https:\/\/example.com\/webhook",
            "events": [],
            "tls": True,
            "authUsername": "username",
            "authPassword": "webhook-password",
            "secret": "ad3d581ca230e2b7059c545e5a",
            "enabled": True,
            "logs": "Failed to connect to remote server.",
            "attempts": 10.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.webhooks.update(
            '<WEBHOOK_ID>',
            '<NAME>',
            'https://example.com/webhook',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.webhooks.delete(
            '<WEBHOOK_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_secret(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Webhook",
            "description": "Notifies the billing service about new users.",
            "url": "https:\/\/example.com\/webhook",
            "events": [],
            "tls": True,
            "authUsername": "username",
            "authPassword": "webhook-password",
            "secret": "ad3d581ca230e2b7059c545e5a",
            "enabled": True,
            "logs": "Failed to connect to remote server.",
            "attempts": 10.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.webhooks.update_secret(
            '<WEBHOOK_ID>',
        )
        self.assertEqual(response.to_dict(), data)
