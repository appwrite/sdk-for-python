from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException

class Tokens(Service):

    def __init__(self, client) -> None:
        super(Tokens, self).__init__(client)

    def list(self, bucket_id: str, file_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        List all the tokens created for a specific file or bucket. You can use the query params to filter your results.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File unique ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: expire
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tokens/buckets/{bucketId}/files/{fileId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_file_token(self, bucket_id: str, file_id: str, expire: str = None) -> Dict[str, Any]:
        """
        Create a new token. A token is linked to a file. Token can be passed as a header or request get parameter.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File unique ID.
        expire : str
            Token expiry date
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tokens/buckets/{bucketId}/files/{fileId}'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')

        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')

        api_path = api_path.replace('{bucketId}', bucket_id)
        api_path = api_path.replace('{fileId}', file_id)

        api_params['expire'] = expire

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get(self, token_id: str) -> Dict[str, Any]:
        """
        Get a token by its unique ID.

        Parameters
        ----------
        token_id : str
            Token ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tokens/{tokenId}'
        api_params = {}
        if token_id is None:
            raise AppwriteException('Missing required parameter: "token_id"')

        api_path = api_path.replace('{tokenId}', token_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update(self, token_id: str, expire: str = None) -> Dict[str, Any]:
        """
        Update a token by its unique ID. Use this endpoint to update a token's expiry date.

        Parameters
        ----------
        token_id : str
            Token unique ID.
        expire : str
            File token expiry date
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tokens/{tokenId}'
        api_params = {}
        if token_id is None:
            raise AppwriteException('Missing required parameter: "token_id"')

        api_path = api_path.replace('{tokenId}', token_id)

        api_params['expire'] = expire

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, token_id: str) -> Dict[str, Any]:
        """
        Delete a token by its unique ID.

        Parameters
        ----------
        token_id : str
            Token ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tokens/{tokenId}'
        api_params = {}
        if token_id is None:
            raise AppwriteException('Missing required parameter: "token_id"')

        api_path = api_path.replace('{tokenId}', token_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)
