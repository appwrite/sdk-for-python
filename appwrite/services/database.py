from ..service import Service
from ..exception import AppwriteException

class Database(Service):

    def __init__(self, client):
        super(Database, self).__init__(client)

    def list_collections(self, search = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_type = None):
        """List Collections"""

        params = {}
        path = '/database/collections'

        if search is not None: 
            params['search'] = search

        if limit is not None: 
            params['limit'] = limit

        if offset is not None: 
            params['offset'] = offset

        if cursor is not None: 
            params['cursor'] = cursor

        if cursor_direction is not None: 
            params['cursorDirection'] = cursor_direction

        if order_type is not None: 
            params['orderType'] = order_type

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_collection(self, collection_id, name, permission, read, write):
        """Create Collection"""

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
        path = '/database/collections'

        if collection_id is not None: 
            params['collectionId'] = collection_id

        if name is not None: 
            params['name'] = name

        if permission is not None: 
            params['permission'] = permission

        if read is not None: 
            params['read'] = read

        if write is not None: 
            params['write'] = write

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_collection(self, collection_id):
        """Get Collection"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/database/collections/{collectionId}'
        path = path.replace('{collectionId}', collection_id)                

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_collection(self, collection_id, name, permission, read = None, write = None, enabled = None):
        """Update Collection"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None: 
            raise AppwriteException('Missing required parameter: "name"')

        if permission is None: 
            raise AppwriteException('Missing required parameter: "permission"')

        params = {}
        path = '/database/collections/{collectionId}'
        path = path.replace('{collectionId}', collection_id)                

        if name is not None: 
            params['name'] = name

        if permission is not None: 
            params['permission'] = permission

        if read is not None: 
            params['read'] = read

        if write is not None: 
            params['write'] = write

        if enabled is not None: 
            params['enabled'] = enabled

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_collection(self, collection_id):
        """Delete Collection"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/database/collections/{collectionId}'
        path = path.replace('{collectionId}', collection_id)                

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_attributes(self, collection_id):
        """List Attributes"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/database/collections/{collectionId}/attributes'
        path = path.replace('{collectionId}', collection_id)                

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_boolean_attribute(self, collection_id, key, required, default = None, array = None):
        """Create Boolean Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/boolean'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if required is not None: 
            params['required'] = required

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_email_attribute(self, collection_id, key, required, default = None, array = None):
        """Create Email Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/email'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if required is not None: 
            params['required'] = required

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_enum_attribute(self, collection_id, key, elements, required, default = None, array = None):
        """Create Enum Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None: 
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/enum'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if elements is not None: 
            params['elements'] = elements

        if required is not None: 
            params['required'] = required

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_float_attribute(self, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create Float Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/float'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if required is not None: 
            params['required'] = required

        if min is not None: 
            params['min'] = min

        if max is not None: 
            params['max'] = max

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_integer_attribute(self, collection_id, key, required, min = None, max = None, default = None, array = None):
        """Create Integer Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/integer'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if required is not None: 
            params['required'] = required

        if min is not None: 
            params['min'] = min

        if max is not None: 
            params['max'] = max

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_ip_attribute(self, collection_id, key, required, default = None, array = None):
        """Create IP Address Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/ip'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if required is not None: 
            params['required'] = required

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_string_attribute(self, collection_id, key, size, required, default = None, array = None):
        """Create String Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if size is None: 
            raise AppwriteException('Missing required parameter: "size"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/string'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if size is not None: 
            params['size'] = size

        if required is not None: 
            params['required'] = required

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_url_attribute(self, collection_id, key, required, default = None, array = None):
        """Create URL Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if required is None: 
            raise AppwriteException('Missing required parameter: "required"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/url'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if required is not None: 
            params['required'] = required

        if default is not None: 
            params['default'] = default

        if array is not None: 
            params['array'] = array

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_attribute(self, collection_id, key):
        """Get Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/{key}'
        path = path.replace('{collectionId}', collection_id)                
        path = path.replace('{key}', key)                

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_attribute(self, collection_id, key):
        """Delete Attribute"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/database/collections/{collectionId}/attributes/{key}'
        path = path.replace('{collectionId}', collection_id)                
        path = path.replace('{key}', key)                

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_documents(self, collection_id, queries = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_attributes = None, order_types = None):
        """List Documents"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/database/collections/{collectionId}/documents'
        path = path.replace('{collectionId}', collection_id)                

        if queries is not None: 
            params['queries'] = queries

        if limit is not None: 
            params['limit'] = limit

        if offset is not None: 
            params['offset'] = offset

        if cursor is not None: 
            params['cursor'] = cursor

        if cursor_direction is not None: 
            params['cursorDirection'] = cursor_direction

        if order_attributes is not None: 
            params['orderAttributes'] = order_attributes

        if order_types is not None: 
            params['orderTypes'] = order_types

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_document(self, collection_id, document_id, data, read = None, write = None):
        """Create Document"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None: 
            raise AppwriteException('Missing required parameter: "document_id"')

        if data is None: 
            raise AppwriteException('Missing required parameter: "data"')

        params = {}
        path = '/database/collections/{collectionId}/documents'
        path = path.replace('{collectionId}', collection_id)                

        if document_id is not None: 
            params['documentId'] = document_id

        if data is not None: 
            params['data'] = data

        if read is not None: 
            params['read'] = read

        if write is not None: 
            params['write'] = write

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_document(self, collection_id, document_id):
        """Get Document"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None: 
            raise AppwriteException('Missing required parameter: "document_id"')

        params = {}
        path = '/database/collections/{collectionId}/documents/{documentId}'
        path = path.replace('{collectionId}', collection_id)                
        path = path.replace('{documentId}', document_id)                

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_document(self, collection_id, document_id, data, read = None, write = None):
        """Update Document"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None: 
            raise AppwriteException('Missing required parameter: "document_id"')

        if data is None: 
            raise AppwriteException('Missing required parameter: "data"')

        params = {}
        path = '/database/collections/{collectionId}/documents/{documentId}'
        path = path.replace('{collectionId}', collection_id)                
        path = path.replace('{documentId}', document_id)                

        if data is not None: 
            params['data'] = data

        if read is not None: 
            params['read'] = read

        if write is not None: 
            params['write'] = write

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def delete_document(self, collection_id, document_id):
        """Delete Document"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None: 
            raise AppwriteException('Missing required parameter: "document_id"')

        params = {}
        path = '/database/collections/{collectionId}/documents/{documentId}'
        path = path.replace('{collectionId}', collection_id)                
        path = path.replace('{documentId}', document_id)                

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_indexes(self, collection_id):
        """List Indexes"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        params = {}
        path = '/database/collections/{collectionId}/indexes'
        path = path.replace('{collectionId}', collection_id)                

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_index(self, collection_id, key, type, attributes, orders = None):
        """Create Index"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        if type is None: 
            raise AppwriteException('Missing required parameter: "type"')

        if attributes is None: 
            raise AppwriteException('Missing required parameter: "attributes"')

        params = {}
        path = '/database/collections/{collectionId}/indexes'
        path = path.replace('{collectionId}', collection_id)                

        if key is not None: 
            params['key'] = key

        if type is not None: 
            params['type'] = type

        if attributes is not None: 
            params['attributes'] = attributes

        if orders is not None: 
            params['orders'] = orders

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_index(self, collection_id, key):
        """Get Index"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/database/collections/{collectionId}/indexes/{key}'
        path = path.replace('{collectionId}', collection_id)                
        path = path.replace('{key}', key)                

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_index(self, collection_id, key):
        """Delete Index"""

        if collection_id is None: 
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None: 
            raise AppwriteException('Missing required parameter: "key"')

        params = {}
        path = '/database/collections/{collectionId}/indexes/{key}'
        path = path.replace('{collectionId}', collection_id)                
        path = path.replace('{key}', key)                

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)
