import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.databases import Databases


class DatabasesServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.databases = Databases(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "databases": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "description": "Customer orders and invoices.",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create(
            '<DATABASE_ID>',
            '<NAME>',
            enabled=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'databaseId': '<DATABASE_ID>',
                'name': '<NAME>',
                'enabled': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_transactions(self, m):
        data = {
            "total": 5.0,
            "transactions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.list_transactions(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/transactions',
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
    def test_create_transaction(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_transaction(
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/transactions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'ttl': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_transaction(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.get_transaction(
            '<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/transactions/<TRANSACTION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_transaction(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_transaction(
            '<TRANSACTION_ID>',
            commit=False,
            rollback=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/transactions/<TRANSACTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'commit': False,
                'rollback': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_transaction(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.delete_transaction(
            '<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/transactions/<TRANSACTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_operations(self, m):
        data = {
            "$id": "259125845563242502",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "operations": 5.0,
            "expiresAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_operations(
            '<TRANSACTION_ID>',
            operations=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/transactions/<TRANSACTION_ID>/operations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'operations': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "description": "Customer orders and invoices.",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.get(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "description": "Customer orders and invoices.",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update(
            '<DATABASE_ID>',
            name='<NAME>',
            enabled=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'description': '<DESCRIPTION>',
            },
        )
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
        response = self.databases.delete(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_collections(self, m):
        data = {
            "total": 5.0,
            "collections": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.list_collections(
            '<DATABASE_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_collection(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Collection",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<NAME>',
            permissions=[],
            document_security=False,
            enabled=False,
            attributes=[],
            indexes=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'collectionId': '<COLLECTION_ID>',
                'name': '<NAME>',
                'permissions': [],
                'documentSecurity': False,
                'enabled': False,
                'attributes': [],
                'indexes': [],
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_collection(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Collection",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.get_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_collection(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Collection",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            name='<NAME>',
            permissions=[],
            document_security=False,
            enabled=False,
            purge=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'permissions': [],
                'documentSecurity': False,
                'enabled': False,
                'purge': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_collection(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.delete_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_attributes(self, m):
        data = {
            "total": 5.0,
            "attributes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.list_attributes(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes',
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
    def test_create_big_int_attribute(self, m):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "bigint",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_big_int_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            min=1,
            max=1,
            default=1,
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/bigint',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'min': 1,
                'max': 1,
                'default': 1,
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_big_int_attribute(self, m):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "bigint",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_big_int_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            1,
            min=1,
            max=1,
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/bigint/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'min': 1,
                'max': 1,
                'default': 1,
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_boolean_attribute(self, m):
        data = {
            "key": "isEnabled",
            "description": "Name shown on the public profile.",
            "type": "boolean",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_boolean_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default=False,
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/boolean',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': False,
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_boolean_attribute(self, m):
        data = {
            "key": "isEnabled",
            "description": "Name shown on the public profile.",
            "type": "boolean",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_boolean_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            False,
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/boolean/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': False,
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_datetime_attribute(self, m):
        data = {
            "key": "birthDay",
            "description": "Name shown on the public profile.",
            "type": "datetime",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "datetime",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_datetime_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default='2020-10-15T06:38:00.000+00:00',
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/datetime',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': '2020-10-15T06:38:00.000+00:00',
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_datetime_attribute(self, m):
        data = {
            "key": "birthDay",
            "description": "Name shown on the public profile.",
            "type": "datetime",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "datetime",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_datetime_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            '2020-10-15T06:38:00.000+00:00',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/datetime/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': '2020-10-15T06:38:00.000+00:00',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_attribute(self, m):
        data = {
            "key": "userEmail",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "email",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_email_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default='email@example.com',
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/email',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': 'email@example.com',
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_attribute(self, m):
        data = {
            "key": "userEmail",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "email",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_email_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            'email@example.com',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/email/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': 'email@example.com',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_enum_attribute(self, m):
        data = {
            "key": "status",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "elements": [],
            "format": "enum",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_enum_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            [],
            False,
            default='active',
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/enum',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'elements': [],
                'required': False,
                'default': 'active',
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_enum_attribute(self, m):
        data = {
            "key": "status",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "elements": [],
            "format": "enum",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_enum_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            [],
            False,
            'active',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/enum/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'elements': [],
                'required': False,
                'default': 'active',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_float_attribute(self, m):
        data = {
            "key": "percentageCompleted",
            "description": "Name shown on the public profile.",
            "type": "double",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_float_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            min=1.0,
            max=1.0,
            default=1.0,
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/float',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'min': 1.0,
                'max': 1.0,
                'default': 1.0,
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_float_attribute(self, m):
        data = {
            "key": "percentageCompleted",
            "description": "Name shown on the public profile.",
            "type": "double",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_float_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            1.0,
            min=1.0,
            max=1.0,
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/float/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'min': 1.0,
                'max': 1.0,
                'default': 1.0,
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_integer_attribute(self, m):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "integer",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_integer_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            min=1,
            max=1,
            default=1,
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/integer',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'min': 1,
                'max': 1,
                'default': 1,
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_integer_attribute(self, m):
        data = {
            "key": "count",
            "description": "Name shown on the public profile.",
            "type": "integer",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_integer_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            1,
            min=1,
            max=1,
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/integer/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'min': 1,
                'max': 1,
                'default': 1,
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_ip_attribute(self, m):
        data = {
            "key": "ipAddress",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "ip",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_ip_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default='192.0.2.0',
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/ip',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': '192.0.2.0',
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_ip_attribute(self, m):
        data = {
            "key": "ipAddress",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "ip",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_ip_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            '192.0.2.0',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/ip/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': '192.0.2.0',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_line_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_line_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/line',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': [],
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_line_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_line_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default=[],
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/line/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': [],
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_longtext_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_longtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default='Hello World',
            array=False,
            encrypt=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/longtext',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': 'Hello World',
                'array': False,
                'encrypt': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_longtext_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_longtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            'Hello World',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/longtext/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': 'Hello World',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mediumtext_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_mediumtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default='Hello World',
            array=False,
            encrypt=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/mediumtext',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': 'Hello World',
                'array': False,
                'encrypt': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mediumtext_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_mediumtext_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            'Hello World',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/mediumtext/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': 'Hello World',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_point_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_point_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/point',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': [],
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_point_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_point_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default=[],
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/point/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': [],
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_polygon_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_polygon_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/polygon',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': [],
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_polygon_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_polygon_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default=[],
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/polygon/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': [],
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_relationship_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "relatedCollection": "collection",
            "relationType": "oneToOne|oneToMany|manyToOne|manyToMany",
            "twoWay": True,
            "twoWayKey": "string",
            "onDelete": "restrict|cascade|setNull",
            "side": "parent|child",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_relationship_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<RELATED_COLLECTION_ID>',
            'oneToOne',
            two_way=False,
            key='<KEY>',
            two_way_key='<TWO_WAY_KEY>',
            on_delete='cascade',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/relationship',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'relatedCollectionId': '<RELATED_COLLECTION_ID>',
                'type': 'oneToOne',
                'twoWay': False,
                'key': '<KEY>',
                'twoWayKey': '<TWO_WAY_KEY>',
                'onDelete': 'cascade',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_relationship_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "relatedCollection": "collection",
            "relationType": "oneToOne|oneToMany|manyToOne|manyToMany",
            "twoWay": True,
            "twoWayKey": "string",
            "onDelete": "restrict|cascade|setNull",
            "side": "parent|child",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_relationship_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            on_delete='cascade',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/relationship/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'onDelete': 'cascade',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_string_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_string_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            1,
            False,
            default='Hello World',
            array=False,
            encrypt=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/string',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'size': 1,
                'required': False,
                'default': 'Hello World',
                'array': False,
                'encrypt': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_string_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_string_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            'Hello World',
            size=1,
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/string/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': 'Hello World',
                'size': 1,
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_text_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_text_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default='Hello World',
            array=False,
            encrypt=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/text',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': 'Hello World',
                'array': False,
                'encrypt': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_text_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_text_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            'Hello World',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/text/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': 'Hello World',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_url_attribute(self, m):
        data = {
            "key": "githubUrl",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "url",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_url_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            default='https://example.com',
            array=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/url',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'required': False,
                'default': 'https://example.com',
                'array': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_url_attribute(self, m):
        data = {
            "key": "githubUrl",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "format": "url",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_url_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            'https://example.com',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/url/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': 'https://example.com',
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_varchar_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_varchar_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            1,
            False,
            default='Hello World',
            array=False,
            encrypt=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/varchar',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'size': 1,
                'required': False,
                'default': 'Hello World',
                'array': False,
                'encrypt': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_varchar_attribute(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "size": 128.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_varchar_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            False,
            'Hello World',
            size=1,
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/varchar/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'required': False,
                'default': 'Hello World',
                'size': 1,
                'newKey': '<NEW_KEY>',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_attribute(self, m):
        data = {
            "key": "isEnabled",
            "description": "Name shown on the public profile.",
            "type": "boolean",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.get_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/<KEY>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_attribute(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.delete_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/attributes/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_documents(self, m):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.list_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
            total=False,
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'transactionId': ['<TRANSACTION_ID>'],
                'total': ['false'],
                'ttl': ['1'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_document(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            {},
            permissions=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'documentId': '<DOCUMENT_ID>',
                'data': {},
                'permissions': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_documents(self, m):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'documents': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_upsert_documents(self, m):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.upsert_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'documents': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_documents(self, m):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            data={},
            queries=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'data': {},
                'queries': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_documents(self, m):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.delete_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'queries': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_query(self, m):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_query(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
            total=False,
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/query',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'queries': [],
                'transactionId': '<TRANSACTION_ID>',
                'total': False,
                'ttl': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_document(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.get_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'transactionId': ['<TRANSACTION_ID>'],
            },
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_upsert_document(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.upsert_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            data={},
            permissions=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'data': {},
                'permissions': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_document(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.update_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            data={},
            permissions=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'data': {},
                'permissions': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_document(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.delete_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_decrement_document_attribute(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.decrement_document_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            '<ATTRIBUTE>',
            value=1.0,
            min=1.0,
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>/<ATTRIBUTE>/decrement',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'value': 1.0,
                'min': 1.0,
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_increment_document_attribute(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$collectionId": "5e5ea5c15117e",
            "$databaseId": "5e5ea5c15117e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.increment_document_attribute(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            '<ATTRIBUTE>',
            value=1.0,
            max=1.0,
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>/<ATTRIBUTE>/increment',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'value': 1.0,
                'max': 1.0,
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_indexes(self, m):
        data = {
            "total": 5.0,
            "indexes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.list_indexes(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes',
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
    def test_create_index(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "index1",
            "description": "Speeds up lookups by email.",
            "type": "primary",
            "status": "available",
            "error": "string",
            "attributes": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.create_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            'key',
            [],
            orders=[],
            lengths=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'type': 'key',
                'attributes': [],
                'orders': [],
                'lengths': [],
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_index(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "index1",
            "description": "Speeds up lookups by email.",
            "type": "primary",
            "status": "available",
            "error": "string",
            "attributes": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.get_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes/<KEY>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_index(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.databases.delete_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/databases/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
