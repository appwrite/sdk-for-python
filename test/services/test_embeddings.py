import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.embeddings.create_text_embeddings(
            [],
            model='nomic-embed-text',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/embeddings/text',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'texts': [],
                'model': 'nomic-embed-text',
            },
        )
        self.assertEqual(response.to_dict(), data)
