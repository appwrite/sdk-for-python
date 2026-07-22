import json
import requests_mock
import unittest

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
    "databases": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "name": "My Database",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "enabled": True,
    "type": "legacy"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create(
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
        "crossRegionReplicaRate": 1,
        "pitrRate": 0.2
    }
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.list_specifications(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_transactions(self, m):
        data = {
    "total": 5.0,
    "transactions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.list_transactions(
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
    "expiresAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_transaction(
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
    "expiresAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get_transaction(
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
    "expiresAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_transaction(
            '<TRANSACTION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_transaction(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.delete_transaction(
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
    "expiresAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_operations(
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
    "type": "legacy"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get(
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
    "type": "legacy"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update(
            '<DATABASE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.delete(
            '<DATABASE_ID>',
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
    "crossRegionReplicas": 1.0,
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
    "error": ""
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_failover(
            '<DATABASE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_replicas(self, m):
        data = {
    "replicas": 2.0,
    "syncMode": "async",
    "members": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get_replicas(
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
        "max": 100.0
    },
    "replicas": [],
    "volumes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get_status(
            '<DATABASE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_tables(self, m):
        data = {
    "total": 5.0,
    "tables": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.list_tables(
            '<DATABASE_ID>',
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
    "enabled": True,
    "rowSecurity": True,
    "columns": [],
    "indexes": [],
    "bytesMax": 65535.0,
    "bytesUsed": 1500.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<NAME>',
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
    "enabled": True,
    "rowSecurity": True,
    "columns": [],
    "indexes": [],
    "bytesMax": 65535.0,
    "bytesUsed": 1500.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )

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
    "enabled": True,
    "rowSecurity": True,
    "columns": [],
    "indexes": [],
    "bytesMax": 65535.0,
    "bytesUsed": 1500.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_table(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.delete_table(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_columns(self, m):
        data = {
    "total": 5.0,
    "columns": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.list_columns(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_big_int_column(self, m):
        data = {
    "key": "count",
    "type": "bigint",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_big_int_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_big_int_column(self, m):
        data = {
    "key": "count",
    "type": "bigint",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_big_int_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            1,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_boolean_column(self, m):
        data = {
    "key": "isEnabled",
    "type": "boolean",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_boolean_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_boolean_column(self, m):
        data = {
    "key": "isEnabled",
    "type": "boolean",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_boolean_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_datetime_column(self, m):
        data = {
    "key": "birthDay",
    "type": "datetime",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_datetime_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_datetime_column(self, m):
        data = {
    "key": "birthDay",
    "type": "datetime",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "datetime"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_datetime_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            '2020-10-15T06:38:00.000+00:00',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_email_column(self, m):
        data = {
    "key": "userEmail",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "email"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_email_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_column(self, m):
        data = {
    "key": "userEmail",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "email"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_email_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            'email@example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_enum_column(self, m):
        data = {
    "key": "status",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "elements": [],
    "format": "enum"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_enum_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            [],
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_enum_column(self, m):
        data = {
    "key": "status",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "elements": [],
    "format": "enum"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_enum_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            [],
            True,
            '<DEFAULT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_float_column(self, m):
        data = {
    "key": "percentageCompleted",
    "type": "double",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_float_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_float_column(self, m):
        data = {
    "key": "percentageCompleted",
    "type": "double",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_float_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            1.0,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_integer_column(self, m):
        data = {
    "key": "count",
    "type": "integer",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_integer_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_integer_column(self, m):
        data = {
    "key": "count",
    "type": "integer",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_integer_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            1,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_ip_column(self, m):
        data = {
    "key": "ipAddress",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "ip"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_ip_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_ip_column(self, m):
        data = {
    "key": "ipAddress",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "ip"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_ip_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            '',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_line_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_line_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_line_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_line_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_longtext_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_longtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_longtext_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_longtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            '<DEFAULT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mediumtext_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_mediumtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mediumtext_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_mediumtext_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            '<DEFAULT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_point_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_point_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_point_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_point_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_polygon_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_polygon_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_polygon_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_polygon_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_relationship_column(self, m):
        data = {
    "key": "fullName",
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
    "side": "parent|child"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_relationship_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<RELATED_TABLE_ID>',
            'oneToOne',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_string_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "size": 128.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_string_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            1,
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_string_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "size": 128.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_string_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            '<DEFAULT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_text_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_text_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_text_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_text_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            '<DEFAULT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_url_column(self, m):
        data = {
    "key": "githubUrl",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "url"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_url_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_url_column(self, m):
        data = {
    "key": "githubUrl",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "format": "url"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_url_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            'https://example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_varchar_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "size": 128.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_varchar_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            1,
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_varchar_column(self, m):
        data = {
    "key": "fullName",
    "type": "string",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "size": 128.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_varchar_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            True,
            '<DEFAULT>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_column(self, m):
        data = {
    "key": "isEnabled",
    "type": "boolean",
    "status": "available",
    "error": "string",
    "required": True,
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_column(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.delete_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_relationship_column(self, m):
        data = {
    "key": "fullName",
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
    "side": "parent|child"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_relationship_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_indexes(self, m):
        data = {
    "total": 5.0,
    "indexes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.list_indexes(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
    "columns": [],
    "lengths": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_index(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
            'key',
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
    "columns": [],
    "lengths": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get_index(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_index(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.delete_index(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_rows(self, m):
        data = {
    "total": 5.0,
    "rows": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.list_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
    "$permissions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            {},
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_rows(self, m):
        data = {
    "total": 5.0,
    "rows": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.create_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_upsert_rows(self, m):
        data = {
    "total": 5.0,
    "rows": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.upsert_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_rows(self, m):
        data = {
    "total": 5.0,
    "rows": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_rows(self, m):
        data = {
    "total": 5.0,
    "rows": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.delete_rows(
            '<DATABASE_ID>',
            '<TABLE_ID>',
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
    "$permissions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.get_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
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
    "$permissions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.upsert_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
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
    "$permissions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.update_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_row(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.delete_row(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
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
    "$permissions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.decrement_row_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            '',
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
    "$permissions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.tables_db.increment_row_column(
            '<DATABASE_ID>',
            '<TABLE_ID>',
            '<ROW_ID>',
            '',
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

