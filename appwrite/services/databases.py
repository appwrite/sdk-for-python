from ..service import Service
from ..exception import AppwriteException

class Databases(Service):

    def __init__(self, client):
        super(Databases, self).__init__(client)

    def list(self, queries = None, search = None):
        """List databases"""

        
        api_path = '/databases'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create(self, database_id, name, enabled = None):
        """Create database"""

        
        api_path = '/databases'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['databaseId'] = database_id
        api_params['name'] = name
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get(self, database_id):
        """Get database"""

        
        api_path = '/databases/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', database_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update(self, database_id, name, enabled = None):
        """Update database"""

        
        api_path = '/databases/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['name'] = name
        api_params['enabled'] = enabled

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, database_id):
        """Delete database"""

        
        api_path = '/databases/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', database_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_collections(self, database_id, queries = None, search = None):
        """List collections"""

        
        api_path = '/databases/{databaseId}/collections'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_collection(self, database_id, collection_id, name, permissions = None, document_security = None, enabled = None):
        """Create collection"""

        
        api_path = '/databases/{databaseId}/collections'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['collectionId'] = collection_id
        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['documentSecurity'] = document_security
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_collection(self, database_id, collection_id):
        """Get collection"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_collection(self, database_id, collection_id, name, permissions = None, document_security = None, enabled = None):
        """Update collection"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['documentSecurity'] = document_security
        api_params['enabled'] = enabled

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_collection(self, database_id, collection_id):
        """Delete collection"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_attributes(self, database_id, collection_id, queries = None):
        """List attributes"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_boolean_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create boolean attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/boolean'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_boolean_attribute(self, database_id, collection_id, key, required, default, new_key = None):
        """Update boolean attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/boolean/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_datetime_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create datetime attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/datetime'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_datetime_attribute(self, database_id, collection_id, key, required, default, new_key = None):
        """Update dateTime attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/datetime/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_email_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create email attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/email'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email_attribute(self, database_id, collection_id, key, required, default, new_key = None):
        """Update email attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/email/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_enum_attribute(self, database_id, collection_id, key, elements, required, default = None, array = None):
        """Create enum attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/enum'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None:
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['elements'] = elements
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_enum_attribute(self, database_id, collection_id, key, elements, required, default, new_key = None):
        """Update enum attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/enum/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None:
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['elements'] = elements
        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_float_attribute(self, database_id, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create float attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/float'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_float_attribute(self, database_id, collection_id, key, required, min, max, default, new_key = None):
        """Update float attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        if min is None:
            raise AppwriteException('Missing required parameter: "min"')

        if max is None:
            raise AppwriteException('Missing required parameter: "max"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_integer_attribute(self, database_id, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create integer attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/integer'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_integer_attribute(self, database_id, collection_id, key, required, min, max, default, new_key = None):
        """Update integer attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/integer/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        if min is None:
            raise AppwriteException('Missing required parameter: "min"')

        if max is None:
            raise AppwriteException('Missing required parameter: "max"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_ip_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create IP address attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/ip'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_ip_attribute(self, database_id, collection_id, key, required, default, new_key = None):
        """Update IP address attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/ip/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_relationship_attribute(self, database_id, collection_id, related_collection_id, type, two_way = None, key = None, two_way_key = None, on_delete = None):
        """Create relationship attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/relationship'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if related_collection_id is None:
            raise AppwriteException('Missing required parameter: "related_collection_id"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['relatedCollectionId'] = related_collection_id
        api_params['type'] = type
        api_params['twoWay'] = two_way
        api_params['key'] = key
        api_params['twoWayKey'] = two_way_key
        api_params['onDelete'] = on_delete

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_string_attribute(self, database_id, collection_id, key, size, required, default = None, array = None, encrypt = None):
        """Create string attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/string'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if size is None:
            raise AppwriteException('Missing required parameter: "size"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['size'] = size
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array
        api_params['encrypt'] = encrypt

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_string_attribute(self, database_id, collection_id, key, required, default, size = None, new_key = None):
        """Update string attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/string/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['size'] = size
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_url_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create URL attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/url'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_url_attribute(self, database_id, collection_id, key, required, default, new_key = None):
        """Update URL attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/url/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_attribute(self, database_id, collection_id, key):
        """Get attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_attribute(self, database_id, collection_id, key):
        """Delete attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_relationship_attribute(self, database_id, collection_id, key, on_delete = None, new_key = None):
        """Update relationship attribute"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}/relationship'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['onDelete'] = on_delete
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_documents(self, database_id, collection_id, queries = None):
        """List documents"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_document(self, database_id, collection_id, document_id, data, permissions = None):
        """Create document"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        if data is None:
            raise AppwriteException('Missing required parameter: "data"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['documentId'] = document_id
        api_params['data'] = data
        api_params['permissions'] = permissions

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_document(self, database_id, collection_id, document_id, queries = None):
        """Get document"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_document(self, database_id, collection_id, document_id, data = None, permissions = None):
        """Update document"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)

        api_params['data'] = data
        api_params['permissions'] = permissions

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_document(self, database_id, collection_id, document_id):
        """Delete document"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_indexes(self, database_id, collection_id, queries = None):
        """List indexes"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_index(self, database_id, collection_id, key, type, attributes, orders = None):
        """Create index"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if attributes is None:
            raise AppwriteException('Missing required parameter: "attributes"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['type'] = type
        api_params['attributes'] = attributes
        api_params['orders'] = orders

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_index(self, database_id, collection_id, key):
        """Get index"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_index(self, database_id, collection_id, key):
        """Delete index"""

        
        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)
