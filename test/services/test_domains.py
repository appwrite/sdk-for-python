import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.domains import Domains


class DomainsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.domains = Domains(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "domains": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.list()
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create(
            '<TEAM_ID>',
            'example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_price(self, m):
        data = {
            "domain": "example.com",
            "tld": "com",
            "available": True,
            "periodYears": 1.0,
            "premium": True,
            "renewalPeriodYears": 1.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_price(
            'example.com',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_prices(self, m):
        data = {
            "total": 5.0,
            "prices": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.list_prices(
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.delete(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_nameservers(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_nameservers(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_verify_nameservers(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.verify_nameservers(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_google_workspace(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_google_workspace(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_google_workspace(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_google_workspace(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_i_cloud(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_i_cloud(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_i_cloud(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_i_cloud(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_mailgun(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_mailgun(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_mailgun(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_mailgun(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_outlook(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_outlook(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_outlook(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_outlook(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_proton_mail(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_proton_mail(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_proton_mail(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_proton_mail(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_preset_zoho(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_preset_zoho(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_preset_zoho(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_preset_zoho(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_records(self, m):
        data = {
            "total": 5.0,
            "dnsRecords": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.list_records(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_a(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_a(
            '<DOMAIN_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_a(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_a(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_aaaa(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_aaaa(
            '<DOMAIN_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_aaaa(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_aaaa(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_alias(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_alias(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_alias(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_alias(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_caa(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_caa(
            '<DOMAIN_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_caa(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_caa(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            'value',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_cname(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_cname(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_cname(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_cname(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_https(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_https(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_https(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_https(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_mx(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_mx(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_mx(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_mx(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_ns(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_ns(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_ns(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_ns(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_record_srv(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_srv(
            '<DOMAIN_ID>',
            'name',
            '<VALUE>',
            1,
            1,
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_srv(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_srv(
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

    @requests_mock.Mocker()
    def test_create_record_txt(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.create_record_txt(
            '<DOMAIN_ID>',
            'name',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_record_txt(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_record_txt(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
            'name',
            '<VALUE>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_record(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_record(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_record(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.delete_record(
            '<DOMAIN_ID>',
            '<RECORD_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_team(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_team(
            '<DOMAIN_ID>',
            '<TEAM_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_transfer_status(self, m):
        data = {
            "status": "pending_registry",
            "reason": "Transfer in progress",
            "timestamp": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.get_transfer_status(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_zone(self, m):
        data = '; café zone\nwww 3600 IN A 192.0.2.1\n'
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=data,
            headers=headers,
        )
        response = self.domains.get_zone(
            '<DOMAIN_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_zone(self, m):
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
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.domains.update_zone(
            '<DOMAIN_ID>',
            '<CONTENT>',
        )
        self.assertEqual(response.to_dict(), data)
