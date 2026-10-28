import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.graphql import Graphql


class GraphqlServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.graphql = Graphql(self.client)

    @requests_mock.Mocker()
    def test_query(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.graphql.query(
            {},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/graphql',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'query': {},
            },
        )
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_mutation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.graphql.mutation(
            {},
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/graphql/mutation',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'query': {},
            },
        )
        self.assertEqual(response, data)
