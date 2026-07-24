from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.organization import Organization as OrganizationModel
from ..models.app_installation_list import AppInstallationList
from ..models.app_installation import AppInstallation
from ..models.key_list import KeyList
from ..enums.organization_key_scopes import OrganizationKeyScopes
from ..models.key import Key
from ..models.membership_list import MembershipList
from ..models.membership import Membership
from ..models.project_list import ProjectList
from ..enums.region import Region
from ..models.project import Project

T = TypeVar('T')

class Organization(Service):

    def __init__(self, client) -> None:
        super(Organization, self).__init__(client)

    def get(
        self,
        model_type: Type[T] = dict
    ) -> OrganizationModel[T]:
        """
        Get the current organization.

        Parameters
        ----------
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        OrganizationModel[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization'
        api_params = {}

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return OrganizationModel.with_data(response, model_type)


    def update(
        self,
        name: str,
        model_type: Type[T] = dict
    ) -> OrganizationModel[T]:
        """
        Update the current organization's name.

        Parameters
        ----------
        name : str
            New organization name. Max length: 128 chars.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        OrganizationModel[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization'
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['name'] = self._normalize_value(name)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return OrganizationModel.with_data(response, model_type)


    def delete(
        self
    ) -> Dict[str, Any]:
        """
        Delete the current organization. All projects that belong to the organization are deleted as well.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization'
        api_params = {}

        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_installations(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> AppInstallationList:
        """
        List app installations on the organization. Any organization member can read installations.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        AppInstallationList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/installations'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppInstallationList)


    def create_installation(
        self,
        app_id: str,
        authorization_details: Optional[str] = None
    ) -> AppInstallation:
        """
        Install an app on the organization. Only organization members with the owner role can install apps. The installation is granted the scopes the app currently requests.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        authorization_details : Optional[str]
            Authorization details granted to the installation as a JSON array of objects, each with a `type` and app-defined fields. The Appwrite Console stores authorized project IDs here.
        
        Returns
        -------
        AppInstallation
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/installations'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')


        api_params['appId'] = self._normalize_value(app_id)
        if authorization_details is not None:
            api_params['authorizationDetails'] = self._normalize_value(authorization_details)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppInstallation)


    def get_installation(
        self,
        installation_id: str
    ) -> AppInstallation:
        """
        Get an app installation on the organization by its unique ID. Any organization member can read installations.

        Parameters
        ----------
        installation_id : str
            Installation unique ID.
        
        Returns
        -------
        AppInstallation
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/installations/{installationId}'
        api_params = {}
        if installation_id is None:
            raise AppwriteException('Missing required parameter: "installation_id"')

        api_path = api_path.replace('{installationId}', str(self._normalize_value(installation_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppInstallation)


    def update_installation(
        self,
        installation_id: str,
        authorization_details: Optional[str] = None
    ) -> AppInstallation:
        """
        Update an app installation on the organization. Only organization members with the owner role can update installations. The installation's granted scopes are refreshed to the scopes the app currently requests; previously issued installation access tokens are revoked.

        Parameters
        ----------
        installation_id : str
            Installation unique ID.
        authorization_details : Optional[str]
            Authorization details granted to the installation as a JSON array of objects, each with a `type` and app-defined fields. Omit to keep the current value.
        
        Returns
        -------
        AppInstallation
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/installations/{installationId}'
        api_params = {}
        if installation_id is None:
            raise AppwriteException('Missing required parameter: "installation_id"')

        api_path = api_path.replace('{installationId}', str(self._normalize_value(installation_id)))

        if authorization_details is not None:
            api_params['authorizationDetails'] = self._normalize_value(authorization_details)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppInstallation)


    def delete_installation(
        self,
        installation_id: str
    ) -> Dict[str, Any]:
        """
        Uninstall an app from the organization by its installation ID. Only organization members with the owner role can remove installations. Previously issued installation access tokens are revoked.

        Parameters
        ----------
        installation_id : str
            Installation unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/installations/{installationId}'
        api_params = {}
        if installation_id is None:
            raise AppwriteException('Missing required parameter: "installation_id"')

        api_path = api_path.replace('{installationId}', str(self._normalize_value(installation_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return response


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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
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
            Key scopes list. Maximum of 200 scopes are allowed.
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
        if expire is not None:
            api_params['expire'] = self._normalize_value(expire)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
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
            Key scopes list. Maximum of 200 scopes are allowed.
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
        if expire is not None:
            api_params['expire'] = self._normalize_value(expire)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_memberships(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> MembershipList:
        """
        Get a list of all memberships from the current organization.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, teamId, invited, joined, confirm, roles
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        MembershipList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/memberships'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MembershipList)


    def create_membership(
        self,
        roles: List[str],
        email: Optional[str] = None,
        user_id: Optional[str] = None,
        phone: Optional[str] = None,
        url: Optional[str] = None,
        name: Optional[str] = None
    ) -> Membership:
        """
        Invite a new member to join the current organization. An email with a link to join the organization will be sent to the new member's email address. If member doesn't exist in the project it will be automatically created.

        Parameters
        ----------
        roles : List[str]
            Array of strings. Use this param to set the user roles in the organization. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 81 characters long.
        email : Optional[str]
            Email of the new organization member.
        user_id : Optional[str]
            ID of the user to be added to the organization.
        phone : Optional[str]
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        url : Optional[str]
            URL to redirect the user back to your app from the invitation email. This parameter is not required when an API key is supplied.
        name : Optional[str]
            Name of the new organization member. Max length: 128 chars.
        
        Returns
        -------
        Membership
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/memberships'
        api_params = {}
        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')


        if email is not None:
            api_params['email'] = self._normalize_value(email)
        if user_id is not None:
            api_params['userId'] = self._normalize_value(user_id)
        if phone is not None:
            api_params['phone'] = self._normalize_value(phone)
        api_params['roles'] = self._normalize_value(roles)
        if url is not None:
            api_params['url'] = self._normalize_value(url)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Membership)


    def get_membership(
        self,
        membership_id: str
    ) -> Membership:
        """
        Get a membership from the current organization by its unique ID.

        Parameters
        ----------
        membership_id : str
            Membership ID.
        
        Returns
        -------
        Membership
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/memberships/{membershipId}'
        api_params = {}
        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        api_path = api_path.replace('{membershipId}', str(self._normalize_value(membership_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Membership)


    def update_membership(
        self,
        membership_id: str,
        roles: List[str]
    ) -> Membership:
        """
        Modify the roles of a member in the current organization.

        Parameters
        ----------
        membership_id : str
            Membership ID.
        roles : List[str]
            An array of strings. Use this param to set the user's roles in the organization. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 81 characters long.
        
        Returns
        -------
        Membership
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/memberships/{membershipId}'
        api_params = {}
        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')

        api_path = api_path.replace('{membershipId}', str(self._normalize_value(membership_id)))

        api_params['roles'] = self._normalize_value(roles)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Membership)


    def delete_membership(
        self,
        membership_id: str
    ) -> Dict[str, Any]:
        """
        Remove a member from the current organization. The member is removed whether they accepted the invitation or not; a pending invitation is revoked.

        Parameters
        ----------
        membership_id : str
            Membership ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organization/memberships/{membershipId}'
        api_params = {}
        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        api_path = api_path.replace('{membershipId}', str(self._normalize_value(membership_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
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
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, teamId, labels, search, accessedAt
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response

