from ..service import Service
from typing import List, Dict, Any, Optional
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.compression import Compression;
from ..input_file import InputFile
from ..enums.image_gravity import ImageGravity;
from ..enums.image_format import ImageFormat;

class Storage(Service):

    def __init__(self, client) -> None:
        super(Storage, self).__init__(client)

    def list_buckets(self, queries: Optional[List[str]] = None, search: Optional[str] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all the storage buckets. You can use the query params to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: enabled, name, fileSecurity, maximumFileSize, encryption, antivirus, transformations
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets'
        api_params = {}

        if queries is not None:
            api_params['queries'] = queries
        if search is not None:
            api_params['search'] = search
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def create_bucket(self, bucket_id: str, name: str, permissions: Optional[List[str]] = None, file_security: Optional[bool] = None, enabled: Optional[bool] = None, maximum_file_size: Optional[float] = None, allowed_file_extensions: Optional[List[str]] = None, compression: Optional[Compression] = None, encryption: Optional[bool] = None, antivirus: Optional[bool] = None, transformations: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a new storage bucket.

        Parameters
        ----------
        bucket_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Bucket name
        permissions : Optional[List[str]]
            An array of permission strings. By default, no user is granted with any permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        file_security : Optional[bool]
            Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.
        maximum_file_size : Optional[float]
            Maximum file size allowed in bytes. Maximum allowed value is 5GB.
        allowed_file_extensions : Optional[List[str]]
            Allowed file extensions. Maximum of 100 extensions are allowed, each 64 characters long.
        compression : Optional[Compression]
            Compression algorithm chosen for compression. Can be one of none,  [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled
        encryption : Optional[bool]
            Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled
        antivirus : Optional[bool]
            Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled
        transformations : Optional[bool]
            Are image transformations enabled?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['bucketId'] = bucket_id
        api_params['name'] = name
        api_params['permissions'] = permissions
        if file_security is not None:
            api_params['fileSecurity'] = file_security
        if enabled is not None:
            api_params['enabled'] = enabled
        if maximum_file_size is not None:
            api_params['maximumFileSize'] = maximum_file_size
        if allowed_file_extensions is not None:
            api_params['allowedFileExtensions'] = allowed_file_extensions
        if compression is not None:
            api_params['compression'] = compression
        if encryption is not None:
            api_params['encryption'] = encryption
        if antivirus is not None:
            api_params['antivirus'] = antivirus
        if transformations is not None:
            api_params['transformations'] = transformations

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_bucket(self, bucket_id: str) -> Dict[str, Any]:
        """
        Get a storage bucket by its unique ID. This endpoint response returns a JSON object with the storage bucket metadata.

        Parameters
        ----------
        bucket_id : str
            Bucket unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_bucket(self, bucket_id: str, name: str, permissions: Optional[List[str]] = None, file_security: Optional[bool] = None, enabled: Optional[bool] = None, maximum_file_size: Optional[float] = None, allowed_file_extensions: Optional[List[str]] = None, compression: Optional[Compression] = None, encryption: Optional[bool] = None, antivirus: Optional[bool] = None, transformations: Optional[bool] = None) -> Dict[str, Any]:
        """
        Update a storage bucket by its unique ID.

        Parameters
        ----------
        bucket_id : str
            Bucket unique ID.
        name : str
            Bucket name
        permissions : Optional[List[str]]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        file_security : Optional[bool]
            Enables configuring permissions for individual file. A user needs one of file or bucket level permissions to access a file. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is bucket enabled? When set to 'disabled', users cannot access the files in this bucket but Server SDKs with and API key can still access the bucket. No files are lost when this is toggled.
        maximum_file_size : Optional[float]
            Maximum file size allowed in bytes. Maximum allowed value is 5GB.
        allowed_file_extensions : Optional[List[str]]
            Allowed file extensions. Maximum of 100 extensions are allowed, each 64 characters long.
        compression : Optional[Compression]
            Compression algorithm chosen for compression. Can be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd), For file size above 20MB compression is skipped even if it's enabled
        encryption : Optional[bool]
            Is encryption enabled? For file size above 20MB encryption is skipped even if it's enabled
        antivirus : Optional[bool]
            Is virus scanning enabled? For file size above 20MB AntiVirus scanning is skipped even if it's enabled
        transformations : Optional[bool]
            Are image transformations enabled?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{bucketId}', bucket_id)

        api_params['name'] = name
        api_params['permissions'] = permissions
        if file_security is not None:
            api_params['fileSecurity'] = file_security
        if enabled is not None:
            api_params['enabled'] = enabled
        if maximum_file_size is not None:
            api_params['maximumFileSize'] = maximum_file_size
        if allowed_file_extensions is not None:
            api_params['allowedFileExtensions'] = allowed_file_extensions
        if compression is not None:
            api_params['compression'] = compression
        if encryption is not None:
            api_params['encryption'] = encryption
        if antivirus is not None:
            api_params['antivirus'] = antivirus
        if transformations is not None:
            api_params['transformations'] = transformations

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_bucket(self, bucket_id: str) -> Dict[str, Any]:
        """
        Delete a storage bucket by its unique ID.

        Parameters
        ----------
        bucket_id : str
            Bucket unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_files(self, bucket_id: str, queries: Optional[List[str]] = None, search: Optional[str] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all the user files. You can use the query params to filter your results.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, signature, mimeType, sizeOriginal, chunksTotal, chunksUploaded
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}/files'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)

        if queries is not None:
            api_params['queries'] = queries
        if search is not None:
            api_params['search'] = search
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def create_file(self, bucket_id: str, file_id: str, file: InputFile, permissions: Optional[List[str]] = None, on_progress = None) -> Dict[str, Any]:
        """
        Create a new file. Before using this route, you should create a new bucket resource using either a [server integration](https://appwrite.io/docs/server/storage#storageCreateBucket) API or directly from your Appwrite console.
        
        Larger files should be uploaded using multiple requests with the [content-range](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Range) header to send a partial request with a maximum supported chunk of `5MB`. The `content-range` header values should always be in bytes.
        
        When the first request is sent, the server will return the **File** object, and the subsequent part request must include the file's **id** in `x-appwrite-id` header to allow the server to know that the partial upload is for the existing file and not for a new one.
        
        If you're creating a new file using one of the Appwrite SDKs, all the chunking logic will be managed by the SDK internally.
        

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        file : InputFile
            Binary file. Appwrite SDKs provide helpers to handle file input. [Learn about file input](https://appwrite.io/docs/products/storage/upload-download#input-file).
        permissions : Optional[List[str]]
            An array of permission strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
                on_progress : callable, optional
            Optional callback for upload progress
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

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
        api_params['file'] = file
        if permissions is not None:
            api_params['permissions'] = permissions

        param_name = 'file'


        upload_id = ''
        upload_id = file_id

        return self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

    def get_file(self, bucket_id: str, file_id: str) -> Dict[str, Any]:
        """
        Get a file by its unique ID. This endpoint response returns a JSON object with the file metadata.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}/files/{fileId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_file(self, bucket_id: str, file_id: str, name: Optional[str] = None, permissions: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Update a file by its unique ID. Only users with write permissions have access to update this resource.

        Parameters
        ----------
        bucket_id : str
            Bucket unique ID.
        file_id : str
            File ID.
        name : Optional[str]
            File name.
        permissions : Optional[List[str]]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}/files/{fileId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        if name is not None:
            api_params['name'] = name
        api_params['permissions'] = permissions

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_file(self, bucket_id: str, file_id: str) -> Dict[str, Any]:
        """
        Delete a file by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

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

    def get_file_download(self, bucket_id: str, file_id: str, token: Optional[str] = None) -> bytes:
        """
        Get a file content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        bucket_id : str
            Storage bucket ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID.
        token : Optional[str]
            File token for accessing this file.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}/files/{fileId}/download'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        if token is not None:
            api_params['token'] = token

        return self.client.call('get', api_path, {
        }, api_params)

    def get_file_preview(self, bucket_id: str, file_id: str, width: Optional[float] = None, height: Optional[float] = None, gravity: Optional[ImageGravity] = None, quality: Optional[float] = None, border_width: Optional[float] = None, border_color: Optional[str] = None, border_radius: Optional[float] = None, opacity: Optional[float] = None, rotation: Optional[float] = None, background: Optional[str] = None, output: Optional[ImageFormat] = None, token: Optional[str] = None) -> bytes:
        """
        Get a file preview image. Currently, this method supports preview for image files (jpg, png, and gif), other supported formats, like pdf, docs, slides, and spreadsheets, will return the file icon image. You can also pass query string arguments for cutting and resizing your preview image. Preview is supported only for image files smaller than 10MB.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID
        width : Optional[float]
            Resize preview image width, Pass an integer between 0 to 4000.
        height : Optional[float]
            Resize preview image height, Pass an integer between 0 to 4000.
        gravity : Optional[ImageGravity]
            Image crop gravity. Can be one of center,top-left,top,top-right,left,right,bottom-left,bottom,bottom-right
        quality : Optional[float]
            Preview image quality. Pass an integer between 0 to 100. Defaults to keep existing image quality.
        border_width : Optional[float]
            Preview image border in pixels. Pass an integer between 0 to 100. Defaults to 0.
        border_color : Optional[str]
            Preview image border color. Use a valid HEX color, no # is needed for prefix.
        border_radius : Optional[float]
            Preview image border radius in pixels. Pass an integer between 0 to 4000.
        opacity : Optional[float]
            Preview image opacity. Only works with images having an alpha channel (like png). Pass a number between 0 to 1.
        rotation : Optional[float]
            Preview image rotation in degrees. Pass an integer between -360 and 360.
        background : Optional[str]
            Preview image background color. Only works with transparent images (png). Use a valid HEX color, no # is needed for prefix.
        output : Optional[ImageFormat]
            Output format type (jpeg, jpg, png, gif and webp).
        token : Optional[str]
            File token for accessing this file.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}/files/{fileId}/preview'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        if width is not None:
            api_params['width'] = width
        if height is not None:
            api_params['height'] = height
        if gravity is not None:
            api_params['gravity'] = gravity
        if quality is not None:
            api_params['quality'] = quality
        if border_width is not None:
            api_params['borderWidth'] = border_width
        if border_color is not None:
            api_params['borderColor'] = border_color
        if border_radius is not None:
            api_params['borderRadius'] = border_radius
        if opacity is not None:
            api_params['opacity'] = opacity
        if rotation is not None:
            api_params['rotation'] = rotation
        if background is not None:
            api_params['background'] = background
        if output is not None:
            api_params['output'] = output
        if token is not None:
            api_params['token'] = token

        return self.client.call('get', api_path, {
        }, api_params)

    def get_file_view(self, bucket_id: str, file_id: str, token: Optional[str] = None) -> bytes:
        """
        Get a file content by its unique ID. This endpoint is similar to the download method but returns with no  'Content-Disposition: attachment' header.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID.
        token : Optional[str]
            File token for accessing this file.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/storage/buckets/{bucketId}/files/{fileId}/view'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        if token is not None:
            api_params['token'] = token

        return self.client.call('get', api_path, {
        }, api_params)
