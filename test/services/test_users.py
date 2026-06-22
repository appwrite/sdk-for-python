import json
import requests_mock
import unittest

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
    "users": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list(
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create(
            '<USER_ID>',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_argon2_user(
            '<USER_ID>',
            'email@example.com',
            'password',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_bcrypt_user(
            '<USER_ID>',
            'email@example.com',
            'password',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_identities(self, m):
        data = {
    "total": 5.0,
    "identities": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list_identities(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_identity(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.delete_identity(
            '<IDENTITY_ID>',
        )

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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_md5_user(
            '<USER_ID>',
            'email@example.com',
            'password',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_ph_pass_user(
            '<USER_ID>',
            'email@example.com',
            'password',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_scrypt_user(
            '<USER_ID>',
            'email@example.com',
            'password',
            '<PASSWORD_SALT>',
            1,
            1,
            1,
            1,
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_scrypt_modified_user(
            '<USER_ID>',
            'email@example.com',
            'password',
            '<PASSWORD_SALT>',
            '<PASSWORD_SALT_SEPARATOR>',
            '<PASSWORD_SIGNER_KEY>',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_sha_user(
            '<USER_ID>',
            'email@example.com',
            'password',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.get(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.delete(
            '<USER_ID>',
        )

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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_email(
            '<USER_ID>',
            'email@example.com',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_impersonator(
            '<USER_ID>',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_jwt(self, m):
        data = {
    "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_jwt(
            '<USER_ID>',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_labels(
            '<USER_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_logs(self, m):
        data = {
    "total": 5.0,
    "logs": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list_logs(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_memberships(self, m):
        data = {
    "total": 5.0,
    "memberships": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list_memberships(
            '<USER_ID>',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_mfa(
            '<USER_ID>',
            True,
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_mfa(
            '<USER_ID>',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_mfa_authenticator(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.delete_mfa_authenticator(
            '<USER_ID>',
            'totp',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_delete_mfa_authenticator(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.delete_mfa_authenticator(
            '<USER_ID>',
            'totp',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_mfa_factors(self, m):
        data = {
    "totp": True,
    "phone": True,
    "email": True,
    "recoveryCode": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list_mfa_factors(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_mfa_factors(self, m):
        data = {
    "totp": True,
    "phone": True,
    "email": True,
    "recoveryCode": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list_mfa_factors(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.get_mfa_recovery_codes(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.get_mfa_recovery_codes(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_mfa_recovery_codes(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_mfa_recovery_codes(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_mfa_recovery_codes(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mfa_recovery_codes(self, m):
        data = {
    "recoveryCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_mfa_recovery_codes(
            '<USER_ID>',
        )

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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_name(
            '<USER_ID>',
            '<NAME>',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_password(
            '<USER_ID>',
            'password',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_phone(
            '<USER_ID>',
            '+12065550100',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.get_prefs(
            '<USER_ID>',
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_prefs(
            '<USER_ID>',
            {},
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_sessions(self, m):
        data = {
    "total": 5.0,
    "sessions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list_sessions(
            '<USER_ID>',
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
    "mfaUpdatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_session(
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_sessions(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.delete_sessions(
            '<USER_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_delete_session(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.delete_session(
            '<USER_ID>',
            '<SESSION_ID>',
        )

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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_status(
            '<USER_ID>',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_targets(self, m):
        data = {
    "total": 5.0,
    "targets": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.list_targets(
            '<USER_ID>',
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
    "expired": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_target(
            '<USER_ID>',
            '<TARGET_ID>',
            'email',
            '<IDENTIFIER>',
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
    "expired": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.get_target(
            '<USER_ID>',
            '<TARGET_ID>',
        )

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
    "expired": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_target(
            '<USER_ID>',
            '<TARGET_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_target(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.delete_target(
            '<USER_ID>',
            '<TARGET_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_token(self, m):
        data = {
    "$id": "bb8ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c168bb8",
    "secret": "",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "phrase": "Golden Fox"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.create_token(
            '<USER_ID>',
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_email_verification(
            '<USER_ID>',
            True,
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
    "accessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.users.update_phone_verification(
            '<USER_ID>',
            True,
        )

        self.assertEqual(response.to_dict(), data)

