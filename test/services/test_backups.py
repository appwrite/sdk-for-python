import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.backups import Backups


class BackupsServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.backups = Backups(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list_archives(self):
        data = {
            "total": 5.0,
            "archives": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.list_archives()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_archive(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.create_archive(
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_archive(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.get_archive(
            '<ARCHIVE_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_archive(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.delete_archive(
            '<ARCHIVE_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_policies(self):
        data = {
            "total": 5.0,
            "policies": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.list_policies()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_policy(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.create_policy(
            '<POLICY_ID>',
            [],
            1,
            'schedule',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_policy(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.get_policy(
            '<POLICY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_policy(self):
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
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.update_policy(
            '<POLICY_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_policy(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.delete_policy(
            '<POLICY_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_create_restoration(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "archiveId": "did8jx6ws45jana098ab7",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.create_restoration(
            '<ARCHIVE_ID>',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_list_restorations(self):
        data = {
            "total": 5.0,
            "restorations": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.list_restorations()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_restoration(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "archiveId": "did8jx6ws45jana098ab7",
            "policyId": "did8jx6ws45jana098ab7",
            "status": "completed",
            "migrationId": "did8jx6ws45jana098ab7",
            "services": [],
            "resources": [],
            "options": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.backups.get_restoration(
            '<RESTORATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)
