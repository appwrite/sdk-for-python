import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.alerts import Alerts


class AlertsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.alerts = Alerts(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "alerts": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.alerts.list(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/alerts',
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
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "monitorId": "5e5ea5c16897e",
            "name": "Bandwidth spike",
            "status": "firing",
            "acknowledgedBy": "5e5ea5c16897e",
            "acknowledgedByName": "Jane Doe",
            "escalationId": "5e5ea5c16897e",
            "escalationStep": 1.0,
            "escalationRound": 0.0,
            "rules": [],
            "severity": "warning",
            "threshold": 5000000,
            "value": 7250000,
            "peak": 9100000,
            "type": "usage",
            "resourceType": "database",
            "resourceId": "5e5ea5c16897e",
            "notifications": 1.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.alerts.get(
            '<ALERT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/alerts/<ALERT_ID>',
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
            "monitorId": "5e5ea5c16897e",
            "name": "Bandwidth spike",
            "status": "firing",
            "acknowledgedBy": "5e5ea5c16897e",
            "acknowledgedByName": "Jane Doe",
            "escalationId": "5e5ea5c16897e",
            "escalationStep": 1.0,
            "escalationRound": 0.0,
            "rules": [],
            "severity": "warning",
            "threshold": 5000000,
            "value": 7250000,
            "peak": 9100000,
            "type": "usage",
            "resourceType": "database",
            "resourceId": "5e5ea5c16897e",
            "notifications": 1.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.alerts.update(
            '<ALERT_ID>',
            False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/alerts/<ALERT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'acknowledged': False,
            },
        )
        self.assertEqual(response.to_dict(), data)
