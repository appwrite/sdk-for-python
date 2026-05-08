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
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_browser(
            'aa',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_credit_card(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_credit_card(
            'amex',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_favicon(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_favicon(
            'https://example.com',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_flag(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_flag(
            'af',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_image(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_image(
            'https://example.com',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_initials(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_initials(
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_qr(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_qr(
            '<TEXT>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_screenshot(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.avatars.get_screenshot(
            'https://example.com',
        )

        self.assertEqual(response, data)

