from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.apps_list import AppsList
from ..models.app import App
from ..models.app_secret_list import AppSecretList
from ..models.app_secret_plaintext import AppSecretPlaintext
from ..models.app_secret import AppSecret

class Apps(Service):

    def __init__(self, client) -> None:
        super(Apps, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> AppsList:
        """
        List applications.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        AppsList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppsList)


    def create(
        self,
        app_id: str,
        name: str,
        redirect_uris: List[str],
        description: Optional[str] = None,
        client_uri: Optional[str] = None,
        logo_uri: Optional[str] = None,
        privacy_policy_url: Optional[str] = None,
        terms_url: Optional[str] = None,
        contacts: Optional[List[str]] = None,
        tagline: Optional[str] = None,
        tags: Optional[List[str]] = None,
        images: Optional[List[str]] = None,
        support_url: Optional[str] = None,
        data_deletion_url: Optional[str] = None,
        post_logout_redirect_uris: Optional[List[str]] = None,
        enabled: Optional[bool] = None,
        type: Optional[str] = None,
        device_flow: Optional[bool] = None,
        team_id: Optional[str] = None
    ) -> App:
        """
        Create a new application.

        Parameters
        ----------
        app_id : str
            Application ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Application name.
        redirect_uris : List[str]
            Redirect URIs (array of valid URLs).
        description : Optional[str]
            Application description shown to users during OAuth2 consent.
        client_uri : Optional[str]
            Application homepage URL shown to users during OAuth2 consent.
        logo_uri : Optional[str]
            Application logo URL shown to users during OAuth2 consent.
        privacy_policy_url : Optional[str]
            Application privacy policy URL shown to users during OAuth2 consent.
        terms_url : Optional[str]
            Application terms of service URL shown to users during OAuth2 consent.
        contacts : Optional[List[str]]
            Application support or security contact emails. Maximum of 100 contacts are allowed.
        tagline : Optional[str]
            Application tagline shown to users during OAuth2 consent.
        tags : Optional[List[str]]
            Application tags shown to users during OAuth2 consent. Maximum of 100 tags are allowed, each up to 64 characters long.
        images : Optional[List[str]]
            Application image URLs shown to users during OAuth2 consent. Maximum of 100 images are allowed.
        support_url : Optional[str]
            Application support URL shown to users during OAuth2 consent.
        data_deletion_url : Optional[str]
            Application data deletion URL shown to users during OAuth2 consent.
        post_logout_redirect_uris : Optional[List[str]]
            Post-logout redirect URIs for OpenID Connect RP-Initiated Logout (array of valid URLs). After ending the user session, the logout endpoint only redirects to URIs in this list.
        enabled : Optional[bool]
            Is application enabled?
        type : Optional[str]
            OAuth2 client type. Use `public` for SPAs, mobile, and native apps that cannot keep a `client_secret` — PKCE is then required at the token endpoint. Use `confidential` for server-side clients that present a `client_secret`. Defaults to `confidential`.
        device_flow : Optional[bool]
            Allow this client to use the OAuth2 Device Authorization Grant (RFC 8628) for input-constrained devices such as TVs and CLIs. Defaults to false.
        team_id : Optional[str]
            Team unique ID.
        
        Returns
        -------
        App
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if redirect_uris is None:
            raise AppwriteException('Missing required parameter: "redirect_uris"')


        api_params['appId'] = self._normalize_value(app_id)
        api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if client_uri is not None:
            api_params['clientUri'] = self._normalize_value(client_uri)
        if logo_uri is not None:
            api_params['logoUri'] = self._normalize_value(logo_uri)
        if privacy_policy_url is not None:
            api_params['privacyPolicyUrl'] = self._normalize_value(privacy_policy_url)
        if terms_url is not None:
            api_params['termsUrl'] = self._normalize_value(terms_url)
        if contacts is not None:
            api_params['contacts'] = self._normalize_value(contacts)
        if tagline is not None:
            api_params['tagline'] = self._normalize_value(tagline)
        if tags is not None:
            api_params['tags'] = self._normalize_value(tags)
        if images is not None:
            api_params['images'] = self._normalize_value(images)
        if support_url is not None:
            api_params['supportUrl'] = self._normalize_value(support_url)
        if data_deletion_url is not None:
            api_params['dataDeletionUrl'] = self._normalize_value(data_deletion_url)
        api_params['redirectUris'] = self._normalize_value(redirect_uris)
        if post_logout_redirect_uris is not None:
            api_params['postLogoutRedirectUris'] = self._normalize_value(post_logout_redirect_uris)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if device_flow is not None:
            api_params['deviceFlow'] = self._normalize_value(device_flow)
        if team_id is not None:
            api_params['teamId'] = self._normalize_value(team_id)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=App)


    def get(
        self,
        app_id: str
    ) -> App:
        """
        Get an application by its unique ID.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        
        Returns
        -------
        App
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=App)


    def update(
        self,
        app_id: str,
        name: str,
        description: Optional[str] = None,
        client_uri: Optional[str] = None,
        logo_uri: Optional[str] = None,
        privacy_policy_url: Optional[str] = None,
        terms_url: Optional[str] = None,
        contacts: Optional[List[str]] = None,
        tagline: Optional[str] = None,
        tags: Optional[List[str]] = None,
        images: Optional[List[str]] = None,
        support_url: Optional[str] = None,
        data_deletion_url: Optional[str] = None,
        enabled: Optional[bool] = None,
        redirect_uris: Optional[List[str]] = None,
        post_logout_redirect_uris: Optional[List[str]] = None,
        type: Optional[str] = None,
        device_flow: Optional[bool] = None
    ) -> App:
        """
        Update an application by its unique ID.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        name : str
            Application name.
        description : Optional[str]
            Application description shown to users during OAuth2 consent.
        client_uri : Optional[str]
            Application homepage URL shown to users during OAuth2 consent.
        logo_uri : Optional[str]
            Application logo URL shown to users during OAuth2 consent.
        privacy_policy_url : Optional[str]
            Application privacy policy URL shown to users during OAuth2 consent.
        terms_url : Optional[str]
            Application terms of service URL shown to users during OAuth2 consent.
        contacts : Optional[List[str]]
            Application support or security contact emails. Maximum of 100 contacts are allowed.
        tagline : Optional[str]
            Application tagline shown to users during OAuth2 consent.
        tags : Optional[List[str]]
            Application tags shown to users during OAuth2 consent. Maximum of 100 tags are allowed, each up to 64 characters long.
        images : Optional[List[str]]
            Application image URLs shown to users during OAuth2 consent. Maximum of 100 images are allowed.
        support_url : Optional[str]
            Application support URL shown to users during OAuth2 consent.
        data_deletion_url : Optional[str]
            Application data deletion URL shown to users during OAuth2 consent.
        enabled : Optional[bool]
            Is application enabled?
        redirect_uris : Optional[List[str]]
            Redirect URIs (array of valid URLs).
        post_logout_redirect_uris : Optional[List[str]]
            Post-logout redirect URIs for OpenID Connect RP-Initiated Logout (array of valid URLs). After ending the user session, the logout endpoint only redirects to URIs in this list.
        type : Optional[str]
            OAuth2 client type. Use `public` for SPAs, mobile, and native apps that cannot keep a `client_secret` — PKCE is then required at the token endpoint. Use `confidential` for server-side clients that present a `client_secret`. Defaults to `confidential`.
        device_flow : Optional[bool]
            Allow this client to use the OAuth2 Device Authorization Grant (RFC 8628) for input-constrained devices such as TVs and CLIs. Defaults to false.
        
        Returns
        -------
        App
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))

        api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if client_uri is not None:
            api_params['clientUri'] = self._normalize_value(client_uri)
        if logo_uri is not None:
            api_params['logoUri'] = self._normalize_value(logo_uri)
        if privacy_policy_url is not None:
            api_params['privacyPolicyUrl'] = self._normalize_value(privacy_policy_url)
        if terms_url is not None:
            api_params['termsUrl'] = self._normalize_value(terms_url)
        if contacts is not None:
            api_params['contacts'] = self._normalize_value(contacts)
        if tagline is not None:
            api_params['tagline'] = self._normalize_value(tagline)
        if tags is not None:
            api_params['tags'] = self._normalize_value(tags)
        if images is not None:
            api_params['images'] = self._normalize_value(images)
        if support_url is not None:
            api_params['supportUrl'] = self._normalize_value(support_url)
        if data_deletion_url is not None:
            api_params['dataDeletionUrl'] = self._normalize_value(data_deletion_url)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if redirect_uris is not None:
            api_params['redirectUris'] = self._normalize_value(redirect_uris)
        if post_logout_redirect_uris is not None:
            api_params['postLogoutRedirectUris'] = self._normalize_value(post_logout_redirect_uris)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if device_flow is not None:
            api_params['deviceFlow'] = self._normalize_value(device_flow)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=App)


    def delete(
        self,
        app_id: str
    ) -> Dict[str, Any]:
        """
        Delete an application by its unique ID.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return response


    def update_labels(
        self,
        app_id: str,
        labels: List[str]
    ) -> App:
        """
        Update the labels of an application. Labels are read-only for clients; only a server SDK using a project API key can set them. Replaces the previous labels.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        labels : List[str]
            Array of application labels. Replaces the previous labels. Maximum of 1000 labels are allowed, each up to 36 alphanumeric characters long.
        
        Returns
        -------
        App
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}/labels'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        if labels is None:
            raise AppwriteException('Missing required parameter: "labels"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))

        api_params['labels'] = self._normalize_value(labels)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=App)


    def list_secrets(
        self,
        app_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> AppSecretList:
        """
        List client secrets for an application.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        AppSecretList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}/secrets'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppSecretList)


    def create_secret(
        self,
        app_id: str
    ) -> AppSecretPlaintext:
        """
        Create a new client secret for an application.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        
        Returns
        -------
        AppSecretPlaintext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}/secrets'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))


        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppSecretPlaintext)


    def get_secret(
        self,
        app_id: str,
        secret_id: str
    ) -> AppSecret:
        """
        Get an application client secret by its unique ID.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        secret_id : str
            Secret unique ID.
        
        Returns
        -------
        AppSecret
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}/secrets/{secretId}'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        if secret_id is None:
            raise AppwriteException('Missing required parameter: "secret_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))
        api_path = api_path.replace('{secretId}', str(self._normalize_value(secret_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AppSecret)


    def delete_secret(
        self,
        app_id: str,
        secret_id: str
    ) -> Dict[str, Any]:
        """
        Delete an application client secret by its unique ID.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        secret_id : str
            Secret unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}/secrets/{secretId}'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        if secret_id is None:
            raise AppwriteException('Missing required parameter: "secret_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))
        api_path = api_path.replace('{secretId}', str(self._normalize_value(secret_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return response


    def update_team(
        self,
        app_id: str,
        team_id: str
    ) -> App:
        """
        Transfer an application to another team by its unique ID.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        team_id : str
            Team ID of the team to transfer application to.
        
        Returns
        -------
        App
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}/team'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))

        api_params['teamId'] = self._normalize_value(team_id)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=App)


    def delete_tokens(
        self,
        app_id: str
    ) -> Dict[str, Any]:
        """
        Revoke all tokens for an application by its unique ID.

        Parameters
        ----------
        app_id : str
            Application unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/apps/{appId}/tokens'
        api_params = {}
        if app_id is None:
            raise AppwriteException('Missing required parameter: "app_id"')

        api_path = api_path.replace('{appId}', str(self._normalize_value(app_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return response

