import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.teams import Teams

class TeamsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.teams = Teams(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
    "total": 5.0,
    "teams": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "VIP",
    "total": 7.0,
    "prefs": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.create(
            '<TEAM_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "VIP",
    "total": 7.0,
    "prefs": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.get(
            '<TEAM_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_name(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "VIP",
    "total": 7.0,
    "prefs": {}
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.update_name(
            '<TEAM_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.delete(
            '<TEAM_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_memberships(self, m):
        data = {
    "total": 5.0,
    "memberships": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.list_memberships(
            '<TEAM_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_membership(self, m):
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
    "roles": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.create_membership(
            '<TEAM_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_membership(self, m):
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
    "roles": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.get_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_membership(self, m):
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
    "roles": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.update_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_membership(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.delete_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_membership_status(self, m):
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
    "roles": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.update_membership_status(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
            '<USER_ID>',
            '<SECRET>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.get_prefs(
            '<TEAM_ID>',
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.teams.update_prefs(
            '<TEAM_ID>',
            {},
        )

        data['data'] = {}
        self.assertEqual(response.to_dict(), data)

