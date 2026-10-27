import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            "apps": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.list(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps',
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
            "installationScopes": [],
            "installationRedirectUrl": "https:\/\/example.com\/setup",
            "secrets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.create(
            '<APP_ID>',
            '<NAME>',
            [],
            description='<DESCRIPTION>',
            client_uri='https://example.com',
            logo_uri='https://example.com',
            privacy_policy_url='https://example.com',
            terms_url='https://example.com',
            contacts=[],
            tagline='<TAGLINE>',
            tags=[],
            images=[],
            support_url='https://example.com',
            data_deletion_url='https://example.com',
            post_logout_redirect_uris=[],
            enabled=False,
            type='public',
            device_flow=False,
            team_id='<TEAM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'appId': '<APP_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'clientUri': 'https://example.com',
                'logoUri': 'https://example.com',
                'privacyPolicyUrl': 'https://example.com',
                'termsUrl': 'https://example.com',
                'contacts': [],
                'tagline': '<TAGLINE>',
                'tags': [],
                'images': [],
                'supportUrl': 'https://example.com',
                'dataDeletionUrl': 'https://example.com',
                'redirectUris': [],
                'postLogoutRedirectUris': [],
                'enabled': False,
                'type': 'public',
                'deviceFlow': False,
                'teamId': '<TEAM_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_installation_scopes(self, m):
        data = {
            "total": 5.0,
            "scopes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.list_installation_scopes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/scopes/installations',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_o_auth2_scopes(self, m):
        data = {
            "total": 5.0,
            "scopes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.list_o_auth2_scopes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/scopes/oauth2',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
            "installationScopes": [],
            "installationRedirectUrl": "https:\/\/example.com\/setup",
            "secrets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.get(
            '<APP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>',
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
            "installationScopes": [],
            "installationRedirectUrl": "https:\/\/example.com\/setup",
            "secrets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.update(
            '<APP_ID>',
            '<NAME>',
            description='<DESCRIPTION>',
            client_uri='https://example.com',
            logo_uri='https://example.com',
            privacy_policy_url='https://example.com',
            terms_url='https://example.com',
            contacts=[],
            tagline='<TAGLINE>',
            tags=[],
            images=[],
            support_url='https://example.com',
            data_deletion_url='https://example.com',
            enabled=False,
            redirect_uris=[],
            post_logout_redirect_uris=[],
            type='public',
            device_flow=False,
            installation_scopes=[],
            installation_redirect_url='https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'clientUri': 'https://example.com',
                'logoUri': 'https://example.com',
                'privacyPolicyUrl': 'https://example.com',
                'termsUrl': 'https://example.com',
                'contacts': [],
                'tagline': '<TAGLINE>',
                'tags': [],
                'images': [],
                'supportUrl': 'https://example.com',
                'dataDeletionUrl': 'https://example.com',
                'enabled': False,
                'redirectUris': [],
                'postLogoutRedirectUris': [],
                'type': 'public',
                'deviceFlow': False,
                'installationScopes': [],
                'installationRedirectUrl': 'https://example.com',
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
        response = self.apps.delete(
            '<APP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_installations(self, m):
        data = {
            "total": 5.0,
            "installations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.list_installations(
            '<APP_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/installations',
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
    def test_get_installation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "scopes": [],
            "authorizationDetails": [],
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.get_installation(
            '<APP_ID>',
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/installations/<INSTALLATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_installation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.delete_installation(
            '<APP_ID>',
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/installations/<INSTALLATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_installation_token(self, m):
        data = {
            "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...",
            "token_type": "Bearer",
            "expires_in": 3600.0,
            "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
            "scope": "openid email profile",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.create_installation_token(
            '<APP_ID>',
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/installations/<INSTALLATION_ID>/tokens',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_keys(self, m):
        data = {
            "total": 5.0,
            "keys": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.list_keys(
            '<APP_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/keys',
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
    def test_create_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "secret": "5f3c8d2a1b9e4f7a6c8b2d1e9f4a7b3c5d8e1f2a9b4c7d6e3f5a8b1c4d7e2f9a",
            "hint": "f5c6c7",
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.create_key(
            '<APP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/keys',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "secret": "5f3c8d2a1b9e4f7a6c8b2d1e9f4a7b3c5d8e1f2a9b4c7d6e3f5a8b1c4d7e2f9a",
            "hint": "f5c6c7",
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.get_key(
            '<APP_ID>',
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/keys/<KEY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_key(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.delete_key(
            '<APP_ID>',
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/keys/<KEY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            "installationScopes": [],
            "installationRedirectUrl": "https:\/\/example.com\/setup",
            "secrets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.update_labels(
            '<APP_ID>',
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/labels',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'labels': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_secrets(self, m):
        data = {
            "total": 5.0,
            "secrets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.list_secrets(
            '<APP_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/secrets',
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
    def test_create_secret(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "secret": "5f3c8d2a1b9e4f7a6c8b2d1e9f4a7b3c5d8e1f2a9b4c7d6e3f5a8b1c4d7e2f9a",
            "hint": "f5c6c7",
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.create_secret(
            '<APP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/secrets',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.get_secret(
            '<APP_ID>',
            '<SECRET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/secrets/<SECRET_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_secret(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.delete_secret(
            '<APP_ID>',
            '<SECRET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/secrets/<SECRET_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            "installationScopes": [],
            "installationRedirectUrl": "https:\/\/example.com\/setup",
            "secrets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.update_team(
            '<APP_ID>',
            '<TEAM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/team',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'teamId': '<TEAM_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_tokens(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.apps.delete_tokens(
            '<APP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/apps/<APP_ID>/tokens',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
