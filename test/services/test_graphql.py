import json
import requests_mock
import unittest

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
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.graphql.query(
            {},
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_mutation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.graphql.mutation(
            {},
        )

        self.assertEqual(response, data)

