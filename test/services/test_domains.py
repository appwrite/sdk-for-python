import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.domains import Domains


class DomainsServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.domains = Domains(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list(self):
        data = {
            "total": 5.0,
            "domains": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.list()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create(
            '<TEAM_ID>',
            'example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_price(self):
        data = {
            "domain": "example.com",
            "tld": "com",
            "available": True,
            "periodYears": 1.0,
            "premium": True,
            "renewalPeriodYears": 1.0,
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_price(
            'example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_prices(self):
        data = {
            "total": 5.0,
            "prices": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.list_prices(
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.delete(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_nameservers(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_nameservers(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_verify_nameservers(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.verify_nameservers(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_preset_google_workspace(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_preset_google_workspace(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_preset_google_workspace(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_preset_google_workspace(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_preset_i_cloud(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_preset_i_cloud(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_preset_i_cloud(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_preset_i_cloud(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_preset_mailgun(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_preset_mailgun(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_preset_mailgun(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_preset_mailgun(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_preset_outlook(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_preset_outlook(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_preset_outlook(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_preset_outlook(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_preset_proton_mail(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_preset_proton_mail(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_preset_proton_mail(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_preset_proton_mail(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_preset_zoho(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_preset_zoho(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_preset_zoho(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_preset_zoho(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_records(self):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.list_records(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_a(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_a(
            '<DOMAIN_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_a(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_a(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_aaaa(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_aaaa(
            '<DOMAIN_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_aaaa(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_aaaa(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_alias(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_alias(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_alias(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_alias(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_caa(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_caa(
            '<DOMAIN_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_caa(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_caa(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_cname(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_cname(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_cname(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_cname(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_https(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_https(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_https(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_https(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_mx(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_mx(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_mx(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_mx(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_ns(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_ns(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_ns(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_ns(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_srv(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_srv(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
            1,
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_srv(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_srv(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
            1,
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_record_txt(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.create_record_txt(
            '<DOMAIN_ID>',
            'name',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_record_txt(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_record_txt(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_record(self):
        data = {
            "$id": "5f40a6e10c65e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "type": "A",
            "name": "mail",
            "value": "192.0.2.1",
            "ttl": 86400.0,
            "priority": 10.0,
            "lock": True,
            "weight": 10.0,
            "port": 443.0,
            "comment": "Mail server record",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_record(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_record(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.delete_record(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_team(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_team(
            '<DOMAIN_ID>',
            '<TEAM_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_transfer_status(self):
        data = {
            "status": "pending_registry",
            "reason": "Transfer in progress",
            "timestamp": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.get_transfer_status(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_zone(self):
        data = '; café zone\nwww 3600 IN A 192.0.2.1\n'
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=data, headers=headers),
        )
        response = await self.domains.get_zone(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_zone(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "domain": "example.com",
            "registrar": "appwrite",
            "nameservers": "Appwrite",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "renewal": "2020-10-15T06:38:00.000+00:00",
            "autoRenewal": True,
            "renewalPrice": 2599.0,
            "teamId": "5e5ea5c16897e",
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.domains.update_zone(
            '<DOMAIN_ID>',
            '<CONTENT>',
        )
        self.assertEqual(response.to_dict(), data)
