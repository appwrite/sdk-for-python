import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.apps import Apps

class AppsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.apps = Apps(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
    "total": 5.0,
    "apps": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Application",
    "description": "Connect your workspace to My Application.",
    "clientUri": "https:\/\/example.com",
    "logoUri": "https:\/\/example.com\/logo.png",
    "privacyPolicyUrl": "https:\/\/example.com\/privacy",
    "termsUrl": "https:\/\/example.com\/terms",
    "contacts": [],
    "tagline": "Automate your workspace.",
    "tags": [],
    "labels": [],
    "images": [],
    "supportUrl": "https:\/\/example.com\/support",
    "dataDeletionUrl": "https:\/\/example.com\/data-deletion",
    "redirectUris": [],
    "postLogoutRedirectUris": [],
    "enabled": True,
    "type": "confidential",
    "deviceFlow": True,
    "teamId": "5e5ea5c16897e",
    "userId": "5e5ea5c16897e",
    "secrets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.create(
            '<APP_ID>',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_o_auth2_scopes(self, m):
        data = {
    "total": 5.0,
    "scopes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.list_o_auth2_scopes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Application",
    "description": "Connect your workspace to My Application.",
    "clientUri": "https:\/\/example.com",
    "logoUri": "https:\/\/example.com\/logo.png",
    "privacyPolicyUrl": "https:\/\/example.com\/privacy",
    "termsUrl": "https:\/\/example.com\/terms",
    "contacts": [],
    "tagline": "Automate your workspace.",
    "tags": [],
    "labels": [],
    "images": [],
    "supportUrl": "https:\/\/example.com\/support",
    "dataDeletionUrl": "https:\/\/example.com\/data-deletion",
    "redirectUris": [],
    "postLogoutRedirectUris": [],
    "enabled": True,
    "type": "confidential",
    "deviceFlow": True,
    "teamId": "5e5ea5c16897e",
    "userId": "5e5ea5c16897e",
    "secrets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.get(
            '<APP_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Application",
    "description": "Connect your workspace to My Application.",
    "clientUri": "https:\/\/example.com",
    "logoUri": "https:\/\/example.com\/logo.png",
    "privacyPolicyUrl": "https:\/\/example.com\/privacy",
    "termsUrl": "https:\/\/example.com\/terms",
    "contacts": [],
    "tagline": "Automate your workspace.",
    "tags": [],
    "labels": [],
    "images": [],
    "supportUrl": "https:\/\/example.com\/support",
    "dataDeletionUrl": "https:\/\/example.com\/data-deletion",
    "redirectUris": [],
    "postLogoutRedirectUris": [],
    "enabled": True,
    "type": "confidential",
    "deviceFlow": True,
    "teamId": "5e5ea5c16897e",
    "userId": "5e5ea5c16897e",
    "secrets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.update(
            '<APP_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.delete(
            '<APP_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_labels(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Application",
    "description": "Connect your workspace to My Application.",
    "clientUri": "https:\/\/example.com",
    "logoUri": "https:\/\/example.com\/logo.png",
    "privacyPolicyUrl": "https:\/\/example.com\/privacy",
    "termsUrl": "https:\/\/example.com\/terms",
    "contacts": [],
    "tagline": "Automate your workspace.",
    "tags": [],
    "labels": [],
    "images": [],
    "supportUrl": "https:\/\/example.com\/support",
    "dataDeletionUrl": "https:\/\/example.com\/data-deletion",
    "redirectUris": [],
    "postLogoutRedirectUris": [],
    "enabled": True,
    "type": "confidential",
    "deviceFlow": True,
    "teamId": "5e5ea5c16897e",
    "userId": "5e5ea5c16897e",
    "secrets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.update_labels(
            '<APP_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_secrets(self, m):
        data = {
    "total": 5.0,
    "secrets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.list_secrets(
            '<APP_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_secret(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "appId": "5e5ea5c16897e",
    "secret": "5f3c8d2a1b9e4f7a6c8b2d1e9f4a7b3c5d8e1f2a9b4c7d6e3f5a8b1c4d7e2f9a",
    "hint": "f5c6c7",
    "createdById": "5e5ea5c16897e",
    "createdByName": "Walter White"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.create_secret(
            '<APP_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_secret(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "appId": "5e5ea5c16897e",
    "secret": "",
    "hint": "f5c6c7",
    "createdById": "5e5ea5c16897e",
    "createdByName": "Walter White"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.get_secret(
            '<APP_ID>',
            '<SECRET_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_secret(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.delete_secret(
            '<APP_ID>',
            '<SECRET_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_team(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Application",
    "description": "Connect your workspace to My Application.",
    "clientUri": "https:\/\/example.com",
    "logoUri": "https:\/\/example.com\/logo.png",
    "privacyPolicyUrl": "https:\/\/example.com\/privacy",
    "termsUrl": "https:\/\/example.com\/terms",
    "contacts": [],
    "tagline": "Automate your workspace.",
    "tags": [],
    "labels": [],
    "images": [],
    "supportUrl": "https:\/\/example.com\/support",
    "dataDeletionUrl": "https:\/\/example.com\/data-deletion",
    "redirectUris": [],
    "postLogoutRedirectUris": [],
    "enabled": True,
    "type": "confidential",
    "deviceFlow": True,
    "teamId": "5e5ea5c16897e",
    "userId": "5e5ea5c16897e",
    "secrets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.update_team(
            '<APP_ID>',
            '<TEAM_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_tokens(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.apps.delete_tokens(
            '<APP_ID>',
        )

        self.assertEqual(response, data)

