import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.account import Account


class AccountServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.account = Account(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
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
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
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
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create(
            '<USER_ID>',
            'email@example.com',
            'password',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'password': 'password',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_consents(self, m):
        data = {
            "total": 5.0,
            "consents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_consents(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/consents',
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
    def test_get_consent(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "appId": "5e5ea5c16897e",
            "cimdUrl": "https:\/\/example.com\/.well-known\/client-metadata.json",
            "scopes": [],
            "resources": [],
            "authorizationDetails": "[{\"type\":\"calendar\",\"identifier\":\"primary\",\"actions\":[\"read_events\",\"create_event\"]}]",
            "expire": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get_consent(
            '<CONSENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/consents/<CONSENT_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_consent(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_consent(
            '<CONSENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/consents/<CONSENT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_consent_tokens(self, m):
        data = {
            "total": 5.0,
            "tokens": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_consent_tokens(
            '<CONSENT_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/consents/<CONSENT_ID>/tokens',
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
    def test_get_consent_token(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "consentId": "5e5ea5c16897e",
            "userId": "5e5ea5c16897e",
            "appId": "5e5ea5c16897e",
            "cimdUrl": "https:\/\/example.com\/.well-known\/client-metadata.json",
            "scopes": [],
            "resources": [],
            "authorizationDetails": "[{\"type\":\"calendar\",\"identifier\":\"primary\",\"actions\":[\"read_events\",\"create_event\"]}]",
            "expire": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get_consent_token(
            '<CONSENT_ID>',
            '<TOKEN_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/consents/<CONSENT_ID>/tokens/<TOKEN_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_consent_token(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_consent_token(
            '<CONSENT_ID>',
            '<TOKEN_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/consents/<CONSENT_ID>/tokens/<TOKEN_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_email(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_email(
            'email@example.com',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
                'password': 'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_identities(self, m):
        data = {
            "total": 5.0,
            "identities": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_identities(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/identities',
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
    def test_delete_identity(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_identity(
            '<IDENTITY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/identities/<IDENTITY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_memberships(self, m):
        data = {
            "total": 5.0,
            "memberships": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_memberships(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/memberships',
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
    def test_update_mfa(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_mfa(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'mfa': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_authenticator(self, m):
        data = {
            "secret": "[SHARED_SECRET]",
            "uri": "otpauth:\/\/totp\/appwrite:user@example.com?secret=[SHARED_SECRET]&issuer=appwrite",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_mfa_authenticator(
            'totp',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/authenticators/totp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_authenticator(self, m):
        data = {
            "secret": "[SHARED_SECRET]",
            "uri": "otpauth:\/\/totp\/appwrite:user@example.com?secret=[SHARED_SECRET]&issuer=appwrite",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_mfa_authenticator(
            'totp',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/authenticators/totp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_authenticator(self, m):
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
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_mfa_authenticator(
            'totp',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/authenticators/totp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'otp': '<OTP>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_authenticator(self, m):
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
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_mfa_authenticator(
            'totp',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/authenticators/totp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'otp': '<OTP>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_mfa_authenticator(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_mfa_authenticator(
            'totp',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/authenticators/totp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_delete_mfa_authenticator(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_mfa_authenticator(
            'totp',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/authenticators/totp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_mfa_challenge(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "expire": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_mfa_challenge(
            'email',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/challenges',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'factor': 'email',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_challenge(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "expire": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_mfa_challenge(
            'email',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/challenges',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'factor': 'email',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_challenge(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_mfa_challenge(
            '<CHALLENGE_ID>',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/challenges',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'challengeId': '<CHALLENGE_ID>',
                'otp': '<OTP>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_challenge(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_mfa_challenge(
            '<CHALLENGE_ID>',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/challenges',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'challengeId': '<CHALLENGE_ID>',
                'otp': '<OTP>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_mfa_factors(self, m):
        data = {
            "totp": True,
            "phone": True,
            "email": True,
            "recoveryCode": True,
            "custom": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_mfa_factors()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/factors',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_mfa_factors(self, m):
        data = {
            "totp": True,
            "phone": True,
            "email": True,
            "recoveryCode": True,
            "custom": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_mfa_factors()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/factors',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mfa_recovery_codes(self, m):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get_mfa_recovery_codes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/recovery-codes',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mfa_recovery_codes(self, m):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get_mfa_recovery_codes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/recovery-codes',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_recovery_codes(self, m):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_mfa_recovery_codes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/recovery-codes',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_recovery_codes(self, m):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_mfa_recovery_codes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/recovery-codes',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_recovery_codes(self, m):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_mfa_recovery_codes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/recovery-codes',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_recovery_codes(self, m):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_mfa_recovery_codes()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/mfa/recovery-codes',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_name(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_name(
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/name',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_passkeys(self, m):
        data = {
            "total": 5.0,
            "passkeys": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_passkeys(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/passkeys',
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
    def test_create_passkey(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "passkeyId": "5e5ea5c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "publicKey": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_passkey(
            passkey_id='<PASSKEY_ID>',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/passkeys',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'passkeyId': '<PASSKEY_ID>',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_passkey(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My laptop",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get_passkey(
            '<PASSKEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/passkeys/<PASSKEY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_passkey(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My laptop",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_passkey(
            '<PASSKEY_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/passkeys/<PASSKEY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_passkey(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_passkey(
            '<PASSKEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/passkeys/<PASSKEY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_passkey_verification(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My laptop",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_passkey_verification(
            '<PASSKEY_ID>',
            {},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/passkeys/<PASSKEY_ID>/verification',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'credential': {},
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_password(
            'password',
            old_password='password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/password',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'password': 'password',
                'oldPassword': 'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_phone(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_phone(
            '+12065550100',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/phone',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'phone': '+12065550100',
                'password': 'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get_prefs()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/prefs',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_prefs(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_prefs(
            {},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/prefs',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'prefs': {},
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_recovery(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_recovery(
            'email@example.com',
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/recovery',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
                'url': 'https://example.com',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_recovery(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_recovery(
            '<USER_ID>',
            '<SECRET>',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/recovery',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
                'password': 'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_recovery_otp(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_recovery_otp(
            'email@example.com',
            phrase=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/recovery/otp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
                'phrase': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_recovery_otp(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_recovery_otp(
            '<USER_ID>',
            '<SECRET>',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/recovery/otp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
                'password': 'password',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_sessions(self, m):
        data = {
            "total": 5.0,
            "sessions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.list_sessions(
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions',
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
    def test_delete_sessions(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_sessions(
            current=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'current': False,
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_anonymous_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_anonymous_session()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/anonymous',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_password_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_email_password_session(
            'email@example.com',
            'password',
            duration=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
                'password': 'password',
                'duration': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_id_token_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_id_token_session(
            'apple',
            '<ID_TOKEN>',
            nonce='<NONCE>',
            access_token='<ACCESS_TOKEN>',
            access_token_expiry=1,
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/id-token',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'provider': 'apple',
                'idToken': '<ID_TOKEN>',
                'nonce': '<NONCE>',
                'accessToken': '<ACCESS_TOKEN>',
                'accessTokenExpiry': 1,
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_magic_url_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_magic_url_session(
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/magic-url',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_phone_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_phone_session(
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/phone',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_session(
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/token',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.get_session(
            '<SESSION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/<SESSION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5bb8c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "provider": "email",
            "providerUid": "user@example.com",
            "providerAccessToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "providerAccessTokenExpiry": "2020-10-15T06:38:00.000+00:00",
            "providerRefreshToken": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
            "ip": "127.0.0.1",
            "osCode": "Mac",
            "osName": "Mac",
            "osVersion": "Mac",
            "clientType": "browser",
            "clientCode": "CM",
            "clientName": "Chrome Mobile iOS",
            "clientVersion": "84.0",
            "clientEngine": "WebKit",
            "clientEngineVersion": "605.1.15",
            "deviceName": "smartphone",
            "deviceBrand": "Google",
            "deviceModel": "Nexus 5",
            "countryCode": "US",
            "countryName": "United States",
            "current": True,
            "factors": [],
            "secret": "5e5bb8c16897e",
            "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_session(
            '<SESSION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/<SESSION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_session(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.delete_session(
            '<SESSION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/sessions/<SESSION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_status(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_status()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/status',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_token(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_email_token(
            '<USER_ID>',
            'email@example.com',
            phrase=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/tokens/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'phrase': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_magic_url_token(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_magic_url_token(
            '<USER_ID>',
            'email@example.com',
            url='https://example.com',
            phrase=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/tokens/magic-url',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'url': 'https://example.com',
                'phrase': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_o_auth2_token(self, m):
        data = None
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_o_auth2_token(
            'amazon',
            success='https://example.com',
            failure='https://example.com',
            scopes=[],
            state='<STATE>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/tokens/oauth2/amazon',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'success': ['https://example.com'],
                'failure': ['https://example.com'],
                'state': ['<STATE>'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_passkey_token(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "passkeyId": "5e5ea5c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "publicKey": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_passkey_token()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/tokens/passkey',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_passkey_token(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_passkey_token(
            '<CHALLENGE_ID>',
            {},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/tokens/passkey',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'challengeId': '<CHALLENGE_ID>',
                'credential': {},
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_phone_token(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_phone_token(
            '<USER_ID>',
            '+12065550100',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/tokens/phone',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'phone': '+12065550100',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_verification(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_email_verification(
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'url': 'https://example.com',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_verification(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_verification(
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'url': 'https://example.com',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_verification(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_email_verification(
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_verification(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_verification(
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_verification_otp(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_email_verification_otp(
            phrase=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/email/otp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'phrase': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_verification_otp(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_email_verification_otp(
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/email/otp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_phone_verification(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.create_phone_verification()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/phone',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_phone_verification(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.account.update_phone_verification(
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/account/verifications/phone',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)
