import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.tables_db import TablesDB


class TablesDBServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.tables_db = TablesDB(self.client)

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
        response = self.tables_db.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb',
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
        response = self.tables_db.create(
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
            '/v1/tablesdb',
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
        response = self.tables_db.list_specifications()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/specifications',
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
        response = self.tables_db.list_transactions(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/transactions',
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
        response = self.tables_db.create_transaction(
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/transactions',
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
        response = self.tables_db.get_transaction(
            '<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/transactions/<TRANSACTION_ID>',
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
        response = self.tables_db.update_transaction(
            '<TRANSACTION_ID>',
            commit=False,
            rollback=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/transactions/<TRANSACTION_ID>',
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
        response = self.tables_db.delete_transaction(
            '<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/transactions/<TRANSACTION_ID>',
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
        response = self.tables_db.create_operations(
            '<TRANSACTION_ID>',
            operations=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/transactions/<TRANSACTION_ID>/operations',
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
        response = self.tables_db.get(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>',
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
        response = self.tables_db.update(
            '<DATABASE_ID>',
            name='<NAME>',
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
            '/v1/tablesdb/<DATABASE_ID>',
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
        response = self.tables_db.delete(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>',
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
        response = self.tables_db.create_failover(
            '<DATABASE_ID>',
            target_replica_id='<TARGET_REPLICA_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/failovers',
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
    def test_list_migrations(self, m):
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
        response = self.tables_db.list_migrations(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/migrations',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "projectId": "5e5ea5c16897e",
            "databaseId": "5e5ea5c16897e",
            "specification": "s-2vcpu-4gb",
            "phase": "pending",
            "attempt": 0.0,
            "lastError": "",
            "lagDocuments": 0.0,
            "changelogWatermark": 0.0,
            "verifiedAt": "2020-10-15T06:38:00.000+00:00",
            "cutoverAt": "2020-10-15T06:38:00.000+00:00",
            "soakUntil": "2020-10-15T06:38:00.000+00:00",
            "autoCutover": True,
            "cutoverRequested": True,
            "paused": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.create_migration(
            '<DATABASE_ID>',
            's-1vcpu-1gb',
            auto_cutover=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/migrations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'specification': 's-1vcpu-1gb',
                'autoCutover': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_migration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "projectId": "5e5ea5c16897e",
            "databaseId": "5e5ea5c16897e",
            "specification": "s-2vcpu-4gb",
            "phase": "pending",
            "attempt": 0.0,
            "lastError": "",
            "lagDocuments": 0.0,
            "changelogWatermark": 0.0,
            "verifiedAt": "2020-10-15T06:38:00.000+00:00",
            "cutoverAt": "2020-10-15T06:38:00.000+00:00",
            "soakUntil": "2020-10-15T06:38:00.000+00:00",
            "autoCutover": True,
            "cutoverRequested": True,
            "paused": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.get_migration(
            '<DATABASE_ID>',
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/migrations/<MIGRATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_migration(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.delete_migration(
            '<DATABASE_ID>',
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/migrations/<MIGRATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_cutover(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "projectId": "5e5ea5c16897e",
            "databaseId": "5e5ea5c16897e",
            "specification": "s-2vcpu-4gb",
            "phase": "pending",
            "attempt": 0.0,
            "lastError": "",
            "lagDocuments": 0.0,
            "changelogWatermark": 0.0,
            "verifiedAt": "2020-10-15T06:38:00.000+00:00",
            "cutoverAt": "2020-10-15T06:38:00.000+00:00",
            "soakUntil": "2020-10-15T06:38:00.000+00:00",
            "autoCutover": True,
            "cutoverRequested": True,
            "paused": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.create_cutover(
            '<DATABASE_ID>',
            '<MIGRATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/migrations/<MIGRATION_ID>/cutovers',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
        response = self.tables_db.list_operations(
            '<DATABASE_ID>',
            status='queued',
            limit=1,
            offset=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/operations',
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
        response = self.tables_db.get_replicas(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/replicas',
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
        response = self.tables_db.get_status(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/status',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_tables(self, m):
        data = {
            "total": 5.0,
            "tables": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.list_tables(
            '<DATABASE_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables',
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
    def test_create_table(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Table",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "rowSecurity": True,
            "columns": [],
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
        response = self.tables_db.create_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<NAME>',
            permissions=[],
            row_security=False,
            enabled=False,
            columns=[],
            indexes=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'tableId': '<TABLE_ID>',
                'name': '<NAME>',
                'permissions': [],
                'rowSecurity': False,
                'enabled': False,
                'columns': [],
                'indexes': [],
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_table(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Table",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "rowSecurity": True,
            "columns": [],
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
        response = self.tables_db.get_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_table(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "databaseId": "5e5ea5c16897e",
            "name": "My Table",
            "description": "Movies available in the catalog.",
            "enabled": True,
            "rowSecurity": True,
            "columns": [],
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
        response = self.tables_db.update_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            name='<NAME>',
            permissions=[],
            row_security=False,
            enabled=False,
            purge=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'permissions': [],
                'rowSecurity': False,
                'enabled': False,
                'purge': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_table(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.delete_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_columns(self, m):
        data = {
            "total": 5.0,
            "columns": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.list_columns(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns',
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
    def test_create_big_int_column(self, m):
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
        response = self.tables_db.create_big_int_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/bigint',
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
    def test_update_big_int_column(self, m):
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
        response = self.tables_db.update_big_int_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/bigint/<KEY>',
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
    def test_create_boolean_column(self, m):
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
        response = self.tables_db.create_boolean_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/boolean',
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
    def test_update_boolean_column(self, m):
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
        response = self.tables_db.update_boolean_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/boolean/<KEY>',
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
    def test_create_datetime_column(self, m):
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
        response = self.tables_db.create_datetime_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/datetime',
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
    def test_update_datetime_column(self, m):
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
        response = self.tables_db.update_datetime_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/datetime/<KEY>',
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
    def test_create_email_column(self, m):
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
        response = self.tables_db.create_email_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/email',
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
    def test_update_email_column(self, m):
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
        response = self.tables_db.update_email_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/email/<KEY>',
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
    def test_create_enum_column(self, m):
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
        response = self.tables_db.create_enum_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/enum',
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
    def test_update_enum_column(self, m):
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
        response = self.tables_db.update_enum_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/enum/<KEY>',
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
    def test_create_float_column(self, m):
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
        response = self.tables_db.create_float_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/float',
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
    def test_update_float_column(self, m):
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
        response = self.tables_db.update_float_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/float/<KEY>',
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
    def test_create_integer_column(self, m):
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
        response = self.tables_db.create_integer_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/integer',
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
    def test_update_integer_column(self, m):
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
        response = self.tables_db.update_integer_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/integer/<KEY>',
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
    def test_create_ip_column(self, m):
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
        response = self.tables_db.create_ip_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/ip',
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
    def test_update_ip_column(self, m):
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
        response = self.tables_db.update_ip_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/ip/<KEY>',
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
    def test_create_line_column(self, m):
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
        response = self.tables_db.create_line_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
            False,
            default=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/line',
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
    def test_update_line_column(self, m):
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
        response = self.tables_db.update_line_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/line/<KEY>',
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
    def test_create_longtext_column(self, m):
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
        response = self.tables_db.create_longtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/longtext',
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
    def test_update_longtext_column(self, m):
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
        response = self.tables_db.update_longtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/longtext/<KEY>',
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
    def test_create_mediumtext_column(self, m):
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
        response = self.tables_db.create_mediumtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/mediumtext',
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
    def test_update_mediumtext_column(self, m):
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
        response = self.tables_db.update_mediumtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/mediumtext/<KEY>',
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
    def test_create_point_column(self, m):
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
        response = self.tables_db.create_point_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
            False,
            default=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/point',
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
    def test_update_point_column(self, m):
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
        response = self.tables_db.update_point_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/point/<KEY>',
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
    def test_create_polygon_column(self, m):
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
        response = self.tables_db.create_polygon_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
            False,
            default=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/polygon',
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
    def test_update_polygon_column(self, m):
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
        response = self.tables_db.update_polygon_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/polygon/<KEY>',
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
    def test_create_relationship_column(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "relatedTable": "table",
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
        response = self.tables_db.create_relationship_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<RELATED_TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/relationship',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'relatedTableId': '<RELATED_TABLE_ID>',
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
    def test_update_relationship_column(self, m):
        data = {
            "key": "fullName",
            "description": "Name shown on the public profile.",
            "type": "string",
            "status": "available",
            "error": "string",
            "required": True,
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "relatedTable": "table",
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
        response = self.tables_db.update_relationship_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
            on_delete='cascade',
            new_key='<NEW_KEY>',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/relationship/<KEY>',
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
    def test_create_string_column(self, m):
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
        response = self.tables_db.create_string_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/string',
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
    def test_update_string_column(self, m):
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
        response = self.tables_db.update_string_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/string/<KEY>',
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
    def test_create_text_column(self, m):
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
        response = self.tables_db.create_text_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/text',
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
    def test_update_text_column(self, m):
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
        response = self.tables_db.update_text_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/text/<KEY>',
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
    def test_create_url_column(self, m):
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
        response = self.tables_db.create_url_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/url',
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
    def test_update_url_column(self, m):
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
        response = self.tables_db.update_url_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/url/<KEY>',
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
    def test_create_varchar_column(self, m):
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
        response = self.tables_db.create_varchar_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/varchar',
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
    def test_update_varchar_column(self, m):
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
        response = self.tables_db.update_varchar_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/varchar/<KEY>',
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
    def test_get_column(self, m):
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
        response = self.tables_db.get_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/<KEY>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_column(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.delete_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/columns/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

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
        response = self.tables_db.list_indexes(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/indexes',
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
            "columns": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.create_index(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/indexes',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'type': 'key',
                'columns': [],
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
            "columns": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.get_index(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/indexes/<KEY>',
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
        response = self.tables_db.delete_index(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<KEY>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/indexes/<KEY>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_rows(self, m):
        data = {
            "total": 5.0,
            "rows": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.list_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
            total=False,
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows',
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
    def test_create_row(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$tableId": "5e5ea5c15117e",
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
        response = self.tables_db.create_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            {},
            permissions=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'rowId': '<ROW_ID>',
                'data': {},
                'permissions': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_rows(self, m):
        data = {
            "total": 5.0,
            "rows": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.create_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            [],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'rows': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_upsert_rows(self, m):
        data = {
            "total": 5.0,
            "rows": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.upsert_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            [],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'rows': [],
                'transactionId': '<TRANSACTION_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_rows(self, m):
        data = {
            "total": 5.0,
            "rows": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.update_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            data={},
            queries=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows',
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
    def test_delete_rows(self, m):
        data = {
            "total": 5.0,
            "rows": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.delete_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows',
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
            "rows": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.create_query(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
            total=False,
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows/query',
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
    def test_get_row(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$tableId": "5e5ea5c15117e",
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
        response = self.tables_db.get_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            queries=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows/<ROW_ID>',
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
    def test_upsert_row(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$tableId": "5e5ea5c15117e",
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
        response = self.tables_db.upsert_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            data={},
            permissions=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows/<ROW_ID>',
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
    def test_update_row(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$tableId": "5e5ea5c15117e",
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
        response = self.tables_db.update_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            data={},
            permissions=[],
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows/<ROW_ID>',
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
    def test_delete_row(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.tables_db.delete_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows/<ROW_ID>',
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
    def test_decrement_row_column(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$tableId": "5e5ea5c15117e",
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
        response = self.tables_db.decrement_row_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            '<COLUMN>',
            value=1.0,
            min=1.0,
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows/<ROW_ID>/<COLUMN>/decrement',
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
    def test_increment_row_column(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$sequence": "1",
            "$tableId": "5e5ea5c15117e",
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
        response = self.tables_db.increment_row_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            '<COLUMN>',
            value=1.0,
            max=1.0,
            transaction_id='<TRANSACTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/tablesdb/<DATABASE_ID>/tables/<TABLE_ID>/rows/<ROW_ID>/<COLUMN>/increment',
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
