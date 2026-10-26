import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.proxy import Proxy


class ProxyServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.proxy = Proxy(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_create_invalidation(self):
        data = {
            "domain": "appwrite.company.com",
            "type": "tag",
            "reference": "products",
            "status": "success",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.create_invalidation(
            'example.com',
            'tag',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_rules(self):
        data = {
            "total": 5.0,
            "rules": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.list_rules()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_api_rule(self):
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
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.create_api_rule(
            'example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_function_rule(self):
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
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.create_function_rule(
            'example.com',
            '<FUNCTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_redirect_rule(self):
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
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.create_redirect_rule(
            'example.com',
            'https://example.com',
            '301',
            '<RESOURCE_ID>',
            'site',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_site_rule(self):
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
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.create_site_rule(
            'example.com',
            '<SITE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_smtp_rule(self):
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
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.create_smtp_rule(
            'example.com',
            '<FUNCTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_rule(self):
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
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.get_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_rule(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.delete_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_rule_status(self):
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
            "renewAt": "datetime",
            "protocol": "http",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.proxy.update_rule_status(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)
