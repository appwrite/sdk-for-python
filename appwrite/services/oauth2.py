from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.oauth2_approve import Oauth2Approve
from ..models.oauth2_authorize import Oauth2Authorize
from ..models.oauth2_device_authorization import Oauth2DeviceAuthorization
from ..models.oauth2_grant import Oauth2Grant
from ..models.oauth2_organization_list import Oauth2OrganizationList
from ..models.oauth2_par import Oauth2PAR
from ..models.oauth2_project_list import Oauth2ProjectList
from ..models.oauth2_reject import Oauth2Reject
from ..models.oauth2_token import Oauth2Token

class Oauth2(Service):

    def __init__(self, client) -> None:
        super(Oauth2, self).__init__(client)

    def approve(
        self,
        grant_id: str,
        authorization_details: Optional[str] = None,
        scope: Optional[str] = None
    ) -> Oauth2Approve:
        """
        Approve an OAuth2 grant after the user gives consent. Returns the `redirectUrl` the end user should be sent to. The consent screen may optionally pass enriched `authorization_details` to record the concrete resources the user selected. You can pass Accept header of `application/json` to receive a JSON response instead of a redirect.

        Parameters
        ----------
        grant_id : str
            Grant ID made during authorization, provided to consent screen in URL search params.
        authorization_details : Optional[str]
            Enriched `authorization_details` the user consented to, replacing what the client requested. Each entry must use a `type` the project accepts. Optional; omit to keep the originally requested details.
        scope : Optional[str]
            Space-separated scopes the user consented to. Must be a subset of the scopes originally requested; identity scopes such as `openid` are always retained. Optional; omit to keep the originally requested scopes.
        
        Returns
        -------
        Oauth2Approve
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/approve'
        api_params = {}
        if grant_id is None:
            raise AppwriteException('Missing required parameter: "grant_id"')

        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        api_params['grant_id'] = self._normalize_value(grant_id)
        if authorization_details is not None:
            api_params['authorization_details'] = self._normalize_value(authorization_details)
        if scope is not None:
            api_params['scope'] = self._normalize_value(scope)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2Approve)


    def authorize(
        self,
        client_id: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        response_type: Optional[str] = None,
        scope: Optional[str] = None,
        state: Optional[str] = None,
        nonce: Optional[str] = None,
        code_challenge: Optional[str] = None,
        code_challenge_method: Optional[str] = None,
        prompt: Optional[str] = None,
        max_age: Optional[float] = None,
        authorization_details: Optional[str] = None,
        resource: Optional[str] = None,
        audience: Optional[str] = None,
        request_uri: Optional[str] = None
    ) -> Oauth2Authorize:
        """
        Begin the OAuth2 authorization flow. When called without a session, the user is redirected to the consent screen without grant ID. When called with a session, the redirect URL includes param for grant ID. You can pass Accept header of `application/json` to receive a JSON response instead of a redirect.

        Parameters
        ----------
        client_id : Optional[str]
            OAuth2 client ID.
        redirect_uri : Optional[str]
            Redirect URI where visitor will be redirected after authorization, whether successful or not.
        response_type : Optional[str]
            OAuth2 / OIDC response type. One of `code` (Authorization Code Flow), `id_token` (Implicit Flow, OIDC login only), or `code id_token` (Hybrid Flow).
        scope : Optional[str]
            Space-separated OAuth2 scopes. Can include project scopes, and built-in scopes: `openid`, `email`, `profile`, `phone`.
        state : Optional[str]
            OAuth2 state. You receive this back in the redirect URI.
        nonce : Optional[str]
            OIDC nonce parameter to prevent replay attacks. Required when response_type includes `id_token`.
        code_challenge : Optional[str]
            PKCE code challenge. Required when OAuth2 app is public.
        code_challenge_method : Optional[str]
            PKCE code challenge method. Required when OAuth2 app is public.
        prompt : Optional[str]
            OIDC prompt parameter for customization of consent screen. Space-separated list of: none, login, consent, select_account.
        max_age : Optional[float]
            OIDC max_age paraleter for customization of consent screen. Maximum allowable elapsed time in seconds since the user last authenticated. If exceeded, re-authentication is required.
        authorization_details : Optional[str]
            Rich authorization request. JSON array of objects, each with a `type` and project-defined fields
        resource : Optional[str]
            RFC 8707 resource indicator URI or URI list. Each value must be an absolute URI without a fragment.
        audience : Optional[str]
            Compatibility alias for a single OAuth2 resource indicator URI.
        request_uri : Optional[str]
            OAuth2 authorization request handle returned by the pushed authorization request endpoint.
        
        Returns
        -------
        Oauth2Authorize
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/authorize'
        api_params = {}
        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        if client_id is not None:
            api_params['client_id'] = self._normalize_value(client_id)
        if redirect_uri is not None:
            api_params['redirect_uri'] = self._normalize_value(redirect_uri)
        if response_type is not None:
            api_params['response_type'] = self._normalize_value(response_type)
        if scope is not None:
            api_params['scope'] = self._normalize_value(scope)
        if state is not None:
            api_params['state'] = self._normalize_value(state)
        if nonce is not None:
            api_params['nonce'] = self._normalize_value(nonce)
        if code_challenge is not None:
            api_params['code_challenge'] = self._normalize_value(code_challenge)
        if code_challenge_method is not None:
            api_params['code_challenge_method'] = self._normalize_value(code_challenge_method)
        if prompt is not None:
            api_params['prompt'] = self._normalize_value(prompt)
        if max_age is not None:
            api_params['max_age'] = self._normalize_value(max_age)
        if authorization_details is not None:
            api_params['authorization_details'] = self._normalize_value(authorization_details)
        if resource is not None:
            api_params['resource'] = self._normalize_value(resource)
        if audience is not None:
            api_params['audience'] = self._normalize_value(audience)
        if request_uri is not None:
            api_params['request_uri'] = self._normalize_value(request_uri)

        response = self.client.call('get', api_path, {
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2Authorize)


    def create_device_authorization(
        self,
        client_id: Optional[str] = None,
        scope: Optional[str] = None,
        authorization_details: Optional[str] = None,
        resource: Optional[str] = None,
        audience: Optional[str] = None
    ) -> Oauth2DeviceAuthorization:
        """
        Start the OAuth2 Device Authorization Grant. Returns the device code, user code, verification URL, expiration, and polling interval.

        Parameters
        ----------
        client_id : Optional[str]
            OAuth2 client ID.
        scope : Optional[str]
            Space-separated OAuth2 scopes. Can include project scopes, and built-in scopes: `openid`, `email`, `profile`.
        authorization_details : Optional[str]
            Rich authorization request. JSON array of objects, each with a `type` and project-defined fields
        resource : Optional[str]
            RFC 8707 resource indicator URI or URI list. Each value must be an absolute URI without a fragment.
        audience : Optional[str]
            Compatibility alias for a single OAuth2 resource indicator URI.
        
        Returns
        -------
        Oauth2DeviceAuthorization
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/device_authorization'
        api_params = {}
        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        if client_id is not None:
            api_params['client_id'] = self._normalize_value(client_id)
        if scope is not None:
            api_params['scope'] = self._normalize_value(scope)
        if authorization_details is not None:
            api_params['authorization_details'] = self._normalize_value(authorization_details)
        if resource is not None:
            api_params['resource'] = self._normalize_value(resource)
        if audience is not None:
            api_params['audience'] = self._normalize_value(audience)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2DeviceAuthorization)


    def create_grant(
        self,
        user_code: str
    ) -> Oauth2Grant:
        """
        Exchange a device flow user code for an OAuth2 grant. The authenticated user is bound to the pending grant. Pass the returned grant ID to the get grant endpoint to render the consent screen, then to the approve or reject endpoint to complete the flow.

        Parameters
        ----------
        user_code : str
            User code displayed on the device.
        
        Returns
        -------
        Oauth2Grant
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/grants'
        api_params = {}
        if user_code is None:
            raise AppwriteException('Missing required parameter: "user_code"')

        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        api_params['user_code'] = self._normalize_value(user_code)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2Grant)


    def get_grant(
        self,
        grant_id: str
    ) -> Oauth2Grant:
        """
        Get an OAuth2 grant by its ID. Used by the consent screen to display the details of the authorization the user is being asked to approve. A grant can only be read by the user it belongs to, or by server SDK.

        Parameters
        ----------
        grant_id : str
            Grant ID made during authorization, provided to consent screen in URL search params.
        
        Returns
        -------
        Oauth2Grant
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/grants/{grant_id}'
        api_params = {}
        if grant_id is None:
            raise AppwriteException('Missing required parameter: "grant_id"')

        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))
        api_path = api_path.replace('{grant_id}', str(self._normalize_value(grant_id)))


        response = self.client.call('get', api_path, {
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2Grant)


    def list_organizations(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None
    ) -> Oauth2OrganizationList:
        """
        List the organizations the OAuth2 access token can access. Resolves the token's `organization` authorization details, expanding the `*` wildcard into the concrete set of organizations the user can see.

        Parameters
        ----------
        limit : Optional[float]
            Maximum number of organizations to return. Between 1 and 5000.
        offset : Optional[float]
            Number of organizations to skip before returning results. Used for pagination.
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Oauth2OrganizationList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/organizations'
        api_params = {}
        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if search is not None:
            api_params['search'] = self._normalize_value(search)

        response = self.client.call('get', api_path, {
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2OrganizationList)


    def create_par(
        self,
        client_id: str,
        redirect_uri: str,
        response_type: str,
        scope: Optional[str] = None,
        state: Optional[str] = None,
        nonce: Optional[str] = None,
        code_challenge: Optional[str] = None,
        code_challenge_method: Optional[str] = None,
        prompt: Optional[str] = None,
        max_age: Optional[float] = None,
        authorization_details: Optional[str] = None,
        resource: Optional[str] = None,
        audience: Optional[str] = None
    ) -> Oauth2PAR:
        """
        Store an OAuth2 authorization request server-side and receive a short-lived request_uri handle for the authorize endpoint.

        Parameters
        ----------
        client_id : str
            OAuth2 client ID.
        redirect_uri : str
            Redirect URI where visitor will be redirected after authorization, whether successful or not.
        response_type : str
            OAuth2 / OIDC response type.
        scope : Optional[str]
            Space-separated OAuth2 scopes. Can include project scopes, and built-in scopes: `openid`, `email`, `profile`, `phone`.
        state : Optional[str]
            OAuth2 state. You receive this back in the redirect URI.
        nonce : Optional[str]
            OIDC nonce parameter to prevent replay attacks. Required when response_type includes `id_token`.
        code_challenge : Optional[str]
            PKCE code challenge. Required when OAuth2 app is public.
        code_challenge_method : Optional[str]
            PKCE code challenge method. Required when OAuth2 app is public.
        prompt : Optional[str]
            OIDC prompt parameter for customization of consent screen. Space-separated list of: none, login, consent, select_account.
        max_age : Optional[float]
            OIDC max_age parameter for customization of consent screen.
        authorization_details : Optional[str]
            Rich authorization request. JSON array of objects, each with a `type` and project-defined fields
        resource : Optional[str]
            RFC 8707 resource indicator URI or URI list. Each value must be an absolute URI without a fragment.
        audience : Optional[str]
            Compatibility alias for a single OAuth2 resource indicator URI.
        
        Returns
        -------
        Oauth2PAR
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/par'
        api_params = {}
        if client_id is None:
            raise AppwriteException('Missing required parameter: "client_id"')

        if redirect_uri is None:
            raise AppwriteException('Missing required parameter: "redirect_uri"')

        if response_type is None:
            raise AppwriteException('Missing required parameter: "response_type"')

        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        api_params['client_id'] = self._normalize_value(client_id)
        api_params['redirect_uri'] = self._normalize_value(redirect_uri)
        api_params['response_type'] = self._normalize_value(response_type)
        if scope is not None:
            api_params['scope'] = self._normalize_value(scope)
        if state is not None:
            api_params['state'] = self._normalize_value(state)
        if nonce is not None:
            api_params['nonce'] = self._normalize_value(nonce)
        if code_challenge is not None:
            api_params['code_challenge'] = self._normalize_value(code_challenge)
        if code_challenge_method is not None:
            api_params['code_challenge_method'] = self._normalize_value(code_challenge_method)
        if prompt is not None:
            api_params['prompt'] = self._normalize_value(prompt)
        api_params['max_age'] = self._normalize_value(max_age)
        if authorization_details is not None:
            api_params['authorization_details'] = self._normalize_value(authorization_details)
        if resource is not None:
            api_params['resource'] = self._normalize_value(resource)
        if audience is not None:
            api_params['audience'] = self._normalize_value(audience)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2PAR)


    def list_projects(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        search: Optional[str] = None
    ) -> Oauth2ProjectList:
        """
        List the projects the OAuth2 access token can access. Resolves the token's `project` authorization details, expanding the `*` wildcard into the concrete set of projects the user can see.

        Parameters
        ----------
        limit : Optional[float]
            Maximum number of projects to return. Between 1 and 5000.
        offset : Optional[float]
            Number of projects to skip before returning results. Used for pagination.
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Oauth2ProjectList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/projects'
        api_params = {}
        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if search is not None:
            api_params['search'] = self._normalize_value(search)

        response = self.client.call('get', api_path, {
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2ProjectList)


    def reject(
        self,
        grant_id: str
    ) -> Oauth2Reject:
        """
        Reject an OAuth2 grant when the user denies consent. Returns the `redirectUrl` the end user should be sent to with an `access_denied` error. You can pass Accept header of `application/json` to receive a JSON response instead of a redirect.

        Parameters
        ----------
        grant_id : str
            Grant ID made during authorization, provided to consent screen in URL search params.
        
        Returns
        -------
        Oauth2Reject
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/reject'
        api_params = {}
        if grant_id is None:
            raise AppwriteException('Missing required parameter: "grant_id"')

        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        api_params['grant_id'] = self._normalize_value(grant_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2Reject)


    def revoke(
        self,
        token: str,
        token_type_hint: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Revoke an OAuth2 access token or refresh token.

        Parameters
        ----------
        token : str
            The access or refresh token to revoke.
        token_type_hint : Optional[str]
            Type of token to revoke (access_token or refresh_token).
        client_id : Optional[str]
            OAuth2 client ID.
        client_secret : Optional[str]
            OAuth2 client secret. Required for confidential apps; omitted for public apps.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/revoke'
        api_params = {}
        if token is None:
            raise AppwriteException('Missing required parameter: "token"')

        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        api_params['token'] = self._normalize_value(token)
        if token_type_hint is not None:
            api_params['token_type_hint'] = self._normalize_value(token_type_hint)
        if client_id is not None:
            api_params['client_id'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['client_secret'] = self._normalize_value(client_secret)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return response


    def create_token(
        self,
        grant_type: str,
        code: Optional[str] = None,
        refresh_token: Optional[str] = None,
        device_code: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code_verifier: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        resource: Optional[str] = None,
        audience: Optional[str] = None
    ) -> Oauth2Token:
        """
        Exchange an OAuth2 authorization code, refresh token, or device code for access and refresh tokens.

        Parameters
        ----------
        grant_type : str
            OAuth2 grant type. Can be one of: `authorization_code`, `refresh_token`, `urn:ietf:params:oauth:grant-type:device_code`.
        code : Optional[str]
            Authorization code to be exchanged for access and refresh tokens. Required for `authorization_code` grant type.
        refresh_token : Optional[str]
            Refresh token to be exchanged for a new access and refresh tokens. Required for `refresh_token` grant type.
        device_code : Optional[str]
            Device code obtained from the device authorization endpoint. Required for `urn:ietf:params:oauth:grant-type:device_code` grant type.
        client_id : Optional[str]
            OAuth2 client ID.
        client_secret : Optional[str]
            OAuth2 client secret. Required for confidential apps.
        code_verifier : Optional[str]
            PKCE code verifier. Required for public apps.
        redirect_uri : Optional[str]
            Redirect URI. Required for `authorization_code` grant type.
        resource : Optional[str]
            RFC 8707 resource indicator URI or URI list. Each value must be an absolute URI without a fragment.
        audience : Optional[str]
            Compatibility alias for a single OAuth2 resource indicator URI.
        
        Returns
        -------
        Oauth2Token
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/oauth2/{project_id}/token'
        api_params = {}
        if grant_type is None:
            raise AppwriteException('Missing required parameter: "grant_type"')

        api_path = api_path.replace('{project_id}', str(self._normalize_value(self.client.get_config('project'))))

        api_params['grant_type'] = self._normalize_value(grant_type)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if refresh_token is not None:
            api_params['refresh_token'] = self._normalize_value(refresh_token)
        if device_code is not None:
            api_params['device_code'] = self._normalize_value(device_code)
        if client_id is not None:
            api_params['client_id'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['client_secret'] = self._normalize_value(client_secret)
        if code_verifier is not None:
            api_params['code_verifier'] = self._normalize_value(code_verifier)
        if redirect_uri is not None:
            api_params['redirect_uri'] = self._normalize_value(redirect_uri)
        if resource is not None:
            api_params['resource'] = self._normalize_value(resource)
        if audience is not None:
            api_params['audience'] = self._normalize_value(audience)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Oauth2Token)

