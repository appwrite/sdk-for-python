from ..service import Service
from ..exception import AppwriteException

class Databases(Service):

    def __init__(self, client):
        super(Databases, self).__init__(client)

    def list(self, queries = None, search = None):
        """List Databases"""

        
        path = '/databases'
        params = {}

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create(self, database_id, name):
        """Create Database"""

        
        path = '/databases'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        params['databaseId'] = database_id
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get(self, database_id):
        """Get Database"""

        
        path = '/databases/{databaseId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        path = path.replace('{databaseId}', database_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update(self, database_id, name):
        """Update Database"""

        
        path = '/databases/{databaseId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        path = path.replace('{databaseId}', database_id)

        params['name'] = name

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete(self, database_id):
        """Delete Database"""

        
        path = '/databases/{databaseId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        path = path.replace('{databaseId}', database_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_collections(self, database_id, queries = None, search = None):
        """List Collections"""

        
        path = '/databases/{databaseId}/collections'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        path = path.replace('{databaseId}', database_id)

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_collection(self, database_id, collection_id, name, permissions = None, document_security = None):
        """Create Collection"""

        
        path = '/databases/{databaseId}/collections'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        path = path.replace('{databaseId}', database_id)

        params['collectionId'] = collection_id
        params['name'] = name
        params['permissions'] = permissions
        params['documentSecurity'] = document_security

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_collection(self, database_id, collection_id):
        """Get Collection"""

        
        path = '/databases/{databaseId}/collections/{collectionId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_collection(self, database_id, collection_id, name, permissions = None, document_security = None, enabled = None):
        """Update Collection"""

        
        path = '/databases/{databaseId}/collections/{collectionId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['name'] = name
        params['permissions'] = permissions
        params['documentSecurity'] = document_security
        params['enabled'] = enabled

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_collection(self, database_id, collection_id):
        """Delete Collection"""

        
        path = '/databases/{databaseId}/collections/{collectionId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_attributes(self, database_id, collection_id):
        """List Attributes"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_boolean_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create Boolean Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/boolean'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_datetime_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create DateTime Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/datetime'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_email_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create Email Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/email'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_enum_attribute(self, database_id, collection_id, key, elements, required, default = None, array = None):
        """Create Enum Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/enum'
        params = {}
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

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['elements'] = elements
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_float_attribute(self, database_id, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create Float Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/float'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['min'] = min
        params['max'] = max
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_integer_attribute(self, database_id, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create Integer Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/integer'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['min'] = min
        params['max'] = max
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_ip_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create IP Address Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/ip'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_string_attribute(self, database_id, collection_id, key, size, required, default = None, array = None):
        """Create String Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/string'
        params = {}
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

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['size'] = size
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_url_attribute(self, database_id, collection_id, key, required, default = None, array = None):
        """Create URL Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/url'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_attribute(self, database_id, collection_id, key):
        """Get Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_attribute(self, database_id, collection_id, key):
        """Delete Attribute"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_documents(self, database_id, collection_id, queries = None):
        """List Documents"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/documents'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['queries'] = queries

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_document(self, database_id, collection_id, document_id, data, permissions = None):
        """Create Document"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/documents'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        if data is None:
            raise AppwriteException('Missing required parameter: "data"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['documentId'] = document_id
        params['data'] = data
        params['permissions'] = permissions

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_document(self, database_id, collection_id, document_id):
        """Get Document"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{documentId}', document_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_document(self, database_id, collection_id, document_id, data = None, permissions = None):
        """Update Document"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{documentId}', document_id)

        params['data'] = data
        params['permissions'] = permissions

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def delete_document(self, database_id, collection_id, document_id):
        """Delete Document"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{documentId}', document_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_indexes(self, database_id, collection_id):
        """List Indexes"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/indexes'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_index(self, database_id, collection_id, key, type, attributes, orders = None):
        """Create Index"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/indexes'
        params = {}
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

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['type'] = type
        params['attributes'] = attributes
        params['orders'] = orders

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_index(self, database_id, collection_id, key):
        """Get Index"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_index(self, database_id, collection_id, key):
        """Delete Index"""

        
        path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
        params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        path = path.replace('{databaseId}', database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)
