import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.webhooks import Webhooks


class WebhooksServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.webhooks = Webhooks(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "webhooks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.webhooks.list(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/webhooks',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
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
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.webhooks.create(
            '<WEBHOOK_ID>',
            'https://example.com/webhook',
            '<NAME>',
            [],
            enabled=False,
            tls=False,
            auth_username='<AUTH_USERNAME>',
            auth_password='password',
            secret='<SECRET>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/webhooks',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'webhookId': '<WEBHOOK_ID>',
                'url': 'https://example.com/webhook',
                'name': '<NAME>',
                'events': [],
                'enabled': False,
                'tls': False,
                'authUsername': '<AUTH_USERNAME>',
                'authPassword': 'password',
                'secret': '<SECRET>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
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
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.webhooks.get(
            '<WEBHOOK_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/webhooks/<WEBHOOK_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
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
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.webhooks.update(
            '<WEBHOOK_ID>',
            '<NAME>',
            'https://example.com/webhook',
            [],
            enabled=False,
            tls=False,
            auth_username='<AUTH_USERNAME>',
            auth_password='password',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/webhooks/<WEBHOOK_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'url': 'https://example.com/webhook',
                'events': [],
                'enabled': False,
                'tls': False,
                'authUsername': '<AUTH_USERNAME>',
                'authPassword': 'password',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.webhooks.delete(
            '<WEBHOOK_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/webhooks/<WEBHOOK_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_secret(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.webhooks.update_secret(
            '<WEBHOOK_ID>',
            secret='<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/webhooks/<WEBHOOK_ID>/secret',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)
