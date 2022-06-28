from ..service import Service
from ..exception import AppwriteException

class Databases(Service):

    def __init__(self, client, database_id):
        super(Databases, self).__init__(client)
        self.database_id = database_id

    def list(self, search = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_type = None):
        """List Databases"""

        params = {}
        path = '/databases'

        params['search'] = search
        params['limit'] = limit
        params['offset'] = offset
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction
        params['orderType'] = order_type

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create(self, name):
        """Create Database"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        params = {}
        path = '/databases'

        params['databaseId'] = self.database_id
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get(self, ):
        """Get Database"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        params = {}
        path = '/databases/{databaseId}'
        path = path.replace('{databaseId}', self.database_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update(self, name):
        """Update Database"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        params = {}
        path = '/databases/{databaseId}'
        path = path.replace('{databaseId}', self.database_id)

        params['name'] = name

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete(self, ):
        """Delete Database"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        params = {}
        path = '/databases/{databaseId}'
        path = path.replace('{databaseId}', self.database_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_collections(self, search = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_type = None):
        """List Collections"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        params = {}
        path = '/databases/{databaseId}/collections'
        path = path.replace('{databaseId}', self.database_id)

        params['search'] = search
        params['limit'] = limit
        params['offset'] = offset
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction
        params['orderType'] = order_type

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_collection(self, collection_id, name, permission, read, write):
        """Create Collection"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if permission is None:
            raise AppwriteException('Missing required parameter: "permission"')

        if read is None:
            raise AppwriteException('Missing required parameter: "read"')

        if write is None:
            raise AppwriteException('Missing required parameter: "write"')

        params = {}
        path = '/databases/{databaseId}/collections'
        path = path.replace('{databaseId}', self.database_id)

        params['collectionId'] = collection_id
        params['name'] = name
        params['permission'] = permission
        params['read'] = read
        params['write'] = write

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_collection(self, collection_id):
        """Get Collection"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_collection(self, collection_id, name, permission, read = None, write = None, enabled = None):
        """Update Collection"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if permission is None:
            raise AppwriteException('Missing required parameter: "permission"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['name'] = name
        params['permission'] = permission
        params['read'] = read
        params['write'] = write
        params['enabled'] = enabled

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_collection(self, collection_id):
        """Delete Collection"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_attributes(self, collection_id):
        """List Attributes"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_boolean_attribute(self, collection_id, key, required, default = None, array = None):
        """Create Boolean Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/boolean'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_email_attribute(self, collection_id, key, required, default = None, array = None):
        """Create Email Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/email'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_enum_attribute(self, collection_id, key, elements, required, default = None, array = None):
        """Create Enum Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None:
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/enum'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['elements'] = elements
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_float_attribute(self, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create Float Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/float'
        path = path.replace('{databaseId}', self.database_id)
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

    def create_integer_attribute(self, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create Integer Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/integer'
        path = path.replace('{databaseId}', self.database_id)
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

    def create_ip_attribute(self, collection_id, key, required, default = None, array = None):
        """Create IP Address Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/ip'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_string_attribute(self, collection_id, key, size, required, default = None, array = None):
        """Create String Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if size is None:
            raise AppwriteException('Missing required parameter: "size"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/string'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['size'] = size
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_url_attribute(self, collection_id, key, required, default = None, array = None):
        """Create URL Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/url'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['required'] = required
        params['default'] = default
        params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_attribute(self, collection_id, key):
        """Get Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_attribute(self, collection_id, key):
        """Delete Attribute"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_documents(self, collection_id, queries = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_attributes = None, order_types = None):
        """List Documents"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/documents'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['queries'] = queries
        params['limit'] = limit
        params['offset'] = offset
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction
        params['orderAttributes'] = order_attributes
        params['orderTypes'] = order_types

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_document(self, collection_id, document_id, data, read = None, write = None):
        """Create Document"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        if data is None:
            raise AppwriteException('Missing required parameter: "data"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/documents'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['documentId'] = document_id
        params['data'] = data
        params['read'] = read
        params['write'] = write

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_document(self, collection_id, document_id):
        """Get Document"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{documentId}', document_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_document(self, collection_id, document_id, data = None, read = None, write = None):
        """Update Document"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{documentId}', document_id)

        params['data'] = data
        params['read'] = read
        params['write'] = write

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def delete_document(self, collection_id, document_id):
        """Delete Document"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{documentId}', document_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_indexes(self, collection_id):
        """List Indexes"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/indexes'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_index(self, collection_id, key, type, attributes, orders = None):
        """Create Index"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if attributes is None:
            raise AppwriteException('Missing required parameter: "attributes"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/indexes'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)

        params['key'] = key
        params['type'] = type
        params['attributes'] = attributes
        params['orders'] = orders

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_index(self, collection_id, key):
        """Get Index"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_index(self, collection_id, key):
        """Delete Index"""

        if self.database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
        path = path.replace('{databaseId}', self.database_id)
        path = path.replace('{collectionId}', collection_id)
        path = path.replace('{key}', key)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)
