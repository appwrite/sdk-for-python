import json
import requests_mock
import unittest

from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.models import *
from appwrite.services.functions import Functions

class FunctionsServiceTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.functions = Functions(self.client)

    @requests_mock.Mocker()
    def test_list(self, m):
        data = {
    "total": 5.0,
    "functions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.list(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "execute": [],
    "name": "My Function",
    "enabled": True,
    "live": True,
    "logging": True,
    "runtime": "python-3.8",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "scopes": [],
    "vars": [],
    "events": [],
    "schedule": "5 4 * * *",
    "timeout": 300.0,
    "entrypoint": "index.js",
    "commands": "npm install",
    "version": "v2",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "functions\/helloWorld",
    "providerSilentMode": True,
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.create(
            '<FUNCTION_ID>',
            '<NAME>',
            'node-14.5',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_runtimes(self, m):
        data = {
    "total": 5.0,
    "runtimes": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.list_runtimes(
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

        response = self.functions.list_specifications(
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "execute": [],
    "name": "My Function",
    "enabled": True,
    "live": True,
    "logging": True,
    "runtime": "python-3.8",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "scopes": [],
    "vars": [],
    "events": [],
    "schedule": "5 4 * * *",
    "timeout": 300.0,
    "entrypoint": "index.js",
    "commands": "npm install",
    "version": "v2",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "functions\/helloWorld",
    "providerSilentMode": True,
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.get(
            '<FUNCTION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "execute": [],
    "name": "My Function",
    "enabled": True,
    "live": True,
    "logging": True,
    "runtime": "python-3.8",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "scopes": [],
    "vars": [],
    "events": [],
    "schedule": "5 4 * * *",
    "timeout": 300.0,
    "entrypoint": "index.js",
    "commands": "npm install",
    "version": "v2",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "functions\/helloWorld",
    "providerSilentMode": True,
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.update(
            '<FUNCTION_ID>',
            '<NAME>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.delete(
            '<FUNCTION_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_function_deployment(self, m):
        data = {
    "$id": "5e5ea5c16897e",
    "$createdAt": "2020-10-15T06:38:00.000+00:00",
    "$updatedAt": "2020-10-15T06:38:00.000+00:00",
    "execute": [],
    "name": "My Function",
    "enabled": True,
    "live": True,
    "logging": True,
    "runtime": "python-3.8",
    "deploymentRetention": 7.0,
    "deploymentId": "5e5ea5c16897e",
    "deploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentId": "5e5ea5c16897e",
    "latestDeploymentCreatedAt": "2020-10-15T06:38:00.000+00:00",
    "latestDeploymentStatus": "ready",
    "scopes": [],
    "vars": [],
    "events": [],
    "schedule": "5 4 * * *",
    "timeout": 300.0,
    "entrypoint": "index.js",
    "commands": "npm install",
    "version": "v2",
    "installationId": "6m40at4ejk5h2u9s1hboo",
    "providerRepositoryId": "appwrite",
    "providerBranch": "main",
    "providerRootDirectory": "functions\/helloWorld",
    "providerSilentMode": True,
    "buildSpecification": "s-1vcpu-512mb",
    "runtimeSpecification": "s-1vcpu-512mb"
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.update_function_deployment(
            '<FUNCTION_ID>',
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

        response = self.functions.list_deployments(
            '<FUNCTION_ID>',
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

        response = self.functions.create_deployment(
            '<FUNCTION_ID>',
            InputFile.from_bytes(bytearray(), "example.file"),
            True,
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

        response = self.functions.create_duplicate_deployment(
            '<FUNCTION_ID>',
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

        response = self.functions.create_template_deployment(
            '<FUNCTION_ID>',
            '<REPOSITORY>',
            '<OWNER>',
            '<ROOT_DIRECTORY>',
            'commit',
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

        response = self.functions.create_vcs_deployment(
            '<FUNCTION_ID>',
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

        response = self.functions.get_deployment(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_deployment(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.delete_deployment(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_deployment_download(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(requests_mock.ANY, requests_mock.ANY, body=data, headers=headers)

        response = self.functions.get_deployment_download(
            '<FUNCTION_ID>',
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

        response = self.functions.update_deployment_status(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_executions(self, m):
        data = {
    "total": 5.0,
    "executions": []
}
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.list_executions(
            '<FUNCTION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_create_execution(self, m):
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

        response = self.functions.create_execution(
            '<FUNCTION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_execution(self, m):
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

        response = self.functions.get_execution(
            '<FUNCTION_ID>',
            '<EXECUTION_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_execution(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.delete_execution(
            '<FUNCTION_ID>',
            '<EXECUTION_ID>',
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

        response = self.functions.list_variables(
            '<FUNCTION_ID>',
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

        response = self.functions.create_variable(
            '<FUNCTION_ID>',
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

        response = self.functions.get_variable(
            '<FUNCTION_ID>',
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

        response = self.functions.update_variable(
            '<FUNCTION_ID>',
            '<VARIABLE_ID>',
        )

        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_variable(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(requests_mock.ANY, requests_mock.ANY, text=json.dumps(data), headers=headers)

        response = self.functions.delete_variable(
            '<FUNCTION_ID>',
            '<VARIABLE_ID>',
        )

        self.assertEqual(response, data)

