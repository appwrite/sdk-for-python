import json
import requests_mock
import unittest

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
    "archives": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.list_archives(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_archive(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "policyId": "did8jx6ws45jana098ab7",
    "size": 100000.0,
    "status": "completed",
    "startedAt": "2020-10-15T06:38:00.000+00:00",
    "migrationId": "did8jx6ws45jana098ab7",
    "services": [],
    "resources": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.create_archive(
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_archive(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "policyId": "did8jx6ws45jana098ab7",
    "size": 100000.0,
    "status": "completed",
    "startedAt": "2020-10-15T06:38:00.000+00:00",
    "migrationId": "did8jx6ws45jana098ab7",
    "services": [],
    "resources": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.get_archive(
            '<ARCHIVE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_archive(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.delete_archive(
            '<ARCHIVE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_policies(self, m):
        data = {
    "total": 5.0,
    "policies": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.list_policies(
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
    "enabled": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.create_policy(
            '<POLICY_ID>',
            [],
            1,
            '',
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
    "enabled": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.get_policy(
            '<POLICY_ID>',
        )

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
    "enabled": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.update_policy(
            '<POLICY_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_policy(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.delete_policy(
            '<POLICY_ID>',
        )

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
    "startedAt": "2020-10-15T06:38:00.000+00:00",
    "migrationId": "did8jx6ws45jana098ab7",
    "services": [],
    "resources": [],
    "options": "{databases.database[{oldId, newId, newName}]}"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.create_restoration(
            '<ARCHIVE_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_restorations(self, m):
        data = {
    "total": 5.0,
    "restorations": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.list_restorations(
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
    "startedAt": "2020-10-15T06:38:00.000+00:00",
    "migrationId": "did8jx6ws45jana098ab7",
    "services": [],
    "resources": [],
    "options": "{databases.database[{oldId, newId, newName}]}"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.backups.get_restoration(
            '<RESTORATION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

