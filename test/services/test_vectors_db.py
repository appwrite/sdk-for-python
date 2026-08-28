import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.vectors_db import VectorsDB


class VectorsDBServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.vectors_db = VectorsDB(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
            "total": 5.0,
            "databases": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.list()
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create(
            '<DATABASE_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_specifications(self, m):
        data = {
            "specifications": [],
            "total": 9.0,
            "pricing": {
                "storageOverageRate": 0.125,
                "bandwidthOverageRate": 0.08,
                "replicaRate": 1,
                "pitrRate": 0.2,
            },
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.list_specifications()
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_transactions(self, m):
        data = {
            "total": 5.0,
            "transactions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.list_transactions()
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_transaction()
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.get_transaction(
            '<TRANSACTION_ID>',
        )
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.update_transaction(
            '<TRANSACTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_transaction(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.delete_transaction(
            '<TRANSACTION_ID>',
        )
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_operations(
            '<TRANSACTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.get(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "My Database",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "enabled": True,
            "type": "legacy",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.update(
            '<DATABASE_ID>',
            '<NAME>',
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
        response = self.vectors_db.delete(
            '<DATABASE_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_collections(self, m):
        data = {
            "total": 5.0,
            "collections": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.list_collections(
            '<DATABASE_ID>',
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
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
            "dimension": 1536.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<NAME>',
            1,
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
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
            "dimension": 1536.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.get_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
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
            "enabled": True,
            "documentSecurity": True,
            "attributes": [],
            "indexes": [],
            "bytesMax": 65535.0,
            "bytesUsed": 1500.0,
            "dimension": 1536.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.update_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_collection(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.delete_collection(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_documents(self, m):
        data = {
            "total": 5.0,
            "documents": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.list_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
            {},
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.upsert_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            [],
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.update_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.delete_documents(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_query(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.get_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.upsert_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.update_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
        )
        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_document(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.delete_document(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<DOCUMENT_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_indexes(self, m):
        data = {
            "total": 5.0,
            "indexes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.list_indexes(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_index(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "index1",
            "type": "primary",
            "status": "available",
            "error": "string",
            "attributes": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
            'hnsw_euclidean',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_index(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "index1",
            "type": "primary",
            "status": "available",
            "error": "string",
            "attributes": [],
            "lengths": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.get_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_index(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.delete_index(
            '<DATABASE_ID>',
            '<COLLECTION_ID>',
            '<KEY>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_failover(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "projectId": "5e5ea5c16897e",
            "name": "My Production Database",
            "api": "postgresql",
            "engine": "postgresql",
            "version": "16",
            "specification": "s-2vcpu-2gb",
            "backend": "edge",
            "hostname": "db-myproject-mydb.fra.appwrite.center",
            "connectionPort": 5432.0,
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
            "storageAutoscalingMaxGb": 500.0,
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.create_failover(
            '<DATABASE_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.list_operations(
            '<DATABASE_ID>',
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
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.get_replicas(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_status(self, m):
        data = {
            "health": "healthy",
            "ready": True,
            "engine": "postgresql",
            "version": "17",
            "uptime": 86400.0,
            "connections": {
                "current": 12.0,
                "max": 100.0,
            },
            "syncMode": "async",
            "syncDegraded": True,
            "syncAcknowledgements": 1.0,
            "syncStandbyCount": 2.0,
            "replicas": [],
            "volumes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.vectors_db.get_status(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)
