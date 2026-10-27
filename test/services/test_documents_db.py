import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.documents_db import DocumentsDB


class DocumentsDBServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.documents_db = DocumentsDB(self.client)

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
        response = self.documents_db.list(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb',
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
        response = self.documents_db.create(
            '<DATABASE_ID>',
            '<NAME>',
            enabled=False,
            description='<DESCRIPTION>',
            specification='serverless',
            replicas=1,
            sync_mode='async',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'databaseId': '<DATABASE_ID>',
                'name': '<NAME>',
                'enabled': False,
                'description': '<DESCRIPTION>',
                'specification': 'serverless',
                'replicas': 1,
                'syncMode': 'async',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_specifications(self, m):
        data = {
            "specifications": [],
            "total": 9.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.documents_db.list_specifications()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/specifications',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
        response = self.documents_db.list_transactions(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/transactions',
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
        response = self.documents_db.create_transaction(
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/transactions',
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
        response = self.documents_db.get_transaction(
            '<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/transactions/<TRANSACTION_ID>',
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
        response = self.documents_db.update_transaction(
            '<TRANSACTION_ID>',
            commit=False,
            rollback=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/transactions/<TRANSACTION_ID>',
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
        response = self.documents_db.delete_transaction(
            '<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/transactions/<TRANSACTION_ID>',
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
        response = self.documents_db.create_operations(
            '<TRANSACTION_ID>',
            operations=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/transactions/<TRANSACTION_ID>/operations',
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
        response = self.documents_db.get(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>',
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
        response = self.documents_db.update(
            '<DATABASE_ID>',
            '<NAME>',
            enabled=False,
            description='<DESCRIPTION>',
            specification='serverless',
            replicas=1,
            sync_mode='async',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'enabled': False,
                'description': '<DESCRIPTION>',
                'specification': 'serverless',
                'replicas': 1,
                'syncMode': 'async',
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
        response = self.documents_db.delete(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>',
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
        response = self.documents_db.list_collections(
            '<DATABASE_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections',
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
        response = self.documents_db.create_collection(
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
            '/v1/documentsdb/<DATABASE_ID>/collections',
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
        response = self.documents_db.get_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>',
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
        response = self.documents_db.update_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<NAME>',
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>',
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
        response = self.documents_db.delete_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>',
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
        response = self.documents_db.list_documents(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
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
        response = self.documents_db.create_document(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
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
        response = self.documents_db.create_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
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
        response = self.documents_db.upsert_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
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
        response = self.documents_db.update_documents(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
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
        response = self.documents_db.delete_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents',
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
        response = self.documents_db.create_query(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/query',
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
        response = self.documents_db.get_document(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
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
        response = self.documents_db.upsert_document(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
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
        response = self.documents_db.update_document(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
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
        response = self.documents_db.delete_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>',
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
        response = self.documents_db.decrement_document_attribute(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>/<ATTRIBUTE>/decrement',
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
        response = self.documents_db.increment_document_attribute(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/documents/<DOCUMENT_ID>/<ATTRIBUTE>/increment',
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
        response = self.documents_db.list_indexes(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes',
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
        response = self.documents_db.create_index(
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
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes',
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
        response = self.documents_db.get_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes/<KEY>',
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
        response = self.documents_db.delete_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/collections/<COLLECTION_ID>/indexes/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_failover(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "projectId": "5e5ea5c16897e",
            "name": "My Production Database",
            "version": "16",
            "specification": "s-2vcpu-2gb",
            "backend": "edge",
            "hostname": "db-myproject-mydb.fra.appwrite.center",
            "connectionUser": "appwrite_user",
            "connectionPassword": "\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022",
            "connectionString": "postgresql:\/\/user:pass@db-myproject-mydb.fra.appwrite.center:5432\/postgres?sslmode=require",
            "ssl": True,
            "status": "ready",
            "containerStatus": "active",
            "lifecycleState": "active",
            "idleTimeoutMinutes": 15.0,
            "cpu": 2000.0,
            "memory": 4096.0,
            "storage": 100.0,
            "storageStatus": "resizing",
            "storageTargetGb": 120.0,
            "storageClass": "ssd",
            "storageMaxGb": 100.0,
            "nodePool": "db-pool-4vcpu-8gb",
            "replicas": 2.0,
            "syncMode": "async",
            "networkMaxConnections": 500.0,
            "networkIdleTimeoutSeconds": 900.0,
            "networkIPAllowlist": [],
            "backupEnabled": True,
            "pitr": True,
            "pitrRetentionDays": 14.0,
            "storageAutoscaling": True,
            "storageAutoscalingThresholdPercent": 85.0,
            "storageAutoscalingMaxGb": 30.0,
            "maintenanceWindowDay": "sun",
            "maintenanceWindowHourUtc": 3.0,
            "metricsEnabled": True,
            "sqlApiEnabled": True,
            "sqlApiAllowedStatements": [],
            "sqlApiMaxRows": 10000.0,
            "sqlApiMaxBytes": 10485760.0,
            "sqlApiTimeoutSeconds": 30.0,
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.documents_db.create_failover(
            '<DATABASE_ID>',
            target_replica_id='<TARGET_REPLICA_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/failovers',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'targetReplicaId': '<TARGET_REPLICA_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_operations(self, m):
        data = {
            "total": 5.0,
            "operations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.documents_db.list_operations(
            '<DATABASE_ID>',
            status='queued',
            limit=1,
            offset=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/operations',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'status': ['queued'],
                'limit': ['1'],
                'offset': ['1'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_replicas(self, m):
        data = {
            "replicas": 2.0,
            "syncMode": "async",
            "syncDegraded": True,
            "syncAcknowledgements": 1.0,
            "syncStandbyCount": 2.0,
            "members": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.documents_db.get_replicas(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/replicas',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_status(self, m):
        data = {
            "health": "healthy",
            "ready": True,
            "engine": "postgresql",
            "version": "17",
            "uptime": 86400.0,
            "syncMode": "async",
            "syncDegraded": True,
            "syncAcknowledgements": 1.0,
            "syncStandbyCount": 2.0,
            "replicas": [],
            "volumes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.documents_db.get_status(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/documentsdb/<DATABASE_ID>/status',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)
