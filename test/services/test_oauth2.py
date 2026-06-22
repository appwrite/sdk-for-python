import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.oauth2 import Oauth2

class Oauth2ServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.oauth2 = Oauth2(self.client)

    @requests_mock.Mocker()
    def test_approve(self, m):
        data = {
    "redirectUrl": "https:\/\/example.com\/callback?code=abcde&state=fghij"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.approve(
            '<GRANT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_authorize(self, m):
        data = {
    "grantId": "5e5ea5c16897e",
    "redirectUrl": "https:\/\/example.com\/callback?code=abcde&state=fghij"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.authorize(
            '<CLIENT_ID>',
            'https://example.com',
            'code',
            '<SCOPE>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_device_authorization(self, m):
        data = {
    "device_code": "5f3c8d2a1b9e4f7a6c8b2d1e9f4a7b3c5d8e1f2a9b4c7d6e3f5a8b1c4d7e2f9a",
    "user_code": "ABCD-EFGH",
    "verification_uri": "https:\/\/cloud.appwrite.io\/console\/oauth2\/device",
    "verification_uri_complete": "https:\/\/cloud.appwrite.io\/console\/oauth2\/device?user_code=ABCD-EFGH",
    "expires_in": 900.0,
    "interval": 5.0
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.create_device_authorization(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_grant(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c16897e",
    "appId": "5e5ea5c16897e",
    "scopes": [],
    "authorizationDetails": "[{\"type\":\"calendar\",\"identifier\":\"primary\",\"actions\":[\"read_events\",\"create_event\"]}]",
    "prompt": "login",
    "redirectUri": "https:\/\/example.com\/callback",
    "authTime": 1592981250.0,
    "expire": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.create_grant(
            '<USER_CODE>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_grant(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "userId": "5e5ea5c16897e",
    "appId": "5e5ea5c16897e",
    "scopes": [],
    "authorizationDetails": "[{\"type\":\"calendar\",\"identifier\":\"primary\",\"actions\":[\"read_events\",\"create_event\"]}]",
    "prompt": "login",
    "redirectUri": "https:\/\/example.com\/callback",
    "authTime": 1592981250.0,
    "expire": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.get_grant(
            '<GRANT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_reject(self, m):
        data = {
    "redirectUrl": "https:\/\/example.com\/callback?error=access_denied&state=fghij"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.reject(
            '<GRANT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_revoke(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.revoke(
            '<TOKEN>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_create_token(self, m):
        data = {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...",
    "token_type": "Bearer",
    "expires_in": 3600.0,
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "scope": "openid email profile"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.oauth2.create_token(
            '<GRANT_TYPE>',
        )

        self.assertEqual(response.to_dict(), data)

