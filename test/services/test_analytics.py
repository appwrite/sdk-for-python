import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.analytics import Analytics


class AnalyticsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.analytics = Analytics(self.client)

    @requests_mock.Mocker()
    def test_list_properties(self, m):
        data = {
            "total": 5.0,
            "properties": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.list_properties(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties',
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
    def test_create_property(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Website",
            "domain": "example.com",
            "enabled": True,
            "allowedOrigins": [],
            "type": "web",
            "identifyUsers": True,
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.create_property(
            '<PROPERTY_ID>',
            '<NAME>',
            domain='<DOMAIN>',
            enabled=False,
            allowed_origins=[],
            identify_users=False,
            type='web',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'propertyId': '<PROPERTY_ID>',
                'name': '<NAME>',
                'domain': '<DOMAIN>',
                'enabled': False,
                'allowedOrigins': [],
                'identifyUsers': False,
                'type': 'web',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_property(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Website",
            "domain": "example.com",
            "enabled": True,
            "allowedOrigins": [],
            "type": "web",
            "identifyUsers": True,
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.get_property(
            '<PROPERTY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_property(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Website",
            "domain": "example.com",
            "enabled": True,
            "allowedOrigins": [],
            "type": "web",
            "identifyUsers": True,
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "firstAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.update_property(
            '<PROPERTY_ID>',
            name='<NAME>',
            domain='<DOMAIN>',
            enabled=False,
            allowed_origins=[],
            identify_users=False,
            type='web',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'domain': '<DOMAIN>',
                'enabled': False,
                'allowedOrigins': [],
                'identifyUsers': False,
                'type': 'web',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_property(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.delete_property(
            '<PROPERTY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_annotations(self, m):
        data = {
            "total": 5.0,
            "annotations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.list_annotations(
            '<PROPERTY_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/annotations',
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
    def test_create_annotation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "propertyId": "5e5ea5c16897e",
            "date": "2020-10-15T06:38:00.000+00:00",
            "content": "Launched the new pricing page",
            "userId": "5e5ea5c16897e",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.create_annotation(
            '<PROPERTY_ID>',
            '<ANNOTATION_ID>',
            '2020-10-15T06:38:00.000+00:00',
            '<CONTENT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/annotations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'annotationId': '<ANNOTATION_ID>',
                'date': '2020-10-15T06:38:00.000+00:00',
                'content': '<CONTENT>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_annotation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "propertyId": "5e5ea5c16897e",
            "date": "2020-10-15T06:38:00.000+00:00",
            "content": "Launched the new pricing page",
            "userId": "5e5ea5c16897e",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.get_annotation(
            '<PROPERTY_ID>',
            '<ANNOTATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/annotations/<ANNOTATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_annotation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "propertyId": "5e5ea5c16897e",
            "date": "2020-10-15T06:38:00.000+00:00",
            "content": "Launched the new pricing page",
            "userId": "5e5ea5c16897e",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.update_annotation(
            '<PROPERTY_ID>',
            '<ANNOTATION_ID>',
            date='2020-10-15T06:38:00.000+00:00',
            content='<CONTENT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/annotations/<ANNOTATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'date': '2020-10-15T06:38:00.000+00:00',
                'content': '<CONTENT>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_annotation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.delete_annotation(
            '<PROPERTY_ID>',
            '<ANNOTATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/annotations/<ANNOTATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_event(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.create_event(
            '<PROPERTY_ID>',
            '<NAME>',
            'https://example.com',
            domain='<DOMAIN>',
            referrer='<REFERRER>',
            screen_width=1,
            session_hash='<SESSION_HASH>',
            scroll_depth=1,
            engagement_time=1,
            props=[],
            user_id='<USER_ID>',
            ip='<IP>',
            user_agent='<USER_AGENT>',
            interactive=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/events',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'url': 'https://example.com',
                'domain': '<DOMAIN>',
                'referrer': '<REFERRER>',
                'screenWidth': 1,
                'sessionHash': '<SESSION_HASH>',
                'scrollDepth': 1,
                'engagementTime': 1,
                'props': [],
                'userId': '<USER_ID>',
                'ip': '<IP>',
                'userAgent': '<USER_AGENT>',
                'interactive': False,
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_metrics(self, m):
        data = {
            "total": 30.0,
            "metrics": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.analytics.list_metrics(
            '<PROPERTY_ID>',
            queries=[],
            interval='1h',
            dimensions=[],
            prop_key='<PROP_KEY>',
            date_range='<DATE_RANGE>',
            start_at='2020-10-15T06:38:00.000+00:00',
            end_at='2020-10-15T06:38:00.000+00:00',
            limit=1,
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/analytics/properties/<PROPERTY_ID>/metrics',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'interval': ['1h'],
                'propKey': ['<PROP_KEY>'],
                'dateRange': ['<DATE_RANGE>'],
                'startAt': ['2020-10-15T06:38:00.000+00:00'],
                'endAt': ['2020-10-15T06:38:00.000+00:00'],
                'limit': ['1'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)
