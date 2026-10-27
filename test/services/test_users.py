import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.users import Users


class UsersServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.users = Users(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "users": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
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
        response = self.users.create(
            '<USER_ID>',
            email='email@example.com',
            phone='+12065550100',
            password='password',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'phone': '+12065550100',
                'password': 'password',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_argon2_user(self, m):
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
        response = self.users.create_argon2_user(
            '<USER_ID>',
            'email@example.com',
            '$argon2id$v=19$m=65536,t=4,p=1$NC8xaW1CVXlIZXFSQi9FRg$0bd4pLo1ytyqvCwl5NSijpm5OIe8J6CjZ1vFemKAg+o',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/argon2',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'password': '$argon2id$v=19$m=65536,t=4,p=1$NC8xaW1CVXlIZXFSQi9FRg$0bd4pLo1ytyqvCwl5NSijpm5OIe8J6CjZ1vFemKAg+o',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_bcrypt_user(self, m):
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
        response = self.users.create_bcrypt_user(
            '<USER_ID>',
            'email@example.com',
            '$2y$10$vBiMe4NOvlbYL1iJUNdqkO.QJy17fvslZQ5oiqKq1G4uwyRWvdrXC',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/bcrypt',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'password': '$2y$10$vBiMe4NOvlbYL1iJUNdqkO.QJy17fvslZQ5oiqKq1G4uwyRWvdrXC',
                'name': '<NAME>',
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
        response = self.users.list_identities(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/identities',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
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
        response = self.users.delete_identity(
            '<IDENTITY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/identities/<IDENTITY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_md5_user(self, m):
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
        response = self.users.create_md5_user(
            '<USER_ID>',
            'email@example.com',
            'password',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/md5',
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
    def test_create_ph_pass_user(self, m):
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
        response = self.users.create_ph_pass_user(
            '<USER_ID>',
            'email@example.com',
            '$P$BrOEFP1YR5W1yHpvvGuoeVUDPmw9ra/',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/phpass',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'password': '$P$BrOEFP1YR5W1yHpvvGuoeVUDPmw9ra/',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_scrypt_user(self, m):
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
        response = self.users.create_scrypt_user(
            '<USER_ID>',
            'email@example.com',
            'password',
            '<PASSWORD_SALT>',
            1,
            1,
            1,
            1,
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/scrypt',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'password': 'password',
                'passwordSalt': '<PASSWORD_SALT>',
                'passwordCpu': 1,
                'passwordMemory': 1,
                'passwordParallel': 1,
                'passwordLength': 1,
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_scrypt_modified_user(self, m):
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
        response = self.users.create_scrypt_modified_user(
            '<USER_ID>',
            'email@example.com',
            'password',
            '<PASSWORD_SALT>',
            '<PASSWORD_SALT_SEPARATOR>',
            '<PASSWORD_SIGNER_KEY>',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/scrypt-modified',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'password': 'password',
                'passwordSalt': '<PASSWORD_SALT>',
                'passwordSaltSeparator': '<PASSWORD_SALT_SEPARATOR>',
                'passwordSignerKey': '<PASSWORD_SIGNER_KEY>',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_sha_user(self, m):
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
        response = self.users.create_sha_user(
            '<USER_ID>',
            'email@example.com',
            'password',
            password_version='sha1',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/sha',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'email': 'email@example.com',
                'password': 'password',
                'passwordVersion': 'sha1',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

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
        response = self.users.get(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>',
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
        response = self.users.delete(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>',
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
        response = self.users.update_email(
            '<USER_ID>',
            'email@example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_impersonator(self, m):
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
        response = self.users.update_impersonator(
            '<USER_ID>',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/impersonator',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'impersonator': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_jwt(self, m):
        data = {
            "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.create_jwt(
            '<USER_ID>',
            session_id='recent()',
            duration=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/jwts',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'sessionId': 'recent()',
                'duration': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_labels(self, m):
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
        response = self.users.update_labels(
            '<USER_ID>',
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/labels',
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
        response = self.users.list_memberships(
            '<USER_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/memberships',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
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
        response = self.users.update_mfa(
            '<USER_ID>',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa',
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
        response = self.users.update_mfa(
            '<USER_ID>',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa',
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
    def test_delete_mfa_authenticator(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.delete_mfa_authenticator(
            '<USER_ID>',
            'totp',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/authenticators/totp',
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
        response = self.users.delete_mfa_authenticator(
            '<USER_ID>',
            'totp',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/authenticators/totp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_mfa_challenge(self, m):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "code": "446372",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.get_mfa_challenge(
            '<USER_ID>',
            '<CHALLENGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/challenges/<CHALLENGE_ID>',
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
        response = self.users.list_mfa_factors(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/factors',
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
        response = self.users.list_mfa_factors(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/factors',
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
        response = self.users.get_mfa_recovery_codes(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/recovery-codes',
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
        response = self.users.get_mfa_recovery_codes(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/recovery-codes',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_recovery_codes(self, m):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.update_mfa_recovery_codes(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/recovery-codes',
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
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.update_mfa_recovery_codes(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/recovery-codes',
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
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.create_mfa_recovery_codes(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/recovery-codes',
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
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.create_mfa_recovery_codes(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/mfa/recovery-codes',
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
        response = self.users.update_name(
            '<USER_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/name',
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
        response = self.users.list_passkeys(
            '<USER_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/passkeys',
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
        response = self.users.get_passkey(
            '<USER_ID>',
            '<PASSKEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/passkeys/<PASSKEY_ID>',
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
        response = self.users.update_passkey(
            '<USER_ID>',
            '<PASSKEY_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/passkeys/<PASSKEY_ID>',
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
        response = self.users.delete_passkey(
            '<USER_ID>',
            '<PASSKEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/passkeys/<PASSKEY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

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
        response = self.users.update_password(
            '<USER_ID>',
            'password',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/password',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'password': 'password',
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
        response = self.users.update_phone(
            '<USER_ID>',
            '+12065550100',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/phone',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'number': '+12065550100',
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
        response = self.users.get_prefs(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/prefs',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.update_prefs(
            '<USER_ID>',
            {},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/prefs',
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
        response = self.users.list_sessions(
            '<USER_ID>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/sessions',
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
        response = self.users.create_session(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/sessions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
        response = self.users.delete_sessions(
            '<USER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/sessions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

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
        response = self.users.delete_session(
            '<USER_ID>',
            '<SESSION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/sessions/<SESSION_ID>',
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
        response = self.users.update_status(
            '<USER_ID>',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/status',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'status': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_targets(self, m):
        data = {
            "total": 5.0,
            "targets": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.list_targets(
            '<USER_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/targets',
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
    def test_create_target(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Apple iPhone 12",
            "userId": "259125845563242502",
            "providerType": "email",
            "identifier": "token",
            "expired": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.create_target(
            '<USER_ID>',
            '<TARGET_ID>',
            'email',
            '<IDENTIFIER>',
            provider_id='<PROVIDER_ID>',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/targets',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'targetId': '<TARGET_ID>',
                'providerType': 'email',
                'identifier': '<IDENTIFIER>',
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_target(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Apple iPhone 12",
            "userId": "259125845563242502",
            "providerType": "email",
            "identifier": "token",
            "expired": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.get_target(
            '<USER_ID>',
            '<TARGET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/targets/<TARGET_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_target(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Apple iPhone 12",
            "userId": "259125845563242502",
            "providerType": "email",
            "identifier": "token",
            "expired": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.update_target(
            '<USER_ID>',
            '<TARGET_ID>',
            identifier='<IDENTIFIER>',
            provider_id='<PROVIDER_ID>',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/targets/<TARGET_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'identifier': '<IDENTIFIER>',
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_target(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.users.delete_target(
            '<USER_ID>',
            '<TARGET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/targets/<TARGET_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_token(self, m):
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
        response = self.users.create_token(
            '<USER_ID>',
            length=1,
            expire=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/tokens',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'length': 1,
                'expire': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_verification(self, m):
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
        response = self.users.update_email_verification(
            '<USER_ID>',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/verification',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'emailVerification': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_phone_verification(self, m):
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
        response = self.users.update_phone_verification(
            '<USER_ID>',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/users/<USER_ID>/verification/phone',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'phoneVerification': False,
            },
        )
        self.assertEqual(response.to_dict(), data)
