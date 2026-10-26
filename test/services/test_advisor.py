import json
import httpx2
import respx
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.advisor import Advisor


class AdvisorServiceTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = Client()
        self.advisor = Advisor(self.client)

    async def asyncTearDown(self):
        await self.client.aclose()

    @respx.mock
    async def test_list_reports(self):
        data = {
            "total": 5.0,
            "reports": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.advisor.list_reports()
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_report(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "type": "lighthouse",
            "title": "Lighthouse audit for https:\/\/appwrite.io\/",
            "summary": "Performance score 78. 4 opportunities found.",
            "targetType": "urls",
            "target": "https:\/\/appwrite.io\/",
            "categories": [],
            "insights": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.advisor.get_report(
            '<REPORT_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_delete_report(self):
        data = ''
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.advisor.delete_report(
            '<REPORT_ID>',
        )
        self.assertEqual(response, data)

    @respx.mock
    async def test_list_insights(self):
        data = {
            "total": 5.0,
            "insights": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.advisor.list_insights(
            '<REPORT_ID>',
        )
        self.assertEqual(response.to_dict(), data)

    @respx.mock
    async def test_get_insight(self):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "reportId": "5e5ea5c16897e",
            "type": "tablesDBIndex",
            "severity": "warning",
            "status": "active",
            "resourceType": "databases",
            "resourceId": "main",
            "parentResourceType": "tables",
            "parentResourceId": "orders",
            "title": "Missing index on collection orders",
            "summary": "Queries against `orders.status` are scanning the full collection.",
            "ctas": [],
        }
        headers = {'Content-Type': 'application/json'}
        respx.route().mock(
            return_value=httpx2.Response(200, text=json.dumps(data), headers=headers),
        )
        response = await self.advisor.get_insight(
            '<REPORT_ID>',
            '<INSIGHT_ID>',
        )
        self.assertEqual(response.to_dict(), data)
