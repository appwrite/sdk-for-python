import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.account import Account


class AccountServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.account = Account(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_get(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create(
            '<USER_ID>',
            'email@example.com',
            'password',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_consents(self):
        data = {
            "total": 5.0,
            "consents": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_consents()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_consent(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get_consent(
            '<CONSENT_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_consent(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_consent(
            '<CONSENT_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_consent_tokens(self):
        data = {
            "total": 5.0,
            "tokens": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_consent_tokens(
            '<CONSENT_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_consent_token(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get_consent_token(
            '<CONSENT_ID>',
            '<TOKEN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_consent_token(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_consent_token(
            '<CONSENT_ID>',
            '<TOKEN_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_email(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_email(
            'email@example.com',
            'password',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_identities(self):
        data = {
            "total": 5.0,
            "identities": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_identities()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_identity(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_identity(
            '<IDENTITY_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_memberships(self):
        data = {
            "total": 5.0,
            "memberships": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_memberships()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mfa(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_mfa(
            True,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_mfa_authenticator(self):
        data = {
            "secret": "[SHARED_SECRET]",
            "uri": "otpauth:\/\/totp\/appwrite:user@example.com?secret=[SHARED_SECRET]&issuer=appwrite",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_mfa_authenticator(
            'totp',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_mfa_authenticator(self):
        data = {
            "secret": "[SHARED_SECRET]",
            "uri": "otpauth:\/\/totp\/appwrite:user@example.com?secret=[SHARED_SECRET]&issuer=appwrite",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_mfa_authenticator(
            'totp',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mfa_authenticator(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_mfa_authenticator(
            'totp',
            '<OTP>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mfa_authenticator(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_mfa_authenticator(
            'totp',
            '<OTP>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_mfa_authenticator(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_mfa_authenticator(
            'totp',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_delete_mfa_authenticator(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_mfa_authenticator(
            'totp',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_create_mfa_challenge(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "expire": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_mfa_challenge(
            'email',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_mfa_challenge(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "expire": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_mfa_challenge(
            'email',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mfa_challenge(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_mfa_challenge(
            '<CHALLENGE_ID>',
            '<OTP>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mfa_challenge(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_mfa_challenge(
            '<CHALLENGE_ID>',
            '<OTP>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_mfa_factors(self):
        data = {
            "totp": True,
            "phone": True,
            "email": True,
            "recoveryCode": True,
            "custom": True,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_mfa_factors()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_mfa_factors(self):
        data = {
            "totp": True,
            "phone": True,
            "email": True,
            "recoveryCode": True,
            "custom": True,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_mfa_factors()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_mfa_recovery_codes(self):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get_mfa_recovery_codes()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_mfa_recovery_codes(self):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get_mfa_recovery_codes()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_mfa_recovery_codes(self):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_mfa_recovery_codes()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_mfa_recovery_codes(self):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_mfa_recovery_codes()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mfa_recovery_codes(self):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_mfa_recovery_codes()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mfa_recovery_codes(self):
        data = {
            "recoveryCodes": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_mfa_recovery_codes()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_name(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_name(
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_passkeys(self):
        data = {
            "total": 5.0,
            "passkeys": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_passkeys()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_passkey(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "passkeyId": "5e5ea5c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "publicKey": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_passkey()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_passkey(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My laptop",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get_passkey(
            '<PASSKEY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_passkey(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My laptop",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_passkey(
            '<PASSKEY_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_passkey(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_passkey(
            '<PASSKEY_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_passkey_verification(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My laptop",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_passkey_verification(
            '<PASSKEY_ID>',
            {},
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_password(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_password(
            'password',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_phone(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_phone(
            '+12065550100',
            'password',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_prefs(self):
        data = {}
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get_prefs()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_prefs(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_prefs(
            {},
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_recovery(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_recovery(
            'email@example.com',
            'https://example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_recovery(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_recovery(
            '<USER_ID>',
            '<SECRET>',
            'password',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_recovery_otp(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_recovery_otp(
            'email@example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_recovery_otp(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_recovery_otp(
            '<USER_ID>',
            '<SECRET>',
            'password',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_sessions(self):
        data = {
            "total": 5.0,
            "sessions": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.list_sessions()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_sessions(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_sessions()
        self.assertEqual(response, data)

    @respx.mock
    async def test_create_anonymous_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_anonymous_session()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_email_password_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_email_password_session(
            'email@example.com',
            'password',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_id_token_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_id_token_session(
            'apple',
            '<ID_TOKEN>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_magic_url_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_magic_url_session(
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_phone_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_phone_session(
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_session(
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.get_session(
            '<SESSION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_session(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_session(
            '<SESSION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_session(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.delete_session(
            '<SESSION_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_status(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_status()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_email_token(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_email_token(
            '<USER_ID>',
            'email@example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_magic_url_token(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_magic_url_token(
            '<USER_ID>',
            'email@example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_o_auth2_token(self):
        data = None
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_o_auth2_token(
            'amazon',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_create_passkey_token(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "passkeyId": "5e5ea5c16897e",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "publicKey": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_passkey_token()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_passkey_token(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_passkey_token(
            '<CHALLENGE_ID>',
            {},
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_phone_token(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_phone_token(
            '<USER_ID>',
            '+12065550100',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_email_verification(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_email_verification(
            'https://example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_verification(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_verification(
            'https://example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_email_verification(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_email_verification(
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_verification(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_verification(
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_email_verification_otp(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_email_verification_otp()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_email_verification_otp(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_email_verification_otp(
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_phone_verification(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.create_phone_verification()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_phone_verification(self):
        data = {
            "$id": "bb8ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c168bb8",
            "secret": "",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "phrase": "Golden Fox",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.account.update_phone_verification(
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)
