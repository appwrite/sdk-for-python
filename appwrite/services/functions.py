from ..service import Service
from typing import List
from ..exception import AppwriteException
from ..enums.runtime import Runtime;
from ..input_file import InputFile
from ..enums.execution_method import ExecutionMethod;

class Functions(Service):

    def __init__(self, client):
        super(Functions, self).__init__(client)

    def list(self, queries: List[str] = None, search: str = None):
        """List functions"""

        api_path = '/functions'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create(self, function_id: str, name: str, runtime: Runtime, execute: List[str] = None, events: List[str] = None, schedule: str = None, timeout: float = None, enabled: bool = None, logging: bool = None, entrypoint: str = None, commands: str = None, scopes: List[str] = None, installation_id: str = None, provider_repository_id: str = None, provider_branch: str = None, provider_silent_mode: bool = None, provider_root_directory: str = None, template_repository: str = None, template_owner: str = None, template_root_directory: str = None, template_version: str = None, specification: str = None):
        """Create function"""

        api_path = '/functions'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if runtime is None:
            raise AppwriteException('Missing required parameter: "runtime"')


        api_params['functionId'] = function_id
        api_params['name'] = name
        api_params['runtime'] = runtime
        api_params['execute'] = execute
        api_params['events'] = events
        api_params['schedule'] = schedule
        api_params['timeout'] = timeout
        api_params['enabled'] = enabled
        api_params['logging'] = logging
        api_params['entrypoint'] = entrypoint
        api_params['commands'] = commands
        api_params['scopes'] = scopes
        api_params['installationId'] = installation_id
        api_params['providerRepositoryId'] = provider_repository_id
        api_params['providerBranch'] = provider_branch
        api_params['providerSilentMode'] = provider_silent_mode
        api_params['providerRootDirectory'] = provider_root_directory
        api_params['templateRepository'] = template_repository
        api_params['templateOwner'] = template_owner
        api_params['templateRootDirectory'] = template_root_directory
        api_params['templateVersion'] = template_version
        api_params['specification'] = specification

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_runtimes(self):
        """List runtimes"""

        api_path = '/functions/runtimes'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_specifications(self):
        """List available function runtime specifications"""

        api_path = '/functions/specifications'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get(self, function_id: str):
        """Get function"""

        api_path = '/functions/{functionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update(self, function_id: str, name: str, runtime: Runtime = None, execute: List[str] = None, events: List[str] = None, schedule: str = None, timeout: float = None, enabled: bool = None, logging: bool = None, entrypoint: str = None, commands: str = None, scopes: List[str] = None, installation_id: str = None, provider_repository_id: str = None, provider_branch: str = None, provider_silent_mode: bool = None, provider_root_directory: str = None, specification: str = None):
        """Update function"""

        api_path = '/functions/{functionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['name'] = name
        api_params['runtime'] = runtime
        api_params['execute'] = execute
        api_params['events'] = events
        api_params['schedule'] = schedule
        api_params['timeout'] = timeout
        api_params['enabled'] = enabled
        api_params['logging'] = logging
        api_params['entrypoint'] = entrypoint
        api_params['commands'] = commands
        api_params['scopes'] = scopes
        api_params['installationId'] = installation_id
        api_params['providerRepositoryId'] = provider_repository_id
        api_params['providerBranch'] = provider_branch
        api_params['providerSilentMode'] = provider_silent_mode
        api_params['providerRootDirectory'] = provider_root_directory
        api_params['specification'] = specification

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, function_id: str):
        """Delete function"""

        api_path = '/functions/{functionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_deployments(self, function_id: str, queries: List[str] = None, search: str = None):
        """List deployments"""

        api_path = '/functions/{functionId}/deployments'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_deployment(self, function_id: str, code: InputFile, activate: bool, entrypoint: str = None, commands: str = None, on_progress = None):
        """Create deployment"""

        api_path = '/functions/{functionId}/deployments'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        if activate is None:
            raise AppwriteException('Missing required parameter: "activate"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['entrypoint'] = entrypoint
        api_params['commands'] = commands
        api_params['code'] = str(code).lower() if type(code) is bool else code
        api_params['activate'] = str(activate).lower() if type(activate) is bool else activate

        param_name = 'code'


        upload_id = ''

        return self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

    def get_deployment(self, function_id: str, deployment_id: str):
        """Get deployment"""

        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_deployment(self, function_id: str, deployment_id: str):
        """Update deployment"""

        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_deployment(self, function_id: str, deployment_id: str):
        """Delete deployment"""

        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_build(self, function_id: str, deployment_id: str, build_id: str = None):
        """Rebuild deployment"""

        api_path = '/functions/{functionId}/deployments/{deploymentId}/build'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)

        api_params['buildId'] = build_id

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_deployment_build(self, function_id: str, deployment_id: str):
        """Cancel deployment"""

        api_path = '/functions/{functionId}/deployments/{deploymentId}/build'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_deployment_download(self, function_id: str, deployment_id: str):
        """Download deployment"""

        api_path = '/functions/{functionId}/deployments/{deploymentId}/download'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_executions(self, function_id: str, queries: List[str] = None, search: str = None):
        """List executions"""

        api_path = '/functions/{functionId}/executions'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_execution(self, function_id: str, body: str = None, xasync: bool = None, path: str = None, method: ExecutionMethod = None, headers: dict = None, scheduled_at: str = None):
        """Create execution"""

        api_path = '/functions/{functionId}/executions'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['body'] = body
        api_params['async'] = xasync
        api_params['path'] = path
        api_params['method'] = method
        api_params['headers'] = headers
        api_params['scheduledAt'] = scheduled_at

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_execution(self, function_id: str, execution_id: str):
        """Get execution"""

        api_path = '/functions/{functionId}/executions/{executionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise AppwriteException('Missing required parameter: "execution_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{executionId}', execution_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_execution(self, function_id: str, execution_id: str):
        """Delete execution"""

        api_path = '/functions/{functionId}/executions/{executionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise AppwriteException('Missing required parameter: "execution_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{executionId}', execution_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_variables(self, function_id: str):
        """List variables"""

        api_path = '/functions/{functionId}/variables'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_variable(self, function_id: str, key: str, value: str):
        """Create variable"""

        api_path = '/functions/{functionId}/variables'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if value is None:
            raise AppwriteException('Missing required parameter: "value"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['key'] = key
        api_params['value'] = value

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_variable(self, function_id: str, variable_id: str):
        """Get variable"""

        api_path = '/functions/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{variableId}', variable_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_variable(self, function_id: str, variable_id: str, key: str, value: str = None):
        """Update variable"""

        api_path = '/functions/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{variableId}', variable_id)

        api_params['key'] = key
        api_params['value'] = value

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_variable(self, function_id: str, variable_id: str):
        """Delete variable"""

        api_path = '/functions/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{variableId}', variable_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)
