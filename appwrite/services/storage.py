from ..service import Service
from ..exception import AppwriteException

class Storage(Service):

    def __init__(self, client):
        super(Storage, self).__init__(client)

    def list_buckets(self, search = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_type = None):
        """List buckets"""

        params = {}
        path = '/storage/buckets'

        params['search'] = search
        params['limit'] = limit
        params['offset'] = offset
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction
        params['orderType'] = order_type

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_bucket(self, bucket_id, name, permission, read = None, write = None, enabled = None, maximum_file_size = None, allowed_file_extensions = None, encryption = None, antivirus = None):
        """Create bucket"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if permission is None:
            raise AppwriteException('Missing required parameter: "permission"')

        params = {}
        path = '/storage/buckets'

        params['bucketId'] = bucket_id
        params['name'] = name
        params['permission'] = permission
        params['read'] = read
        params['write'] = write
        params['enabled'] = enabled
        params['maximumFileSize'] = maximum_file_size
        params['allowedFileExtensions'] = allowed_file_extensions
        params['encryption'] = encryption
        params['antivirus'] = antivirus

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_bucket(self, bucket_id):
        """Get Bucket"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        params = {}
        path = '/storage/buckets/{bucketId}'
        path = path.replace('{bucketId}', bucket_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_bucket(self, bucket_id, name, permission, read = None, write = None, enabled = None, maximum_file_size = None, allowed_file_extensions = None, encryption = None, antivirus = None):
        """Update Bucket"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if permission is None:
            raise AppwriteException('Missing required parameter: "permission"')

        params = {}
        path = '/storage/buckets/{bucketId}'
        path = path.replace('{bucketId}', bucket_id)

        params['name'] = name
        params['permission'] = permission
        params['read'] = read
        params['write'] = write
        params['enabled'] = enabled
        params['maximumFileSize'] = maximum_file_size
        params['allowedFileExtensions'] = allowed_file_extensions
        params['encryption'] = encryption
        params['antivirus'] = antivirus

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_bucket(self, bucket_id):
        """Delete Bucket"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        params = {}
        path = '/storage/buckets/{bucketId}'
        path = path.replace('{bucketId}', bucket_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_files(self, bucket_id, search = None, limit = None, offset = None, cursor = None, cursor_direction = None, order_type = None):
        """List Files"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        params = {}
        path = '/storage/buckets/{bucketId}/files'
        path = path.replace('{bucketId}', bucket_id)

        params['search'] = search
        params['limit'] = limit
        params['offset'] = offset
        params['cursor'] = cursor
        params['cursorDirection'] = cursor_direction
        params['orderType'] = order_type

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_file(self, bucket_id, file_id, file, read = None, write = None, on_progress = None):
        """Create File"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        if file is None:
            raise AppwriteException('Missing required parameter: "file"')

        params = {}
        path = '/storage/buckets/{bucketId}/files'
        path = path.replace('{bucketId}', bucket_id)

        params['fileId'] = file_id
        params['file'] = str(file).lower() if type(file) is bool else file
        params['read'] = read
        params['write'] = write
        param_name = 'file'


        upload_id = ''
        upload_id = file_id

        return self.client.chunked_upload(path, {
            'content-type': 'multipart/form-data',
        }, params, param_name, on_progress, upload_id)

    def get_file(self, bucket_id, file_id):
        """Get File"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        params = {}
        path = '/storage/buckets/{bucketId}/files/{fileId}'
        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_file(self, bucket_id, file_id, read = None, write = None):
        """Update File"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        params = {}
        path = '/storage/buckets/{bucketId}/files/{fileId}'
        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)

        params['read'] = read
        params['write'] = write

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete_file(self, bucket_id, file_id):
        """Delete File"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        params = {}
        path = '/storage/buckets/{bucketId}/files/{fileId}'
        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def get_file_download(self, bucket_id, file_id):
        """Get File for Download"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        params = {}
        path = '/storage/buckets/{bucketId}/files/{fileId}/download'
        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_file_preview(self, bucket_id, file_id, width = None, height = None, gravity = None, quality = None, border_width = None, border_color = None, border_radius = None, opacity = None, rotation = None, background = None, output = None):
        """Get File Preview"""

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        params = {}
        path = '/storage/buckets/{bucketId}/files/{fileId}/preview'
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

        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        params = {}
        path = '/storage/buckets/{bucketId}/files/{fileId}/view'
        path = path.replace('{bucketId}', bucket_id)
        path = path.replace('{fileId}', file_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
