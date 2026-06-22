from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.presence_list import PresenceList
from ..models.presence import Presence

class Presences(Service):

    def __init__(self, client) -> None:
        super(Presences, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
        ttl: Optional[float] = None
    ) -> PresenceList:
        """
        List presence logs. Expired entries are filtered out automatically.
        

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        ttl : Optional[float]
            TTL (seconds) for caching list responses. Responses are stored in an in-memory key-value cache, keyed per project, collection, schema version (attributes and indexes), caller authorization roles, and the exact query — so users with different permissions never share cached entries. Schema changes invalidate cached entries automatically; document writes do not, so choose a TTL you are comfortable serving as stale data. Set to 0 to disable caching. Must be between 0 and 86400 (24 hours).
        
        Returns
        -------
        PresenceList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/presences'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)
        if ttl is not None:
            api_params['ttl'] = self._normalize_value(ttl)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PresenceList)


    def get(
        self,
        presence_id: str
    ) -> Presence:
        """
        Get a presence log by its unique ID. Entries whose `expiresAt` is in the past are treated as not found.
        

        Parameters
        ----------
        presence_id : str
            Presence unique ID.
        
        Returns
        -------
        Presence
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/presences/{presenceId}'
        api_params = {}
        if presence_id is None:
            raise AppwriteException('Missing required parameter: "presence_id"')

        api_path = api_path.replace('{presenceId}', str(self._normalize_value(presence_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Presence)


    def upsert(
        self,
        presence_id: str,
        user_id: str,
        status: str,
        permissions: Optional[List[str]] = None,
        expires_at: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Presence:
        """
        Create or update a presence log by its user ID.
        

        Parameters
        ----------
        presence_id : str
            Presence unique ID.
        user_id : str
            User ID.
        status : str
            Presence status.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        expires_at : Optional[str]
            Presence expiry datetime.
        metadata : Optional[Dict[str, Any]]
            Presence metadata object.
        
        Returns
        -------
        Presence
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/presences/{presenceId}'
        api_params = {}
        if presence_id is None:
            raise AppwriteException('Missing required parameter: "presence_id"')

        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if status is None:
            raise AppwriteException('Missing required parameter: "status"')

        api_path = api_path.replace('{presenceId}', str(self._normalize_value(presence_id)))

        api_params['userId'] = self._normalize_value(user_id)
        api_params['status'] = self._normalize_value(status)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if expires_at is not None:
            api_params['expiresAt'] = self._normalize_value(expires_at)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Presence)


    def update(
        self,
        presence_id: str,
        user_id: str,
        status: Optional[str] = None,
        expires_at: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        permissions: Optional[List[str]] = None,
        purge: Optional[bool] = None
    ) -> Presence:
        """
        Update a presence log by its unique ID. Using the patch method you can pass only specific fields that will get updated.
        

        Parameters
        ----------
        presence_id : str
            Presence unique ID.
        user_id : str
            User ID.
        status : Optional[str]
            Presence status.
        expires_at : Optional[str]
            Presence expiry datetime.
        metadata : Optional[Dict[str, Any]]
            Presence metadata object.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        purge : Optional[bool]
            When true, purge cached responses used by list presences endpoint.
        
        Returns
        -------
        Presence
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/presences/{presenceId}'
        api_params = {}
        if presence_id is None:
            raise AppwriteException('Missing required parameter: "presence_id"')

        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{presenceId}', str(self._normalize_value(presence_id)))

        api_params['userId'] = self._normalize_value(user_id)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if expires_at is not None:
            api_params['expiresAt'] = self._normalize_value(expires_at)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if purge is not None:
            api_params['purge'] = self._normalize_value(purge)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Presence)


    def delete(
        self,
        presence_id: str
    ) -> Dict[str, Any]:
        """
        Delete a presence log by its unique ID.
        

        Parameters
        ----------
        presence_id : str
            Presence unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/presences/{presenceId}'
        api_params = {}
        if presence_id is None:
            raise AppwriteException('Missing required parameter: "presence_id"')

        api_path = api_path.replace('{presenceId}', str(self._normalize_value(presence_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response

