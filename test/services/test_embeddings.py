import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.embeddings import Embeddings


class EmbeddingsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.embeddings = Embeddings(self.client)

    @requests_mock.Mocker()
    def test_create_text_embeddings(self, m):
        data = {
            "total": 5.0,
            "embeddings": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            requests_mock.ANY,
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.embeddings.create_text_embeddings(
            [],
        )
        self.assertEqual(response.to_dict(), data)
