import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.mysql import Mysql


class MysqlServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.mysql = Mysql(self.client)

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
        response = self.mysql.list()
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.create(
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
        response = self.mysql.list_specifications()
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.get(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.update(
            '<DATABASE_ID>',
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
        response = self.mysql.delete(
            '<DATABASE_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_backups(self, m):
        data = {
            "total": 5.0,
            "backups": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_backups(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_backup(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "projectId": "5e5ea5c16897e",
            "policyId": "5e5ea5c16897e",
            "trigger": "schedule",
            "type": "full",
            "requestedType": "incremental",
            "fallbackReason": "PostgreSQL incremental backups are not offered because they cannot be restored: archived WAL is physical and cannot replay onto a logically-restored base. A full backup was taken instead; use a point-in-time restore (targetTime) to recover to a moment between fulls.",
            "status": "completed",
            "sizeBytes": 1073741824.0,
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_backup(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_backup_policies(self, m):
        data = {
            "total": 5.0,
            "policies": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_backup_policies(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_backup_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "Hourly backups",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "services": [],
            "resources": [],
            "retention": 7.0,
            "schedule": "0 * * * *",
            "type": "full",
            "enabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
            '<NAME>',
            '',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_backup_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "Hourly backups",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "services": [],
            "resources": [],
            "retention": 7.0,
            "schedule": "0 * * * *",
            "type": "full",
            "enabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_backup_policy(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "name": "Hourly backups",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "services": [],
            "resources": [],
            "retention": 7.0,
            "schedule": "0 * * * *",
            "type": "full",
            "enabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_backup_policy(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.delete_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_backup_storage(self, m):
        data = {
            "provider": "s3",
            "bucket": "my-backup-bucket",
            "region": "us-east-1",
            "prefix": "backups\/",
            "endpoint": "https:\/\/minio.example.com",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_backup_storage(
            '<DATABASE_ID>',
            's3',
            '<BUCKET>',
            '<ACCESS_KEY>',
            '<SECRET_KEY>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_backup(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "projectId": "5e5ea5c16897e",
            "policyId": "5e5ea5c16897e",
            "trigger": "schedule",
            "type": "full",
            "requestedType": "incremental",
            "fallbackReason": "PostgreSQL incremental backups are not offered because they cannot be restored: archived WAL is physical and cannot replay onto a logically-restored base. A full backup was taken instead; use a point-in-time restore (targetTime) to recover to a moment between fulls.",
            "status": "completed",
            "sizeBytes": 1073741824.0,
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_backup(
            '<DATABASE_ID>',
            '<BACKUP_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_backup(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.delete_backup(
            '<DATABASE_ID>',
            '<BACKUP_ID>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_branches(self, m):
        data = {
            "total": 2.0,
            "branches": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_branches(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_branch(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.create_branch(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_branch(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.delete_branch(
            '<DATABASE_ID>',
            '<BRANCH_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_credentials(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "type": "update",
            "status": "completed",
            "attempts": 1.0,
            "errorCode": "Interrupted",
            "errorMessage": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_credentials(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_execution(self, m):
        data = {
            "rows": [],
            "rowCount": 1.0,
            "columns": [],
            "durationMs": 12.0,
            "truncated": True,
            "bytes": 1024.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_execution(
            '<DATABASE_ID>',
            '<SQL>',
        )
        self.assertEqual(response.to_dict(), data)

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
            "credentialGeneration": 1.0,
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
        response = self.mysql.create_failover(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_maintenance(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.update_maintenance(
            '<DATABASE_ID>',
            'sun',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_migration(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.create_migration(
            '<DATABASE_ID>',
            'shared',
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
        response = self.mysql.list_operations(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_pitr(self, m):
        data = {
            "earliest": "2020-10-15T06:38:00.000+00:00",
            "latest": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_pitr(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_pooler(self, m):
        data = {
            "enabled": True,
            "mode": "transaction",
            "maxConnections": 200.0,
            "defaultPoolSize": 25.0,
            "port": 6432.0,
            "readWriteSplitting": True,
            "poolerCpuRequest": "100m",
            "poolerCpuLimit": "200m",
            "poolerMemoryRequest": "64Mi",
            "poolerMemoryLimit": "128Mi",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_pooler(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_pooler(self, m):
        data = {
            "enabled": True,
            "mode": "transaction",
            "maxConnections": 200.0,
            "defaultPoolSize": 25.0,
            "port": 6432.0,
            "readWriteSplitting": True,
            "poolerCpuRequest": "100m",
            "poolerCpuLimit": "200m",
            "poolerMemoryRequest": "64Mi",
            "poolerMemoryLimit": "128Mi",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_pooler(
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
        response = self.mysql.get_replicas(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_restorations(self, m):
        data = {
            "total": 5.0,
            "restorations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_restorations(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_restoration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "sourceDatabaseId": "5e5ea5c16897e",
            "projectId": "5e5ea5c16897e",
            "backupId": "5e5ea5c16897e",
            "type": "backup",
            "status": "completed",
            "targetTime": "2020-10-15T06:38:00.000+00:00",
            "startedAt": "2020-10-15T06:38:00.000+00:00",
            "completedAt": "2020-10-15T06:38:00.000+00:00",
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_restoration(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_restoration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "sourceDatabaseId": "5e5ea5c16897e",
            "projectId": "5e5ea5c16897e",
            "backupId": "5e5ea5c16897e",
            "type": "backup",
            "status": "completed",
            "targetTime": "2020-10-15T06:38:00.000+00:00",
            "startedAt": "2020-10-15T06:38:00.000+00:00",
            "completedAt": "2020-10-15T06:38:00.000+00:00",
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_restoration(
            '<DATABASE_ID>',
            '<RESTORATION_ID>',
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
        response = self.mysql.get_status(
            '<DATABASE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_upgrade(self, m):
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
            "credentialGeneration": 1.0,
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
        response = self.mysql.create_upgrade(
            '<DATABASE_ID>',
            '<TARGET_VERSION>',
        )
        self.assertEqual(response.to_dict(), data)
