from ..service import Service
from ..exception import AppwriteException

class Storage(Service):

    def __init__(self, client):
        super(Storage, self).__init__(client)

    def list_buckets(self, queries = None, search = None):
        """List buckets"""

        
        path = '/storage/buckets'
        params = {}

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_bucket(self, bucket_id, name, permissions = None, file_security = None, enabled = None, maximum_file_size = None, allowed_file_extensions = None, compression = None, encryption = None, antivirus = None):
        """Create bucket"""

        
        path = '/storage/buckets'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        params['bucketId'] = bucket_id
        params['name'] = name
        params['permissions'] = permissions
        params['fileSecurity'] = file_security
        params['enabled'] = enabled
        params['maximumFileSize'] = maximum_file_size
        params['allowedFileExtensions'] = allowed_file_extensions
        params['compression'] = compression
        params['encryption'] = encryption
        params['antivirus'] = antivirus

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_bucket(self, bucket_id):
        """Get Bucket"""

        
        path = '/storage/buckets/{bucketId}'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        path = path.replace('{bucketId}', bucket_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_bucket(self, bucket_id, name, permissions = None, file_security = None, enabled = None, maximum_file_size = None, allowed_file_extensions = None, compression = None, encryption = None, antivirus = None):
        """Update Bucket"""

        
        path = '/storage/buckets/{bucketId}'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        path = path.replace('{bucketId}', bucket_id)

        params['name'] = name
        params['permissions'] = permissions
        params['fileSecurity'] = file_security
        params['enabled'] = enabled
        params['maximumFileSize'] = maximum_file_size
        params['allowedFileExtensions'] = allowed_file_extensions
        params['compression'] = compression
        params['encryption'] = encryption
        params['antivirus'] = antivirus

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_bucket(self, bucket_id):
        """Delete Bucket"""

        
        path = '/storage/buckets/{bucketId}'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        path = path.replace('{bucketId}', bucket_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_files(self, bucket_id, queries = None, search = None):
        """List Files"""

        
        path = '/storage/buckets/{bucketId}/files'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        path = path.replace('{bucketId}', bucket_id)

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_file(self, bucket_id, file_id, file, permissions = None, on_progress = None):
        """Create File"""

        
        path = '/storage/buckets/{bucketId}/files'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        if file is None:
            raise AppwriteException('Missing required parameter: "file"')

        path = path.replace('{bucketId}', bucket_id)

        params['fileId'] = file_id
        params['file'] = str(file).lower() if type(file) is bool else file
        params['permissions'] = permissions

        param_name = 'file'


        upload_id = ''
        upload_id = file_id

        return self.client.chunked_upload(path, {
            'content-type': 'multipart/form-data',
        }, params, param_name, on_progress, upload_id)

    def get_file(self, bucket_id, file_id):
        """Get File"""

        
        path = '/storage/buckets/{bucketId}/files/{fileId}'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_file(self, bucket_id, file_id, permissions = None):
        """Update File"""

        
        path = '/storage/buckets/{bucketId}/files/{fileId}'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)

        params['permissions'] = permissions

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_file(self, bucket_id, file_id):
        """Delete File"""

        
        path = '/storage/buckets/{bucketId}/files/{fileId}'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def get_file_download(self, bucket_id, file_id):
        """Get File for Download"""

        
        path = '/storage/buckets/{bucketId}/files/{fileId}/download'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_file_preview(self, bucket_id, file_id, width = None, height = None, gravity = None, quality = None, border_width = None, border_color = None, border_radius = None, opacity = None, rotation = None, background = None, output = None):
        """Get File Preview"""

        
        path = '/storage/buckets/{bucketId}/files/{fileId}/preview'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)

        params['width'] = width
        params['height'] = height
        params['gravity'] = gravity
        params['quality'] = quality
        params['borderWidth'] = border_width
        params['borderColor'] = border_color
        params['borderRadius'] = border_radius
        params['opacity'] = opacity
        params['rotation'] = rotation
        params['background'] = background
        params['output'] = output

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_file_view(self, bucket_id, file_id):
        """Get File for View"""

        
        path = '/storage/buckets/{bucketId}/files/{fileId}/view'
        params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
