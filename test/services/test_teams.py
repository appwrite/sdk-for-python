import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.teams import Teams


class TeamsServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.teams = Teams(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list(self):
        data = {
            "total": 5.0,
            "teams": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.list()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "VIP",
            "total": 7.0,
            "prefs": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.create(
            '<TEAM_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "VIP",
            "total": 7.0,
            "prefs": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.get(
            '<TEAM_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_name(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "VIP",
            "total": 7.0,
            "prefs": {},
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.update_name(
            '<TEAM_ID>',
            '<NAME>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.delete(
            '<TEAM_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_installations(self):
        data = {
            "total": 5.0,
            "installations": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.list_installations(
            '<TEAM_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_installation(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "scopes": [],
            "authorizationDetails": [],
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.create_installation(
            '<TEAM_ID>',
            '<APP_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_installation(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "scopes": [],
            "authorizationDetails": [],
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.get_installation(
            '<TEAM_ID>',
            '<INSTALLATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_installation(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "scopes": [],
            "authorizationDetails": [],
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.update_installation(
            '<TEAM_ID>',
            '<INSTALLATION_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_installation(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.delete_installation(
            '<TEAM_ID>',
            '<INSTALLATION_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_memberships(self):
        data = {
            "total": 5.0,
            "memberships": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.list_memberships(
            '<TEAM_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_create_membership(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "userName": "John Doe",
            "userEmail": "john@appwrite.io",
            "userPhone": "+1 555 555 5555",
            "teamId": "5e5ea5c16897e",
            "teamName": "VIP",
            "invited": "2020-10-15T06:38:00.000+00:00",
            "joined": "2020-10-15T06:38:00.000+00:00",
            "confirm": True,
            "mfa": True,
            "userAccessedAt": "2020-10-15T06:38:00.000+00:00",
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.create_membership(
            '<TEAM_ID>',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_membership(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "userName": "John Doe",
            "userEmail": "john@appwrite.io",
            "userPhone": "+1 555 555 5555",
            "teamId": "5e5ea5c16897e",
            "teamName": "VIP",
            "invited": "2020-10-15T06:38:00.000+00:00",
            "joined": "2020-10-15T06:38:00.000+00:00",
            "confirm": True,
            "mfa": True,
            "userAccessedAt": "2020-10-15T06:38:00.000+00:00",
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.get_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_membership(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "userName": "John Doe",
            "userEmail": "john@appwrite.io",
            "userPhone": "+1 555 555 5555",
            "teamId": "5e5ea5c16897e",
            "teamName": "VIP",
            "invited": "2020-10-15T06:38:00.000+00:00",
            "joined": "2020-10-15T06:38:00.000+00:00",
            "confirm": True,
            "mfa": True,
            "userAccessedAt": "2020-10-15T06:38:00.000+00:00",
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.update_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
            [],
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_membership(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.delete_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_update_membership_status(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "userName": "John Doe",
            "userEmail": "john@appwrite.io",
            "userPhone": "+1 555 555 5555",
            "teamId": "5e5ea5c16897e",
            "teamName": "VIP",
            "invited": "2020-10-15T06:38:00.000+00:00",
            "joined": "2020-10-15T06:38:00.000+00:00",
            "confirm": True,
            "mfa": True,
            "userAccessedAt": "2020-10-15T06:38:00.000+00:00",
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.update_membership_status(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
            '<USER_ID>',
            '<SECRET>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_prefs(self):
        data = {}
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.get_prefs(
            '<TEAM_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_update_prefs(self):
        data = {}
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.teams.update_prefs(
            '<TEAM_ID>',
            {},
        )
        self.assertEqual(response.to_dict(), data)
