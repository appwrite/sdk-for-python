from ..service import Service
from ..exception import AppwriteException

class Functions(Service):

    def __init__(self, client):
        super(Functions, self).__init__(client)

    def list(self, queries = None, search = None):
        """List Functions"""

        
        path = '/functions'
        params = {}

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create(self, function_id, name, execute, runtime, events = None, schedule = None, timeout = None, enabled = None):
        """Create Function"""

        
        path = '/functions'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if execute is None:
            raise AppwriteException('Missing required parameter: "execute"')

        if runtime is None:
            raise AppwriteException('Missing required parameter: "runtime"')


        params['functionId'] = function_id
        params['name'] = name
        params['execute'] = execute
        params['runtime'] = runtime
        params['events'] = events
        params['schedule'] = schedule
        params['timeout'] = timeout
        params['enabled'] = enabled

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def list_runtimes(self):
        """List runtimes"""

        
        path = '/functions/runtimes'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get(self, function_id):
        """Get Function"""

        
        path = '/functions/{functionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update(self, function_id, name, execute, events = None, schedule = None, timeout = None, enabled = None):
        """Update Function"""

        
        path = '/functions/{functionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if execute is None:
            raise AppwriteException('Missing required parameter: "execute"')

        path = path.replace('{functionId}', function_id)

        params['name'] = name
        params['execute'] = execute
        params['events'] = events
        params['schedule'] = schedule
        params['timeout'] = timeout
        params['enabled'] = enabled

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete(self, function_id):
        """Delete Function"""

        
        path = '/functions/{functionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_deployments(self, function_id, queries = None, search = None):
        """List Deployments"""

        
        path = '/functions/{functionId}/deployments'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_deployment(self, function_id, entrypoint, code, activate, on_progress = None):
        """Create Deployment"""

        
        path = '/functions/{functionId}/deployments'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if entrypoint is None:
            raise AppwriteException('Missing required parameter: "entrypoint"')

        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        if activate is None:
            raise AppwriteException('Missing required parameter: "activate"')

        path = path.replace('{functionId}', function_id)

        params['entrypoint'] = entrypoint
        params['code'] = str(code).lower() if type(code) is bool else code
        params['activate'] = str(activate).lower() if type(activate) is bool else activate

        param_name = 'code'


        upload_id = ''

        return self.client.chunked_upload(path, {
            'content-type': 'multipart/form-data',
        }, params, param_name, on_progress, upload_id)

    def get_deployment(self, function_id, deployment_id):
        """Get Deployment"""

        
        path = '/functions/{functionId}/deployments/{deploymentId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_deployment(self, function_id, deployment_id):
        """Update Function Deployment"""

        
        path = '/functions/{functionId}/deployments/{deploymentId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def delete_deployment(self, function_id, deployment_id):
        """Delete Deployment"""

        
        path = '/functions/{functionId}/deployments/{deploymentId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def retry_build(self, function_id, deployment_id, build_id):
        """Retry Build"""

        
        path = '/functions/{functionId}/deployments/{deploymentId}/builds/{buildId}'
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


        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def list_executions(self, function_id, queries = None, search = None):
        """List Executions"""

        
        path = '/functions/{functionId}/executions'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_execution(self, function_id, data = None, xasync = None):
        """Create Execution"""

        
        path = '/functions/{functionId}/executions'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)

        params['data'] = data
        params['async'] = xasync

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_execution(self, function_id, execution_id):
        """Get Execution"""

        
        path = '/functions/{functionId}/executions/{executionId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise AppwriteException('Missing required parameter: "execution_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{executionId}', execution_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def list_variables(self, function_id):
        """List Variables"""

        
        path = '/functions/{functionId}/variables'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        path = path.replace('{functionId}', function_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_variable(self, function_id, key, value):
        """Create Variable"""

        
        path = '/functions/{functionId}/variables'
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

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_variable(self, function_id, variable_id):
        """Get Variable"""

        
        path = '/functions/{functionId}/variables/{variableId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{variableId}', variable_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_variable(self, function_id, variable_id, key, value = None):
        """Update Variable"""

        
        path = '/functions/{functionId}/variables/{variableId}'
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

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_variable(self, function_id, variable_id):
        """Delete Variable"""

        
        path = '/functions/{functionId}/variables/{variableId}'
        params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        path = path.replace('{functionId}', function_id)
        path = path.replace('{variableId}', variable_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)
