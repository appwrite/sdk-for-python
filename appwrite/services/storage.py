from ..service import Service
from ..exception import AppwriteException

class Storage(Service):

    def __init__(self, client):
        super(Storage, self).__init__(client)

    def list_buckets(self, queries = None, search = None):
        """List buckets"""

        
        api_path = '/storage/buckets'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_bucket(self, bucket_id, name, permissions = None, file_security = None, enabled = None, maximum_file_size = None, allowed_file_extensions = None, compression = None, encryption = None, antivirus = None):
        """Create bucket"""

        
        api_path = '/storage/buckets'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['bucketId'] = bucket_id
        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['fileSecurity'] = file_security
        api_params['enabled'] = enabled
        api_params['maximumFileSize'] = maximum_file_size
        api_params['allowedFileExtensions'] = allowed_file_extensions
        api_params['compression'] = compression
        api_params['encryption'] = encryption
        api_params['antivirus'] = antivirus

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_bucket(self, bucket_id):
        """Get bucket"""

        
        api_path = '/storage/buckets/{bucketId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_bucket(self, bucket_id, name, permissions = None, file_security = None, enabled = None, maximum_file_size = None, allowed_file_extensions = None, compression = None, encryption = None, antivirus = None):
        """Update bucket"""

        
        api_path = '/storage/buckets/{bucketId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{bucketId}', bucket_id)

        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['fileSecurity'] = file_security
        api_params['enabled'] = enabled
        api_params['maximumFileSize'] = maximum_file_size
        api_params['allowedFileExtensions'] = allowed_file_extensions
        api_params['compression'] = compression
        api_params['encryption'] = encryption
        api_params['antivirus'] = antivirus

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_bucket(self, bucket_id):
        """Delete bucket"""

        
        api_path = '/storage/buckets/{bucketId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_files(self, bucket_id, queries = None, search = None):
        """List files"""

        
        api_path = '/storage/buckets/{bucketId}/files'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_file(self, bucket_id, file_id, file, permissions = None, on_progress = None):
        """Create file"""

        
        api_path = '/storage/buckets/{bucketId}/files'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        if file is None:
            raise AppwriteException('Missing required parameter: "file"')

        api_path = api_path.replace('{bucketId}', bucket_id)

        api_params['fileId'] = file_id
        api_params['file'] = str(file).lower() if type(file) is bool else file
        api_params['permissions'] = permissions

        param_name = 'file'


        upload_id = ''
        upload_id = file_id

        return self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

    def get_file(self, bucket_id, file_id):
        """Get file"""

        
        api_path = '/storage/buckets/{bucketId}/files/{fileId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_file(self, bucket_id, file_id, name = None, permissions = None):
        """Update file"""

        
        api_path = '/storage/buckets/{bucketId}/files/{fileId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        api_params['name'] = name
        api_params['permissions'] = permissions

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_file(self, bucket_id, file_id):
        """Delete file"""

        
        api_path = '/storage/buckets/{bucketId}/files/{fileId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_file_download(self, bucket_id, file_id):
        """Get file for download"""

        
        api_path = '/storage/buckets/{bucketId}/files/{fileId}/download'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_file_preview(self, bucket_id, file_id, width = None, height = None, gravity = None, quality = None, border_width = None, border_color = None, border_radius = None, opacity = None, rotation = None, background = None, output = None):
        """Get file preview"""

        
        api_path = '/storage/buckets/{bucketId}/files/{fileId}/preview'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        api_params['width'] = width
        api_params['height'] = height
        api_params['gravity'] = gravity
        api_params['quality'] = quality
        api_params['borderWidth'] = border_width
        api_params['borderColor'] = border_color
        api_params['borderRadius'] = border_radius
        api_params['opacity'] = opacity
        api_params['rotation'] = rotation
        api_params['background'] = background
        api_params['output'] = output

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_file_view(self, bucket_id, file_id):
        """Get file for view"""

        
        api_path = '/storage/buckets/{bucketId}/files/{fileId}/view'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)
