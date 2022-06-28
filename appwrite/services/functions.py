from ..service import Service
from ..exception import AppwriteException

class Functions(Service):

    def __init__(self, client):
        super(Functions, self).__init__(client)

    def list(self, search = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_type = None):
        """List Functions"""

        params = {}
        path = '/functions'

        params['search'] = search
        params['limit'] = limit
        params['offset'] = offset
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction
        params['orderType'] = order_type

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create(self, function_id, name, execute, runtime, vars = None, events = None, schedule = None, timeout = None):
        """Create Function"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if execute is None:
            raise AppwriteException('Missing required parameter: "execute"')

        if runtime is None:
            raise AppwriteException('Missing required parameter: "runtime"')

        params = {}
        path = '/functions'

        params['functionId'] = function_id
        params['name'] = name
        params['execute'] = execute
        params['runtime'] = runtime
        params['vars'] = vars
        params['events'] = events
        params['schedule'] = schedule
        params['timeout'] = timeout

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def list_runtimes(self):
        """List runtimes"""

        params = {}
        path = '/functions/runtimes'


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get(self, function_id):
        """Get Function"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        params = {}
        path = '/functions/{functionId}'
        path = path.replace('{functionId}', function_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update(self, function_id, name, execute, vars = None, events = None, schedule = None, timeout = None):
        """Update Function"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if execute is None:
            raise AppwriteException('Missing required parameter: "execute"')

        params = {}
        path = '/functions/{functionId}'
        path = path.replace('{functionId}', function_id)

        params['name'] = name
        params['execute'] = execute
        params['vars'] = vars
        params['events'] = events
        params['schedule'] = schedule
        params['timeout'] = timeout

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete(self, function_id):
        """Delete Function"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        params = {}
        path = '/functions/{functionId}'
        path = path.replace('{functionId}', function_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_deployments(self, function_id, search = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_type = None):
        """List Deployments"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        params = {}
        path = '/functions/{functionId}/deployments'
        path = path.replace('{functionId}', function_id)

        params['search'] = search
        params['limit'] = limit
        params['offset'] = offset
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction
        params['orderType'] = order_type

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_deployment(self, function_id, entrypoint, code, activate, on_progress = None):
        """Create Deployment"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if entrypoint is None:
            raise AppwriteException('Missing required parameter: "entrypoint"')

        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        if activate is None:
            raise AppwriteException('Missing required parameter: "activate"')

        params = {}
        path = '/functions/{functionId}/deployments'
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

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        params = {}
        path = '/functions/{functionId}/deployments/{deploymentId}'
        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_deployment(self, function_id, deployment_id):
        """Update Function Deployment"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        params = {}
        path = '/functions/{functionId}/deployments/{deploymentId}'
        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def delete_deployment(self, function_id, deployment_id):
        """Delete Deployment"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        params = {}
        path = '/functions/{functionId}/deployments/{deploymentId}'
        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def retry_build(self, function_id, deployment_id, build_id):
        """Retry Build"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        if build_id is None:
            raise AppwriteException('Missing required parameter: "build_id"')

        params = {}
        path = '/functions/{functionId}/deployments/{deploymentId}/builds/{buildId}'
        path = path.replace('{functionId}', function_id)
        path = path.replace('{deploymentId}', deployment_id)
        path = path.replace('{buildId}', build_id)


        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def list_executions(self, function_id, limit = None, offset = None, search = None, cursor = None, cursor_direction = None):
        """List Executions"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        params = {}
        path = '/functions/{functionId}/executions'
        path = path.replace('{functionId}', function_id)

        params['limit'] = limit
        params['offset'] = offset
        params['search'] = search
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_execution(self, function_id, data = None, xasync = None):
        """Create Execution"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        params = {}
        path = '/functions/{functionId}/executions'
        path = path.replace('{functionId}', function_id)

        params['data'] = data
        params['async'] = xasync

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_execution(self, function_id, execution_id):
        """Get Execution"""

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise AppwriteException('Missing required parameter: "execution_id"')

        params = {}
        path = '/functions/{functionId}/executions/{executionId}'
        path = path.replace('{functionId}', function_id)
        path = path.replace('{executionId}', execution_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
