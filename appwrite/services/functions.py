from ..service import Service
from ..exception import AppwriteException

class Functions(Service):

    def __init__(self, client):
        super(Functions, self).__init__(client)

    def list(self, queries = None, search = None):
        """List Functions"""

        
        api_path = '/functions'
        params = {}

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def create(self, function_id, name, runtime, execute = None, events = None, schedule = None, timeout = None, enabled = None, logging = None, entrypoint = None, commands = None, installation_id = None, provider_repository_id = None, provider_branch = None, provider_silent_mode = None, provider_root_directory = None, template_repository = None, template_owner = None, template_root_directory = None, template_branch = None):
        """Create Function"""

        
        api_path = '/functions'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if runtime is None:
            raise AppwriteException('Missing required parameter: "runtime"')


        params['functionId'] = function_id
        params['name'] = name
        params['runtime'] = runtime
        params['execute'] = execute
        params['events'] = events
        params['schedule'] = schedule
        params['timeout'] = timeout
        params['enabled'] = enabled
        params['logging'] = logging
        params['entrypoint'] = entrypoint
        params['commands'] = commands
        params['installationId'] = installation_id
        params['providerRepositoryId'] = provider_repository_id
        params['providerBranch'] = provider_branch
        params['providerSilentMode'] = provider_silent_mode
        params['providerRootDirectory'] = provider_root_directory
        params['templateRepository'] = template_repository
        params['templateOwner'] = template_owner
        params['templateRootDirectory'] = template_root_directory
        params['templateBranch'] = template_branch

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_runtimes(self):
        """List runtimes"""

        
        api_path = '/functions/runtimes'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get(self, function_id):
        """Get Function"""

        
        api_path = '/functions/{functionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def update(self, function_id, name, runtime, execute = None, events = None, schedule = None, timeout = None, enabled = None, logging = None, entrypoint = None, commands = None, installation_id = None, provider_repository_id = None, provider_branch = None, provider_silent_mode = None, provider_root_directory = None):
        """Update Function"""

        
        api_path = '/functions/{functionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if runtime is None:
            raise AppwriteException('Missing required parameter: "runtime"')

        path = path.replace('{functionId}', function_id)

        params['name'] = name
        params['runtime'] = runtime
        params['execute'] = execute
        params['events'] = events
        params['schedule'] = schedule
        params['timeout'] = timeout
        params['enabled'] = enabled
        params['logging'] = logging
        params['entrypoint'] = entrypoint
        params['commands'] = commands
        params['installationId'] = installation_id
        params['providerRepositoryId'] = provider_repository_id
        params['providerBranch'] = provider_branch
        params['providerSilentMode'] = provider_silent_mode
        params['providerRootDirectory'] = provider_root_directory

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, params)

    def delete(self, function_id):
        """Delete Function"""

        
        api_path = '/functions/{functionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_deployments(self, function_id, queries = None, search = None):
        """List Deployments"""

        
        api_path = '/functions/{functionId}/deployments'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def create_deployment(self, function_id, code, activate, entrypoint = None, commands = None, on_progress = None):
        """Create Deployment"""

        
        api_path = '/functions/{functionId}/deployments'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        if activate is None:
            raise AppwriteException('Missing required parameter: "activate"')

        path = path.replace('{functionId}', function_id)

        params['entrypoint'] = entrypoint
        params['commands'] = commands
        params['code'] = str(code).lower() if type(code) is bool else code
        params['activate'] = str(activate).lower() if type(activate) is bool else activate

        param_name = 'code'


        upload_id = ''

        return self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, params, param_name, on_progress, upload_id)

    def get_deployment(self, function_id, deployment_id):
        """Get Deployment"""

        
        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def update_deployment(self, function_id, deployment_id):
        """Update Function Deployment"""

        
        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, params)

    def delete_deployment(self, function_id, deployment_id):
        """Delete Deployment"""

        
        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, params)

    def create_build(self, function_id, deployment_id, build_id):
        """Create Build"""

        
        api_path = '/functions/{functionId}/deployments/{deploymentId}/builds/{buildId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        if build_id is None:
            raise AppwriteException('Missing required parameter: "build_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)
        path = path.replace('{buildId}', build_id)


        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, params)

    def download_deployment(self, function_id, deployment_id):
        """Download Deployment"""

        
        api_path = '/functions/{functionId}/deployments/{deploymentId}/download'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_executions(self, function_id, queries = None, search = None):
        """List Executions"""

        
        api_path = '/functions/{functionId}/executions'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def create_execution(self, function_id, body = None, xasync = None, path = None, method = None, headers = None):
        """Create Execution"""

        
        api_path = '/functions/{functionId}/executions'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)

        params['body'] = body
        params['async'] = xasync
        params['path'] = path
        params['method'] = method
        params['headers'] = headers

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_execution(self, function_id, execution_id):
        """Get Execution"""

        
        api_path = '/functions/{functionId}/executions/{executionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise AppwriteException('Missing required parameter: "execution_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{executionId}', execution_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_variables(self, function_id):
        """List Variables"""

        
        api_path = '/functions/{functionId}/variables'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def create_variable(self, function_id, key, value):
        """Create Variable"""

        
        api_path = '/functions/{functionId}/variables'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if value is None:
            raise AppwriteException('Missing required parameter: "value"')

        path = path.replace('{functionId}', function_id)

        params['key'] = key
        params['value'] = value

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_variable(self, function_id, variable_id):
        """Get Variable"""

        
        api_path = '/functions/{functionId}/variables/{variableId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{variableId}', variable_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def update_variable(self, function_id, variable_id, key, value = None):
        """Update Variable"""

        
        api_path = '/functions/{functionId}/variables/{variableId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{variableId}', variable_id)

        params['key'] = key
        params['value'] = value

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, params)

    def delete_variable(self, function_id, variable_id):
        """Delete Variable"""

        
        api_path = '/functions/{functionId}/variables/{variableId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{variableId}', variable_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, params)
