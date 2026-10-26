import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.messaging import Messaging


class MessagingServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.messaging = Messaging(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list_messages(self):
        data = {
            "total": 5.0,
            "messages": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.list_messages()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_email(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_email(
            '<MESSAGE_ID>',
            '<SUBJECT>',
            '<CONTENT>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_email(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_email(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_push(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_push(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_push(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_push(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_sms(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_sms(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_sms(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_sms(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_sms(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_sms(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_message(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "providerType": "email",
            "topics": [],
            "users": [],
            "targets": [],
            "deliveredTotal": 1.0,
            "data": {},
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.get_message(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.delete(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_targets(self):
        data = {
            "total": 5.0,
            "targets": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.list_targets(
            '<MESSAGE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_providers(self):
        data = {
            "total": 5.0,
            "providers": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.list_providers()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_apns_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_apns_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_apns_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_apns_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_appwrite_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_appwrite_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_appwrite_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_appwrite_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_fcm_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_fcm_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_fcm_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_fcm_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_mailgun_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_mailgun_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_mailgun_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_mailgun_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_msg91_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_msg91_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_msg91_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_msg91_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_resend_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_resend_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_resend_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_resend_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_sendgrid_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_sendgrid_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_sendgrid_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_sendgrid_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_ses_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_ses_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_ses_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_ses_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_smtp_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_smtp_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_smtp_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_smtp_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_telesign_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_telesign_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_telesign_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_telesign_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_textmagic_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_textmagic_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_textmagic_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_textmagic_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_twilio_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_twilio_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_twilio_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_twilio_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_vonage_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_vonage_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_vonage_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_vonage_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_provider(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Mailgun",
            "provider": "mailgun",
            "enabled": True,
            "type": "sms",
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.get_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_provider(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.delete_provider(
            '<PROVIDER_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_topics(self):
        data = {
            "total": 5.0,
            "topics": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.list_topics()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_topic(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "events",
            "description": "Order status updates sent to customers.",
            "emailTotal": 100.0,
            "smsTotal": 100.0,
            "pushTotal": 100.0,
            "subscribe": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_topic(
            '<TOPIC_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_topic(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "events",
            "description": "Order status updates sent to customers.",
            "emailTotal": 100.0,
            "smsTotal": 100.0,
            "pushTotal": 100.0,
            "subscribe": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.get_topic(
            '<TOPIC_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_topic(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "events",
            "description": "Order status updates sent to customers.",
            "emailTotal": 100.0,
            "smsTotal": 100.0,
            "pushTotal": 100.0,
            "subscribe": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.update_topic(
            '<TOPIC_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_topic(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.delete_topic(
            '<TOPIC_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_subscribers(self):
        data = {
            "total": 5.0,
            "subscribers": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.list_subscribers(
            '<TOPIC_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_subscriber(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "targetId": "259125845563242502",
            "target": {
                "$id": "259125845563242502",
                "$createdAt": "2020-10-15T06:38:00.000+00:00",
                "$updatedAt": "2020-10-15T06:38:00.000+00:00",
                "name": "Apple iPhone 12",
                "userId": "259125845563242502",
                "providerType": "email",
                "identifier": "token",
                "expired": True,
            },
            "userId": "5e5ea5c16897e",
            "userName": "Aegon Targaryen",
            "topicId": "259125845563242502",
            "providerType": "email",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.create_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
            '<TARGET_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_subscriber(self):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "targetId": "259125845563242502",
            "target": {
                "$id": "259125845563242502",
                "$createdAt": "2020-10-15T06:38:00.000+00:00",
                "$updatedAt": "2020-10-15T06:38:00.000+00:00",
                "name": "Apple iPhone 12",
                "userId": "259125845563242502",
                "providerType": "email",
                "identifier": "token",
                "expired": True,
            },
            "userId": "5e5ea5c16897e",
            "userName": "Aegon Targaryen",
            "topicId": "259125845563242502",
            "providerType": "email",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.get_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_subscriber(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.messaging.delete_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )
        self.assertEqual(response, data)
