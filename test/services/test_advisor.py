import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.advisor import Advisor

class AdvisorServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.advisor = Advisor(self.client)

    @requests_mock.Mocker()
    def test_list_reports(self, m):
        data = {
    "total": 5.0,
    "reports": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.advisor.list_reports(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_report(self, m):
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
    "insights": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.advisor.get_report(
            '<REPORT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_report(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.advisor.delete_report(
            '<REPORT_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_insights(self, m):
        data = {
    "total": 5.0,
    "insights": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.advisor.list_insights(
            '<REPORT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_insight(self, m):
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
    "ctas": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.advisor.get_insight(
            '<REPORT_ID>',
            '<INSIGHT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

