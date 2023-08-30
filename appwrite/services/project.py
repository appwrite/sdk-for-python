from ..service import Service
from ..exception import AppwriteException

class Project(Service):

    def __init__(self, client):
        super(Project, self).__init__(client)

    def list_variables(self):
        """List Variables"""

        
        api_path = '/project/variables'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def create_variable(self, key, value):
        """Create Variable"""

        
        api_path = '/project/variables'
        params = {}
        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if value is None:
            raise AppwriteException('Missing required parameter: "value"')


        params['key'] = key
        params['value'] = value

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_variable(self, variable_id):
        """Get Variable"""

        
        api_path = '/project/variables/{variableId}'
        params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        path = path.replace('{variableId}', variable_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def update_variable(self, variable_id, key, value = None):
        """Update Variable"""

        
        api_path = '/project/variables/{variableId}'
        params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        path = path.replace('{variableId}', variable_id)

        params['key'] = key
        params['value'] = value

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, params)

    def delete_variable(self, variable_id):
        """Delete Variable"""

        
        api_path = '/project/variables/{variableId}'
        params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        path = path.replace('{variableId}', variable_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, params)
