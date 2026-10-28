import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql',
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
        response = self.mysql.create(
            '<DATABASE_ID>',
            '<NAME>',
            version='17',
            specification='<SPECIFICATION>',
            replicas=1,
            sync_mode='async',
            network_idle_timeout_seconds=1,
            network_ip_allowlist=[],
            idle_timeout_minutes=1,
            pitr=False,
            pitr_retention_days=1,
            storage_autoscaling=False,
            storage_autoscaling_threshold_percent=1,
            storage_autoscaling_max_gb=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'databaseId': '<DATABASE_ID>',
                'name': '<NAME>',
                'version': '17',
                'specification': '<SPECIFICATION>',
                'replicas': 1,
                'syncMode': 'async',
                'networkIdleTimeoutSeconds': 1,
                'networkIPAllowlist': [],
                'idleTimeoutMinutes': 1,
                'pitr': False,
                'pitrRetentionDays': 1,
                'storageAutoscaling': False,
                'storageAutoscalingThresholdPercent': 1,
                'storageAutoscalingMaxGb': 1,
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
        response = self.mysql.list_specifications()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/specifications',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
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
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update(
            '<DATABASE_ID>',
            name='<NAME>',
            status='ready',
            specification='<SPECIFICATION>',
            replicas=1,
            sync_mode='async',
            network_idle_timeout_seconds=1,
            network_ip_allowlist=[],
            idle_timeout_minutes=1,
            pitr=False,
            pitr_retention_days=1,
            storage_autoscaling=False,
            storage_autoscaling_threshold_percent=1,
            storage_autoscaling_max_gb=1,
            metrics_trace_sample_rate=1.0,
            metrics_slow_query_log_threshold_ms=1,
            sql_api_enabled=False,
            sql_api_allowed_statements=[],
            sql_api_max_rows=1,
            sql_api_max_bytes=1,
            sql_api_timeout_seconds=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'status': 'ready',
                'specification': '<SPECIFICATION>',
                'replicas': 1,
                'syncMode': 'async',
                'networkIdleTimeoutSeconds': 1,
                'networkIPAllowlist': [],
                'idleTimeoutMinutes': 1,
                'pitr': False,
                'pitrRetentionDays': 1,
                'storageAutoscaling': False,
                'storageAutoscalingThresholdPercent': 1,
                'storageAutoscalingMaxGb': 1,
                'metricsTraceSampleRate': 1.0,
                'metricsSlowQueryLogThresholdMs': 1,
                'sqlApiEnabled': False,
                'sqlApiAllowedStatements': [],
                'sqlApiMaxRows': 1,
                'sqlApiMaxBytes': 1,
                'sqlApiTimeoutSeconds': 1,
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
        response = self.mysql.delete(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_backups(self, m):
        data = {
            "total": 5.0,
            "backups": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_backups(
            '<DATABASE_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups',
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
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_backup(
            '<DATABASE_ID>',
            type='full',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'type': 'full',
            },
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_backup_policies(
            '<DATABASE_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/policies',
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
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
            '<NAME>',
            'schedule',
            1,
            type='full',
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/policies',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'policyId': '<POLICY_ID>',
                'name': '<NAME>',
                'schedule': 'schedule',
                'retention': 1,
                'type': 'full',
                'enabled': False,
            },
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/policies/<POLICY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
            name='<NAME>',
            schedule='schedule',
            retention=1,
            enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/policies/<POLICY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'schedule': 'schedule',
                'retention': 1,
                'enabled': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_backup_policy(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.delete_backup_policy(
            '<DATABASE_ID>',
            '<POLICY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/policies/<POLICY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            'PUT',
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
            region='<REGION>',
            prefix='<PREFIX>',
            endpoint='https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/storage',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'provider': 's3',
                'bucket': '<BUCKET>',
                'region': '<REGION>',
                'prefix': '<PREFIX>',
                'endpoint': 'https://example.com',
                'accessKey': '<ACCESS_KEY>',
                'secretKey': '<SECRET_KEY>',
            },
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_backup(
            '<DATABASE_ID>',
            '<BACKUP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/<BACKUP_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_backup(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.delete_backup(
            '<DATABASE_ID>',
            '<BACKUP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/backups/<BACKUP_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_branches(self, m):
        data = {
            "total": 2.0,
            "branches": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_branches(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/branches',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_branch(self, m):
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
        response = self.mysql.create_branch(
            '<DATABASE_ID>',
            branch_id='<BRANCH_ID>',
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/branches',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'branchId': '<BRANCH_ID>',
                'ttl': 1,
            },
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
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.delete_branch(
            '<DATABASE_ID>',
            '<BRANCH_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/branches/<BRANCH_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_credentials(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/credentials',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_execution(
            '<DATABASE_ID>',
            '<SQL>',
            bindings={},
            timeout_seconds=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/executions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'sql': '<SQL>',
                'bindings': {},
                'timeoutSeconds': 1,
            },
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
        response = self.mysql.create_failover(
            '<DATABASE_ID>',
            target_replica_id='<TARGET_REPLICA_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/failovers',
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
    def test_update_maintenance(self, m):
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
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_maintenance(
            '<DATABASE_ID>',
            'sun',
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/maintenance',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'day': 'sun',
                'hourUtc': 1,
            },
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
        response = self.mysql.create_migration(
            '<DATABASE_ID>',
            'shared',
            specification='<SPECIFICATION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/migrations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'targetType': 'shared',
                'specification': '<SPECIFICATION>',
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
        response = self.mysql.list_operations(
            '<DATABASE_ID>',
            status='queued',
            limit=1,
            offset=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/operations',
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
    def test_get_pitr(self, m):
        data = {
            "earliest": "2020-10-15T06:38:00.000+00:00",
            "latest": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_pitr(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/pitr',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_pooler(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/pooler',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.update_pooler(
            '<DATABASE_ID>',
            mode='transaction',
            max_connections=1,
            default_pool_size=1,
            read_write_splitting=False,
            pooler_cpu_request='<POOLER_CPU_REQUEST>',
            pooler_cpu_limit='<POOLER_CPU_LIMIT>',
            pooler_memory_request='<POOLER_MEMORY_REQUEST>',
            pooler_memory_limit='<POOLER_MEMORY_LIMIT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/pooler',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'mode': 'transaction',
                'maxConnections': 1,
                'defaultPoolSize': 1,
                'readWriteSplitting': False,
                'poolerCpuRequest': '<POOLER_CPU_REQUEST>',
                'poolerCpuLimit': '<POOLER_CPU_LIMIT>',
                'poolerMemoryRequest': '<POOLER_MEMORY_REQUEST>',
                'poolerMemoryLimit': '<POOLER_MEMORY_LIMIT>',
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
        response = self.mysql.get_replicas(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/replicas',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_restorations(self, m):
        data = {
            "total": 5.0,
            "restorations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.list_restorations(
            '<DATABASE_ID>',
            status='pending',
            type='backup',
            limit=1,
            offset=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/restorations',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'status': ['pending'],
                'type': ['backup'],
                'limit': ['1'],
                'offset': ['1'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_restoration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "projectId": "5e5ea5c16897e",
            "type": "backup",
            "restoreMode": "clone",
            "status": "completed",
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.create_restoration(
            '<DATABASE_ID>',
            type='backup',
            backup_id='<BACKUP_ID>',
            target_database_id='<TARGET_DATABASE_ID>',
            target_time='2020-10-15T06:38:00.000+00:00',
            restore_mode='in_place',
            target_name='<TARGET_NAME>',
            auto_promote=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/restorations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'type': 'backup',
                'backupId': '<BACKUP_ID>',
                'targetDatabaseId': '<TARGET_DATABASE_ID>',
                'targetTime': '2020-10-15T06:38:00.000+00:00',
                'restoreMode': 'in_place',
                'targetName': '<TARGET_NAME>',
                'autoPromote': False,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_restoration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "projectId": "5e5ea5c16897e",
            "type": "backup",
            "restoreMode": "clone",
            "status": "completed",
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.get_restoration(
            '<DATABASE_ID>',
            '<RESTORATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/restorations/<RESTORATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_promote_restoration(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "databaseId": "5e5ea5c16897e",
            "projectId": "5e5ea5c16897e",
            "type": "backup",
            "restoreMode": "clone",
            "status": "completed",
            "error": "",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.mysql.promote_restoration(
            '<DATABASE_ID>',
            '<RESTORATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/restorations/<RESTORATION_ID>/promotions',
        )
        sent = json.loads(request.body or '{}')
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
        response = self.mysql.get_status(
            '<DATABASE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/status',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_upgrade(self, m):
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
        response = self.mysql.create_upgrade(
            '<DATABASE_ID>',
            '<TARGET_VERSION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/mysql/<DATABASE_ID>/upgrades',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'targetVersion': '<TARGET_VERSION>',
            },
        )
        self.assertEqual(response.to_dict(), data)
