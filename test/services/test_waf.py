import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.waf import Waf


class WafServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.waf = Waf(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list_rules(self):
        data = {
            "total": 5.0,
            "rules": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.list_rules()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_bypass_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.create_bypass_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_bypass_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.update_bypass_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_challenge_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.create_challenge_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_challenge_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.update_challenge_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_deny_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.create_deny_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_deny_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.update_deny_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_rate_limit_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.create_rate_limit_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            1,
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_rate_limit_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.update_rate_limit_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_redirect_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.create_redirect_rule(
            '<RULE_ID>',
            'api',
            '<NAME>',
            '<LOCATION>',
            1,
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_redirect_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.update_redirect_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_rule(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.get_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_rule(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.waf.delete_rule(
            '<RULE_ID>',
        )
        self.assertEqual(response, data)
