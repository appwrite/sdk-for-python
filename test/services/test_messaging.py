import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            "messages": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.list_messages(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages',
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_email(
            '<MESSAGE_ID>',
            '<SUBJECT>',
            '<CONTENT>',
            topics=[],
            users=[],
            targets=[],
            cc=[],
            bcc=[],
            attachments=[],
            draft=False,
            html=False,
            scheduled_at='2020-10-15T06:38:00.000+00:00',
            reply_to_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            emails=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'messageId': '<MESSAGE_ID>',
                'subject': '<SUBJECT>',
                'content': '<CONTENT>',
                'topics': [],
                'users': [],
                'targets': [],
                'cc': [],
                'bcc': [],
                'attachments': [],
                'draft': False,
                'html': False,
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
                'replyToEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'emails': [],
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_email(
            '<MESSAGE_ID>',
            topics=[],
            users=[],
            targets=[],
            subject='<SUBJECT>',
            content='<CONTENT>',
            draft=False,
            html=False,
            cc=[],
            bcc=[],
            scheduled_at='2020-10-15T06:38:00.000+00:00',
            attachments=[],
            reply_to_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            emails=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/email/<MESSAGE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'topics': [],
                'users': [],
                'targets': [],
                'subject': '<SUBJECT>',
                'content': '<CONTENT>',
                'draft': False,
                'html': False,
                'cc': [],
                'bcc': [],
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
                'attachments': [],
                'replyToEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'emails': [],
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_push(
            '<MESSAGE_ID>',
            title='<TITLE>',
            body='<BODY>',
            topics=[],
            users=[],
            targets=[],
            data={},
            action='<ACTION>',
            image='<ID1:ID2>',
            icon='<ICON>',
            sound='<SOUND>',
            color='<COLOR>',
            tag='<TAG>',
            badge=1,
            draft=False,
            scheduled_at='2020-10-15T06:38:00.000+00:00',
            content_available=False,
            critical=False,
            priority='normal',
            channel_id='<CHANNEL_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/push',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'messageId': '<MESSAGE_ID>',
                'title': '<TITLE>',
                'body': '<BODY>',
                'topics': [],
                'users': [],
                'targets': [],
                'data': {},
                'action': '<ACTION>',
                'image': '<ID1:ID2>',
                'icon': '<ICON>',
                'sound': '<SOUND>',
                'color': '<COLOR>',
                'tag': '<TAG>',
                'badge': 1,
                'draft': False,
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
                'contentAvailable': False,
                'critical': False,
                'priority': 'normal',
                'channelId': '<CHANNEL_ID>',
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_push(
            '<MESSAGE_ID>',
            topics=[],
            users=[],
            targets=[],
            title='<TITLE>',
            body='<BODY>',
            data={},
            action='<ACTION>',
            image='<ID1:ID2>',
            icon='<ICON>',
            sound='<SOUND>',
            color='<COLOR>',
            tag='<TAG>',
            badge=1,
            draft=False,
            scheduled_at='2020-10-15T06:38:00.000+00:00',
            content_available=False,
            critical=False,
            priority='normal',
            channel_id='<CHANNEL_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/push/<MESSAGE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'topics': [],
                'users': [],
                'targets': [],
                'title': '<TITLE>',
                'body': '<BODY>',
                'data': {},
                'action': '<ACTION>',
                'image': '<ID1:ID2>',
                'icon': '<ICON>',
                'sound': '<SOUND>',
                'color': '<COLOR>',
                'tag': '<TAG>',
                'badge': 1,
                'draft': False,
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
                'contentAvailable': False,
                'critical': False,
                'priority': 'normal',
                'channelId': '<CHANNEL_ID>',
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
            topics=[],
            users=[],
            targets=[],
            draft=False,
            scheduled_at='2020-10-15T06:38:00.000+00:00',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'messageId': '<MESSAGE_ID>',
                'content': '<CONTENT>',
                'topics': [],
                'users': [],
                'targets': [],
                'draft': False,
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_sms(
            '<MESSAGE_ID>',
            '<CONTENT>',
            topics=[],
            users=[],
            targets=[],
            draft=False,
            scheduled_at='2020-10-15T06:38:00.000+00:00',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'messageId': '<MESSAGE_ID>',
                'content': '<CONTENT>',
                'topics': [],
                'users': [],
                'targets': [],
                'draft': False,
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_sms(
            '<MESSAGE_ID>',
            topics=[],
            users=[],
            targets=[],
            content='<CONTENT>',
            draft=False,
            scheduled_at='2020-10-15T06:38:00.000+00:00',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms/<MESSAGE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'topics': [],
                'users': [],
                'targets': [],
                'content': '<CONTENT>',
                'draft': False,
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_sms(
            '<MESSAGE_ID>',
            topics=[],
            users=[],
            targets=[],
            content='<CONTENT>',
            draft=False,
            scheduled_at='2020-10-15T06:38:00.000+00:00',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/sms/<MESSAGE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'topics': [],
                'users': [],
                'targets': [],
                'content': '<CONTENT>',
                'draft': False,
                'scheduledAt': '2020-10-15T06:38:00.000+00:00',
            },
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
            "status": "processing",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_message(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/<MESSAGE_ID>',
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
        response = self.messaging.delete(
            '<MESSAGE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/<MESSAGE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

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
        response = self.messaging.list_targets(
            '<MESSAGE_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/messages/<MESSAGE_ID>/targets',
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
    def test_list_providers(self, m):
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
        response = self.messaging.list_providers(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers',
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
    def test_create_apns_provider(self, m):
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
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            auth_key='<AUTH_KEY>',
            auth_key_id='<AUTH_KEY_ID>',
            team_id='<TEAM_ID>',
            bundle_id='<BUNDLE_ID>',
            sandbox=False,
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'authKey': '<AUTH_KEY>',
                'authKeyId': '<AUTH_KEY_ID>',
                'teamId': '<TEAM_ID>',
                'bundleId': '<BUNDLE_ID>',
                'sandbox': False,
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_apns_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            auth_key='<AUTH_KEY>',
            auth_key_id='<AUTH_KEY_ID>',
            team_id='<TEAM_ID>',
            bundle_id='<BUNDLE_ID>',
            sandbox=False,
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'authKey': '<AUTH_KEY>',
                'authKeyId': '<AUTH_KEY_ID>',
                'teamId': '<TEAM_ID>',
                'bundleId': '<BUNDLE_ID>',
                'sandbox': False,
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            auth_key='<AUTH_KEY>',
            auth_key_id='<AUTH_KEY_ID>',
            team_id='<TEAM_ID>',
            bundle_id='<BUNDLE_ID>',
            sandbox=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'authKey': '<AUTH_KEY>',
                'authKeyId': '<AUTH_KEY_ID>',
                'teamId': '<TEAM_ID>',
                'bundleId': '<BUNDLE_ID>',
                'sandbox': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_apns_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            auth_key='<AUTH_KEY>',
            auth_key_id='<AUTH_KEY_ID>',
            team_id='<TEAM_ID>',
            bundle_id='<BUNDLE_ID>',
            sandbox=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/apns/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'authKey': '<AUTH_KEY>',
                'authKeyId': '<AUTH_KEY_ID>',
                'teamId': '<TEAM_ID>',
                'bundleId': '<BUNDLE_ID>',
                'sandbox': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_appwrite_provider(self, m):
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
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_appwrite_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            enabled=False,
            qos=1,
            expiry=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/appwrite',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'enabled': False,
                'qos': 1,
                'expiry': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_appwrite_provider(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_appwrite_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            qos=1,
            expiry=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/appwrite/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'qos': 1,
                'expiry': 1,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            service_account_json={},
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'serviceAccountJSON': {},
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_fcm_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            service_account_json={},
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'serviceAccountJSON': {},
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            service_account_json={},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'serviceAccountJSON': {},
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_fcm_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            service_account_json={},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/fcm/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'serviceAccountJSON': {},
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_mailgun_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            api_key='<API_KEY>',
            domain='example.com',
            is_eu_region=False,
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='email@example.com',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/mailgun',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'apiKey': '<API_KEY>',
                'domain': 'example.com',
                'isEuRegion': False,
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': 'email@example.com',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_mailgun_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            api_key='<API_KEY>',
            domain='example.com',
            is_eu_region=False,
            enabled=False,
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='<REPLY_TO_EMAIL>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/mailgun/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'apiKey': '<API_KEY>',
                'domain': 'example.com',
                'isEuRegion': False,
                'enabled': False,
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': '<REPLY_TO_EMAIL>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_msg91_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            template_id='<TEMPLATE_ID>',
            sender_id='<SENDER_ID>',
            auth_key='<AUTH_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/msg91',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'templateId': '<TEMPLATE_ID>',
                'senderId': '<SENDER_ID>',
                'authKey': '<AUTH_KEY>',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_msg91_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            template_id='<TEMPLATE_ID>',
            sender_id='<SENDER_ID>',
            auth_key='<AUTH_KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/msg91/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'templateId': '<TEMPLATE_ID>',
                'senderId': '<SENDER_ID>',
                'authKey': '<AUTH_KEY>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_resend_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            api_key='<API_KEY>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='email@example.com',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/resend',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'apiKey': '<API_KEY>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': 'email@example.com',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_resend_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            api_key='<API_KEY>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='<REPLY_TO_EMAIL>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/resend/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'apiKey': '<API_KEY>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': '<REPLY_TO_EMAIL>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_sendgrid_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            api_key='<API_KEY>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='email@example.com',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/sendgrid',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'apiKey': '<API_KEY>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': 'email@example.com',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_sendgrid_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            api_key='<API_KEY>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='<REPLY_TO_EMAIL>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/sendgrid/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'apiKey': '<API_KEY>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': '<REPLY_TO_EMAIL>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_ses_provider(self, m):
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
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_ses_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            access_key='<ACCESS_KEY>',
            secret_key='<SECRET_KEY>',
            region='<REGION>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='email@example.com',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/ses',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'accessKey': '<ACCESS_KEY>',
                'secretKey': '<SECRET_KEY>',
                'region': '<REGION>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': 'email@example.com',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_ses_provider(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_ses_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            access_key='<ACCESS_KEY>',
            secret_key='<SECRET_KEY>',
            region='<REGION>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='<REPLY_TO_EMAIL>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/ses/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'accessKey': '<ACCESS_KEY>',
                'secretKey': '<SECRET_KEY>',
                'region': '<REGION>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': '<REPLY_TO_EMAIL>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
            port=1,
            username='<USERNAME>',
            password='password',
            encryption='none',
            auto_tls=False,
            mailer='<MAILER>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='email@example.com',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'host': '<HOST>',
                'port': 1,
                'username': '<USERNAME>',
                'password': 'password',
                'encryption': 'none',
                'autoTLS': False,
                'mailer': '<MAILER>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': 'email@example.com',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_smtp_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            '<HOST>',
            port=1,
            username='<USERNAME>',
            password='password',
            encryption='none',
            auto_tls=False,
            mailer='<MAILER>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='email@example.com',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'host': '<HOST>',
                'port': 1,
                'username': '<USERNAME>',
                'password': 'password',
                'encryption': 'none',
                'autoTLS': False,
                'mailer': '<MAILER>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': 'email@example.com',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            host='<HOST>',
            port=1,
            username='<USERNAME>',
            password='password',
            encryption='none',
            auto_tls=False,
            mailer='<MAILER>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='<REPLY_TO_EMAIL>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'host': '<HOST>',
                'port': 1,
                'username': '<USERNAME>',
                'password': 'password',
                'encryption': 'none',
                'autoTLS': False,
                'mailer': '<MAILER>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': '<REPLY_TO_EMAIL>',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_smtp_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            host='<HOST>',
            port=1,
            username='<USERNAME>',
            password='password',
            encryption='none',
            auto_tls=False,
            mailer='<MAILER>',
            from_name='<FROM_NAME>',
            from_email='email@example.com',
            reply_to_name='<REPLY_TO_NAME>',
            reply_to_email='<REPLY_TO_EMAIL>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/smtp/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'host': '<HOST>',
                'port': 1,
                'username': '<USERNAME>',
                'password': 'password',
                'encryption': 'none',
                'autoTLS': False,
                'mailer': '<MAILER>',
                'fromName': '<FROM_NAME>',
                'fromEmail': 'email@example.com',
                'replyToName': '<REPLY_TO_NAME>',
                'replyToEmail': '<REPLY_TO_EMAIL>',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_telesign_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            xfrom='+12065550100',
            customer_id='<CUSTOMER_ID>',
            api_key='<API_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/telesign',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'from': '+12065550100',
                'customerId': '<CUSTOMER_ID>',
                'apiKey': '<API_KEY>',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_telesign_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            customer_id='<CUSTOMER_ID>',
            api_key='<API_KEY>',
            xfrom='<FROM>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/telesign/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'customerId': '<CUSTOMER_ID>',
                'apiKey': '<API_KEY>',
                'from': '<FROM>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_textmagic_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            xfrom='+12065550100',
            username='<USERNAME>',
            api_key='<API_KEY>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/textmagic',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'from': '+12065550100',
                'username': '<USERNAME>',
                'apiKey': '<API_KEY>',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_textmagic_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            username='<USERNAME>',
            api_key='<API_KEY>',
            xfrom='<FROM>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/textmagic/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'username': '<USERNAME>',
                'apiKey': '<API_KEY>',
                'from': '<FROM>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_twilio_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            xfrom='<FROM>',
            account_sid='<ACCOUNT_SID>',
            auth_token='<AUTH_TOKEN>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/twilio',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'from': '<FROM>',
                'accountSid': '<ACCOUNT_SID>',
                'authToken': '<AUTH_TOKEN>',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_twilio_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            account_sid='<ACCOUNT_SID>',
            auth_token='<AUTH_TOKEN>',
            xfrom='<FROM>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/twilio/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'accountSid': '<ACCOUNT_SID>',
                'authToken': '<AUTH_TOKEN>',
                'from': '<FROM>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_vonage_provider(
            '<PROVIDER_ID>',
            '<NAME>',
            xfrom='+12065550100',
            api_key='<API_KEY>',
            api_secret='<API_SECRET>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/vonage',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'providerId': '<PROVIDER_ID>',
                'name': '<NAME>',
                'from': '+12065550100',
                'apiKey': '<API_KEY>',
                'apiSecret': '<API_SECRET>',
                'enabled': False,
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_vonage_provider(
            '<PROVIDER_ID>',
            name='<NAME>',
            enabled=False,
            api_key='<API_KEY>',
            api_secret='<API_SECRET>',
            xfrom='<FROM>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/vonage/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'apiKey': '<API_KEY>',
                'apiSecret': '<API_SECRET>',
                'from': '<FROM>',
            },
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
            "credentials": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/<PROVIDER_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_provider(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.delete_provider(
            '<PROVIDER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/providers/<PROVIDER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_topics(self, m):
        data = {
            "total": 5.0,
            "topics": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.list_topics(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics',
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
    def test_create_topic(self, m):
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
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_topic(
            '<TOPIC_ID>',
            '<NAME>',
            subscribe=[],
            qos=1,
            expiry=1,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'topicId': '<TOPIC_ID>',
                'name': '<NAME>',
                'subscribe': [],
                'qos': 1,
                'expiry': 1,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_topic(self, m):
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
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_topic(
            '<TOPIC_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_topic(self, m):
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
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.update_topic(
            '<TOPIC_ID>',
            name='<NAME>',
            subscribe=[],
            qos=1,
            expiry=1,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'subscribe': [],
                'qos': 1,
                'expiry': 1,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_topic(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.delete_topic(
            '<TOPIC_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_subscribers(self, m):
        data = {
            "total": 5.0,
            "subscribers": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.list_subscribers(
            '<TOPIC_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers',
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
                "expired": True,
            },
            "userId": "5e5ea5c16897e",
            "userName": "Aegon Targaryen",
            "topicId": "259125845563242502",
            "providerType": "email",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.create_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
            '<TARGET_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'subscriberId': '<SUBSCRIBER_ID>',
                'targetId': '<TARGET_ID>',
            },
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
                "expired": True,
            },
            "userId": "5e5ea5c16897e",
            "userName": "Aegon Targaryen",
            "topicId": "259125845563242502",
            "providerType": "email",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.get_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers/<SUBSCRIBER_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_subscriber(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.messaging.delete_subscriber(
            '<TOPIC_ID>',
            '<SUBSCRIBER_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/messaging/topics/<TOPIC_ID>/subscribers/<SUBSCRIBER_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
