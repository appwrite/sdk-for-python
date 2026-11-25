import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.monitors import Monitors


class MonitorsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.monitors = Monitors(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "monitors": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.list(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors',
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
    def test_create_dns_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.create_dns_monitor(
            '<MONITOR_ID>',
            '<NAME>',
            'example.com',
            record='A',
            resolver='<RESOLVER>',
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/dns',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'monitorId': '<MONITOR_ID>',
                'name': '<NAME>',
                'domain': 'example.com',
                'record': 'A',
                'resolver': '<RESOLVER>',
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_dns_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.update_dns_monitor(
            '<MONITOR_ID>',
            name='<NAME>',
            domain='example.com',
            record='A',
            resolver='<RESOLVER>',
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/dns/<MONITOR_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'domain': 'example.com',
                'record': 'A',
                'resolver': '<RESOLVER>',
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_http_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.create_http_monitor(
            '<MONITOR_ID>',
            '<NAME>',
            'https://example.com/health',
            method='GET',
            headers={},
            body='<BODY>',
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/http',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'monitorId': '<MONITOR_ID>',
                'name': '<NAME>',
                'url': 'https://example.com/health',
                'method': 'GET',
                'headers': {},
                'body': '<BODY>',
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_http_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.update_http_monitor(
            '<MONITOR_ID>',
            name='<NAME>',
            url='https://example.com/health',
            method='GET',
            headers={},
            body='<BODY>',
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/http/<MONITOR_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'url': 'https://example.com/health',
                'method': 'GET',
                'headers': {},
                'body': '<BODY>',
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.create_smtp_monitor(
            '<MONITOR_ID>',
            '<NAME>',
            'example.com',
            1,
            tls_mode='none',
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/smtp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'monitorId': '<MONITOR_ID>',
                'name': '<NAME>',
                'host': 'example.com',
                'port': 1,
                'tlsMode': 'none',
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_smtp_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.update_smtp_monitor(
            '<MONITOR_ID>',
            name='<NAME>',
            host='example.com',
            port=1,
            tls_mode='none',
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/smtp/<MONITOR_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'host': 'example.com',
                'port': 1,
                'tlsMode': 'none',
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_tcp_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.create_tcp_monitor(
            '<MONITOR_ID>',
            '<NAME>',
            'example.com',
            1,
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/tcp',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'monitorId': '<MONITOR_ID>',
                'name': '<NAME>',
                'host': 'example.com',
                'port': 1,
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_tcp_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.update_tcp_monitor(
            '<MONITOR_ID>',
            name='<NAME>',
            host='example.com',
            port=1,
            rules=[],
            interval=1,
            timeout=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/tcp/<MONITOR_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'host': 'example.com',
                'port': 1,
                'rules': [],
                'interval': 1,
                'timeout': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_usage_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.create_usage_monitor(
            '<MONITOR_ID>',
            '<NAME>',
            [],
            window=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/usage',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'monitorId': '<MONITOR_ID>',
                'name': '<NAME>',
                'rules': [],
                'window': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_usage_monitor(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.update_usage_monitor(
            '<MONITOR_ID>',
            name='<NAME>',
            rules=[],
            window=1,
            cooldown=1,
            enabled=False,
            notify=[],
            severity='info',
            escalation_id='<ESCALATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/usage/<MONITOR_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'rules': [],
                'window': 1,
                'cooldown': 1,
                'enabled': False,
                'notify': [],
                'severity': 'info',
                'escalationId': '<ESCALATION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Bandwidth spike",
            "projectId": "5e5ea5c16897e",
            "rules": [],
            "type": "usage",
            "resourceType": "database",
            "resourceId": "main",
            "window": 3600.0,
            "cooldown": 3600.0,
            "enabled": True,
            "notify": [],
            "escalationId": "5e5ea5c16897e",
            "severity": "warning",
            "status": "ok",
            "alertId": "5e5ea5c16897e",
            "interval": 60.0,
            "timeout": 10.0,
            "url": "https:\/\/example.com\/health",
            "body": "",
            "domain": "example.com",
            "resolver": "1.1.1.1",
            "host": "mail.example.com",
            "port": 587.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.monitors.get(
            '<MONITOR_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/<MONITOR_ID>',
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
        response = self.monitors.delete(
            '<MONITOR_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/monitors/<MONITOR_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
