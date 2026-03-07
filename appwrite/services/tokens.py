from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.resource_token_list import ResourceTokenList;
from ..models.resource_token import ResourceToken;

class Tokens(Service):

    def __init__(self, client) -> None:
        super(Tokens, self).__init__(client)

    def list(
        self,
        bucket_id: str,
        file_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> ResourceTokenList:
        """
        List all the tokens created for a specific file or bucket. You can use the query params to filter your results.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File unique ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: expire
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ResourceTokenList
            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{bucketId}', str(self._normalize_value(bucket_id)))
        api_path = api_path.replace('{fileId}', str(self._normalize_value(file_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ResourceTokenList)


    def create_file_token(
        self,
        bucket_id: str,
        file_id: str,
        expire: Optional[str] = None
    ) -> ResourceToken:
        """
        Create a new token. A token is linked to a file. Token can be passed as a request URL search parameter.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File unique ID.
        expire : Optional[str]
            Token expiry date
        
        Returns
        -------
        ResourceToken
            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{bucketId}', str(self._normalize_value(bucket_id)))
        api_path = api_path.replace('{fileId}', str(self._normalize_value(file_id)))

        api_params['expire'] = self._normalize_value(expire)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ResourceToken)


    def get(
        self,
        token_id: str
    ) -> ResourceToken:
        """
        Get a token by its unique ID.

        Parameters
        ----------
        token_id : str
            Token ID.
        
        Returns
        -------
        ResourceToken
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tokens/{tokenId}'
        api_params = {}
        if token_id is None:
            raise AppwriteException('Missing required parameter: "token_id"')

        api_path = api_path.replace('{tokenId}', str(self._normalize_value(token_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ResourceToken)


    def update(
        self,
        token_id: str,
        expire: Optional[str] = None
    ) -> ResourceToken:
        """
        Update a token by its unique ID. Use this endpoint to update a token's expiry date.

        Parameters
        ----------
        token_id : str
            Token unique ID.
        expire : Optional[str]
            File token expiry date
        
        Returns
        -------
        ResourceToken
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tokens/{tokenId}'
        api_params = {}
        if token_id is None:
            raise AppwriteException('Missing required parameter: "token_id"')

        api_path = api_path.replace('{tokenId}', str(self._normalize_value(token_id)))

        api_params['expire'] = self._normalize_value(expire)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ResourceToken)


    def delete(
        self,
        token_id: str
    ) -> Dict[str, Any]:
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

        api_path = api_path.replace('{tokenId}', str(self._normalize_value(token_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

