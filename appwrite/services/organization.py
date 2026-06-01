from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.key_list import KeyList
from ..enums.organization_key_scopes import OrganizationKeyScopes
from ..models.key import Key
from ..models.project_list import ProjectList
from ..enums.region import Region
from ..models.project import Project

class Organization(Service):

    def __init__(self, client) -> None:
        super(Organization, self).__init__(client)

    def list_keys(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> KeyList:
        """
        Get a list of all API keys from the current organization.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: expire, accessedAt, name, scopes
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        KeyList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/keys'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=KeyList)


    def create_key(
        self,
        key_id: str,
        name: str,
        scopes: List[OrganizationKeyScopes],
        expire: Optional[str] = None
    ) -> Key:
        """
        Create a new organization API key.

        Parameters
        ----------
        key_id : str
            Key ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Key name. Max length: 128 chars.
        scopes : List[OrganizationKeyScopes]
            Key scopes list. Maximum of 100 scopes are allowed.
        expire : Optional[str]
            Expiration time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Use null for unlimited expiration.
        
        Returns
        -------
        Key
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/keys'
        api_params = {}
        if key_id is None:
            raise AppwriteException('Missing required parameter: "key_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if scopes is None:
            raise AppwriteException('Missing required parameter: "scopes"')


        api_params['keyId'] = self._normalize_value(key_id)
        api_params['name'] = self._normalize_value(name)
        api_params['scopes'] = self._normalize_value(scopes)
        api_params['expire'] = self._normalize_value(expire)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Key)


    def get_key(
        self,
        key_id: str
    ) -> Key:
        """
        Get a key by its unique ID. This endpoint returns details about a specific API key in your organization including its scopes.

        Parameters
        ----------
        key_id : str
            Key unique ID.
        
        Returns
        -------
        Key
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/keys/{keyId}'
        api_params = {}
        if key_id is None:
            raise AppwriteException('Missing required parameter: "key_id"')

        api_path = api_path.replace('{keyId}', str(self._normalize_value(key_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Key)


    def update_key(
        self,
        key_id: str,
        name: str,
        scopes: List[OrganizationKeyScopes],
        expire: Optional[str] = None
    ) -> Key:
        """
        Update a key by its unique ID. Use this endpoint to update the name, scopes, or expiration time of an API key.

        Parameters
        ----------
        key_id : str
            Key unique ID.
        name : str
            Key name. Max length: 128 chars.
        scopes : List[OrganizationKeyScopes]
            Key scopes list. Maximum of 100 scopes are allowed.
        expire : Optional[str]
            Expiration time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Use null for unlimited expiration.
        
        Returns
        -------
        Key
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/keys/{keyId}'
        api_params = {}
        if key_id is None:
            raise AppwriteException('Missing required parameter: "key_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if scopes is None:
            raise AppwriteException('Missing required parameter: "scopes"')

        api_path = api_path.replace('{keyId}', str(self._normalize_value(key_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['scopes'] = self._normalize_value(scopes)
        api_params['expire'] = self._normalize_value(expire)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Key)


    def delete_key(
        self,
        key_id: str
    ) -> Dict[str, Any]:
        """
        Delete a key by its unique ID. Once deleted, the key can no longer be used to authenticate API calls.

        Parameters
        ----------
        key_id : str
            Key unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/keys/{keyId}'
        api_params = {}
        if key_id is None:
            raise AppwriteException('Missing required parameter: "key_id"')

        api_path = api_path.replace('{keyId}', str(self._normalize_value(key_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_projects(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> ProjectList:
        """
        Get a list of all projects. You can use the query params to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, teamId, labels, search
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ProjectList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/projects'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ProjectList)


    def create_project(
        self,
        project_id: str,
        name: str,
        region: Optional[Region] = None
    ) -> Project:
        """
        Create a new project.

        Parameters
        ----------
        project_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, and hyphen. Can't start with a special char. Max length is 36 chars.
        name : str
            Project name. Max length: 128 chars.
        region : Optional[Region]
            Project Region.
        
        Returns
        -------
        Project
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/projects'
        api_params = {}
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['projectId'] = self._normalize_value(project_id)
        api_params['name'] = self._normalize_value(name)
        if region is not None:
            api_params['region'] = self._normalize_value(region)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Project)


    def get_project(
        self,
        project_id: str
    ) -> Project:
        """
        Get a project.

        Parameters
        ----------
        project_id : str
            Project unique ID.
        
        Returns
        -------
        Project
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/projects/{projectId}'
        api_params = {}
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')

        api_path = api_path.replace('{projectId}', str(self._normalize_value(project_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Project)


    def update_project(
        self,
        project_id: str,
        name: str
    ) -> Project:
        """
        Update a project by its unique ID.

        Parameters
        ----------
        project_id : str
            Project unique ID.
        name : str
            Project name. Max length: 128 chars.
        
        Returns
        -------
        Project
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/projects/{projectId}'
        api_params = {}
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{projectId}', str(self._normalize_value(project_id)))

        api_params['name'] = self._normalize_value(name)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Project)


    def delete_project(
        self,
        project_id: str
    ) -> Dict[str, Any]:
        """
        Delete a project by its unique ID.

        Parameters
        ----------
        project_id : str
            Project unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/projects/{projectId}'
        api_params = {}
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')

        api_path = api_path.replace('{projectId}', str(self._normalize_value(project_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

