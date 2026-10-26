import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.activities import Activities


class ActivitiesServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.activities = Activities(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list_events(self):
        data = {
            "total": 5.0,
            "events": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.activities.list_events()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_event(self):
        data = {
            "$id": "5e5ea5c16897e",
            "actorType": "user",
            "actorId": "610fc2f985ee0",
            "actorEmail": "john@appwrite.io",
            "actorName": "John Doe",
            "resourceParent": "database\/ID",
            "resourceType": "collection",
            "resourceId": "610fc2f985ee0",
            "resource": "collections\/610fc2f985ee0",
            "event": "account.sessions.create",
            "userAgent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/86.0.4240.198 Safari\/537.36",
            "ip": "127.0.0.1",
            "mode": "admin",
            "country": "US",
            "continentCode": "NA",
            "city": "Mountain View",
            "subdivisions": "California",
            "isp": "Google",
            "autonomousSystemNumber": "15169",
            "autonomousSystemOrganization": "GOOGLE",
            "connectionType": "cable",
            "connectionUsageType": "residential",
            "connectionOrganization": "Google LLC",
            "time": "2020-10-15T06:38:00.000+00:00",
            "projectId": "610fc2f985ee0",
            "teamId": "610fc2f985ee0",
            "hostname": "appwrite.io",
            "sdk": "web",
            "sdkVersion": "14.0.0",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.activities.get_event(
            '<EVENT_ID>',
        )
        self.assertEqual(response.to_dict(), data)
