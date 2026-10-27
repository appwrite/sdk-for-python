import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.organization import Organization


class OrganizationServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.organization = Organization(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "VIP",
            "total": 7.0,
            "prefs": {},
            "budgetAlerts": [],
            "billingPlan": "tier-1",
            "billingPlanId": "tier-1",
            "billingPlanDetails": {
                "$id": "tier-0",
                "name": "Hobby",
                "desc": "Hobby plan",
                "order": 0.0,
                "price": 25,
                "trial": 14.0,
                "bandwidth": 25.0,
                "storage": 25.0,
                "imageTransformations": 100.0,
                "screenshotsGenerated": 50.0,
                "webhooks": 25.0,
                "wafRules": 2.0,
                "environments": 5.0,
                "projects": 2.0,
                "platforms": 3.0,
                "users": 25.0,
                "teams": 25.0,
                "databases": 25.0,
                "databasesReads": 500000.0,
                "databasesWrites": 250000.0,
                "databasesBatchSize": 100.0,
                "buckets": 25.0,
                "fileSize": 25.0,
                "functions": 25.0,
                "sites": 1.0,
                "executions": 25.0,
                "executionsRetentionCount": 10000.0,
                "GBHours": 100.0,
                "realtime": 25.0,
                "realtimeMessages": 100000.0,
                "messages": 1000.0,
                "topics": 1.0,
                "authPhone": 10.0,
                "domains": 5.0,
                "usageLogs": 30.0,
                "projectInactivityDays": 7.0,
                "alertLimit": 80.0,
                "addons": {},
                "budgetCapEnabled": True,
                "customSmtp": True,
                "emailBranding": True,
                "requiresPaymentMethod": True,
                "requiresBillingAddress": True,
                "isAvailable": True,
                "selfService": True,
                "premiumSupport": True,
                "budgeting": True,
                "supportsMockNumbers": True,
                "supportsOrganizationRoles": True,
                "supportsCredits": True,
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.get()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "VIP",
            "total": 7.0,
            "prefs": {},
            "budgetAlerts": [],
            "billingPlan": "tier-1",
            "billingPlanId": "tier-1",
            "billingPlanDetails": {
                "$id": "tier-0",
                "name": "Hobby",
                "desc": "Hobby plan",
                "order": 0.0,
                "price": 25,
                "trial": 14.0,
                "bandwidth": 25.0,
                "storage": 25.0,
                "imageTransformations": 100.0,
                "screenshotsGenerated": 50.0,
                "webhooks": 25.0,
                "wafRules": 2.0,
                "environments": 5.0,
                "projects": 2.0,
                "platforms": 3.0,
                "users": 25.0,
                "teams": 25.0,
                "databases": 25.0,
                "databasesReads": 500000.0,
                "databasesWrites": 250000.0,
                "databasesBatchSize": 100.0,
                "buckets": 25.0,
                "fileSize": 25.0,
                "functions": 25.0,
                "sites": 1.0,
                "executions": 25.0,
                "executionsRetentionCount": 10000.0,
                "GBHours": 100.0,
                "realtime": 25.0,
                "realtimeMessages": 100000.0,
                "messages": 1000.0,
                "topics": 1.0,
                "authPhone": 10.0,
                "domains": 5.0,
                "usageLogs": 30.0,
                "projectInactivityDays": 7.0,
                "alertLimit": 80.0,
                "addons": {},
                "budgetCapEnabled": True,
                "customSmtp": True,
                "emailBranding": True,
                "requiresPaymentMethod": True,
                "requiresBillingAddress": True,
                "isAvailable": True,
                "selfService": True,
                "premiumSupport": True,
                "budgeting": True,
                "supportsMockNumbers": True,
                "supportsOrganizationRoles": True,
                "supportsCredits": True,
                "supportsDedicatedDatabases": True,
                "supportsDisposableEmailValidation": True,
                "supportsCanonicalEmailValidation": True,
                "supportsFreeEmailValidation": True,
                "supportsCorporateEmailValidation": True,
                "supportsProjectSpecificRoles": True,
                "usagePerProject": True,
                "supportedAddons": {
                    "baa": True,
                    "premiumGeoDB": True,
                    "premiumGeoDBOrg": True,
                },
                "deploymentSize": 30.0,
                "buildSize": 2000.0,
                "functionsIntervalMinimum": 60.0,
                "functionsAllowCron": True,
                "databasesAllowEncrypt": True,
                "group": "pro",
                "databaseComputeCredit": 10,
            },
            "billingEmail": "billing@org.example",
            "status": "active",
            "markedForDeletion": True,
            "platform": "imagine",
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.update(
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.delete()
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_installations(self, m):
        data = {
            "total": 5.0,
            "installations": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.list_installations(
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/installations',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_installation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "scopes": [],
            "authorizationDetails": [],
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.create_installation(
            '<APP_ID>',
            authorization_details='<AUTHORIZATION_DETAILS>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/installations',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'appId': '<APP_ID>',
                'authorizationDetails': '<AUTHORIZATION_DETAILS>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_installation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "scopes": [],
            "authorizationDetails": [],
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.get_installation(
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/installations/<INSTALLATION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_installation(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "appId": "5e5ea5c16897e",
            "teamId": "5e5ea5c16897e",
            "scopes": [],
            "authorizationDetails": [],
            "createdById": "5e5ea5c16897e",
            "createdByName": "Walter White",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.update_installation(
            '<INSTALLATION_ID>',
            authorization_details='<AUTHORIZATION_DETAILS>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/installations/<INSTALLATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'authorizationDetails': '<AUTHORIZATION_DETAILS>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_installation(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.delete_installation(
            '<INSTALLATION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/installations/<INSTALLATION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_memberships(self, m):
        data = {
            "total": 5.0,
            "memberships": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.list_memberships(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/memberships',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_membership(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "userName": "John Doe",
            "userEmail": "john@appwrite.io",
            "userPhone": "+1 555 555 5555",
            "teamId": "5e5ea5c16897e",
            "teamName": "VIP",
            "invited": "2020-10-15T06:38:00.000+00:00",
            "joined": "2020-10-15T06:38:00.000+00:00",
            "confirm": True,
            "mfa": True,
            "userAccessedAt": "2020-10-15T06:38:00.000+00:00",
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.create_membership(
            [],
            email='email@example.com',
            user_id='<USER_ID>',
            phone='+12065550100',
            url='https://example.com',
            name='<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/memberships',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'email': 'email@example.com',
                'userId': '<USER_ID>',
                'phone': '+12065550100',
                'roles': [],
                'url': 'https://example.com',
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_membership(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "userName": "John Doe",
            "userEmail": "john@appwrite.io",
            "userPhone": "+1 555 555 5555",
            "teamId": "5e5ea5c16897e",
            "teamName": "VIP",
            "invited": "2020-10-15T06:38:00.000+00:00",
            "joined": "2020-10-15T06:38:00.000+00:00",
            "confirm": True,
            "mfa": True,
            "userAccessedAt": "2020-10-15T06:38:00.000+00:00",
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.get_membership(
            '<MEMBERSHIP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/memberships/<MEMBERSHIP_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_membership(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "userId": "5e5ea5c16897e",
            "userName": "John Doe",
            "userEmail": "john@appwrite.io",
            "userPhone": "+1 555 555 5555",
            "teamId": "5e5ea5c16897e",
            "teamName": "VIP",
            "invited": "2020-10-15T06:38:00.000+00:00",
            "joined": "2020-10-15T06:38:00.000+00:00",
            "confirm": True,
            "mfa": True,
            "userAccessedAt": "2020-10-15T06:38:00.000+00:00",
            "roles": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.update_membership(
            '<MEMBERSHIP_ID>',
            [],
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/memberships/<MEMBERSHIP_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'roles': [],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_membership(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.delete_membership(
            '<MEMBERSHIP_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/memberships/<MEMBERSHIP_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_projects(self, m):
        data = {
            "total": 5.0,
            "projects": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.list_projects(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'search': ['<SEARCH>'],
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_project(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.create_project(
            '<PROJECT_ID>',
            '<NAME>',
            region='fra',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'projectId': '<PROJECT_ID>',
                'name': '<NAME>',
                'region': 'fra',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_project(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.get_project(
            '<PROJECT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_project(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "New Project",
            "teamId": "1592981250",
            "region": "fra",
            "smtpEnabled": True,
            "smtpSenderName": "John Appwrite",
            "smtpSenderEmail": "john@appwrite.io",
            "smtpReplyToName": "Support Team",
            "smtpReplyToEmail": "support@appwrite.io",
            "smtpHost": "mail.appwrite.io",
            "smtpPort": 25.0,
            "smtpUsername": "emailuser",
            "smtpPassword": "smtp-password",
            "smtpSecure": "tls",
            "pingCount": 1.0,
            "pingedAt": "2020-10-15T06:38:00.000+00:00",
            "labels": [],
            "status": "active",
            "onboarding": {},
            "authMethods": [],
            "services": [],
            "protocols": [],
            "blocks": [],
            "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.update_project(
            '<PROJECT_ID>',
            '<NAME>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_project(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.delete_project(
            '<PROJECT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_project_keys(self, m):
        data = {
            "total": 5.0,
            "keys": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.list_project_keys(
            '<PROJECT_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>/keys',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'total': ['false'],
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_ephemeral_project_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.create_ephemeral_project_key(
            '<PROJECT_ID>',
            [],
            1,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>/keys/ephemeral',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'scopes': [],
                'duration': 1,
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_project_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.get_project_key(
            '<PROJECT_ID>',
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>/keys/<KEY_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_project_key(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My API Key",
            "description": "Used by the nightly backup job.",
            "expire": "2020-10-15T06:38:00.000+00:00",
            "scopes": [],
            "secret": "919c2d18fb5d4...a2ae413da83346ad2",
            "accessedAt": "2020-10-15T06:38:00.000+00:00",
            "sdks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.update_project_key(
            '<PROJECT_ID>',
            '<KEY_ID>',
            '<NAME>',
            [],
            expire='2020-10-15T06:38:00.000+00:00',
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>/keys/<KEY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'scopes': [],
                'expire': '2020-10-15T06:38:00.000+00:00',
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_project_key(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.organization.delete_project_key(
            '<PROJECT_ID>',
            '<KEY_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/organization/projects/<PROJECT_ID>/keys/<KEY_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
