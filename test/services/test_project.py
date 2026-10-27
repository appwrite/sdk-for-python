import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.project import Project


class ProjectServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.project = Project(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
        response = self.project.delete()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_auth_method(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_auth_method(
            'email-password',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/auth-methods/email-password',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_environments(self, m):
        data = {
            "total": 5.0,
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_environments(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments',
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
    def test_create_environment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_environment(
            '<ENVIRONMENT_ID>',
            '<NAME>',
            resources=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'environmentId': '<ENVIRONMENT_ID>',
                'name': '<NAME>',
                'resources': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_environment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_environment(
            '<ENVIRONMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments/<ENVIRONMENT_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_environment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_environment(
            '<ENVIRONMENT_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments/<ENVIRONMENT_ID>',
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
    def test_delete_environment(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_environment(
            '<ENVIRONMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/environments/<ENVIRONMENT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

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
        response = self.project.list_keys(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys',
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
    def test_create_ephemeral_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_ephemeral_key(
            [],
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/ephemeral',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'scopes': [],
                'duration': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_key(
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/<KEY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_key(
            '<KEY_ID>',
            '<NAME>',
            [],
            expire='2020-10-15T06:38:00.000+00:00',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/<KEY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'scopes': [],
                'expire': '2020-10-15T06:38:00.000+00:00',
                'description': '<DESCRIPTION>',
            },
        )
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
        response = self.project.delete_key(
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/keys/<KEY_ID>',
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
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_labels(
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/labels',
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
    def test_list_mock_phones(self, m):
        data = {
            "total": 5.0,
            "mockNumbers": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_mock_phones(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones',
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
    def test_create_mock_phone(self, m):
        data = {
            "number": "+1612842323",
            "otp": "123456",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_mock_phone(
            '+12065550100',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'number': '+12065550100',
                'otp': '<OTP>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mock_phone(self, m):
        data = {
            "number": "+1612842323",
            "otp": "123456",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_mock_phone(
            '+12065550100',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones/+12065550100',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mock_phone(self, m):
        data = {
            "number": "+1612842323",
            "otp": "123456",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_mock_phone(
            '+12065550100',
            '<OTP>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones/+12065550100',
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
    def test_delete_mock_phone(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_mock_phone(
            '+12065550100',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/mock-phones/+12065550100',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_o_auth2_providers(self, m):
        data = {
            "total": 5.0,
            "providers": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_o_auth2_providers(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2',
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
    def test_update_o_auth2_server(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_server(
            False,
            'https://example.com',
            scopes=[],
            authorization_details_types=[],
            access_token_duration=1,
            refresh_token_duration=1,
            public_access_token_duration=1,
            public_refresh_token_duration=1,
            installation_access_token_duration=1,
            confidential_pkce=False,
            verification_url='https://example.com',
            user_code_length=1,
            user_code_format='numeric',
            device_code_duration=1,
            default_scopes=[],
            installation_scopes=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2-server',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
                'authorizationUrl': 'https://example.com',
                'scopes': [],
                'authorizationDetailsTypes': [],
                'accessTokenDuration': 1,
                'refreshTokenDuration': 1,
                'publicAccessTokenDuration': 1,
                'publicRefreshTokenDuration': 1,
                'installationAccessTokenDuration': 1,
                'confidentialPkce': False,
                'verificationUrl': 'https://example.com',
                'userCodeLength': 1,
                'userCodeFormat': 'numeric',
                'deviceCodeDuration': 1,
                'defaultScopes': [],
                'installationScopes': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_amazon(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "amzn1.application-oa2-client.87400c00000000000000000000063d5b2",
            "clientSecret": "79ffe4000000000000000000000000000000000000000000000000000002de55",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_amazon(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/amazon',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_apple(self, m):
        data = {
            "$id": "apple",
            "enabled": True,
            "serviceId": "ip.appwrite.app.web",
            "keyId": "P4000000N8",
            "teamId": "D4000000R6",
            "p8File": "-----BEGIN PRIVATE KEY-----MIGTAg...jy2Xbna-----END PRIVATE KEY-----",
            "nativeEnabled": True,
            "nativeClientIds": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_apple(
            service_id='<SERVICE_ID>',
            key_id='<KEY_ID>',
            team_id='<TEAM_ID>',
            p8_file='<P8_FILE>',
            enabled=False,
            native_client_ids=[],
            native_enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/apple',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'serviceId': '<SERVICE_ID>',
                'keyId': '<KEY_ID>',
                'teamId': '<TEAM_ID>',
                'p8File': '<P8_FILE>',
                'enabled': False,
                'nativeClientIds': [],
                'nativeEnabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_appwrite(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "6a42000000000000b5a0",
            "clientSecret": "b86afd000000000000000000000000000000000000000000000000000ced5f93",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_appwrite(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/appwrite',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_auth0(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "OaOkIA000000000000000000005KLSYq",
            "clientSecret": "zXz0000-00000000000000000000000000000-00000000000000000000PJafnF",
            "prompt": [],
            "endpoint": "example.us.auth0.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_auth0(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            endpoint='<ENDPOINT>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/auth0',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'endpoint': '<ENDPOINT>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_authentik(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "dTKOPa0000000000000000000000000000e7G8hv",
            "clientSecret": "ntQadq000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Hp5WK",
            "endpoint": "example.authentik.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_authentik(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            endpoint='<ENDPOINT>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/authentik',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'endpoint': '<ENDPOINT>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_autodesk(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "5zw90v00000000000000000000kVYXN7",
            "clientSecret": "7I000000000000MW",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_autodesk(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/autodesk',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_bitbucket(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "key": "Knt70000000000ByRc",
            "secret": "NMfLZJ00000000000000000000TLQdDx",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_bitbucket(
            key='<KEY>',
            secret='<SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/bitbucket',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'secret': '<SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_bitly(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "d95151000000000000000000000000000067af9b",
            "clientSecret": "a13e250000000000000000000000000000d73095",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_bitly(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/bitly',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_box(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "deglcs00000000000000000000x2og6y",
            "clientSecret": "OKM1f100000000000000000000eshEif",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_box(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/box',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_cloudflare(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "4b866000000000000000000000c9e4e2",
            "clientSecret": "cfoc_5Q6YRl0000000000000000000000000000000000003d214f",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_cloudflare(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/cloudflare',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_dailymotion(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "apiKey": "07a9000000000000067f",
            "apiSecret": "a399a90000000000000000000000000000d90639",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_dailymotion(
            api_key='<API_KEY>',
            api_secret='<API_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/dailymotion',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'apiKey': '<API_KEY>',
                'apiSecret': '<API_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_discord(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "950722000000343754",
            "clientSecret": "YmPXnM000000000000000000002zFg5D",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_discord(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/discord',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_disqus(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "publicKey": "cgegH70000000000000000000000000000000000000000000000000000Hr1nYX",
            "secretKey": "W7Bykj00000000000000000000000000000000000000000000000000003o43w9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_disqus(
            public_key='<PUBLIC_KEY>',
            secret_key='<SECRET_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/disqus',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'publicKey': '<PUBLIC_KEY>',
                'secretKey': '<SECRET_KEY>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_dropbox(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "appKey": "jl000000000009t",
            "appSecret": "g200000000000vw",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_dropbox(
            app_key='<APP_KEY>',
            app_secret='<APP_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/dropbox',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'appKey': '<APP_KEY>',
                'appSecret': '<APP_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_etsy(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "keyString": "nsgzxh0000000000008j85a2",
            "sharedSecret": "tp000000ru",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_etsy(
            key_string='<KEY_STRING>',
            shared_secret='<SHARED_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/etsy',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'keyString': '<KEY_STRING>',
                'sharedSecret': '<SHARED_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_facebook(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "appId": "260600000007694",
            "appSecret": "2d0b2800000000000000000000d38af4",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_facebook(
            app_id='<APP_ID>',
            app_secret='<APP_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/facebook',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'appId': '<APP_ID>',
                'appSecret': '<APP_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_figma(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "byay5H0000000000VtiI40",
            "clientSecret": "yEpOYn0000000000000000004iIsU5",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_figma(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/figma',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_fusion_auth(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "b2222c00-0000-0000-0000-000000862097",
            "clientSecret": "Jx4s0C0000000000000000000000000000000wGqLsc",
            "endpoint": "example.fusionauth.io",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_fusion_auth(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            endpoint='<ENDPOINT>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/fusionauth',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'endpoint': '<ENDPOINT>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_git_hub(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "e4d87900000000540733",
            "clientSecret": "5e07c00000000000000000000000000000198bcc",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_git_hub(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/github',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_gitlab(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "applicationId": "d41ffe0000000000000000000000000000000000000000000000000000d5e252",
            "secret": "gloas-838cfa0000000000000000000000000000000000000000000000000000ecbb38",
            "endpoint": "https:\/\/gitlab.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_gitlab(
            application_id='<APPLICATION_ID>',
            secret='<SECRET>',
            endpoint='https://example.com',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/gitlab',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'applicationId': '<APPLICATION_ID>',
                'secret': '<SECRET>',
                'endpoint': 'https://example.com',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_google(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "120000000095-92ifjb00000000000000000000g7ijfb.apps.googleusercontent.com",
            "clientSecret": "GOCSPX-2k8gsR0000000000000000VNahJj",
            "prompt": [],
            "nativeEnabled": True,
            "nativeClientIds": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_google(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            prompt=[],
            enabled=False,
            native_client_ids=[],
            native_enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/google',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'prompt': [],
                'enabled': False,
                'nativeClientIds': [],
                'nativeEnabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_hugging_face(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "2ab9cff9-d711-40ad-a91e-b08a49c42d24",
            "clientSecret": "oauth_app_secret_wcLhRtl000000000000000000000xbNdLt",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_hugging_face(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/huggingface',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_kakao(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "839ff5000000000000000000013206de",
            "clientSecret": "jLNVOK00000000000000000000yJebea",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_kakao(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/kakao',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_keycloak(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "appwrite-o0000000st-app",
            "clientSecret": "jdjrJd00000000000000000000HUsaZO",
            "endpoint": "keycloak.example.com",
            "realmName": "appwrite-realm",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_keycloak(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            endpoint='<ENDPOINT>',
            realm_name='<REALM_NAME>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/keycloak',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'endpoint': '<ENDPOINT>',
                'realmName': '<REALM_NAME>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_kick(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "01KQ7C00000000000001MFHS32",
            "clientSecret": "34ac5600000000000000000000000000000000000000000000000000e830c8b",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_kick(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/kick',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_linkedin(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "770000000000dv",
            "primaryClientSecret": "WPL_AP1.2Bf0000000000000.\/HtlYw==",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_linkedin(
            client_id='<CLIENT_ID>',
            primary_client_secret='<PRIMARY_CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/linkedin',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'primaryClientSecret': '<PRIMARY_CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_microsoft(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "applicationId": "00001111-aaaa-2222-bbbb-3333cccc4444",
            "applicationSecret": "A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",
            "prompt": [],
            "tenant": "common",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_microsoft(
            application_id='<APPLICATION_ID>',
            application_secret='<APPLICATION_SECRET>',
            tenant='<TENANT>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/microsoft',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'applicationId': '<APPLICATION_ID>',
                'applicationSecret': '<APPLICATION_SECRET>',
                'tenant': '<TENANT>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_notion(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "oauthClientId": "341d8700-0000-0000-0000-000000446ee3",
            "oauthClientSecret": "secret_dLUr4b000000000000000000000000000000lFHAa9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_notion(
            oauth_client_id='<OAUTH_CLIENT_ID>',
            oauth_client_secret='<OAUTH_CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/notion',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'oauthClientId': '<OAUTH_CLIENT_ID>',
                'oauthClientSecret': '<OAUTH_CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_oidc(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "qibI2x0000000000000000000000000006L2YFoG",
            "clientSecret": "Ah68ed000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003qpcHV",
            "prompt": [],
            "wellKnownURL": "https:\/\/myoauth.com\/.well-known\/openid-configuration",
            "authorizationURL": "https:\/\/myoauth.com\/oauth2\/authorize",
            "tokenURL": "https:\/\/myoauth.com\/oauth2\/token",
            "userInfoURL": "https:\/\/myoauth.com\/oauth2\/userinfo",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_oidc(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            well_known_url='https://example.com',
            authorization_url='https://example.com',
            token_url='https://example.com',
            user_info_url='https://example.com',
            prompt=[],
            max_age=1,
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/oidc',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'wellKnownURL': 'https://example.com',
                'authorizationURL': 'https://example.com',
                'tokenURL': 'https://example.com',
                'userInfoURL': 'https://example.com',
                'prompt': [],
                'maxAge': 1,
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_okta(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "0oa00000000000000698",
            "clientSecret": "Kiq0000000000000000000000000000000000000-00000000000H2L5-3SJ-vRV",
            "prompt": [],
            "domain": "trial-6400025.okta.com",
            "authorizationServerId": "aus000000000000000h7z",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_okta(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            domain='example.com',
            authorization_server_id='<AUTHORIZATION_SERVER_ID>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/okta',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'domain': 'example.com',
                'authorizationServerId': '<AUTHORIZATION_SERVER_ID>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_paypal(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB",
            "secretKey": "EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_paypal(
            client_id='<CLIENT_ID>',
            secret_key='<SECRET_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/paypal',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'secretKey': '<SECRET_KEY>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_paypal_sandbox(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB",
            "secretKey": "EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_paypal_sandbox(
            client_id='<CLIENT_ID>',
            secret_key='<SECRET_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/paypalSandbox',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'secretKey': '<SECRET_KEY>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_podio(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "appwrite-oauth-test-app",
            "clientSecret": "Rn247T0000000000000000000000000000000000000000000000000000W2zWTN",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_podio(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/podio',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_resend(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
            "clientSecret": "9c1e4b00000000000000000000000000000000000000000000000000a72d5f4",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_resend(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/resend',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_salesforce(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "customerKey": "3MVG9I0000000000000000000000000000000000000000000000000000000000000000000000000C5Aejq",
            "customerSecret": "3w000000000000e2",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_salesforce(
            customer_key='<CUSTOMER_KEY>',
            customer_secret='<CUSTOMER_SECRET>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/salesforce',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'customerKey': '<CUSTOMER_KEY>',
                'customerSecret': '<CUSTOMER_SECRET>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_slack(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "23000000089.15000000000023",
            "clientSecret": "81656000000000000000000000f3d2fd",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_slack(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/slack',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_spotify(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "6ec271000000000000000000009beace",
            "clientSecret": "db068a000000000000000000008b5b9f",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_spotify(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/spotify',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_stripe(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "ca_UKibXX0000000000000000000006byvR",
            "apiSecretKey": "sk_51SfOd000000000000000000000000000000000000000000000000000000000000000000000000000000000000000QGWYfp",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_stripe(
            client_id='<CLIENT_ID>',
            api_secret_key='<API_SECRET_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/stripe',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'apiSecretKey': '<API_SECRET_KEY>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tik_tok(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "awz000000000tyw0",
            "clientSecret": "6wXewM00000000000000000000yXnite",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_tik_tok(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/tiktok',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tradeshift(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "oauth2ClientId": "appwrite-test-org.appwrite-test-app",
            "oauth2ClientSecret": "7cb52700-0000-0000-0000-000000ca5b83",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_tradeshift(
            oauth2_client_id='<OAUTH2_CLIENT_ID>',
            oauth2_client_secret='<OAUTH2_CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/tradeshift',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'oauth2ClientId': '<OAUTH2_CLIENT_ID>',
                'oauth2ClientSecret': '<OAUTH2_CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tradeshift_sandbox(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "oauth2ClientId": "appwrite-test-org.appwrite-test-app",
            "oauth2ClientSecret": "7cb52700-0000-0000-0000-000000ca5b83",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_tradeshift_sandbox(
            oauth2_client_id='<OAUTH2_CLIENT_ID>',
            oauth2_client_secret='<OAUTH2_CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/tradeshiftBox',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'oauth2ClientId': '<OAUTH2_CLIENT_ID>',
                'oauth2ClientSecret': '<OAUTH2_CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_twitch(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "vvi0in000000000000000000ikmt9p",
            "clientSecret": "pmapue000000000000000000zylw3v",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_twitch(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/twitch',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_webflow(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "8bb20000000000000000000000000000000000000000000000000000000040dd",
            "clientSecret": "59bf00000000000000000000000000000000000000000000000000000000fe59",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_webflow(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/webflow',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_word_press(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "130005",
            "clientSecret": "PlBfJS0000000000000000000000000000000000000000000000000000EdUZJk",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_word_press(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/wordpress',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_x(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "customerKey": "slzZV0000000000000NFLaWT",
            "secretKey": "tkEPkp00000000000000000000000000000000000000FTxbI9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_x(
            customer_key='<CUSTOMER_KEY>',
            secret_key='<SECRET_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/x',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'customerKey': '<CUSTOMER_KEY>',
                'secretKey': '<SECRET_KEY>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_yahoo(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "dj0yJm000000000000000000000000000000000000000000000000000000000000000000000000000000000000Z4PWRm",
            "clientSecret": "cf978f0000000000000000000000000000c5e2e9",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_yahoo(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/yahoo',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_yandex(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "6a8a6a0000000000000000000091483c",
            "clientSecret": "bbf98500000000000000000000c75a63",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_yandex(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/yandex',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_zoho(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "1000.83C178000000000000000000RPNX0B",
            "clientSecret": "fb5cac000000000000000000000000000000a68f6e",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_zoho(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
            prompt=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/zoho',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
                'prompt': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_zoom(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "QMAC00000000000000w0AQ",
            "clientSecret": "GAWsG4000000000000000000007U01ON",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_o_auth2_zoom(
            client_id='<CLIENT_ID>',
            client_secret='<CLIENT_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/zoom',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'clientId': '<CLIENT_ID>',
                'clientSecret': '<CLIENT_SECRET>',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_o_auth2_provider(self, m):
        data = {
            "$id": "github",
            "enabled": True,
            "clientId": "e4d87900000000540733",
            "clientSecret": "5e07c00000000000000000000000000000198bcc",
            "prompt": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_o_auth2_provider(
            'amazon',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/oauth2/amazon',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_platforms(self, m):
        data = {
            "total": 5.0,
            "platforms": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_platforms(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms',
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
    def test_create_android_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "applicationId": "com.company.appname",
            "fingerprints": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_android_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<APPLICATION_ID>',
            fingerprints=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/android',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'platformId': '<PLATFORM_ID>',
                'name': '<NAME>',
                'applicationId': '<APPLICATION_ID>',
                'fingerprints': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_android_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "applicationId": "com.company.appname",
            "fingerprints": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_android_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<APPLICATION_ID>',
            fingerprints=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/android/<PLATFORM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'applicationId': '<APPLICATION_ID>',
                'fingerprints': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_apple_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "bundleIdentifier": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_apple_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<BUNDLE_IDENTIFIER>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/apple',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'platformId': '<PLATFORM_ID>',
                'name': '<NAME>',
                'bundleIdentifier': '<BUNDLE_IDENTIFIER>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_apple_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "bundleIdentifier": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_apple_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<BUNDLE_IDENTIFIER>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/apple/<PLATFORM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'bundleIdentifier': '<BUNDLE_IDENTIFIER>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_linux_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_linux_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/linux',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'platformId': '<PLATFORM_ID>',
                'name': '<NAME>',
                'packageName': '<PACKAGE_NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_linux_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_linux_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/linux/<PLATFORM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'packageName': '<PACKAGE_NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_web_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "hostname": "app.example.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_web_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            'app.example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/web',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'platformId': '<PLATFORM_ID>',
                'name': '<NAME>',
                'hostname': 'app.example.com',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_web_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "hostname": "app.example.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_web_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            'app.example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/web/<PLATFORM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'hostname': 'app.example.com',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_windows_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageIdentifierName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_windows_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_IDENTIFIER_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/windows',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'platformId': '<PLATFORM_ID>',
                'name': '<NAME>',
                'packageIdentifierName': '<PACKAGE_IDENTIFIER_NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_windows_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "packageIdentifierName": "com.company.appname",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_windows_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_IDENTIFIER_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/windows/<PLATFORM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'packageIdentifierName': '<PACKAGE_IDENTIFIER_NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_platform(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Web App",
            "type": "web",
            "hostname": "app.example.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_platform(
            '<PLATFORM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/<PLATFORM_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_platform(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_platform(
            '<PLATFORM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/platforms/<PLATFORM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_policies(self, m):
        data = {
            "total": 10.0,
            "policies": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_policies(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies',
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
    def test_update_deny_aliased_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_aliased_email_policy(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-aliased-email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_corporate_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_corporate_email_policy(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-corporate-email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_disposable_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_disposable_email_policy(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-disposable-email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_free_email_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_free_email_policy(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-free-email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_realtime_guests_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_deny_realtime_guests_policy(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/deny-realtime-guests',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_membership_privacy_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_membership_privacy_policy(
            user_id=False,
            user_email=False,
            user_phone=False,
            user_name=False,
            user_mfa=False,
            user_accessed_at=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/membership-privacy',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': False,
                'userEmail': False,
                'userPhone': False,
                'userName': False,
                'userMFA': False,
                'userAccessedAt': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_factors_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_mfa_factors_policy(
            totp=False,
            email=False,
            phone=False,
            custom=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/mfa-factors',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'totp': False,
                'email': False,
                'phone': False,
                'custom': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_passkey_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_passkey_policy(
            '<RP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/passkey',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'rpId': '<RP_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_dictionary_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_dictionary_policy(
            False,
            deny_list=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-dictionary',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
                'denyList': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_history_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_history_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-history',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'total': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_personal_data_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_personal_data_policy(
            False,
            deny_list=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-personal-data',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
                'denyList': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_pwned_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_pwned_policy(
            enabled=False,
            sessions=False,
            users=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-pwned',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
                'sessions': False,
                'users': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_rotation_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_rotation_policy(
            enabled=False,
            max_age=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-rotation',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
                'maxAge': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_strength_policy(self, m):
        data = {
            "$id": "password-dictionary",
            "min": 12.0,
            "uppercase": True,
            "lowercase": True,
            "number": True,
            "symbols": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_password_strength_policy(
            min=1,
            uppercase=False,
            lowercase=False,
            number=False,
            symbols=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-strength',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'min': 1,
                'uppercase': False,
                'lowercase': False,
                'number': False,
                'symbols': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_alert_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_alert_policy(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-alert',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_duration_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_duration_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-duration',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'duration': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_invalidation_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_invalidation_policy(
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-invalidation',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_limit_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_session_limit_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/session-limit',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'total': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_user_limit_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_user_limit_policy(
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/user-limit',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'total': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_policy(self, m):
        data = {
            "$id": "password-dictionary",
            "enabled": True,
            "denyList": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_policy(
            'password-dictionary',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/policies/password-dictionary',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_protocol(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_protocol(
            'rest',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/protocols/rest',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_service(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_service(
            'account',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/services/account',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'enabled': False,
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
        response = self.project.delete_sessions()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/sessions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_smtp(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_smtp(
            host='example.com',
            port=1,
            username='<USERNAME>',
            password='password',
            sender_email='email@example.com',
            sender_name='<SENDER_NAME>',
            reply_to_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            secure='tls',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/smtp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'host': 'example.com',
                'port': 1,
                'username': '<USERNAME>',
                'password': 'password',
                'senderEmail': 'email@example.com',
                'senderName': '<SENDER_NAME>',
                'replyToEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'secure': 'tls',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_test(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_smtp_test(
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/smtp/tests',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'emails': [],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_email_templates(self, m):
        data = {
            "total": 5.0,
            "templates": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_email_templates(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/templates/email',
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
    def test_update_email_template(self, m):
        data = {
            "templateId": "verification",
            "locale": "en_us",
            "message": "Click on the link to verify your account.",
            "senderName": "My User",
            "senderEmail": "mail@appwrite.io",
            "replyToEmail": "emails@appwrite.io",
            "replyToName": "Support Team",
            "subject": "Please verify your email address",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_email_template(
            'verification',
            locale='af',
            subject='<SUBJECT>',
            message='<MESSAGE>',
            sender_name='<SENDER_NAME>',
            sender_email='email@example.com',
            reply_to_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/templates/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'templateId': 'verification',
                'locale': 'af',
                'subject': '<SUBJECT>',
                'message': '<MESSAGE>',
                'senderName': '<SENDER_NAME>',
                'senderEmail': 'email@example.com',
                'replyToEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_email_template(self, m):
        data = {
            "templateId": "verification",
            "locale": "en_us",
            "message": "Click on the link to verify your account.",
            "senderName": "My User",
            "senderEmail": "mail@appwrite.io",
            "replyToEmail": "emails@appwrite.io",
            "replyToName": "Support Team",
            "subject": "Please verify your email address",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_email_template(
            'verification',
            locale='af',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/templates/email/verification',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'locale': ['af'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_variables(self, m):
        data = {
            "total": 5.0,
            "variables": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.list_variables(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables',
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
    def test_create_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.create_variable(
            '<VARIABLE_ID>',
            '<KEY>',
            '<VALUE>',
            secret=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'variableId': '<VARIABLE_ID>',
                'key': '<KEY>',
                'value': '<VALUE>',
                'secret': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.get_variable(
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables/<VARIABLE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.update_variable(
            '<VARIABLE_ID>',
            key='<KEY>',
            value='<VALUE>',
            secret=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables/<VARIABLE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'value': '<VALUE>',
                'secret': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_variable(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.project.delete_variable(
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/project/variables/<VARIABLE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
