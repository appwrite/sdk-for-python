import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.health import Health

class HealthServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.health = Health(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "name": "database",
    "ping": 128.0,
    "status": "pass"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_antivirus(self, m):
        data = {
    "version": "1.0.0",
    "status": "online"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_antivirus(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_audits_db(self, m):
        data = {
    "total": 5.0,
    "statuses": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_audits_db(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_cache(self, m):
        data = {
    "total": 5.0,
    "statuses": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_cache(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_certificate(self, m):
        data = {
    "name": "\/CN=www.google.com",
    "subjectSN": "",
    "issuerOrganisation": "",
    "validFrom": "1704200998",
    "validTo": "1711458597",
    "signatureTypeSN": "RSA-SHA256"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_certificate(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_console_pausing(self, m):
        data = {
    "name": "database",
    "ping": 128.0,
    "status": "pass"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_console_pausing(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_db(self, m):
        data = {
    "total": 5.0,
    "statuses": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_db(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_pub_sub(self, m):
        data = {
    "total": 5.0,
    "statuses": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_pub_sub(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_audits(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_audits(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_builds(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_builds(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_certificates(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_certificates(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_databases(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_databases(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_deletes(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_deletes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_failed_jobs(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_failed_jobs(
            'v1-database',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_functions(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_functions(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_logs(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_logs(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_mails(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_mails(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_messaging(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_messaging(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_migrations(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_migrations(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_stats_resources(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_stats_resources(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_usage(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_usage(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_queue_webhooks(self, m):
        data = {
    "size": 8.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_queue_webhooks(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_storage(self, m):
        data = {
    "name": "database",
    "ping": 128.0,
    "status": "pass"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_storage(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_storage_local(self, m):
        data = {
    "name": "database",
    "ping": 128.0,
    "status": "pass"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_storage_local(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_time(self, m):
        data = {
    "remoteTime": 1639490751.0,
    "localTime": 1639490844.0,
    "diff": 93.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.health.get_time(
        )

        self.assertEqual(response.to_dict(), data)

