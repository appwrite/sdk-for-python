import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.waf import Waf


class WafServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.waf = Waf(self.client)

    @requests_mock.Mocker()
    def test_list_rules(self, m):
        data = {
            "total": 5.0,
            "rules": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.list_rules(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules',
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
    def test_create_bypass_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_bypass_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            resource_id='<RESOURCE_ID>',
            description='<DESCRIPTION>',
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/bypass',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'ruleId': '<RULE_ID>',
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_bypass_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_bypass_rule(
            '<RULE_ID>',
            resource_type='api',
            resource_id='<RESOURCE_ID>',
            name='<NAME>',
            description='<DESCRIPTION>',
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/bypass/<RULE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_challenge_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "challengeType": "compute",
            "difficulty": 3.0,
            "ttl": 1800.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_challenge_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            resource_id='<RESOURCE_ID>',
            description='<DESCRIPTION>',
            challenge_type='compute',
            priority=1,
            enabled=False,
            conditions=[],
            difficulty=1,
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/challenge',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'ruleId': '<RULE_ID>',
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'challengeType': 'compute',
                'priority': 1,
                'enabled': False,
                'conditions': [],
                'difficulty': 1,
                'ttl': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_challenge_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "challengeType": "compute",
            "difficulty": 3.0,
            "ttl": 1800.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_challenge_rule(
            '<RULE_ID>',
            resource_type='api',
            resource_id='<RESOURCE_ID>',
            name='<NAME>',
            description='<DESCRIPTION>',
            challenge_type='compute',
            priority=1,
            enabled=False,
            conditions=[],
            difficulty=1,
            ttl=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/challenge/<RULE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'challengeType': 'compute',
                'priority': 1,
                'enabled': False,
                'conditions': [],
                'difficulty': 1,
                'ttl': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_deny_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_deny_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            resource_id='<RESOURCE_ID>',
            description='<DESCRIPTION>',
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/deny',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'ruleId': '<RULE_ID>',
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_deny_rule(
            '<RULE_ID>',
            resource_type='api',
            resource_id='<RESOURCE_ID>',
            name='<NAME>',
            description='<DESCRIPTION>',
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/deny/<RULE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_rate_limit_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "limit": 1000.0,
            "interval": 60.0,
            "key": "userId",
            "strategy": "slidingWindow",
            "maxBucketSize": 200.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_rate_limit_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            1,
            1,
            resource_id='<RESOURCE_ID>',
            description='<DESCRIPTION>',
            key='ip',
            strategy='fixedWindow',
            max_bucket_size=1,
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/rate-limit',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'ruleId': '<RULE_ID>',
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'limit': 1,
                'interval': 1,
                'key': 'ip',
                'strategy': 'fixedWindow',
                'maxBucketSize': 1,
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_rate_limit_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "limit": 1000.0,
            "interval": 60.0,
            "key": "userId",
            "strategy": "slidingWindow",
            "maxBucketSize": 200.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_rate_limit_rule(
            '<RULE_ID>',
            resource_type='api',
            resource_id='<RESOURCE_ID>',
            name='<NAME>',
            description='<DESCRIPTION>',
            limit=1,
            interval=1,
            key='ip',
            max_bucket_size=1,
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/rate-limit/<RULE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'limit': 1,
                'interval': 1,
                'key': 'ip',
                'maxBucketSize': 1,
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_redirect_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "location": "\/maintenance",
            "statusCode": 301.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.create_redirect_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            '<LOCATION>',
            1,
            resource_id='<RESOURCE_ID>',
            description='<DESCRIPTION>',
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/redirect',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'ruleId': '<RULE_ID>',
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'location': '<LOCATION>',
                'statusCode': 1,
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_redirect_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
            "location": "\/maintenance",
            "statusCode": 301.0,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.update_redirect_rule(
            '<RULE_ID>',
            resource_type='api',
            resource_id='<RESOURCE_ID>',
            name='<NAME>',
            description='<DESCRIPTION>',
            location='<LOCATION>',
            status_code=1,
            priority=1,
            enabled=False,
            conditions=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/redirect/<RULE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'resourceType': 'api',
                'resourceId': '<RESOURCE_ID>',
                'name': '<NAME>',
                'description': '<DESCRIPTION>',
                'location': '<LOCATION>',
                'statusCode': 1,
                'priority': 1,
                'enabled': False,
                'conditions': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_rule(self, m):
        data = {
            "$id": "wafRule1",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "Block anonymous POST traffic",
            "description": "Blocks anonymous POST calls to \/v1\/graphql",
            "teamId": "5e5ea5c16897e",
            "projectId": "cloudConsole",
            "resourceType": "functions",
            "resourceId": "functionId",
            "action": "deny",
            "priority": 100.0,
            "enabled": True,
            "conditions": [],
            "config": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.get_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/<RULE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_rule(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.waf.delete_rule(
            '<RULE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/waf/rules/<RULE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
