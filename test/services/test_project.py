import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.project import Project

class ProjectServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.project = Project(self.client)

    @requests_mock.Mocker()
    def test_get(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.get(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.delete(
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_auth_method(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_auth_method(
            'email-password',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_keys(self, m):
        data = {
    "total": 5.0,
    "keys": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.list_keys(
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

        response = self.project.create_key(
            '<KEY_ID>',
            '<NAME>',
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_ephemeral_key(self, m):
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

        response = self.project.create_ephemeral_key(
            [],
            1,
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

        response = self.project.get_key(
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

        response = self.project.update_key(
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

        response = self.project.delete_key(
            '<KEY_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_labels(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_labels(
            [],
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_mock_phones(self, m):
        data = {
    "total": 5.0,
    "mockNumbers": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.list_mock_phones(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_mock_phone(self, m):
        data = {
    "number": "+1612842323",
    "otp": "123456",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_mock_phone(
            '+12065550100',
            '<OTP>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_mock_phone(self, m):
        data = {
    "number": "+1612842323",
    "otp": "123456",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.get_mock_phone(
            '+12065550100',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_mock_phone(self, m):
        data = {
    "number": "+1612842323",
    "otp": "123456",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_mock_phone(
            '+12065550100',
            '<OTP>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_mock_phone(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.delete_mock_phone(
            '+12065550100',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_o_auth2_providers(self, m):
        data = {
    "total": 5.0,
    "providers": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.list_o_auth2_providers(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_server(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_server(
            True,
            'https://example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_amazon(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "amzn1.application-oa2-client.87400c00000000000000000000063d5b2",
    "clientSecret": "79ffe4000000000000000000000000000000000000000000000000000002de55"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_amazon(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_apple(self, m):
        data = {
    "$id": "apple",
    "enabled": True,
    "serviceId": "ip.appwrite.app.web",
    "keyId": "P4000000N8",
    "teamId": "D4000000R6",
    "p8File": "-----BEGIN PRIVATE KEY-----MIGTAg...jy2Xbna-----END PRIVATE KEY-----"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_apple(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_auth0(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "OaOkIA000000000000000000005KLSYq",
    "clientSecret": "zXz0000-00000000000000000000000000000-00000000000000000000PJafnF",
    "endpoint": "example.us.auth0.com"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_auth0(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_authentik(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "dTKOPa0000000000000000000000000000e7G8hv",
    "clientSecret": "ntQadq000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Hp5WK",
    "endpoint": "example.authentik.com"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_authentik(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_autodesk(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "5zw90v00000000000000000000kVYXN7",
    "clientSecret": "7I000000000000MW"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_autodesk(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_bitbucket(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "key": "Knt70000000000ByRc",
    "secret": "NMfLZJ00000000000000000000TLQdDx"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_bitbucket(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_bitly(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "d95151000000000000000000000000000067af9b",
    "clientSecret": "a13e250000000000000000000000000000d73095"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_bitly(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_box(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "deglcs00000000000000000000x2og6y",
    "clientSecret": "OKM1f100000000000000000000eshEif"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_box(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_dailymotion(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "apiKey": "07a9000000000000067f",
    "apiSecret": "a399a90000000000000000000000000000d90639"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_dailymotion(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_discord(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "950722000000343754",
    "clientSecret": "YmPXnM000000000000000000002zFg5D"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_discord(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_disqus(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "publicKey": "cgegH70000000000000000000000000000000000000000000000000000Hr1nYX",
    "secretKey": "W7Bykj00000000000000000000000000000000000000000000000000003o43w9"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_disqus(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_dropbox(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "appKey": "jl000000000009t",
    "appSecret": "g200000000000vw"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_dropbox(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_etsy(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "keyString": "nsgzxh0000000000008j85a2",
    "sharedSecret": "tp000000ru"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_etsy(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_facebook(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "appId": "260600000007694",
    "appSecret": "2d0b2800000000000000000000d38af4"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_facebook(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_figma(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "byay5H0000000000VtiI40",
    "clientSecret": "yEpOYn0000000000000000004iIsU5"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_figma(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_fusion_auth(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "b2222c00-0000-0000-0000-000000862097",
    "clientSecret": "Jx4s0C0000000000000000000000000000000wGqLsc",
    "endpoint": "example.fusionauth.io"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_fusion_auth(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_git_hub(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "e4d87900000000540733",
    "clientSecret": "5e07c00000000000000000000000000000198bcc"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_git_hub(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_gitlab(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "applicationId": "d41ffe0000000000000000000000000000000000000000000000000000d5e252",
    "secret": "gloas-838cfa0000000000000000000000000000000000000000000000000000ecbb38",
    "endpoint": "https:\/\/gitlab.com"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_gitlab(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_google(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "120000000095-92ifjb00000000000000000000g7ijfb.apps.googleusercontent.com",
    "clientSecret": "GOCSPX-2k8gsR0000000000000000VNahJj",
    "prompt": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_google(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_keycloak(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "appwrite-o0000000st-app",
    "clientSecret": "jdjrJd00000000000000000000HUsaZO",
    "endpoint": "keycloak.example.com",
    "realmName": "appwrite-realm"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_keycloak(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_kick(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "01KQ7C00000000000001MFHS32",
    "clientSecret": "34ac5600000000000000000000000000000000000000000000000000e830c8b"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_kick(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_linkedin(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "770000000000dv",
    "primaryClientSecret": "WPL_AP1.2Bf0000000000000.\/HtlYw=="
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_linkedin(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_microsoft(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "applicationId": "00001111-aaaa-2222-bbbb-3333cccc4444",
    "applicationSecret": "A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",
    "tenant": "common"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_microsoft(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_notion(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "oauthClientId": "341d8700-0000-0000-0000-000000446ee3",
    "oauthClientSecret": "secret_dLUr4b000000000000000000000000000000lFHAa9"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_notion(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_oidc(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "qibI2x0000000000000000000000000006L2YFoG",
    "clientSecret": "Ah68ed000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003qpcHV",
    "wellKnownURL": "https:\/\/myoauth.com\/.well-known\/openid-configuration",
    "authorizationURL": "https:\/\/myoauth.com\/oauth2\/authorize",
    "tokenURL": "https:\/\/myoauth.com\/oauth2\/token",
    "userInfoURL": "https:\/\/myoauth.com\/oauth2\/userinfo"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_oidc(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_okta(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "0oa00000000000000698",
    "clientSecret": "Kiq0000000000000000000000000000000000000-00000000000H2L5-3SJ-vRV",
    "domain": "trial-6400025.okta.com",
    "authorizationServerId": "aus000000000000000h7z"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_okta(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_paypal(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB",
    "secretKey": "EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_paypal(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_paypal_sandbox(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB",
    "secretKey": "EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_paypal_sandbox(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_podio(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "appwrite-oauth-test-app",
    "clientSecret": "Rn247T0000000000000000000000000000000000000000000000000000W2zWTN"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_podio(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_salesforce(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "customerKey": "3MVG9I0000000000000000000000000000000000000000000000000000000000000000000000000C5Aejq",
    "customerSecret": "3w000000000000e2"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_salesforce(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_slack(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "23000000089.15000000000023",
    "clientSecret": "81656000000000000000000000f3d2fd"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_slack(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_spotify(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "6ec271000000000000000000009beace",
    "clientSecret": "db068a000000000000000000008b5b9f"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_spotify(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_stripe(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "ca_UKibXX0000000000000000000006byvR",
    "apiSecretKey": "sk_51SfOd000000000000000000000000000000000000000000000000000000000000000000000000000000000000000QGWYfp"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_stripe(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tradeshift(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "oauth2ClientId": "appwrite-test-org.appwrite-test-app",
    "oauth2ClientSecret": "7cb52700-0000-0000-0000-000000ca5b83"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_tradeshift(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_tradeshift_sandbox(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "oauth2ClientId": "appwrite-test-org.appwrite-test-app",
    "oauth2ClientSecret": "7cb52700-0000-0000-0000-000000ca5b83"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_tradeshift_sandbox(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_twitch(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "vvi0in000000000000000000ikmt9p",
    "clientSecret": "pmapue000000000000000000zylw3v"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_twitch(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_word_press(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "130005",
    "clientSecret": "PlBfJS0000000000000000000000000000000000000000000000000000EdUZJk"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_word_press(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_x(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "customerKey": "slzZV0000000000000NFLaWT",
    "secretKey": "tkEPkp00000000000000000000000000000000000000FTxbI9"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_x(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_yahoo(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "dj0yJm000000000000000000000000000000000000000000000000000000000000000000000000000000000000Z4PWRm",
    "clientSecret": "cf978f0000000000000000000000000000c5e2e9"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_yahoo(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_yandex(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "6a8a6a0000000000000000000091483c",
    "clientSecret": "bbf98500000000000000000000c75a63"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_yandex(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_zoho(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "1000.83C178000000000000000000RPNX0B",
    "clientSecret": "fb5cac000000000000000000000000000000a68f6e"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_zoho(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_o_auth2_zoom(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "QMAC00000000000000w0AQ",
    "clientSecret": "GAWsG4000000000000000000007U01ON"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_o_auth2_zoom(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_o_auth2_provider(self, m):
        data = {
    "$id": "github",
    "enabled": True,
    "clientId": "e4d87900000000540733",
    "clientSecret": "5e07c00000000000000000000000000000198bcc"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.get_o_auth2_provider(
            'amazon',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_platforms(self, m):
        data = {
    "total": 5.0,
    "platforms": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.list_platforms(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_android_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "applicationId": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_android_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<APPLICATION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_android_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "applicationId": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_android_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<APPLICATION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_apple_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "bundleIdentifier": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_apple_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<BUNDLE_IDENTIFIER>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_apple_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "bundleIdentifier": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_apple_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<BUNDLE_IDENTIFIER>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_linux_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "packageName": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_linux_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_linux_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "packageName": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_linux_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_web_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "hostname": "app.example.com"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_web_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            'app.example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_web_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "hostname": "app.example.com"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_web_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            'app.example.com',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_windows_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "packageIdentifierName": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_windows_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_IDENTIFIER_NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_windows_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "packageIdentifierName": "com.company.appname"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_windows_platform(
            '<PLATFORM_ID>',
            '<NAME>',
            '<PACKAGE_IDENTIFIER_NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_platform(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Web App",
    "type": "web",
    "hostname": "app.example.com"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.get_platform(
            '<PLATFORM_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_platform(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.delete_platform(
            '<PLATFORM_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_policies(self, m):
        data = {
    "total": 10.0,
    "policies": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.list_policies(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_aliased_email_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_deny_aliased_email_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_corporate_email_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_deny_corporate_email_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_disposable_email_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_deny_disposable_email_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_deny_free_email_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_deny_free_email_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_membership_privacy_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_membership_privacy_policy(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_dictionary_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_password_dictionary_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_history_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_password_history_policy(
            1,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_personal_data_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_password_personal_data_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_password_strength_policy(self, m):
        data = {
    "$id": "password-dictionary",
    "min": 12.0,
    "uppercase": True,
    "lowercase": True,
    "number": True,
    "symbols": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_password_strength_policy(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_alert_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_session_alert_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_duration_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_session_duration_policy(
            1,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_invalidation_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_session_invalidation_policy(
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_session_limit_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_session_limit_policy(
            1,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_user_limit_policy(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_user_limit_policy(
            1,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_policy(self, m):
        data = {
    "$id": "password-dictionary",
    "enabled": True
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.get_policy(
            'password-dictionary',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_protocol(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_protocol(
            'rest',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_service(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_service(
            'account',
            True,
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_smtp(self, m):
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
    "authMethods": [],
    "services": [],
    "protocols": [],
    "blocks": [],
    "consoleAccessedAt": "2020-10-15T06:38:00.000+00:00"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_smtp(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_smtp_test(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_smtp_test(
            [],
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_email_templates(self, m):
        data = {
    "total": 5.0,
    "templates": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.list_email_templates(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_email_template(self, m):
        data = {
    "templateId": "verification",
    "locale": "en_us",
    "message": "Click on the link to verify your account.",
    "senderName": "My User",
    "senderEmail": "mail@appwrite.io",
    "replyToEmail": "emails@appwrite.io",
    "replyToName": "Support Team",
    "subject": "Please verify your email address"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_email_template(
            'verification',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_email_template(self, m):
        data = {
    "templateId": "verification",
    "locale": "en_us",
    "message": "Click on the link to verify your account.",
    "senderName": "My User",
    "senderEmail": "mail@appwrite.io",
    "replyToEmail": "emails@appwrite.io",
    "replyToName": "Support Team",
    "subject": "Please verify your email address"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.get_email_template(
            'verification',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_variables(self, m):
        data = {
    "total": 5.0,
    "variables": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.list_variables(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_variable(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "key": "API_KEY",
    "value": "myPa$$word1",
    "secret": True,
    "resourceType": "function",
    "resourceId": "myAwesomeFunction"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.create_variable(
            '<VARIABLE_ID>',
            '<KEY>',
            '<VALUE>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_variable(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "key": "API_KEY",
    "value": "myPa$$word1",
    "secret": True,
    "resourceType": "function",
    "resourceId": "myAwesomeFunction"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.get_variable(
            '<VARIABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_variable(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "key": "API_KEY",
    "value": "myPa$$word1",
    "secret": True,
    "resourceType": "function",
    "resourceId": "myAwesomeFunction"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.update_variable(
            '<VARIABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_variable(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.project.delete_variable(
            '<VARIABLE_ID>',
        )

        self.assertEqual(response, data)

