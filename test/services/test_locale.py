import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.locale import Locale

class LocaleServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.locale = Locale(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "ip": "127.0.0.1",
    "countryCode": "US",
    "country": "United States",
    "continentCode": "NA",
    "continent": "North America",
    "eu": True,
    "currency": "USD"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.get(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_codes(self, m):
        data = {
    "total": 5.0,
    "localeCodes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.list_codes(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_continents(self, m):
        data = {
    "total": 5.0,
    "continents": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.list_continents(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_countries(self, m):
        data = {
    "total": 5.0,
    "countries": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.list_countries(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_countries_eu(self, m):
        data = {
    "total": 5.0,
    "countries": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.list_countries_eu(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_countries_phones(self, m):
        data = {
    "total": 5.0,
    "phones": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.list_countries_phones(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_currencies(self, m):
        data = {
    "total": 5.0,
    "currencies": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.list_currencies(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_languages(self, m):
        data = {
    "total": 5.0,
    "languages": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.locale.list_languages(
        )

        self.assertEqual(response.to_dict(), data)

