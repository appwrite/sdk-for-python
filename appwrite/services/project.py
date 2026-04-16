from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.key_list import KeyList;
from ..enums.scopes import Scopes;
from ..models.key import Key;
from ..models.project import Project as ProjectModel;
from ..models.platform_list import PlatformList;
from ..models.platform_android import PlatformAndroid;
from ..models.platform_apple import PlatformApple;
from ..models.platform_linux import PlatformLinux;
from ..models.platform_web import PlatformWeb;
from ..models.platform_windows import PlatformWindows;
from ..enums.protocol_id import ProtocolId;
from ..enums.service_id import ServiceId;
from ..models.variable_list import VariableList;
from ..models.variable import Variable;

class Project(Service):

    def __init__(self, client) -> None:
        super(Project, self).__init__(client)

    def list_keys(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> KeyList:
        """
        Get a list of all API keys from the current project.

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

        api_path = '/project/keys'
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
        scopes: List[Scopes],
        expire: Optional[str] = None
    ) -> Key:
        """
        Create a new API key. It's recommended to have multiple API keys with strict scopes for separate functions within your project.

        Parameters
        ----------
        key_id : str
            Key ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Key name. Max length: 128 chars.
        scopes : List[Scopes]
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

        api_path = '/project/keys'
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
        Get a key by its unique ID. 

        Parameters
        ----------
        key_id : str
            Key ID.
        
        Returns
        -------
        Key
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/keys/{keyId}'
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
        scopes: List[Scopes],
        expire: Optional[str] = None
    ) -> Key:
        """
        Update a key by its unique ID. Use this endpoint to update the name, scopes, or expiration time of an API key.

        Parameters
        ----------
        key_id : str
            Key ID.
        name : str
            Key name. Max length: 128 chars.
        scopes : List[Scopes]
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

        api_path = '/project/keys/{keyId}'
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
            Key ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/keys/{keyId}'
        api_params = {}
        if key_id is None:
            raise AppwriteException('Missing required parameter: "key_id"')

        api_path = api_path.replace('{keyId}', str(self._normalize_value(key_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_labels(
        self,
        labels: List[str]
    ) -> ProjectModel:
        """
        Update the project labels. Labels can be used to easily filter projects in an organization.

        Parameters
        ----------
        labels : List[str]
            Array of project labels. Replaces the previous labels. Maximum of 1000 labels are allowed, each up to 36 alphanumeric characters long.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/labels'
        api_params = {}
        if labels is None:
            raise AppwriteException('Missing required parameter: "labels"')


        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def list_platforms(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> PlatformList:
        """
        Get a list of all platforms in the project. This endpoint returns an array of all platforms and their configurations.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: type, name, hostname, bundleIdentifier, applicationId, packageIdentifierName, packageName
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        PlatformList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PlatformList)


    def create_android_platform(
        self,
        platform_id: str,
        name: str,
        application_id: str
    ) -> PlatformAndroid:
        """
        Create a new Android platform for your project. Use this endpoint to register a new Android platform where your users will run your application which will interact with the Appwrite API.

        Parameters
        ----------
        platform_id : str
            Platform ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Platform name. Max length: 128 chars.
        application_id : str
            Android application ID. Max length: 256 chars.
        
        Returns
        -------
        PlatformAndroid
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/android'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if application_id is None:
            raise AppwriteException('Missing required parameter: "application_id"')


        api_params['platformId'] = self._normalize_value(platform_id)
        api_params['name'] = self._normalize_value(name)
        api_params['applicationId'] = self._normalize_value(application_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformAndroid)


    def update_android_platform(
        self,
        platform_id: str,
        name: str,
        application_id: str
    ) -> PlatformAndroid:
        """
        Update an Android platform by its unique ID. Use this endpoint to update the platform's name or application ID.

        Parameters
        ----------
        platform_id : str
            Platform ID.
        name : str
            Platform name. Max length: 128 chars.
        application_id : str
            Android application ID. Max length: 256 chars.
        
        Returns
        -------
        PlatformAndroid
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/android/{platformId}'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if application_id is None:
            raise AppwriteException('Missing required parameter: "application_id"')

        api_path = api_path.replace('{platformId}', str(self._normalize_value(platform_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['applicationId'] = self._normalize_value(application_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformAndroid)


    def create_apple_platform(
        self,
        platform_id: str,
        name: str,
        bundle_identifier: str
    ) -> PlatformApple:
        """
        Create a new Apple platform for your project. Use this endpoint to register a new Apple platform where your users will run your application which will interact with the Appwrite API.

        Parameters
        ----------
        platform_id : str
            Platform ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Platform name. Max length: 128 chars.
        bundle_identifier : str
            Apple bundle identifier. Max length: 256 chars.
        
        Returns
        -------
        PlatformApple
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/apple'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if bundle_identifier is None:
            raise AppwriteException('Missing required parameter: "bundle_identifier"')


        api_params['platformId'] = self._normalize_value(platform_id)
        api_params['name'] = self._normalize_value(name)
        api_params['bundleIdentifier'] = self._normalize_value(bundle_identifier)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformApple)


    def update_apple_platform(
        self,
        platform_id: str,
        name: str,
        bundle_identifier: str
    ) -> PlatformApple:
        """
        Update an Apple platform by its unique ID. Use this endpoint to update the platform's name or bundle identifier.

        Parameters
        ----------
        platform_id : str
            Platform ID.
        name : str
            Platform name. Max length: 128 chars.
        bundle_identifier : str
            Apple bundle identifier. Max length: 256 chars.
        
        Returns
        -------
        PlatformApple
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/apple/{platformId}'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if bundle_identifier is None:
            raise AppwriteException('Missing required parameter: "bundle_identifier"')

        api_path = api_path.replace('{platformId}', str(self._normalize_value(platform_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['bundleIdentifier'] = self._normalize_value(bundle_identifier)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformApple)


    def create_linux_platform(
        self,
        platform_id: str,
        name: str,
        package_name: str
    ) -> PlatformLinux:
        """
        Create a new Linux platform for your project. Use this endpoint to register a new Linux platform where your users will run your application which will interact with the Appwrite API.

        Parameters
        ----------
        platform_id : str
            Platform ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Platform name. Max length: 128 chars.
        package_name : str
            Linux package name. Max length: 256 chars.
        
        Returns
        -------
        PlatformLinux
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/linux'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if package_name is None:
            raise AppwriteException('Missing required parameter: "package_name"')


        api_params['platformId'] = self._normalize_value(platform_id)
        api_params['name'] = self._normalize_value(name)
        api_params['packageName'] = self._normalize_value(package_name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformLinux)


    def update_linux_platform(
        self,
        platform_id: str,
        name: str,
        package_name: str
    ) -> PlatformLinux:
        """
        Update a Linux platform by its unique ID. Use this endpoint to update the platform's name or package name.

        Parameters
        ----------
        platform_id : str
            Platform ID.
        name : str
            Platform name. Max length: 128 chars.
        package_name : str
            Linux package name. Max length: 256 chars.
        
        Returns
        -------
        PlatformLinux
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/linux/{platformId}'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if package_name is None:
            raise AppwriteException('Missing required parameter: "package_name"')

        api_path = api_path.replace('{platformId}', str(self._normalize_value(platform_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['packageName'] = self._normalize_value(package_name)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformLinux)


    def create_web_platform(
        self,
        platform_id: str,
        name: str,
        hostname: str
    ) -> PlatformWeb:
        """
        Create a new web platform for your project. Use this endpoint to register a new platform where your users will run your application which will interact with the Appwrite API.

        Parameters
        ----------
        platform_id : str
            Platform ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Platform name. Max length: 128 chars.
        hostname : str
            Platform web hostname. Max length: 256 chars.
        
        Returns
        -------
        PlatformWeb
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/web'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if hostname is None:
            raise AppwriteException('Missing required parameter: "hostname"')


        api_params['platformId'] = self._normalize_value(platform_id)
        api_params['name'] = self._normalize_value(name)
        api_params['hostname'] = self._normalize_value(hostname)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformWeb)


    def update_web_platform(
        self,
        platform_id: str,
        name: str,
        hostname: str
    ) -> PlatformWeb:
        """
        Update a web platform by its unique ID. Use this endpoint to update the platform's name or hostname.

        Parameters
        ----------
        platform_id : str
            Platform ID.
        name : str
            Platform name. Max length: 128 chars.
        hostname : str
            Platform web hostname. Max length: 256 chars.
        
        Returns
        -------
        PlatformWeb
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/web/{platformId}'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if hostname is None:
            raise AppwriteException('Missing required parameter: "hostname"')

        api_path = api_path.replace('{platformId}', str(self._normalize_value(platform_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['hostname'] = self._normalize_value(hostname)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformWeb)


    def create_windows_platform(
        self,
        platform_id: str,
        name: str,
        package_identifier_name: str
    ) -> PlatformWindows:
        """
        Create a new Windows platform for your project. Use this endpoint to register a new Windows platform where your users will run your application which will interact with the Appwrite API.

        Parameters
        ----------
        platform_id : str
            Platform ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Platform name. Max length: 128 chars.
        package_identifier_name : str
            Windows package identifier name. Max length: 256 chars.
        
        Returns
        -------
        PlatformWindows
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/windows'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if package_identifier_name is None:
            raise AppwriteException('Missing required parameter: "package_identifier_name"')


        api_params['platformId'] = self._normalize_value(platform_id)
        api_params['name'] = self._normalize_value(name)
        api_params['packageIdentifierName'] = self._normalize_value(package_identifier_name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformWindows)


    def update_windows_platform(
        self,
        platform_id: str,
        name: str,
        package_identifier_name: str
    ) -> PlatformWindows:
        """
        Update a Windows platform by its unique ID. Use this endpoint to update the platform's name or package identifier name.

        Parameters
        ----------
        platform_id : str
            Platform ID.
        name : str
            Platform name. Max length: 128 chars.
        package_identifier_name : str
            Windows package identifier name. Max length: 256 chars.
        
        Returns
        -------
        PlatformWindows
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/windows/{platformId}'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if package_identifier_name is None:
            raise AppwriteException('Missing required parameter: "package_identifier_name"')

        api_path = api_path.replace('{platformId}', str(self._normalize_value(platform_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['packageIdentifierName'] = self._normalize_value(package_identifier_name)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PlatformWindows)


    def get_platform(
        self,
        platform_id: str
    ) -> Union[PlatformWeb, PlatformApple, PlatformAndroid, PlatformWindows, PlatformLinux]:
        """
        Get a platform by its unique ID. This endpoint returns the platform's details, including its name, type, and key configurations.

        Parameters
        ----------
        platform_id : str
            Platform ID.
        
        Returns
        -------
        Union[PlatformWeb, PlatformApple, PlatformAndroid, PlatformWindows, PlatformLinux]
            API response as one of the typed response models
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/{platformId}'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        api_path = api_path.replace('{platformId}', str(self._normalize_value(platform_id)))


        response = self.client.call('get', api_path, {
        }, api_params)
        if not isinstance(response, dict):
            raise AppwriteException('Expected object response when hydrating a response model')

        if response.get('type') == 'web':
            return self._parse_response(response, model=PlatformWeb)

        if response.get('type') == 'apple':
            return self._parse_response(response, model=PlatformApple)

        if response.get('type') == 'android':
            return self._parse_response(response, model=PlatformAndroid)

        if response.get('type') == 'windows':
            return self._parse_response(response, model=PlatformWindows)

        if response.get('type') == 'linux':
            return self._parse_response(response, model=PlatformLinux)

        raise AppwriteException('Unable to match response to any known model')


    def delete_platform(
        self,
        platform_id: str
    ) -> Dict[str, Any]:
        """
        Delete a platform by its unique ID. This endpoint removes the platform and all its configurations from the project.

        Parameters
        ----------
        platform_id : str
            Platform ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/platforms/{platformId}'
        api_params = {}
        if platform_id is None:
            raise AppwriteException('Missing required parameter: "platform_id"')

        api_path = api_path.replace('{platformId}', str(self._normalize_value(platform_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_protocol_status(
        self,
        protocol_id: ProtocolId,
        enabled: bool
    ) -> ProjectModel:
        """
        Update the status of a specific protocol. Use this endpoint to enable or disable a protocol in your project. 

        Parameters
        ----------
        protocol_id : ProtocolId
            Protocol name. Can be one of: rest, graphql, websocket
        enabled : bool
            Protocol status.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/protocols/{protocolId}/status'
        api_params = {}
        if protocol_id is None:
            raise AppwriteException('Missing required parameter: "protocol_id"')

        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')

        api_path = api_path.replace('{protocolId}', str(self._normalize_value(protocol_id)))

        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_service_status(
        self,
        service_id: ServiceId,
        enabled: bool
    ) -> ProjectModel:
        """
        Update the status of a specific service. Use this endpoint to enable or disable a service in your project. 

        Parameters
        ----------
        service_id : ServiceId
            Service name. Can be one of: account, avatars, databases, tablesdb, locale, health, project, storage, teams, users, vcs, sites, functions, proxy, graphql, migrations, messaging
        enabled : bool
            Service status.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/services/{serviceId}/status'
        api_params = {}
        if service_id is None:
            raise AppwriteException('Missing required parameter: "service_id"')

        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')

        api_path = api_path.replace('{serviceId}', str(self._normalize_value(service_id)))

        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def list_variables(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> VariableList:
        """
        Get a list of all project environment variables.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, resourceType, resourceId, secret
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        VariableList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VariableList)


    def create_variable(
        self,
        variable_id: str,
        key: str,
        value: str,
        secret: Optional[bool] = None
    ) -> Variable:
        """
        Create a new project environment variable. These variables can be accessed by all functions and sites in the project.

        Parameters
        ----------
        variable_id : str
            Variable ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        key : str
            Variable key. Max length: 255 chars.
        value : str
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only projects can read them during build and runtime.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if value is None:
            raise AppwriteException('Missing required parameter: "value"')


        api_params['variableId'] = self._normalize_value(variable_id)
        api_params['key'] = self._normalize_value(key)
        api_params['value'] = self._normalize_value(value)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def get_variable(
        self,
        variable_id: str
    ) -> Variable:
        """
        Get a variable by its unique ID. 

        Parameters
        ----------
        variable_id : str
            Variable ID.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables/{variableId}'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Variable)


    def update_variable(
        self,
        variable_id: str,
        key: Optional[str] = None,
        value: Optional[str] = None,
        secret: Optional[bool] = None
    ) -> Variable:
        """
        Update variable by its unique ID.

        Parameters
        ----------
        variable_id : str
            Variable ID.
        key : Optional[str]
            Variable key. Max length: 255 chars.
        value : Optional[str]
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only projects can read them during build and runtime.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables/{variableId}'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['value'] = self._normalize_value(value)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def delete_variable(
        self,
        variable_id: str
    ) -> Dict[str, Any]:
        """
        Delete a variable by its unique ID. 

        Parameters
        ----------
        variable_id : str
            Variable ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables/{variableId}'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

