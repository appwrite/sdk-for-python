import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.graphql import Graphql


class GraphqlServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.graphql = Graphql(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_query(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.graphql.query(
            {},
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_mutation(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.graphql.mutation(
            {},
        )
        self.assertEqual(response, data)
