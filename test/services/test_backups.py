import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.backups import Backups


class BackupsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.backups = Backups(self.client)

    @requests_mock.Mocker()
    def test_list_archives(self, m):
        data = {
            "total": 5.0,
            "archives": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.list_archives(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/archives',
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
    def test_create_archive(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.create_archive(
            [],
            resource_id='<RESOURCE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/archives',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'services': [],
                'resourceId': '<RESOURCE_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_archive(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.get_archive(
            '<ARCHIVE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/archives/<ARCHIVE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_archive(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.delete_archive(
            '<ARCHIVE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/archives/<ARCHIVE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_policies(self, m):
        data = {
            "total": 5.0,
            "policies": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.list_policies(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/policies',
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
    def test_create_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "Hourly backups",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "services": [],
            "resources": [],
            "retention": 7.0,
            "schedule": "0 * * * *",
            "type": "full",
            "enabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.create_policy(
            '<POLICY_ID>',
            [],
            1,
            'schedule',
            name='<NAME>',
            resource_id='<RESOURCE_ID>',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/policies',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'policyId': '<POLICY_ID>',
                'name': '<NAME>',
                'services': [],
                'resourceId': '<RESOURCE_ID>',
                'enabled': False,
                'retention': 1,
                'schedule': 'schedule',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "Hourly backups",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "services": [],
            "resources": [],
            "retention": 7.0,
            "schedule": "0 * * * *",
            "type": "full",
            "enabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.get_policy(
            '<POLICY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/policies/<POLICY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "Hourly backups",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "services": [],
            "resources": [],
            "retention": 7.0,
            "schedule": "0 * * * *",
            "type": "full",
            "enabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.update_policy(
            '<POLICY_ID>',
            name='<NAME>',
            retention=1,
            schedule='schedule',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/policies/<POLICY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'retention': 1,
                'schedule': 'schedule',
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_policy(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.delete_policy(
            '<POLICY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/policies/<POLICY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_restoration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "archiveId": "did8jx6ws45jana098ab7",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.create_restoration(
            '<ARCHIVE_ID>',
            [],
            new_resource_id='<NEW_RESOURCE_ID>',
            new_resource_name='<NEW_RESOURCE_NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/restoration',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'archiveId': '<ARCHIVE_ID>',
                'services': [],
                'newResourceId': '<NEW_RESOURCE_ID>',
                'newResourceName': '<NEW_RESOURCE_NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_restorations(self, m):
        data = {
            "total": 5.0,
            "restorations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.list_restorations(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/restorations',
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
    def test_get_restoration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "archiveId": "did8jx6ws45jana098ab7",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.backups.get_restoration(
            '<RESTORATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/backups/restorations/<RESTORATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)
