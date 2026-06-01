import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.activities import Activities

class ActivitiesServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.activities = Activities(self.client)

    @requests_mock.Mocker()
    def test_list_events(self, m):
        data = {
    "total": 5.0,
    "events": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.activities.list_events(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_event(self, m):
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
    "time": "2020-10-15T06:38:00.000+00:00",
    "projectId": "610fc2f985ee0",
    "teamId": "610fc2f985ee0",
    "hostname": "appwrite.io",
    "osCode": "Mac",
    "osName": "Mac",
    "osVersion": "Mac",
    "clientType": "browser",
    "clientCode": "CM",
    "clientName": "Chrome Mobile iOS",
    "clientVersion": "84.0",
    "clientEngine": "WebKit",
    "clientEngineVersion": "605.1.15",
    "deviceName": "smartphone",
    "deviceBrand": "Google",
    "deviceModel": "Nexus 5",
    "countryCode": "US",
    "countryName": "United States"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.activities.get_event(
            '<EVENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

