import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.sites import Sites

class SitesServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.sites = Sites(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
    "total": 5.0,
    "sites": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Site",
    "enabled": True,
    "live": True,
    "logging": True,
    "framework": "react",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "deploymentScreenshotLight": "5e5ea5c16897e",
    "deploymentScreenshotDark": "5e5ea5c16897e",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "vars": [],
    "timeout": 300.0,
    "installCommand": "npm install",
    "buildCommand": "npm run build",
    "startCommand": "node custom-server.mjs",
    "outputDirectory": "build",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "sites\/helloWorld",
    "providerSilentMode": True,
    "providerBranches": [],
    "providerPaths": [],
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb",
    "buildRuntime": "node-22",
    "adapter": "static",
    "fallbackFile": "index.html"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.create(
            '<SITE_ID>',
            '<NAME>',
            'analog',
            'node-14.5',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_frameworks(self, m):
        data = {
    "total": 5.0,
    "frameworks": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.list_frameworks(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_specifications(self, m):
        data = {
    "total": 5.0,
    "specifications": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.list_specifications(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Site",
    "enabled": True,
    "live": True,
    "logging": True,
    "framework": "react",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "deploymentScreenshotLight": "5e5ea5c16897e",
    "deploymentScreenshotDark": "5e5ea5c16897e",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "vars": [],
    "timeout": 300.0,
    "installCommand": "npm install",
    "buildCommand": "npm run build",
    "startCommand": "node custom-server.mjs",
    "outputDirectory": "build",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "sites\/helloWorld",
    "providerSilentMode": True,
    "providerBranches": [],
    "providerPaths": [],
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb",
    "buildRuntime": "node-22",
    "adapter": "static",
    "fallbackFile": "index.html"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.get(
            '<SITE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Site",
    "enabled": True,
    "live": True,
    "logging": True,
    "framework": "react",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "deploymentScreenshotLight": "5e5ea5c16897e",
    "deploymentScreenshotDark": "5e5ea5c16897e",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "vars": [],
    "timeout": 300.0,
    "installCommand": "npm install",
    "buildCommand": "npm run build",
    "startCommand": "node custom-server.mjs",
    "outputDirectory": "build",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "sites\/helloWorld",
    "providerSilentMode": True,
    "providerBranches": [],
    "providerPaths": [],
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb",
    "buildRuntime": "node-22",
    "adapter": "static",
    "fallbackFile": "index.html"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.update(
            '<SITE_ID>',
            '<NAME>',
            'analog',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.delete(
            '<SITE_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_site_deployment(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "name": "My Site",
    "enabled": True,
    "live": True,
    "logging": True,
    "framework": "react",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "deploymentScreenshotLight": "5e5ea5c16897e",
    "deploymentScreenshotDark": "5e5ea5c16897e",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "vars": [],
    "timeout": 300.0,
    "installCommand": "npm install",
    "buildCommand": "npm run build",
    "startCommand": "node custom-server.mjs",
    "outputDirectory": "build",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "sites\/helloWorld",
    "providerSilentMode": True,
    "providerBranches": [],
    "providerPaths": [],
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb",
    "buildRuntime": "node-22",
    "adapter": "static",
    "fallbackFile": "index.html"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.update_site_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_deployments(self, m):
        data = {
    "total": 5.0,
    "deployments": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.list_deployments(
            '<SITE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_deployment(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "type": "vcs",
    "resourceId": "5e5ea6g16897e",
    "resourceType": "functions",
    "entrypoint": "index.js",
    "sourceSize": 128.0,
    "buildSize": 128.0,
    "totalSize": 128.0,
    "buildId": "5e5ea5c16897e",
    "activate": True,
    "screenshotLight": "5e5ea5c16897e",
    "screenshotDark": "5e5ea5c16897e",
    "status": "ready",
    "buildLogs": "Compiling source files...",
    "buildDuration": 128.0,
    "providerRepositoryName": "database",
    "providerRepositoryOwner": "utopia",
    "providerRepositoryUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function",
    "providerCommitHash": "7c3f25d",
    "providerCommitAuthorUrl": "https:\/\/github.com\/vermakhushboo",
    "providerCommitAuthor": "Khushboo Verma",
    "providerCommitMessage": "Update index.js",
    "providerCommitUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function\/commit\/60c0416257a9cbcdd96b2d370c38d8f8d150ccfb",
    "providerBranch": "0.7.x",
    "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.create_deployment(
            '<SITE_ID>',
            InputFile.from_bytes(bytearray(), "example.file"),
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_duplicate_deployment(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "type": "vcs",
    "resourceId": "5e5ea6g16897e",
    "resourceType": "functions",
    "entrypoint": "index.js",
    "sourceSize": 128.0,
    "buildSize": 128.0,
    "totalSize": 128.0,
    "buildId": "5e5ea5c16897e",
    "activate": True,
    "screenshotLight": "5e5ea5c16897e",
    "screenshotDark": "5e5ea5c16897e",
    "status": "ready",
    "buildLogs": "Compiling source files...",
    "buildDuration": 128.0,
    "providerRepositoryName": "database",
    "providerRepositoryOwner": "utopia",
    "providerRepositoryUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function",
    "providerCommitHash": "7c3f25d",
    "providerCommitAuthorUrl": "https:\/\/github.com\/vermakhushboo",
    "providerCommitAuthor": "Khushboo Verma",
    "providerCommitMessage": "Update index.js",
    "providerCommitUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function\/commit\/60c0416257a9cbcdd96b2d370c38d8f8d150ccfb",
    "providerBranch": "0.7.x",
    "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.create_duplicate_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_template_deployment(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "type": "vcs",
    "resourceId": "5e5ea6g16897e",
    "resourceType": "functions",
    "entrypoint": "index.js",
    "sourceSize": 128.0,
    "buildSize": 128.0,
    "totalSize": 128.0,
    "buildId": "5e5ea5c16897e",
    "activate": True,
    "screenshotLight": "5e5ea5c16897e",
    "screenshotDark": "5e5ea5c16897e",
    "status": "ready",
    "buildLogs": "Compiling source files...",
    "buildDuration": 128.0,
    "providerRepositoryName": "database",
    "providerRepositoryOwner": "utopia",
    "providerRepositoryUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function",
    "providerCommitHash": "7c3f25d",
    "providerCommitAuthorUrl": "https:\/\/github.com\/vermakhushboo",
    "providerCommitAuthor": "Khushboo Verma",
    "providerCommitMessage": "Update index.js",
    "providerCommitUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function\/commit\/60c0416257a9cbcdd96b2d370c38d8f8d150ccfb",
    "providerBranch": "0.7.x",
    "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.create_template_deployment(
            '<SITE_ID>',
            '<REPOSITORY>',
            '<OWNER>',
            '<ROOT_DIRECTORY>',
            'branch',
            '<REFERENCE>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_vcs_deployment(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "type": "vcs",
    "resourceId": "5e5ea6g16897e",
    "resourceType": "functions",
    "entrypoint": "index.js",
    "sourceSize": 128.0,
    "buildSize": 128.0,
    "totalSize": 128.0,
    "buildId": "5e5ea5c16897e",
    "activate": True,
    "screenshotLight": "5e5ea5c16897e",
    "screenshotDark": "5e5ea5c16897e",
    "status": "ready",
    "buildLogs": "Compiling source files...",
    "buildDuration": 128.0,
    "providerRepositoryName": "database",
    "providerRepositoryOwner": "utopia",
    "providerRepositoryUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function",
    "providerCommitHash": "7c3f25d",
    "providerCommitAuthorUrl": "https:\/\/github.com\/vermakhushboo",
    "providerCommitAuthor": "Khushboo Verma",
    "providerCommitMessage": "Update index.js",
    "providerCommitUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function\/commit\/60c0416257a9cbcdd96b2d370c38d8f8d150ccfb",
    "providerBranch": "0.7.x",
    "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.create_vcs_deployment(
            '<SITE_ID>',
            'branch',
            '<REFERENCE>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_deployment(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "type": "vcs",
    "resourceId": "5e5ea6g16897e",
    "resourceType": "functions",
    "entrypoint": "index.js",
    "sourceSize": 128.0,
    "buildSize": 128.0,
    "totalSize": 128.0,
    "buildId": "5e5ea5c16897e",
    "activate": True,
    "screenshotLight": "5e5ea5c16897e",
    "screenshotDark": "5e5ea5c16897e",
    "status": "ready",
    "buildLogs": "Compiling source files...",
    "buildDuration": 128.0,
    "providerRepositoryName": "database",
    "providerRepositoryOwner": "utopia",
    "providerRepositoryUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function",
    "providerCommitHash": "7c3f25d",
    "providerCommitAuthorUrl": "https:\/\/github.com\/vermakhushboo",
    "providerCommitAuthor": "Khushboo Verma",
    "providerCommitMessage": "Update index.js",
    "providerCommitUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function\/commit\/60c0416257a9cbcdd96b2d370c38d8f8d150ccfb",
    "providerBranch": "0.7.x",
    "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.get_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_deployment(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.delete_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_deployment_download(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.sites.get_deployment_download(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_deployment_status(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "type": "vcs",
    "resourceId": "5e5ea6g16897e",
    "resourceType": "functions",
    "entrypoint": "index.js",
    "sourceSize": 128.0,
    "buildSize": 128.0,
    "totalSize": 128.0,
    "buildId": "5e5ea5c16897e",
    "activate": True,
    "screenshotLight": "5e5ea5c16897e",
    "screenshotDark": "5e5ea5c16897e",
    "status": "ready",
    "buildLogs": "Compiling source files...",
    "buildDuration": 128.0,
    "providerRepositoryName": "database",
    "providerRepositoryOwner": "utopia",
    "providerRepositoryUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function",
    "providerCommitHash": "7c3f25d",
    "providerCommitAuthorUrl": "https:\/\/github.com\/vermakhushboo",
    "providerCommitAuthor": "Khushboo Verma",
    "providerCommitMessage": "Update index.js",
    "providerCommitUrl": "https:\/\/github.com\/vermakhushboo\/g4-node-function\/commit\/60c0416257a9cbcdd96b2d370c38d8f8d150ccfb",
    "providerBranch": "0.7.x",
    "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.update_deployment_status(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_logs(self, m):
        data = {
    "total": 5.0,
    "executions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.list_logs(
            '<SITE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_log(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "$permissions": [],
    "functionId": "5e5ea6g16897e",
    "deploymentId": "5e5ea5c16897e",
    "trigger": "http",
    "status": "processing",
    "requestMethod": "GET",
    "requestPath": "\/articles?id=5",
    "requestHeaders": [],
    "responseStatusCode": 200.0,
    "responseBody": "",
    "responseHeaders": [],
    "logs": "",
    "errors": "",
    "duration": 0.4
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.get_log(
            '<SITE_ID>',
            '<LOG_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_log(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.delete_log(
            '<SITE_ID>',
            '<LOG_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_variables(self, m):
        data = {
    "total": 5.0,
    "variables": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.list_variables(
            '<SITE_ID>',
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

        response = self.sites.create_variable(
            '<SITE_ID>',
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

        response = self.sites.get_variable(
            '<SITE_ID>',
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

        response = self.sites.update_variable(
            '<SITE_ID>',
            '<VARIABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_variable(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.sites.delete_variable(
            '<SITE_ID>',
            '<VARIABLE_ID>',
        )

        self.assertEqual(response, data)

