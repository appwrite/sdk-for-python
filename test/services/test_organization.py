import json
import requests_mock
import unittest

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
    "billingBudget": 50.0,
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
        "members": 25.0,
        "webhooks": 25.0,
        "wafRules": 2.0,
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
        "activityLogs": 7.0,
        "usageLogs": 30.0,
        "projectInactivityDays": 7.0,
        "alertLimit": 80.0,
        "usage": {
            "bandwidth": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "executions": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "member": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtime": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtimeMessages": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtimeBandwidth": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "storage": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "users": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "GBHours": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "imageTransformations": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "credits": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            }
        },
        "addons": {
            "seats": {
                "supported": True,
                "planIncluded": 1.0,
                "limit": 5.0,
                "type": "numeric",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "projects": {
                "supported": True,
                "planIncluded": 1.0,
                "limit": 5.0,
                "type": "numeric",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            }
        },
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
        "supportsDisposableEmailValidation": True,
        "supportsCanonicalEmailValidation": True,
        "supportsFreeEmailValidation": True,
        "supportsCorporateEmailValidation": True,
        "supportsProjectSpecificRoles": True,
        "backupsEnabled": True,
        "usagePerProject": True,
        "supportedAddons": {
            "baa": True,
            "premiumGeoDB": True,
            "premiumGeoDBOrg": True
        },
        "backupPolicies": 1.0,
        "deploymentSize": 30.0,
        "buildSize": 2000.0,
        "databasesAllowEncrypt": True,
        "group": "pro"
    },
    "billingEmail": "billing@org.example",
    "billingStartDate": "2020-10-15T06:38:00.000+00:00",
    "billingCurrentInvoiceDate": "2020-10-15T06:38:00.000+00:00",
    "billingNextInvoiceDate": "2020-10-15T06:38:00.000+00:00",
    "billingTrialStartDate": "2020-10-15T06:38:00.000+00:00",
    "billingTrialDays": 14.0,
    "billingAggregationId": "adbc3de4rddfsd",
    "billingInvoiceId": "adbc3de4rddfsd",
    "paymentMethodId": "adbc3de4rddfsd",
    "billingAddressId": "adbc3de4rddfsd",
    "backupPaymentMethodId": "adbc3de4rddfsd",
    "status": "active",
    "remarks": "Pending initial payment",
    "agreementBAA": "",
    "programManagerName": "",
    "programManagerCalendar": "",
    "programDiscordChannelName": "",
    "programDiscordChannelUrl": "",
    "billingPlanDowngrade": "tier-1",
    "billingTaxId": "",
    "markedForDeletion": True,
    "platform": "imagine",
    "projects": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.get(
        )

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
    "billingBudget": 50.0,
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
        "members": 25.0,
        "webhooks": 25.0,
        "wafRules": 2.0,
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
        "activityLogs": 7.0,
        "usageLogs": 30.0,
        "projectInactivityDays": 7.0,
        "alertLimit": 80.0,
        "usage": {
            "bandwidth": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "executions": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "member": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtime": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtimeMessages": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "realtimeBandwidth": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "storage": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "users": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "GBHours": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "imageTransformations": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "credits": {
                "name": "",
                "unit": "GB",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            }
        },
        "addons": {
            "seats": {
                "supported": True,
                "planIncluded": 1.0,
                "limit": 5.0,
                "type": "numeric",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            },
            "projects": {
                "supported": True,
                "planIncluded": 1.0,
                "limit": 5.0,
                "type": "numeric",
                "currency": "USD",
                "price": 5,
                "value": 25.0,
                "invoiceDesc": ""
            }
        },
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
        "supportsDisposableEmailValidation": True,
        "supportsCanonicalEmailValidation": True,
        "supportsFreeEmailValidation": True,
        "supportsCorporateEmailValidation": True,
        "supportsProjectSpecificRoles": True,
        "backupsEnabled": True,
        "usagePerProject": True,
        "supportedAddons": {
            "baa": True,
            "premiumGeoDB": True,
            "premiumGeoDBOrg": True
        },
        "backupPolicies": 1.0,
        "deploymentSize": 30.0,
        "buildSize": 2000.0,
        "databasesAllowEncrypt": True,
        "group": "pro"
    },
    "billingEmail": "billing@org.example",
    "billingStartDate": "2020-10-15T06:38:00.000+00:00",
    "billingCurrentInvoiceDate": "2020-10-15T06:38:00.000+00:00",
    "billingNextInvoiceDate": "2020-10-15T06:38:00.000+00:00",
    "billingTrialStartDate": "2020-10-15T06:38:00.000+00:00",
    "billingTrialDays": 14.0,
    "billingAggregationId": "adbc3de4rddfsd",
    "billingInvoiceId": "adbc3de4rddfsd",
    "paymentMethodId": "adbc3de4rddfsd",
    "billingAddressId": "adbc3de4rddfsd",
    "backupPaymentMethodId": "adbc3de4rddfsd",
    "status": "active",
    "remarks": "Pending initial payment",
    "agreementBAA": "",
    "programManagerName": "",
    "programManagerCalendar": "",
    "programDiscordChannelName": "",
    "programDiscordChannelUrl": "",
    "billingPlanDowngrade": "tier-1",
    "billingTaxId": "",
    "markedForDeletion": True,
    "platform": "imagine",
    "projects": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.update(
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.delete(
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_keys(self, m):
        data = {
    "total": 5.0,
    "keys": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.list_keys(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.create_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.get_key(
            '<KEY_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_key(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My API Key",
    "expire": "2020-10-15T06:38:00.000+00:00",
    "scopes": [],
    "secret": "919c2d18fb5d4...a2ae413da83346ad2",
    "accessedAt": "2020-10-15T06:38:00.000+00:00",
    "sdks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.update_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_key(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.delete_key(
            '<KEY_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_memberships(self, m):
        data = {
    "total": 5.0,
    "memberships": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.list_memberships(
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
    "roles": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.create_membership(
            [],
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
    "roles": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.get_membership(
            '<MEMBERSHIP_ID>',
        )

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
    "roles": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.update_membership(
            '<MEMBERSHIP_ID>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_membership(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.delete_membership(
            '<MEMBERSHIP_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_projects(self, m):
        data = {
    "total": 5.0,
    "projects": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.list_projects(
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
    "devKeys": [],
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
    "wafEnabled": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.create_project(
            '',
            '<NAME>',
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
    "devKeys": [],
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
    "wafEnabled": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.get_project(
            '<PROJECT_ID>',
        )

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
    "devKeys": [],
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
    "wafEnabled": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.update_project(
            '<PROJECT_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_project(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.organization.delete_project(
            '<PROJECT_ID>',
        )

        self.assertEqual(response, data)

