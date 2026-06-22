import json
import requests_mock
import unittest

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
    "webhooks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.webhooks.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Webhook",
    "url": "https:\/\/example.com\/webhook",
    "events": [],
    "tls": True,
    "authUsername": "username",
    "authPassword": "webhook-password",
    "secret": "ad3d581ca230e2b7059c545e5a",
    "enabled": True,
    "logs": "Failed to connect to remote server.",
    "attempts": 10.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.webhooks.create(
            '<WEBHOOK_ID>',
            '',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Webhook",
    "url": "https:\/\/example.com\/webhook",
    "events": [],
    "tls": True,
    "authUsername": "username",
    "authPassword": "webhook-password",
    "secret": "ad3d581ca230e2b7059c545e5a",
    "enabled": True,
    "logs": "Failed to connect to remote server.",
    "attempts": 10.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.webhooks.get(
            '<WEBHOOK_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Webhook",
    "url": "https:\/\/example.com\/webhook",
    "events": [],
    "tls": True,
    "authUsername": "username",
    "authPassword": "webhook-password",
    "secret": "ad3d581ca230e2b7059c545e5a",
    "enabled": True,
    "logs": "Failed to connect to remote server.",
    "attempts": 10.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.webhooks.update(
            '<WEBHOOK_ID>',
            '<NAME>',
            '',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.webhooks.delete(
            '<WEBHOOK_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_secret(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Webhook",
    "url": "https:\/\/example.com\/webhook",
    "events": [],
    "tls": True,
    "authUsername": "username",
    "authPassword": "webhook-password",
    "secret": "ad3d581ca230e2b7059c545e5a",
    "enabled": True,
    "logs": "Failed to connect to remote server.",
    "attempts": 10.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.webhooks.update_secret(
            '<WEBHOOK_ID>',
        )

        self.assertEqual(response.to_dict(), data)

