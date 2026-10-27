import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_browser(
            'aa',
            width=1,
            height=1,
            quality=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/browsers/aa',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'width': ['1'],
                'height': ['1'],
                'quality': ['1'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_credit_card(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_credit_card(
            'amex',
            width=1,
            height=1,
            quality=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/credit-cards/amex',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'width': ['1'],
                'height': ['1'],
                'quality': ['1'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_favicon(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_favicon(
            'https://example.com',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/favicon',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'url': ['https://example.com'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_flag(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_flag(
            'af',
            width=1,
            height=1,
            quality=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/flags/af',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'width': ['1'],
                'height': ['1'],
                'quality': ['1'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_image(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_image(
            'https://example.com',
            width=1,
            height=1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/image',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'url': ['https://example.com'],
                'width': ['1'],
                'height': ['1'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_initials(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_initials(
            name='<NAME>',
            width=1,
            height=1,
            background='FFFFFF',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/initials',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'name': ['<NAME>'],
                'width': ['1'],
                'height': ['1'],
                'background': ['FFFFFF'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_photo(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_photo(
            width=1,
            height=1,
            quality=1,
            output='png',
            rating='g',
            user_id='current()',
            email_hash='<EMAIL_HASH>',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/photo',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'width': ['1'],
                'height': ['1'],
                'quality': ['1'],
                'output': ['png'],
                'rating': ['g'],
                'userId': ['current()'],
                'emailHash': ['<EMAIL_HASH>'],
                'name': ['<NAME>'],
            },
        )
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
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.avatars.update_photo(
            InputFile.from_bytes(bytearray(), "example.file"),
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/photo',
        )
        sent = dict(
            re.findall(
                r'form-data; name="([^"\[]+)[^\r\n]*\r\n(?:[^\r\n]+\r\n)*\r\n(.*?)\r\n--',
                request.body.decode('latin-1'),
                re.S,
            )
        )
        self.assertEqual(
            sent,
            {
                'file': '',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_photo(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.avatars.delete_photo()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/photo',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_qr(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_qr(
            '<TEXT>',
            size=1,
            margin=1,
            download=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/qr',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'text': ['<TEXT>'],
                'size': ['1'],
                'margin': ['1'],
                'download': ['false'],
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_screenshot(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.avatars.get_screenshot(
            'https://example.com',
            headers={},
            viewport_width=1,
            viewport_height=1,
            scale=1.0,
            theme='dark',
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
            fullpage=False,
            locale='en-US',
            timezone='America/New_York',
            latitude=1.0,
            longitude=1.0,
            accuracy=1.0,
            touch=False,
            permissions=[],
            sleep=1,
            width=1,
            height=1,
            quality=1,
            output='jpeg',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/avatars/screenshots',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'url': ['https://example.com'],
                'viewportWidth': ['1'],
                'viewportHeight': ['1'],
                'scale': ['1.0'],
                'theme': ['dark'],
                'userAgent': ['Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15'],
                'fullpage': ['false'],
                'locale': ['en-US'],
                'timezone': ['America/New_York'],
                'latitude': ['1.0'],
                'longitude': ['1.0'],
                'accuracy': ['1.0'],
                'touch': ['false'],
                'sleep': ['1'],
                'width': ['1'],
                'height': ['1'],
                'quality': ['1'],
                'output': ['jpeg'],
            },
        )
        self.assertEqual(response, data)
