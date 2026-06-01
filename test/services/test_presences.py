import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.presences import Presences

class PresencesServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.presences = Presences(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
    "total": 5.0,
    "presences": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.presences.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "userId": "674af8f3e12a5f9ac0be",
    "source": "HTTP"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.presences.get(
            '<PRESENCE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_upsert(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "userId": "674af8f3e12a5f9ac0be",
    "source": "HTTP"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.presences.upsert(
            '<PRESENCE_ID>',
            '<USER_ID>',
            '<STATUS>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "userId": "674af8f3e12a5f9ac0be",
    "source": "HTTP"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.presences.update(
            '<PRESENCE_ID>',
            '<USER_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.presences.delete(
            '<PRESENCE_ID>',
        )

        self.assertEqual(response, data)

