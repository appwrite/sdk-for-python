import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            "teams": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams',
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
    def test_create(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "VIP",
            "total": 7.0,
            "prefs": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.create(
            '<TEAM_ID>',
            '<NAME>',
            roles=[],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'teamId': '<TEAM_ID>',
                'name': '<NAME>',
                'roles': [],
            },
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
            "prefs": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.get(
            '<TEAM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_name(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "VIP",
            "total": 7.0,
            "prefs": {},
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.update_name(
            '<TEAM_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
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
        response = self.teams.delete(
            '<TEAM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_installations(self, m):
        data = {
            "total": 5.0,
            "installations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.list_installations(
            '<TEAM_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/installations',
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
    def test_create_installation(self, m):
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
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.create_installation(
            '<TEAM_ID>',
            '<APP_ID>',
            authorization_details='<AUTHORIZATION_DETAILS>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/installations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'appId': '<APP_ID>',
                'authorizationDetails': '<AUTHORIZATION_DETAILS>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_installation(self, m):
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
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.get_installation(
            '<TEAM_ID>',
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/installations/<INSTALLATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_installation(self, m):
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
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.update_installation(
            '<TEAM_ID>',
            '<INSTALLATION_ID>',
            authorization_details='<AUTHORIZATION_DETAILS>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/installations/<INSTALLATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'authorizationDetails': '<AUTHORIZATION_DETAILS>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_installation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.delete_installation(
            '<TEAM_ID>',
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/installations/<INSTALLATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_memberships(self, m):
        data = {
            "total": 5.0,
            "memberships": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.list_memberships(
            '<TEAM_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/memberships',
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
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.create_membership(
            '<TEAM_ID>',
            [],
            email='email@example.com',
            user_id='<USER_ID>',
            phone='+12065550100',
            url='https://example.com',
            name='<NAME>',
            membership_id='<MEMBERSHIP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/memberships',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
                'userId': '<USER_ID>',
                'phone': '+12065550100',
                'roles': [],
                'url': 'https://example.com',
                'name': '<NAME>',
                'membershipId': '<MEMBERSHIP_ID>',
            },
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
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.get_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/memberships/<MEMBERSHIP_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
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
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.update_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/memberships/<MEMBERSHIP_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'roles': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_membership(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.delete_membership(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/memberships/<MEMBERSHIP_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
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
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.update_membership_status(
            '<TEAM_ID>',
            '<MEMBERSHIP_ID>',
            '<USER_ID>',
            '<SECRET>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/memberships/<MEMBERSHIP_ID>/status',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'userId': '<USER_ID>',
                'secret': '<SECRET>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.get_prefs(
            '<TEAM_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/prefs',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_prefs(self, m):
        data = {}
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.teams.update_prefs(
            '<TEAM_ID>',
            {},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/teams/<TEAM_ID>/prefs',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'prefs': {},
            },
        )
        self.assertEqual(response.to_dict(), data)
