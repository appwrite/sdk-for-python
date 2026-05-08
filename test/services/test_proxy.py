import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.proxy import Proxy

class ProxyServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.proxy = Proxy(self.client)

    @requests_mock.Mocker()
    def test_list_rules(self, m):
        data = {
    "total": 5.0,
    "rules": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.list_rules(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_api_rule(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "domain": "appwrite.company.com",
    "type": "deployment",
    "trigger": "manual",
    "redirectUrl": "https:\/\/appwrite.io\/docs",
    "redirectStatusCode": 301.0,
    "deploymentId": "n3u9feiwmf",
    "deploymentResourceId": "n3u9feiwmf",
    "deploymentVcsProviderBranch": "main",
    "status": "verified",
    "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
    "renewAt": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.create_api_rule(
            '',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_function_rule(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "domain": "appwrite.company.com",
    "type": "deployment",
    "trigger": "manual",
    "redirectUrl": "https:\/\/appwrite.io\/docs",
    "redirectStatusCode": 301.0,
    "deploymentId": "n3u9feiwmf",
    "deploymentResourceId": "n3u9feiwmf",
    "deploymentVcsProviderBranch": "main",
    "status": "verified",
    "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
    "renewAt": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.create_function_rule(
            '',
            '<FUNCTION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_redirect_rule(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "domain": "appwrite.company.com",
    "type": "deployment",
    "trigger": "manual",
    "redirectUrl": "https:\/\/appwrite.io\/docs",
    "redirectStatusCode": 301.0,
    "deploymentId": "n3u9feiwmf",
    "deploymentResourceId": "n3u9feiwmf",
    "deploymentVcsProviderBranch": "main",
    "status": "verified",
    "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
    "renewAt": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.create_redirect_rule(
            '',
            'https://example.com',
            '301',
            '<RESOURCE_ID>',
            'site',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_site_rule(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "domain": "appwrite.company.com",
    "type": "deployment",
    "trigger": "manual",
    "redirectUrl": "https:\/\/appwrite.io\/docs",
    "redirectStatusCode": 301.0,
    "deploymentId": "n3u9feiwmf",
    "deploymentResourceId": "n3u9feiwmf",
    "deploymentVcsProviderBranch": "main",
    "status": "verified",
    "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
    "renewAt": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.create_site_rule(
            '',
            '<SITE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_rule(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "domain": "appwrite.company.com",
    "type": "deployment",
    "trigger": "manual",
    "redirectUrl": "https:\/\/appwrite.io\/docs",
    "redirectStatusCode": 301.0,
    "deploymentId": "n3u9feiwmf",
    "deploymentResourceId": "n3u9feiwmf",
    "deploymentVcsProviderBranch": "main",
    "status": "verified",
    "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
    "renewAt": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.get_rule(
            '<RULE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_rule(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.delete_rule(
            '<RULE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_rule_status(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "domain": "appwrite.company.com",
    "type": "deployment",
    "trigger": "manual",
    "redirectUrl": "https:\/\/appwrite.io\/docs",
    "redirectStatusCode": 301.0,
    "deploymentId": "n3u9feiwmf",
    "deploymentResourceId": "n3u9feiwmf",
    "deploymentVcsProviderBranch": "main",
    "status": "verified",
    "logs": "Verification of DNS records failed with DNS resolver 8.8.8.8. Domain stage.myapp.com does not have DNS record.",
    "renewAt": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.proxy.update_rule_status(
            '<RULE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

