import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.avatars import Avatars


class AvatarsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.avatars = Avatars(self.client)

    @requests_mock.Mocker()
    def test_get_browser(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_browser(
            'aa',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_credit_card(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_credit_card(
            'amex',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_favicon(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_favicon(
            'https://example.com',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_flag(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_flag(
            'af',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_image(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_image(
            'https://example.com',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_initials(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_initials()
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_photo(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_photo()
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_photo(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "John Doe",
            "registration": "2020-10-15T06:38:00.000+00:00",
            "status": True,
            "labels": [],
            "passwordUpdate": "2020-10-15T06:38:00.000+00:00",
            "email": "john@appwrite.io",
            "phone": "+4930901820",
            "emailVerification": True,
            "phoneVerification": True,
            "mfa": True,
            "prefs": {},
            "targets": [],
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.avatars.update_photo(
            InputFile.from_bytes(bytearray(), "example.file"),
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_photo(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.avatars.delete_photo()
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_qr(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_qr(
            '<TEXT>',
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_screenshot(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_screenshot(
            'https://example.com',
        )
        self.assertEqual(response, data)
