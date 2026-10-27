import json
import re
import requests_mock
import unittest
from urllib.parse import parse_qs, unquote, urlsplit

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
            "sites": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.sites.list(
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites',
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
            "name": "My Site",
            "description": "Marketing site for the spring launch.",
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
            "scopes": [],
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
            "fallbackFile": "index.html",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'POST',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.sites.create(
            '<SITE_ID>',
            '<NAME>',
            'analog',
            'node-14.5',
            enabled=False,
            logging=False,
            timeout=1,
            install_command='<INSTALL_COMMAND>',
            build_command='<BUILD_COMMAND>',
            start_command='<START_COMMAND>',
            output_directory='<OUTPUT_DIRECTORY>',
            adapter='static',
            installation_id='<INSTALLATION_ID>',
            fallback_file='<FALLBACK_FILE>',
            provider_repository_id='<PROVIDER_REPOSITORY_ID>',
            provider_branch='<PROVIDER_BRANCH>',
            provider_silent_mode=False,
            provider_root_directory='<PROVIDER_ROOT_DIRECTORY>',
            provider_branches=[],
            provider_paths=[],
            build_specification='s-1vcpu-512mb',
            runtime_specification='s-1vcpu-512mb',
            deployment_retention=1,
            scopes=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'siteId': '<SITE_ID>',
                'name': '<NAME>',
                'framework': 'analog',
                'enabled': False,
                'logging': False,
                'timeout': 1,
                'installCommand': '<INSTALL_COMMAND>',
                'buildCommand': '<BUILD_COMMAND>',
                'startCommand': '<START_COMMAND>',
                'outputDirectory': '<OUTPUT_DIRECTORY>',
                'buildRuntime': 'node-14.5',
                'adapter': 'static',
                'installationId': '<INSTALLATION_ID>',
                'fallbackFile': '<FALLBACK_FILE>',
                'providerRepositoryId': '<PROVIDER_REPOSITORY_ID>',
                'providerBranch': '<PROVIDER_BRANCH>',
                'providerSilentMode': False,
                'providerRootDirectory': '<PROVIDER_ROOT_DIRECTORY>',
                'providerBranches': [],
                'providerPaths': [],
                'buildSpecification': 's-1vcpu-512mb',
                'runtimeSpecification': 's-1vcpu-512mb',
                'deploymentRetention': 1,
                'scopes': [],
                'description': '<DESCRIPTION>',
            },
        )
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_frameworks(self, m):
        data = {
            "total": 5.0,
            "frameworks": [],
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.sites.list_frameworks(
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/frameworks',
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
        response = self.sites.list_specifications(
            type='runtimes',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/specifications',
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
            "name": "My Site",
            "description": "Marketing site for the spring launch.",
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
            "scopes": [],
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
            "fallbackFile": "index.html",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'GET',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.sites.get(
            '<SITE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>',
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
            "name": "My Site",
            "description": "Marketing site for the spring launch.",
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
            "scopes": [],
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
            "fallbackFile": "index.html",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PUT',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.sites.update(
            '<SITE_ID>',
            '<NAME>',
            'analog',
            enabled=False,
            logging=False,
            timeout=1,
            install_command='<INSTALL_COMMAND>',
            build_command='<BUILD_COMMAND>',
            start_command='<START_COMMAND>',
            output_directory='<OUTPUT_DIRECTORY>',
            build_runtime='node-14.5',
            adapter='static',
            fallback_file='<FALLBACK_FILE>',
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
            scopes=[],
            description='<DESCRIPTION>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'name': '<NAME>',
                'framework': 'analog',
                'enabled': False,
                'logging': False,
                'timeout': 1,
                'installCommand': '<INSTALL_COMMAND>',
                'buildCommand': '<BUILD_COMMAND>',
                'startCommand': '<START_COMMAND>',
                'outputDirectory': '<OUTPUT_DIRECTORY>',
                'buildRuntime': 'node-14.5',
                'adapter': 'static',
                'fallbackFile': '<FALLBACK_FILE>',
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
                'scopes': [],
                'description': '<DESCRIPTION>',
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
        response = self.sites.delete(
            '<SITE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)

    @requests_mock.Mocker()
    def test_update_site_deployment(self, m):
        data = {
            "$id": "5e5ea5c16897e",
            "$createdAt": "2020-10-15T06:38:00.000+00:00",
            "$updatedAt": "2020-10-15T06:38:00.000+00:00",
            "name": "My Site",
            "description": "Marketing site for the spring launch.",
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
            "scopes": [],
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
            "fallbackFile": "index.html",
        }
        headers = {'Content-Type': 'application/json'}
        m.request(
            'PATCH',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.sites.update_site_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployment',
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
        response = self.sites.list_deployments(
            '<SITE_ID>',
            queries=[],
            search='<SEARCH>',
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments',
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
        response = self.sites.create_deployment(
            '<SITE_ID>',
            InputFile.from_bytes(bytearray(), "example.file"),
            install_command='<INSTALL_COMMAND>',
            build_command='<BUILD_COMMAND>',
            output_directory='<OUTPUT_DIRECTORY>',
            activate=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments',
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
                'installCommand': '<INSTALL_COMMAND>',
                'buildCommand': '<BUILD_COMMAND>',
                'outputDirectory': '<OUTPUT_DIRECTORY>',
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
        response = self.sites.create_duplicate_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments/duplicate',
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
        response = self.sites.create_template_deployment(
            '<SITE_ID>',
            '<REPOSITORY>',
            '<OWNER>',
            '<ROOT_DIRECTORY>',
            'branch',
            '<REFERENCE>',
            activate=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments/template',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(
            sent,
            {
                'repository': '<REPOSITORY>',
                'owner': '<OWNER>',
                'rootDirectory': '<ROOT_DIRECTORY>',
                'type': 'branch',
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
        response = self.sites.create_vcs_deployment(
            '<SITE_ID>',
            'branch',
            '<REFERENCE>',
            activate=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments/vcs',
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
        response = self.sites.get_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments/<DEPLOYMENT_ID>',
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
        response = self.sites.delete_deployment(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments/<DEPLOYMENT_ID>',
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
        response = self.sites.get_deployment_download(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
            type='source',
            token='<TOKEN>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments/<DEPLOYMENT_ID>/download',
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
        response = self.sites.update_deployment_status(
            '<SITE_ID>',
            '<DEPLOYMENT_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/deployments/<DEPLOYMENT_ID>/status',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_list_logs(self, m):
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
        response = self.sites.list_logs(
            '<SITE_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/logs',
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
    def test_get_log(self, m):
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
        response = self.sites.get_log(
            '<SITE_ID>',
            '<LOG_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/logs/<LOG_ID>',
        )
        sent = parse_qs(url.query, keep_blank_values=True)
        self.assertEqual(sent, {})
        self.assertEqual(response.to_dict(), data)

    @requests_mock.Mocker()
    def test_delete_log(self, m):
        data = ''
        headers = {'Content-Type': 'application/json'}
        m.request(
            'DELETE',
            requests_mock.ANY,
            text=json.dumps(data),
            headers=headers,
        )
        response = self.sites.delete_log(
            '<SITE_ID>',
            '<LOG_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/logs/<LOG_ID>',
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
        response = self.sites.list_variables(
            '<SITE_ID>',
            queries=[],
            total=False,
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/variables',
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
        response = self.sites.create_variable(
            '<SITE_ID>',
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
            '/v1/sites/<SITE_ID>/variables',
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
        response = self.sites.get_variable(
            '<SITE_ID>',
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/variables/<VARIABLE_ID>',
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
        response = self.sites.update_variable(
            '<SITE_ID>',
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
            '/v1/sites/<SITE_ID>/variables/<VARIABLE_ID>',
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
        response = self.sites.delete_variable(
            '<SITE_ID>',
            '<VARIABLE_ID>',
        )
        request = m.last_request
        url = urlsplit(request.url)
        self.assertEqual(
            unquote(url.path),
            '/v1/sites/<SITE_ID>/variables/<VARIABLE_ID>',
        )
        sent = json.loads(request.body or '{}')
        self.assertEqual(sent, {})
        self.assertEqual(response, data)
