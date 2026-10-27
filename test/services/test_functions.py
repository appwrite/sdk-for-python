import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            "functions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions',
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
    def test_create(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "execute": [],
            "name": "My Function",
            "description": "Sends a welcome email to newly registered users.",
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
            "providerBranches": [],
            "providerPaths": [],
            "buildSpecification": "s-1vcpu-512mb",
            "runtimeSpecification": "s-1vcpu-512mb",
            "emailEnabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.create(
            '<FUNCTION_ID>',
            '<NAME>',
            'node-14.5',
            execute=[],
            events=[],
            schedule='0 0 * * *',
            timeout=1,
            enabled=False,
            logging=False,
            entrypoint='<ENTRYPOINT>',
            commands='<COMMANDS>',
            scopes=[],
            installation_id='<INSTALLATION_ID>',
            provider_repository_id='<PROVIDER_REPOSITORY_ID>',
            provider_branch='<PROVIDER_BRANCH>',
            provider_silent_mode=False,
            provider_root_directory='<PROVIDER_ROOT_DIRECTORY>',
            provider_branches=[],
            provider_paths=[],
            build_specification='s-1vcpu-512mb',
            runtime_specification='s-1vcpu-512mb',
            deployment_retention=1,
            interval=1,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'functionId': '<FUNCTION_ID>',
                'name': '<NAME>',
                'runtime': 'node-14.5',
                'execute': [],
                'events': [],
                'schedule': '0 0 * * *',
                'timeout': 1,
                'enabled': False,
                'logging': False,
                'entrypoint': '<ENTRYPOINT>',
                'commands': '<COMMANDS>',
                'scopes': [],
                'installationId': '<INSTALLATION_ID>',
                'providerRepositoryId': '<PROVIDER_REPOSITORY_ID>',
                'providerBranch': '<PROVIDER_BRANCH>',
                'providerSilentMode': False,
                'providerRootDirectory': '<PROVIDER_ROOT_DIRECTORY>',
                'providerBranches': [],
                'providerPaths': [],
                'buildSpecification': 's-1vcpu-512mb',
                'runtimeSpecification': 's-1vcpu-512mb',
                'deploymentRetention': 1,
                'interval': 1,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_runtimes(self, m):
        data = {
            "total": 5.0,
            "runtimes": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.list_runtimes(
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/runtimes',
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
    def test_list_specifications(self, m):
        data = {
            "total": 5.0,
            "specifications": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.list_specifications(
            type='runtimes',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/specifications',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'type': ['runtimes'],
                'total': ['false'],
            },
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
            "description": "Sends a welcome email to newly registered users.",
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
            "providerBranches": [],
            "providerPaths": [],
            "buildSpecification": "s-1vcpu-512mb",
            "runtimeSpecification": "s-1vcpu-512mb",
            "emailEnabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.get(
            '<FUNCTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>',
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
            "execute": [],
            "name": "My Function",
            "description": "Sends a welcome email to newly registered users.",
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
            "providerBranches": [],
            "providerPaths": [],
            "buildSpecification": "s-1vcpu-512mb",
            "runtimeSpecification": "s-1vcpu-512mb",
            "emailEnabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.update(
            '<FUNCTION_ID>',
            '<NAME>',
            runtime='node-14.5',
            execute=[],
            events=[],
            schedule='0 0 * * *',
            timeout=1,
            enabled=False,
            logging=False,
            entrypoint='<ENTRYPOINT>',
            commands='<COMMANDS>',
            scopes=[],
            installation_id='<INSTALLATION_ID>',
            provider_repository_id='<PROVIDER_REPOSITORY_ID>',
            provider_branch='<PROVIDER_BRANCH>',
            provider_silent_mode=False,
            provider_root_directory='<PROVIDER_ROOT_DIRECTORY>',
            provider_branches=[],
            provider_paths=[],
            build_specification='s-1vcpu-512mb',
            runtime_specification='s-1vcpu-512mb',
            deployment_retention=1,
            interval=1,
            description='<DESCRIPTION>',
            email_enabled=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'runtime': 'node-14.5',
                'execute': [],
                'events': [],
                'schedule': '0 0 * * *',
                'timeout': 1,
                'enabled': False,
                'logging': False,
                'entrypoint': '<ENTRYPOINT>',
                'commands': '<COMMANDS>',
                'scopes': [],
                'installationId': '<INSTALLATION_ID>',
                'providerRepositoryId': '<PROVIDER_REPOSITORY_ID>',
                'providerBranch': '<PROVIDER_BRANCH>',
                'providerSilentMode': False,
                'providerRootDirectory': '<PROVIDER_ROOT_DIRECTORY>',
                'providerBranches': [],
                'providerPaths': [],
                'buildSpecification': 's-1vcpu-512mb',
                'runtimeSpecification': 's-1vcpu-512mb',
                'deploymentRetention': 1,
                'interval': 1,
                'description': '<DESCRIPTION>',
                'emailEnabled': False,
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
        response = self.functions.delete(
            '<FUNCTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_function_deployment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "execute": [],
            "name": "My Function",
            "description": "Sends a welcome email to newly registered users.",
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
            "providerBranches": [],
            "providerPaths": [],
            "buildSpecification": "s-1vcpu-512mb",
            "runtimeSpecification": "s-1vcpu-512mb",
            "emailEnabled": True,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.update_function_deployment(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployment',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'deploymentId': '<DEPLOYMENT_ID>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_deployments(self, m):
        data = {
            "total": 5.0,
            "deployments": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.list_deployments(
            '<FUNCTION_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments',
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
            "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.create_deployment(
            '<FUNCTION_ID>',
            InputFile.from_bytes(bytearray(), "example.file"),
            False,
            entrypoint='<ENTRYPOINT>',
            commands='<COMMANDS>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments',
        )
        sent = dict(
            re.findall(
                r'form-data; name="([^"\[]+)[^\r\n]*\r\n(?:[^\r\n]+\r\n)*\r\n(.*?)\r\n--',
                request.body.decode('latin-1'),
                re.S,
            )
        )
        self.assertEqual(
            sent,
            {
                'entrypoint': '<ENTRYPOINT>',
                'commands': '<COMMANDS>',
                'code': '',
                'activate': 'false',
            },
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
            "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.create_duplicate_deployment(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
            build_id='<BUILD_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments/duplicate',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'deploymentId': '<DEPLOYMENT_ID>',
                'buildId': '<BUILD_ID>',
            },
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
            "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.create_template_deployment(
            '<FUNCTION_ID>',
            '<REPOSITORY>',
            '<OWNER>',
            '<ROOT_DIRECTORY>',
            'commit',
            '<REFERENCE>',
            activate=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments/template',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'repository': '<REPOSITORY>',
                'owner': '<OWNER>',
                'rootDirectory': '<ROOT_DIRECTORY>',
                'type': 'commit',
                'reference': '<REFERENCE>',
                'activate': False,
            },
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
            "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.create_vcs_deployment(
            '<FUNCTION_ID>',
            'branch',
            '<REFERENCE>',
            activate=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments/vcs',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'type': 'branch',
                'reference': '<REFERENCE>',
                'activate': False,
            },
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
            "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.get_deployment(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments/<DEPLOYMENT_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_deployment(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.delete_deployment(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments/<DEPLOYMENT_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_get_deployment_download(self, m):
        data = bytearray()
        headers = {'Content-Type': 'application/octet-stream'}
        m.request(
            'GET',
            requests_mock.ANY,
            body=data,
            headers=headers,
        )
        response = self.functions.get_deployment_download(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
            type='source',
            token='<TOKEN>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments/<DEPLOYMENT_ID>/download',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(
            sent,
            {
                'type': ['source'],
                'token': ['<TOKEN>'],
            },
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
            "providerBranchUrl": "https:\/\/github.com\/vermakhushboo\/appwrite\/tree\/0.7.x",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.update_deployment_status(
            '<FUNCTION_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/deployments/<DEPLOYMENT_ID>/status',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_executions(self, m):
        data = {
            "total": 5.0,
            "executions": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.list_executions(
            '<FUNCTION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/executions',
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
    def test_create_execution(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "resourceId": "5e5ea6g16897e",
            "resourceType": "functions",
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
            "duration": 1.23,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.create_execution(
            '<FUNCTION_ID>',
            body='<BODY>',
            xasync=False,
            path='<PATH>',
            method='GET',
            headers={},
            scheduled_at='<SCHEDULED_AT>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/executions',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'body': '<BODY>',
                'async': False,
                'path': '<PATH>',
                'method': 'GET',
                'headers': {},
                'scheduledAt': '<SCHEDULED_AT>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_execution(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "$permissions": [],
            "resourceId": "5e5ea6g16897e",
            "resourceType": "functions",
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
            "duration": 1.23,
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.get_execution(
            '<FUNCTION_ID>',
            '<EXECUTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/executions/<EXECUTION_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_execution(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.delete_execution(
            '<FUNCTION_ID>',
            '<EXECUTION_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/executions/<EXECUTION_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_list_variables(self, m):
        data = {
            "total": 5.0,
            "variables": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.list_variables(
            '<FUNCTION_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/variables',
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
    def test_create_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.create_variable(
            '<FUNCTION_ID>',
            '<VARIABLE_ID>',
            '<KEY>',
            '<VALUE>',
            secret=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/variables',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'variableId': '<VARIABLE_ID>',
                'key': '<KEY>',
                'value': '<VALUE>',
                'secret': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_get_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.get_variable(
            '<FUNCTION_ID>',
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/variables/<VARIABLE_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_update_variable(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "key": "API_KEY",
            "description": "Stripe secret key used at checkout.",
            "value": "myPa$$word1",
            "secret": True,
            "resourceType": "function",
            "resourceId": "myAwesomeFunction",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.update_variable(
            '<FUNCTION_ID>',
            '<VARIABLE_ID>',
            key='<KEY>',
            value='<VALUE>',
            secret=False,
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/variables/<VARIABLE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'key': '<KEY>',
                'value': '<VALUE>',
                'secret': False,
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_variable(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.functions.delete_variable(
            '<FUNCTION_ID>',
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/functions/<FUNCTION_ID>/variables/<VARIABLE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
