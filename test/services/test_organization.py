import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.organization import Organization

class OrganizationServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.organization = Organization(self.client)

    @requests_mock.Mocker()
    def test_list_keys(self, m):
        data = {
    "total": 5.0,
    "keys": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.list_keys(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.create_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.get_key(
            '<KEY_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.update_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_key(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.delete_key(
            '<KEY_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_projects(self, m):
        data = {
    "total": 5.0,
    "projects": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.list_projects(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_project(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "New Project",
    "teamId": "1592981250",
    "devKeys": [],
    "smtpEnabled": True,
    "smtpSenderName": "John Appwrite",
    "smtpSenderEmail": "john@appwrite.io",
    "smtpReplyToName": "Support Team",
    "smtpReplyToEmail": "support@appwrite.io",
    "smtpHost": "mail.appwrite.io",
    "smtpPort": 25.0,
    "smtpUsername": "emailuser",
    "smtpPassword": "",
    "smtpSecure": "tls",
    "pingCount": 1.0,
    "pingedAt": "2020-10-15T06:38:00.000+00:00",
    "labels": [],
    "status": "active",
    "authMethods": [],
    "services": [],
    "protocols": [],
    "region": "fra",
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.create_project(
            '',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_project(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "New Project",
    "teamId": "1592981250",
    "devKeys": [],
    "smtpEnabled": True,
    "smtpSenderName": "John Appwrite",
    "smtpSenderEmail": "john@appwrite.io",
    "smtpReplyToName": "Support Team",
    "smtpReplyToEmail": "support@appwrite.io",
    "smtpHost": "mail.appwrite.io",
    "smtpPort": 25.0,
    "smtpUsername": "emailuser",
    "smtpPassword": "",
    "smtpSecure": "tls",
    "pingCount": 1.0,
    "pingedAt": "2020-10-15T06:38:00.000+00:00",
    "labels": [],
    "status": "active",
    "authMethods": [],
    "services": [],
    "protocols": [],
    "region": "fra",
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.get_project(
            '<PROJECT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_project(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "New Project",
    "teamId": "1592981250",
    "devKeys": [],
    "smtpEnabled": True,
    "smtpSenderName": "John Appwrite",
    "smtpSenderEmail": "john@appwrite.io",
    "smtpReplyToName": "Support Team",
    "smtpReplyToEmail": "support@appwrite.io",
    "smtpHost": "mail.appwrite.io",
    "smtpPort": 25.0,
    "smtpUsername": "emailuser",
    "smtpPassword": "",
    "smtpSecure": "tls",
    "pingCount": 1.0,
    "pingedAt": "2020-10-15T06:38:00.000+00:00",
    "labels": [],
    "status": "active",
    "authMethods": [],
    "services": [],
    "protocols": [],
    "region": "fra",
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.update_project(
            '<PROJECT_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_project(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.delete_project(
            '<PROJECT_ID>',
        )

        self.assertEqual(response, data)

