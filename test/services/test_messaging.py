import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.messaging import Messaging

class MessagingServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.messaging = Messaging(self.client)

    @requests_mock.Mocker()
    def test_list_messages(self, m):
        data = {
    "total": 5.0,
    "messages": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_messages(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_email(
            '<MESSAGE_ID>',
            '<SUBJECT>',
            '<CONTENT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_email(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_push(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_push(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_push(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_push(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_sms(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_sms(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_sms(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_sms(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_sms(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_sms(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_message(self, m):
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
    "status": "processing"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.get_message(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.delete(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_message_logs(self, m):
        data = {
    "total": 5.0,
    "logs": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_message_logs(
            '<MESSAGE_ID>',
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

        response = self.messaging.list_targets(
            '<MESSAGE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_providers(self, m):
        data = {
    "total": 5.0,
    "providers": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_providers(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_apns_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_apns_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_apns_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_apns_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_fcm_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_fcm_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_fcm_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_fcm_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mailgun_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_mailgun_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mailgun_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_mailgun_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_msg91_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_msg91_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_msg91_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_msg91_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_resend_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_resend_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_resend_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_resend_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_sendgrid_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_sendgrid_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_sendgrid_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_sendgrid_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_smtp_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_smtp_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_telesign_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_telesign_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_telesign_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_telesign_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_textmagic_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_textmagic_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_textmagic_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_textmagic_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_twilio_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_twilio_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_twilio_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_twilio_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_vonage_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_vonage_provider(
            '<PROVIDER_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_vonage_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_vonage_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_provider(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "Mailgun",
    "provider": "mailgun",
    "enabled": True,
    "type": "sms",
    "credentials": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.get_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_provider(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.delete_provider(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_provider_logs(self, m):
        data = {
    "total": 5.0,
    "logs": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_provider_logs(
            '<PROVIDER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_subscriber_logs(self, m):
        data = {
    "total": 5.0,
    "logs": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_subscriber_logs(
            '<SUBSCRIBER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_topics(self, m):
        data = {
    "total": 5.0,
    "topics": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_topics(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_topic(self, m):
        data = {
    "$id": "259125845563242502",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "events",
    "emailTotal": 100.0,
    "smsTotal": 100.0,
    "pushTotal": 100.0,
    "subscribe": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_topic(
            '<TOPIC_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_topic(self, m):
        data = {
    "$id": "259125845563242502",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "events",
    "emailTotal": 100.0,
    "smsTotal": 100.0,
    "pushTotal": 100.0,
    "subscribe": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.get_topic(
            '<TOPIC_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_topic(self, m):
        data = {
    "$id": "259125845563242502",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "events",
    "emailTotal": 100.0,
    "smsTotal": 100.0,
    "pushTotal": 100.0,
    "subscribe": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.update_topic(
            '<TOPIC_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_topic(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.delete_topic(
            '<TOPIC_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_topic_logs(self, m):
        data = {
    "total": 5.0,
    "logs": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_topic_logs(
            '<TOPIC_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_subscribers(self, m):
        data = {
    "total": 5.0,
    "subscribers": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.list_subscribers(
            '<TOPIC_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_subscriber(self, m):
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
        "expired": True
    },
    "userId": "5e5ea5c16897e",
    "userName": "Aegon Targaryen",
    "topicId": "259125845563242502",
    "providerType": "email"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.create_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
            '<TARGET_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_subscriber(self, m):
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
        "expired": True
    },
    "userId": "5e5ea5c16897e",
    "userName": "Aegon Targaryen",
    "topicId": "259125845563242502",
    "providerType": "email"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.get_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_subscriber(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.messaging.delete_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )

        self.assertEqual(response, data)

