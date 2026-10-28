import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.migrations import Migrations


class MigrationsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.migrations = Migrations(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "migrations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations',
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
    def test_create_appwrite_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_appwrite_migration(
            [],
            'https://example.com',
            '<PROJECT_ID>',
            '<API_KEY>',
            on_duplicate='fail',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/appwrite',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resources': [],
                'endpoint': 'https://example.com',
                'projectId': '<PROJECT_ID>',
                'apiKey': '<API_KEY>',
                'onDuplicate': 'fail',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_csv_export(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_csv_export(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<FILENAME>',
            columns=[],
            queries=[],
            delimiter='<DELIMITER>',
            enclosure='<ENCLOSURE>',
            escape='<ESCAPE>',
            header=False,
            notify=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/csv/exports',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'databaseId': '<DATABASE_ID>',
                'collectionId': '<COLLECTION_ID>',
                'filename': '<FILENAME>',
                'columns': [],
                'queries': [],
                'delimiter': '<DELIMITER>',
                'enclosure': '<ENCLOSURE>',
                'escape': '<ESCAPE>',
                'header': False,
                'notify': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_csv_import(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_csv_import(
            '<BUCKET_ID>',
            '<FILE_ID>',
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            internal_file=False,
            on_duplicate='fail',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/csv/imports',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'bucketId': '<BUCKET_ID>',
                'fileId': '<FILE_ID>',
                'databaseId': '<DATABASE_ID>',
                'collectionId': '<COLLECTION_ID>',
                'internalFile': False,
                'onDuplicate': 'fail',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_firebase_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_firebase_migration(
            [],
            '<SERVICE_ACCOUNT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/firebase',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resources': [],
                'serviceAccount': '<SERVICE_ACCOUNT>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_json_export(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_json_export(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<FILENAME>',
            columns=[],
            queries=[],
            notify=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/json/exports',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'databaseId': '<DATABASE_ID>',
                'collectionId': '<COLLECTION_ID>',
                'filename': '<FILENAME>',
                'columns': [],
                'queries': [],
                'notify': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_json_import(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_json_import(
            '<BUCKET_ID>',
            '<FILE_ID>',
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            internal_file=False,
            on_duplicate='fail',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/json/imports',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'bucketId': '<BUCKET_ID>',
                'fileId': '<FILE_ID>',
                'databaseId': '<DATABASE_ID>',
                'collectionId': '<COLLECTION_ID>',
                'internalFile': False,
                'onDuplicate': 'fail',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_n_host_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_n_host_migration(
            [],
            '<SUBDOMAIN>',
            '<REGION>',
            '<ADMIN_SECRET>',
            '<DATABASE>',
            '<USERNAME>',
            'password',
            port=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/nhost',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resources': [],
                'subdomain': '<SUBDOMAIN>',
                'region': '<REGION>',
                'adminSecret': '<ADMIN_SECRET>',
                'database': '<DATABASE>',
                'username': '<USERNAME>',
                'password': 'password',
                'port': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_supabase_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.create_supabase_migration(
            [],
            'https://example.com',
            '<API_KEY>',
            '<DATABASE_HOST>',
            '<USERNAME>',
            'password',
            port=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/supabase',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resources': [],
                'endpoint': 'https://example.com',
                'apiKey': '<API_KEY>',
                'databaseHost': '<DATABASE_HOST>',
                'username': '<USERNAME>',
                'password': 'password',
                'port': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.get(
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/<MIGRATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_retry(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "status": "pending",
            "stage": "init",
            "source": "Appwrite",
            "destination": "Appwrite",
            "resources": [],
            "resourceId": "collectionId",
            "resourceInternalId": "1",
            "resourceType": "collection",
            "parentResourceId": "databaseId",
            "parentResourceInternalId": "1",
            "parentResourceType": "database",
            "destinationResourceId": "databaseId",
            "destinationResourceInternalId": "1",
            "destinationResourceType": "database",
            "statusCounters": {},
            "resourceData": [],
            "errors": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.migrations.retry(
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/<MIGRATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
        response = self.migrations.delete(
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/migrations/<MIGRATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
