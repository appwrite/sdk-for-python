from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.project import Project as ProjectModel
from ..enums.project_auth_method_id import ProjectAuthMethodId
from ..models.key_list import KeyList
from ..enums.project_key_scopes import ProjectKeyScopes
from ..models.key import Key
from ..models.ephemeral_key import EphemeralKey
from ..models.mock_number_list import MockNumberList
from ..models.mock_number import MockNumber
from ..models.o_auth2_provider_list import OAuth2ProviderList
from ..models.o_auth2_amazon import OAuth2Amazon
from ..models.o_auth2_apple import OAuth2Apple
from ..models.o_auth2_appwrite import OAuth2Appwrite
from ..models.o_auth2_auth0 import OAuth2Auth0
from ..models.o_auth2_authentik import OAuth2Authentik
from ..models.o_auth2_autodesk import OAuth2Autodesk
from ..models.o_auth2_bitbucket import OAuth2Bitbucket
from ..models.o_auth2_bitly import OAuth2Bitly
from ..models.o_auth2_box import OAuth2Box
from ..models.o_auth2_dailymotion import OAuth2Dailymotion
from ..models.o_auth2_discord import OAuth2Discord
from ..models.o_auth2_disqus import OAuth2Disqus
from ..models.o_auth2_dropbox import OAuth2Dropbox
from ..models.o_auth2_etsy import OAuth2Etsy
from ..models.o_auth2_facebook import OAuth2Facebook
from ..models.o_auth2_figma import OAuth2Figma
from ..models.o_auth2_fusion_auth import OAuth2FusionAuth
from ..models.o_auth2_github import OAuth2Github
from ..models.o_auth2_gitlab import OAuth2Gitlab
from ..enums.project_o_auth2_google_prompt import ProjectOAuth2GooglePrompt
from ..models.o_auth2_google import OAuth2Google
from ..models.o_auth2_keycloak import OAuth2Keycloak
from ..models.o_auth2_kick import OAuth2Kick
from ..models.o_auth2_linkedin import OAuth2Linkedin
from ..models.o_auth2_microsoft import OAuth2Microsoft
from ..models.o_auth2_notion import OAuth2Notion
from ..enums.project_o_auth2_oidc_prompt import ProjectOAuth2OidcPrompt
from ..models.o_auth2_oidc import OAuth2Oidc
from ..models.o_auth2_okta import OAuth2Okta
from ..models.o_auth2_paypal import OAuth2Paypal
from ..models.o_auth2_podio import OAuth2Podio
from ..models.o_auth2_salesforce import OAuth2Salesforce
from ..models.o_auth2_slack import OAuth2Slack
from ..models.o_auth2_spotify import OAuth2Spotify
from ..models.o_auth2_stripe import OAuth2Stripe
from ..models.o_auth2_tradeshift import OAuth2Tradeshift
from ..models.o_auth2_twitch import OAuth2Twitch
from ..models.o_auth2_word_press import OAuth2WordPress
from ..models.o_auth2_x import OAuth2X
from ..models.o_auth2_yahoo import OAuth2Yahoo
from ..models.o_auth2_yandex import OAuth2Yandex
from ..models.o_auth2_zoho import OAuth2Zoho
from ..models.o_auth2_zoom import OAuth2Zoom
from ..enums.project_o_auth_provider_id import ProjectOAuthProviderId
from ..models.platform_list import PlatformList
from ..models.platform_android import PlatformAndroid
from ..models.platform_apple import PlatformApple
from ..models.platform_linux import PlatformLinux
from ..models.platform_web import PlatformWeb
from ..models.platform_windows import PlatformWindows
from ..models.policy_list import PolicyList
from ..models.policy_password_strength import PolicyPasswordStrength
from ..enums.project_policy_id import ProjectPolicyId
from ..models.policy_password_dictionary import PolicyPasswordDictionary
from ..models.policy_password_history import PolicyPasswordHistory
from ..models.policy_password_personal_data import PolicyPasswordPersonalData
from ..models.policy_session_alert import PolicySessionAlert
from ..models.policy_session_duration import PolicySessionDuration
from ..models.policy_session_invalidation import PolicySessionInvalidation
from ..models.policy_session_limit import PolicySessionLimit
from ..models.policy_user_limit import PolicyUserLimit
from ..models.policy_membership_privacy import PolicyMembershipPrivacy
from ..models.policy_deny_aliased_email import PolicyDenyAliasedEmail
from ..models.policy_deny_disposable_email import PolicyDenyDisposableEmail
from ..models.policy_deny_free_email import PolicyDenyFreeEmail
from ..models.policy_deny_corporate_email import PolicyDenyCorporateEmail
from ..enums.project_protocol_id import ProjectProtocolId
from ..enums.project_service_id import ProjectServiceId
from ..enums.project_smtp_secure import ProjectSMTPSecure
from ..models.email_template_list import EmailTemplateList
from ..enums.project_email_template_id import ProjectEmailTemplateId
from ..enums.project_email_template_locale import ProjectEmailTemplateLocale
from ..models.email_template import EmailTemplate
from ..models.variable_list import VariableList
from ..models.variable import Variable

class Project(Service):

    def __init__(self, client) -> None:
        super(Project, self).__init__(client)

    def get(
        self
    ) -> ProjectModel:
        """
        Get a project.

        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project'
        api_params = {}

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def delete(
        self
    ) -> Dict[str, Any]:
        """
        Delete a project.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project'
        api_params = {}

        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_auth_method(
        self,
        method_id: ProjectAuthMethodId,
        enabled: bool
    ) -> ProjectModel:
        """
        Update properties of a specific auth method. Use this endpoint to enable or disable a method in your project. 

        Parameters
        ----------
        method_id : ProjectAuthMethodId
            Auth Method ID. Possible values: email-password,magic-url,email-otp,anonymous,invites,jwt,phone
        enabled : bool
            Auth method status.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/auth-methods/{methodId}'
        api_params = {}
        if method_id is None:
            raise AppwriteException('Missing required parameter: "method_id"')

        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')

        api_path = api_path.replace('{methodId}', str(self._normalize_value(method_id)))

        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=KeyList)


    def create_key(
        self,
        key_id: str,
        name: str,
        scopes: List[ProjectKeyScopes],
        expire: Optional[str] = None
    ) -> Key:
        """
        Create a new API key. It's recommended to have multiple API keys with strict scopes for separate functions within your project.
        
        You can also create an ephemeral API key if you need a short-lived key instead.

        Parameters
        ----------
        key_id : str
            Key ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Key name. Max length: 128 chars.
        scopes : List[ProjectKeyScopes]
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
        if expire is not None:
            api_params['expire'] = self._normalize_value(expire)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Key)


    def create_ephemeral_key(
        self,
        scopes: List[ProjectKeyScopes],
        duration: float
    ) -> EphemeralKey:
        """
        Create a new ephemeral API key. It's recommended to have multiple API keys with strict scopes for separate functions within your project.
        
        You can also create a standard API key if you need a longer-lived key instead.

        Parameters
        ----------
        scopes : List[ProjectKeyScopes]
            Key scopes list. Maximum of 200 scopes are allowed.
        duration : float
            Time in seconds before ephemeral key expires. Maximum duration is 3600 seconds.
        
        Returns
        -------
        EphemeralKey
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/keys/ephemeral'
        api_params = {}
        if scopes is None:
            raise AppwriteException('Missing required parameter: "scopes"')

        if duration is None:
            raise AppwriteException('Missing required parameter: "duration"')


        api_params['scopes'] = self._normalize_value(scopes)
        api_params['duration'] = self._normalize_value(duration)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=EphemeralKey)


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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Key)


    def update_key(
        self,
        key_id: str,
        name: str,
        scopes: List[ProjectKeyScopes],
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
        scopes : List[ProjectKeyScopes]
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
            'X-Appwrite-Project': self.client.get_config('project'),
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def list_mock_phones(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> MockNumberList:
        """
        Get a list of all mock phones in the project. This endpoint returns an array of all mock phones and their OTPs.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        MockNumberList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/mock-phones'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MockNumberList)


    def create_mock_phone(
        self,
        number: str,
        otp: str
    ) -> MockNumber:
        """
        Create a new mock phone for your project. Use this endpoint to register a mock phone number and its sign-in OTP for your testers.

        Parameters
        ----------
        number : str
            Phone number to associate with the mock phone. Must be a valid E.164 formatted phone number.
        otp : str
            One-time password (OTP) to associate with the mock phone. Must be a 6-digit numeric code.
        
        Returns
        -------
        MockNumber
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/mock-phones'
        api_params = {}
        if number is None:
            raise AppwriteException('Missing required parameter: "number"')

        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')


        api_params['number'] = self._normalize_value(number)
        api_params['otp'] = self._normalize_value(otp)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MockNumber)


    def get_mock_phone(
        self,
        number: str
    ) -> MockNumber:
        """
        Get a mock phone by its unique number. This endpoint returns the mock phone's OTP.

        Parameters
        ----------
        number : str
            Phone number associated with the mock phone. Must be a valid E.164 formatted phone number.
        
        Returns
        -------
        MockNumber
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/mock-phones/{number}'
        api_params = {}
        if number is None:
            raise AppwriteException('Missing required parameter: "number"')

        api_path = api_path.replace('{number}', str(self._normalize_value(number)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MockNumber)


    def update_mock_phone(
        self,
        number: str,
        otp: str
    ) -> MockNumber:
        """
        Update a mock phone by its unique number. Use this endpoint to update the mock phone's OTP.

        Parameters
        ----------
        number : str
            Phone number associated with the mock phone. Must be a valid E.164 formatted phone number.
        otp : str
            One-time password (OTP) to associate with the mock phone. Must be a 6-digit numeric code.
        
        Returns
        -------
        MockNumber
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/mock-phones/{number}'
        api_params = {}
        if number is None:
            raise AppwriteException('Missing required parameter: "number"')

        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')

        api_path = api_path.replace('{number}', str(self._normalize_value(number)))

        api_params['otp'] = self._normalize_value(otp)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=MockNumber)


    def delete_mock_phone(
        self,
        number: str
    ) -> Dict[str, Any]:
        """
        Delete a mock phone by its unique number. This endpoint removes the mock phone and its OTP configuration from the project.

        Parameters
        ----------
        number : str
            Phone number associated with the mock phone. Must be a valid E.164 formatted phone number.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/mock-phones/{number}'
        api_params = {}
        if number is None:
            raise AppwriteException('Missing required parameter: "number"')

        api_path = api_path.replace('{number}', str(self._normalize_value(number)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_o_auth2_providers(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> OAuth2ProviderList:
        """
        Get a list of all OAuth2 providers supported by the server, along with the project's configuration for each. Credential fields are write-only and always returned empty.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        OAuth2ProviderList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2ProviderList)


    def update_o_auth2_server(
        self,
        enabled: bool,
        authorization_url: str,
        scopes: Optional[List[str]] = None,
        authorization_details_types: Optional[List[str]] = None,
        access_token_duration: Optional[float] = None,
        refresh_token_duration: Optional[float] = None,
        public_access_token_duration: Optional[float] = None,
        public_refresh_token_duration: Optional[float] = None,
        confidential_pkce: Optional[bool] = None,
        verification_url: Optional[str] = None,
        user_code_length: Optional[float] = None,
        user_code_format: Optional[str] = None,
        device_code_duration: Optional[float] = None,
        default_scopes: Optional[List[str]] = None
    ) -> ProjectModel:
        """
        Update the OAuth2 server (OIDC provider) configuration.

        Parameters
        ----------
        enabled : bool
            Enable or disable the OAuth2 server.
        authorization_url : str
            URL to your application with consent screen.
        scopes : Optional[List[str]]
            List of allowed OAuth2 scopes. Maximum of 100 scopes are allowed, each up to 128 characters long.
        authorization_details_types : Optional[List[str]]
            List of accepted `authorization_details` types. Maximum of 100 types are allowed, each up to 128 characters long.
        access_token_duration : Optional[float]
            Access token duration in seconds for confidential clients (server-side apps that authenticate with a client secret). Leave empty to use default 8 hours.
        refresh_token_duration : Optional[float]
            Refresh token duration in seconds for confidential clients (server-side apps that authenticate with a client secret). Leave empty to use default 1 year.
        public_access_token_duration : Optional[float]
            Access token duration in seconds for public clients (SPAs, mobile, and native apps that cannot keep a client secret). Leave empty to use default 1 hour.
        public_refresh_token_duration : Optional[float]
            Refresh token duration in seconds for public clients (SPAs, mobile, and native apps that cannot keep a client secret). Leave empty to use default 30 days.
        confidential_pkce : Optional[bool]
            When enabled, PKCE is required for confidential clients (server-side flows using client_secret). PKCE is always required for public clients regardless of this setting.
        verification_url : Optional[str]
            URL to your application page where users enter the device flow user code. Required to enable the Device Authorization Grant.
        user_code_length : Optional[float]
            Number of characters in the device flow user code, excluding the formatting separator. Shorter codes are easier to type but weaker; pair short codes with short expiry. Leave empty to use default 8.
        user_code_format : Optional[str]
            Character set for device flow user codes: `numeric` (digits only — best for numeric keypads and TV remotes), `alphabetic` (letters only), or `alphanumeric` (letters and digits — highest entropy per character). Defaults to `alphanumeric`.
        device_code_duration : Optional[float]
            Lifetime in seconds of device flow device codes and user codes. Device codes are intentionally short-lived. Leave empty to use default 600.
        default_scopes : Optional[List[str]]
            List of OAuth2 scopes used when an authorization request omits the scope parameter. Every default scope must also be allowed by the OAuth2 server. Maximum of 100 scopes are allowed, each up to 128 characters long.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2-server'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')

        if authorization_url is None:
            raise AppwriteException('Missing required parameter: "authorization_url"')


        api_params['enabled'] = self._normalize_value(enabled)
        api_params['authorizationUrl'] = self._normalize_value(authorization_url)
        if scopes is not None:
            api_params['scopes'] = self._normalize_value(scopes)
        if authorization_details_types is not None:
            api_params['authorizationDetailsTypes'] = self._normalize_value(authorization_details_types)
        if access_token_duration is not None:
            api_params['accessTokenDuration'] = self._normalize_value(access_token_duration)
        if refresh_token_duration is not None:
            api_params['refreshTokenDuration'] = self._normalize_value(refresh_token_duration)
        if public_access_token_duration is not None:
            api_params['publicAccessTokenDuration'] = self._normalize_value(public_access_token_duration)
        if public_refresh_token_duration is not None:
            api_params['publicRefreshTokenDuration'] = self._normalize_value(public_refresh_token_duration)
        if confidential_pkce is not None:
            api_params['confidentialPkce'] = self._normalize_value(confidential_pkce)
        if verification_url is not None:
            api_params['verificationUrl'] = self._normalize_value(verification_url)
        if user_code_length is not None:
            api_params['userCodeLength'] = self._normalize_value(user_code_length)
        if user_code_format is not None:
            api_params['userCodeFormat'] = self._normalize_value(user_code_format)
        if device_code_duration is not None:
            api_params['deviceCodeDuration'] = self._normalize_value(device_code_duration)
        if default_scopes is not None:
            api_params['defaultScopes'] = self._normalize_value(default_scopes)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_o_auth2_amazon(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Amazon:
        """
        Update the project OAuth2 Amazon configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Amazon OAuth2 app. For example: amzn1.application-oa2-client.87400c00000000000000000000063d5b2
        client_secret : Optional[str]
            'Client Secret' of Amazon OAuth2 app. For example: 79ffe4000000000000000000000000000000000000000000000000000002de55
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Amazon
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/amazon'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Amazon)


    def update_o_auth2_apple(
        self,
        service_id: Optional[str] = None,
        key_id: Optional[str] = None,
        team_id: Optional[str] = None,
        p8_file: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Apple:
        """
        Update the project OAuth2 Apple configuration.

        Parameters
        ----------
        service_id : Optional[str]
            'Service ID' of Apple OAuth2 app. For example: ip.appwrite.app.web
        key_id : Optional[str]
            'Key ID' of Apple OAuth2 app. For example: P4000000N8
        team_id : Optional[str]
            'Team ID' of Apple OAuth2 app. For example: D4000000R6
        p8_file : Optional[str]
            Contents of the Apple OAuth2 app .p8 private key file. The secret key wrapped by the PEM markers is 200 characters long. For example: -----BEGIN PRIVATE KEY-----MIGTAg...jy2Xbna-----END PRIVATE KEY-----
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Apple
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/apple'
        api_params = {}

        if service_id is not None:
            api_params['serviceId'] = self._normalize_value(service_id)
        if key_id is not None:
            api_params['keyId'] = self._normalize_value(key_id)
        if team_id is not None:
            api_params['teamId'] = self._normalize_value(team_id)
        if p8_file is not None:
            api_params['p8File'] = self._normalize_value(p8_file)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Apple)


    def update_o_auth2_appwrite(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Appwrite:
        """
        Update the project OAuth2 Appwrite configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Appwrite OAuth2 app. For example: 6a42000000000000b5a0
        client_secret : Optional[str]
            'Client Secret' of Appwrite OAuth2 app. For example: b86afd000000000000000000000000000000000000000000000000000ced5f93
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Appwrite
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/appwrite'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Appwrite)


    def update_o_auth2_auth0(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        endpoint: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Auth0:
        """
        Update the project OAuth2 Auth0 configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Auth0 OAuth2 app. For example: OaOkIA000000000000000000005KLSYq
        client_secret : Optional[str]
            'Client Secret' of Auth0 OAuth2 app. For example: zXz0000-00000000000000000000000000000-00000000000000000000PJafnF
        endpoint : Optional[str]
            Domain of Auth0 instance. For example: example.us.auth0.com
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Auth0
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/auth0'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if endpoint is not None:
            api_params['endpoint'] = self._normalize_value(endpoint)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Auth0)


    def update_o_auth2_authentik(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        endpoint: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Authentik:
        """
        Update the project OAuth2 Authentik configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Authentik OAuth2 app. For example: dTKOPa0000000000000000000000000000e7G8hv
        client_secret : Optional[str]
            'Client Secret' of Authentik OAuth2 app. For example: ntQadq000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Hp5WK
        endpoint : Optional[str]
            Domain of Authentik instance. For example: example.authentik.com
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Authentik
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/authentik'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if endpoint is not None:
            api_params['endpoint'] = self._normalize_value(endpoint)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Authentik)


    def update_o_auth2_autodesk(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Autodesk:
        """
        Update the project OAuth2 Autodesk configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Autodesk OAuth2 app. For example: 5zw90v00000000000000000000kVYXN7
        client_secret : Optional[str]
            'Client Secret' of Autodesk OAuth2 app. For example: 7I000000000000MW
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Autodesk
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/autodesk'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Autodesk)


    def update_o_auth2_bitbucket(
        self,
        key: Optional[str] = None,
        secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Bitbucket:
        """
        Update the project OAuth2 Bitbucket configuration.

        Parameters
        ----------
        key : Optional[str]
            'Key' of Bitbucket OAuth2 app. For example: Knt70000000000ByRc
        secret : Optional[str]
            'Secret' of Bitbucket OAuth2 app. For example: NMfLZJ00000000000000000000TLQdDx
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Bitbucket
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/bitbucket'
        api_params = {}

        if key is not None:
            api_params['key'] = self._normalize_value(key)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Bitbucket)


    def update_o_auth2_bitly(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Bitly:
        """
        Update the project OAuth2 Bitly configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Bitly OAuth2 app. For example: d95151000000000000000000000000000067af9b
        client_secret : Optional[str]
            'Client Secret' of Bitly OAuth2 app. For example: a13e250000000000000000000000000000d73095
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Bitly
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/bitly'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Bitly)


    def update_o_auth2_box(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Box:
        """
        Update the project OAuth2 Box configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Box OAuth2 app. For example: deglcs00000000000000000000x2og6y
        client_secret : Optional[str]
            'Client Secret' of Box OAuth2 app. For example: OKM1f100000000000000000000eshEif
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Box
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/box'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Box)


    def update_o_auth2_dailymotion(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Dailymotion:
        """
        Update the project OAuth2 Dailymotion configuration.

        Parameters
        ----------
        api_key : Optional[str]
            'API Key' of Dailymotion OAuth2 app. For example: 07a9000000000000067f
        api_secret : Optional[str]
            'API Secret' of Dailymotion OAuth2 app. For example: a399a90000000000000000000000000000d90639
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Dailymotion
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/dailymotion'
        api_params = {}

        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if api_secret is not None:
            api_params['apiSecret'] = self._normalize_value(api_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Dailymotion)


    def update_o_auth2_discord(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Discord:
        """
        Update the project OAuth2 Discord configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Discord OAuth2 app. For example: 950722000000343754
        client_secret : Optional[str]
            'Client Secret' of Discord OAuth2 app. For example: YmPXnM000000000000000000002zFg5D
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Discord
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/discord'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Discord)


    def update_o_auth2_disqus(
        self,
        public_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Disqus:
        """
        Update the project OAuth2 Disqus configuration.

        Parameters
        ----------
        public_key : Optional[str]
            'Public Key, also known as API Key' of Disqus OAuth2 app. For example: cgegH70000000000000000000000000000000000000000000000000000Hr1nYX
        secret_key : Optional[str]
            'Secret Key, also known as API Secret' of Disqus OAuth2 app. For example: W7Bykj00000000000000000000000000000000000000000000000000003o43w9
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Disqus
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/disqus'
        api_params = {}

        if public_key is not None:
            api_params['publicKey'] = self._normalize_value(public_key)
        if secret_key is not None:
            api_params['secretKey'] = self._normalize_value(secret_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Disqus)


    def update_o_auth2_dropbox(
        self,
        app_key: Optional[str] = None,
        app_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Dropbox:
        """
        Update the project OAuth2 Dropbox configuration.

        Parameters
        ----------
        app_key : Optional[str]
            'App Key' of Dropbox OAuth2 app. For example: jl000000000009t
        app_secret : Optional[str]
            'App Secret' of Dropbox OAuth2 app. For example: g200000000000vw
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Dropbox
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/dropbox'
        api_params = {}

        if app_key is not None:
            api_params['appKey'] = self._normalize_value(app_key)
        if app_secret is not None:
            api_params['appSecret'] = self._normalize_value(app_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Dropbox)


    def update_o_auth2_etsy(
        self,
        key_string: Optional[str] = None,
        shared_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Etsy:
        """
        Update the project OAuth2 Etsy configuration.

        Parameters
        ----------
        key_string : Optional[str]
            'Keystring' of Etsy OAuth2 app. For example: nsgzxh0000000000008j85a2
        shared_secret : Optional[str]
            'Shared Secret' of Etsy OAuth2 app. For example: tp000000ru
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Etsy
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/etsy'
        api_params = {}

        if key_string is not None:
            api_params['keyString'] = self._normalize_value(key_string)
        if shared_secret is not None:
            api_params['sharedSecret'] = self._normalize_value(shared_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Etsy)


    def update_o_auth2_facebook(
        self,
        app_id: Optional[str] = None,
        app_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Facebook:
        """
        Update the project OAuth2 Facebook configuration.

        Parameters
        ----------
        app_id : Optional[str]
            'App ID' of Facebook OAuth2 app. For example: 260600000007694
        app_secret : Optional[str]
            'App Secret' of Facebook OAuth2 app. For example: 2d0b2800000000000000000000d38af4
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Facebook
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/facebook'
        api_params = {}

        if app_id is not None:
            api_params['appId'] = self._normalize_value(app_id)
        if app_secret is not None:
            api_params['appSecret'] = self._normalize_value(app_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Facebook)


    def update_o_auth2_figma(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Figma:
        """
        Update the project OAuth2 Figma configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Figma OAuth2 app. For example: byay5H0000000000VtiI40
        client_secret : Optional[str]
            'Client Secret' of Figma OAuth2 app. For example: yEpOYn0000000000000000004iIsU5
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Figma
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/figma'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Figma)


    def update_o_auth2_fusion_auth(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        endpoint: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2FusionAuth:
        """
        Update the project OAuth2 FusionAuth configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of FusionAuth OAuth2 app. For example: b2222c00-0000-0000-0000-000000862097
        client_secret : Optional[str]
            'Client Secret' of FusionAuth OAuth2 app. For example: Jx4s0C0000000000000000000000000000000wGqLsc
        endpoint : Optional[str]
            Domain of FusionAuth instance. For example: example.fusionauth.io
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2FusionAuth
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/fusionauth'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if endpoint is not None:
            api_params['endpoint'] = self._normalize_value(endpoint)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2FusionAuth)


    def update_o_auth2_git_hub(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Github:
        """
        Update the project OAuth2 GitHub configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'OAuth2 app Client ID, or App ID' of GitHub OAuth2 app. For example: e4d87900000000540733. Example of wrong value: 370006
        client_secret : Optional[str]
            'Client Secret' of GitHub OAuth2 app. For example: 5e07c00000000000000000000000000000198bcc
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Github
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/github'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Github)


    def update_o_auth2_gitlab(
        self,
        application_id: Optional[str] = None,
        secret: Optional[str] = None,
        endpoint: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Gitlab:
        """
        Update the project OAuth2 Gitlab configuration.

        Parameters
        ----------
        application_id : Optional[str]
            'Application ID' of Gitlab OAuth2 app. For example: d41ffe0000000000000000000000000000000000000000000000000000d5e252
        secret : Optional[str]
            'Secret' of Gitlab OAuth2 app. For example: gloas-838cfa0000000000000000000000000000000000000000000000000000ecbb38
        endpoint : Optional[str]
            Endpoint URL of self-hosted GitLab instance. For example: https://gitlab.com
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Gitlab
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/gitlab'
        api_params = {}

        if application_id is not None:
            api_params['applicationId'] = self._normalize_value(application_id)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)
        if endpoint is not None:
            api_params['endpoint'] = self._normalize_value(endpoint)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Gitlab)


    def update_o_auth2_google(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        prompt: Optional[List[ProjectOAuth2GooglePrompt]] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Google:
        """
        Update the project OAuth2 Google configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Google OAuth2 app. For example: 120000000095-92ifjb00000000000000000000g7ijfb.apps.googleusercontent.com
        client_secret : Optional[str]
            'Client Secret' of Google OAuth2 app. For example: GOCSPX-2k8gsR0000000000000000VNahJj
        prompt : Optional[List[ProjectOAuth2GooglePrompt]]
            Array of Google OAuth2 prompt values. If "none" is included, it must be the only element. "none" means: don't display any authentication or consent screens. Must not be specified with other values. "consent" means: prompt the user for consent. "select_account" means: prompt the user to select an account.
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Google
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/google'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if prompt is not None:
            api_params['prompt'] = self._normalize_value(prompt)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Google)


    def update_o_auth2_keycloak(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        endpoint: Optional[str] = None,
        realm_name: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Keycloak:
        """
        Update the project OAuth2 Keycloak configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Keycloak OAuth2 app. For example: appwrite-o0000000st-app
        client_secret : Optional[str]
            'Client Secret' of Keycloak OAuth2 app. For example: jdjrJd00000000000000000000HUsaZO
        endpoint : Optional[str]
            Domain of Keycloak instance. For example: keycloak.example.com
        realm_name : Optional[str]
            Keycloak realm name. For example: appwrite-realm
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Keycloak
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/keycloak'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if endpoint is not None:
            api_params['endpoint'] = self._normalize_value(endpoint)
        if realm_name is not None:
            api_params['realmName'] = self._normalize_value(realm_name)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Keycloak)


    def update_o_auth2_kick(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Kick:
        """
        Update the project OAuth2 Kick configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Kick OAuth2 app. For example: 01KQ7C00000000000001MFHS32
        client_secret : Optional[str]
            'Client Secret' of Kick OAuth2 app. For example: 34ac5600000000000000000000000000000000000000000000000000e830c8b
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Kick
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/kick'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Kick)


    def update_o_auth2_linkedin(
        self,
        client_id: Optional[str] = None,
        primary_client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Linkedin:
        """
        Update the project OAuth2 Linkedin configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Linkedin OAuth2 app. For example: 770000000000dv
        primary_client_secret : Optional[str]
            'Primary Client Secret or Secondary Client Secret' of Linkedin OAuth2 app. For example: WPL_AP1.2Bf0000000000000./HtlYw==
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Linkedin
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/linkedin'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if primary_client_secret is not None:
            api_params['primaryClientSecret'] = self._normalize_value(primary_client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Linkedin)


    def update_o_auth2_microsoft(
        self,
        application_id: Optional[str] = None,
        application_secret: Optional[str] = None,
        tenant: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Microsoft:
        """
        Update the project OAuth2 Microsoft configuration.

        Parameters
        ----------
        application_id : Optional[str]
            'Entra ID Application ID, also known as Client ID' of Microsoft OAuth2 app. For example: 00001111-aaaa-2222-bbbb-3333cccc4444
        application_secret : Optional[str]
            'Entra ID Application Secret, also known as Client Secret' of Microsoft OAuth2 app. For example: A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u
        tenant : Optional[str]
            Microsoft Entra ID tenant identifier. Use 'common', 'organizations', 'consumers' or a specific tenant ID. For example: common
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Microsoft
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/microsoft'
        api_params = {}

        if application_id is not None:
            api_params['applicationId'] = self._normalize_value(application_id)
        if application_secret is not None:
            api_params['applicationSecret'] = self._normalize_value(application_secret)
        if tenant is not None:
            api_params['tenant'] = self._normalize_value(tenant)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Microsoft)


    def update_o_auth2_notion(
        self,
        oauth_client_id: Optional[str] = None,
        oauth_client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Notion:
        """
        Update the project OAuth2 Notion configuration.

        Parameters
        ----------
        oauth_client_id : Optional[str]
            'OAuth Client ID' of Notion OAuth2 app. For example: 341d8700-0000-0000-0000-000000446ee3
        oauth_client_secret : Optional[str]
            'OAuth Client Secret' of Notion OAuth2 app. For example: secret_dLUr4b000000000000000000000000000000lFHAa9
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Notion
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/notion'
        api_params = {}

        if oauth_client_id is not None:
            api_params['oauthClientId'] = self._normalize_value(oauth_client_id)
        if oauth_client_secret is not None:
            api_params['oauthClientSecret'] = self._normalize_value(oauth_client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Notion)


    def update_o_auth2_oidc(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        well_known_url: Optional[str] = None,
        authorization_url: Optional[str] = None,
        token_url: Optional[str] = None,
        user_info_url: Optional[str] = None,
        prompt: Optional[List[ProjectOAuth2OidcPrompt]] = None,
        max_age: Optional[float] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Oidc:
        """
        Update the project OAuth2 Oidc configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Oidc OAuth2 app. For example: qibI2x0000000000000000000000000006L2YFoG
        client_secret : Optional[str]
            'Client Secret' of Oidc OAuth2 app. For example: Ah68ed000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003qpcHV
        well_known_url : Optional[str]
            OpenID Connect well-known configuration URL. When provided, authorization, token, and user info endpoints can be discovered automatically. For example: https://myoauth.com/.well-known/openid-configuration
        authorization_url : Optional[str]
            OpenID Connect authorization endpoint URL. Required when wellKnownURL is not provided. For example: https://myoauth.com/oauth2/authorize
        token_url : Optional[str]
            OpenID Connect token endpoint URL. Required when wellKnownURL is not provided. For example: https://myoauth.com/oauth2/token
        user_info_url : Optional[str]
            OpenID Connect user info endpoint URL. Required when wellKnownURL is not provided. For example: https://myoauth.com/oauth2/userinfo
        prompt : Optional[List[ProjectOAuth2OidcPrompt]]
            Array of OpenID Connect prompt values controlling the authentication and consent screens. If "none" is included, it must be the only element. "none" means: don't display any authentication or consent screens. "login" means: prompt the user to re-authenticate. "consent" means: prompt the user for consent. "select_account" means: prompt the user to select an account.
        max_age : Optional[float]
            Maximum authentication age in seconds. When set, the user must have authenticated within this many seconds, otherwise they are prompted to re-authenticate.
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Oidc
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/oidc'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if well_known_url is not None:
            api_params['wellKnownURL'] = self._normalize_value(well_known_url)
        if authorization_url is not None:
            api_params['authorizationURL'] = self._normalize_value(authorization_url)
        if token_url is not None:
            api_params['tokenURL'] = self._normalize_value(token_url)
        if user_info_url is not None:
            api_params['userInfoURL'] = self._normalize_value(user_info_url)
        if prompt is not None:
            api_params['prompt'] = self._normalize_value(prompt)
        if max_age is not None:
            api_params['maxAge'] = self._normalize_value(max_age)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Oidc)


    def update_o_auth2_okta(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        domain: Optional[str] = None,
        authorization_server_id: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Okta:
        """
        Update the project OAuth2 Okta configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Okta OAuth2 app. For example: 0oa00000000000000698
        client_secret : Optional[str]
            'Client Secret' of Okta OAuth2 app. For example: Kiq0000000000000000000000000000000000000-00000000000H2L5-3SJ-vRV
        domain : Optional[str]
            Okta company domain. Required when enabling the provider. For example: trial-6400025.okta.com. Example of wrong value: trial-6400025-admin.okta.com, or https://trial-6400025.okta.com/
        authorization_server_id : Optional[str]
            Custom Authorization Servers. Optional, can be left empty or unconfigured. For example: aus000000000000000h7z
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Okta
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/okta'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        if authorization_server_id is not None:
            api_params['authorizationServerId'] = self._normalize_value(authorization_server_id)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Okta)


    def update_o_auth2_paypal(
        self,
        client_id: Optional[str] = None,
        secret_key: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Paypal:
        """
        Update the project OAuth2 Paypal configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Paypal OAuth2 app. For example: AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB
        secret_key : Optional[str]
            'Secret Key 1 or Secret Key 2' of Paypal OAuth2 app. For example: EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Paypal
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/paypal'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if secret_key is not None:
            api_params['secretKey'] = self._normalize_value(secret_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Paypal)


    def update_o_auth2_paypal_sandbox(
        self,
        client_id: Optional[str] = None,
        secret_key: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Paypal:
        """
        Update the project OAuth2 PaypalSandbox configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of PaypalSandbox OAuth2 app. For example: AdhIEG7-000000000000-0000000000000000000000000000000-0000000000000000000000-2pyB
        secret_key : Optional[str]
            'Secret Key 1 or Secret Key 2' of PaypalSandbox OAuth2 app. For example: EH8KCXtew--000000000000000000000000000000000000000_C-1_5UP_000000000000000CB7KDp
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Paypal
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/paypalSandbox'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if secret_key is not None:
            api_params['secretKey'] = self._normalize_value(secret_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Paypal)


    def update_o_auth2_podio(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Podio:
        """
        Update the project OAuth2 Podio configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Podio OAuth2 app. For example: appwrite-o0000000st-app
        client_secret : Optional[str]
            'Client Secret' of Podio OAuth2 app. For example: Rn247T0000000000000000000000000000000000000000000000000000W2zWTN
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Podio
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/podio'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Podio)


    def update_o_auth2_salesforce(
        self,
        customer_key: Optional[str] = None,
        customer_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Salesforce:
        """
        Update the project OAuth2 Salesforce configuration.

        Parameters
        ----------
        customer_key : Optional[str]
            'Consumer Key' of Salesforce OAuth2 app. For example: 3MVG9I0000000000000000000000000000000000000000000000000000000000000000000000000C5Aejq
        customer_secret : Optional[str]
            'Consumer Secret' of Salesforce OAuth2 app. For example: 3w000000000000e2
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Salesforce
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/salesforce'
        api_params = {}

        if customer_key is not None:
            api_params['customerKey'] = self._normalize_value(customer_key)
        if customer_secret is not None:
            api_params['customerSecret'] = self._normalize_value(customer_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Salesforce)


    def update_o_auth2_slack(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Slack:
        """
        Update the project OAuth2 Slack configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Slack OAuth2 app. For example: 23000000089.15000000000023
        client_secret : Optional[str]
            'Client Secret' of Slack OAuth2 app. For example: 81656000000000000000000000f3d2fd
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Slack
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/slack'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Slack)


    def update_o_auth2_spotify(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Spotify:
        """
        Update the project OAuth2 Spotify configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Spotify OAuth2 app. For example: 6ec271000000000000000000009beace
        client_secret : Optional[str]
            'Client Secret' of Spotify OAuth2 app. For example: db068a000000000000000000008b5b9f
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Spotify
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/spotify'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Spotify)


    def update_o_auth2_stripe(
        self,
        client_id: Optional[str] = None,
        api_secret_key: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Stripe:
        """
        Update the project OAuth2 Stripe configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Stripe OAuth2 app. For example: ca_UKibXX0000000000000000000006byvR
        api_secret_key : Optional[str]
            'API Secret Key' of Stripe OAuth2 app. For example: sk_51SfOd000000000000000000000000000000000000000000000000000000000000000000000000000000000000000QGWYfp
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Stripe
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/stripe'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if api_secret_key is not None:
            api_params['apiSecretKey'] = self._normalize_value(api_secret_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Stripe)


    def update_o_auth2_tradeshift(
        self,
        oauth2_client_id: Optional[str] = None,
        oauth2_client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Tradeshift:
        """
        Update the project OAuth2 Tradeshift configuration.

        Parameters
        ----------
        oauth2_client_id : Optional[str]
            'OAuth2 Client ID' of Tradeshift OAuth2 app. For example: appwrite-tes00000.0000000000est-app
        oauth2_client_secret : Optional[str]
            'OAuth2 Client Secret' of Tradeshift OAuth2 app. For example: 7cb52700-0000-0000-0000-000000ca5b83
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Tradeshift
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/tradeshift'
        api_params = {}

        if oauth2_client_id is not None:
            api_params['oauth2ClientId'] = self._normalize_value(oauth2_client_id)
        if oauth2_client_secret is not None:
            api_params['oauth2ClientSecret'] = self._normalize_value(oauth2_client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Tradeshift)


    def update_o_auth2_tradeshift_sandbox(
        self,
        oauth2_client_id: Optional[str] = None,
        oauth2_client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Tradeshift:
        """
        Update the project OAuth2 Tradeshift Sandbox configuration.

        Parameters
        ----------
        oauth2_client_id : Optional[str]
            'OAuth2 Client ID' of Tradeshift Sandbox OAuth2 app. For example: appwrite-tes00000.0000000000est-app
        oauth2_client_secret : Optional[str]
            'OAuth2 Client Secret' of Tradeshift Sandbox OAuth2 app. For example: 7cb52700-0000-0000-0000-000000ca5b83
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Tradeshift
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/tradeshiftBox'
        api_params = {}

        if oauth2_client_id is not None:
            api_params['oauth2ClientId'] = self._normalize_value(oauth2_client_id)
        if oauth2_client_secret is not None:
            api_params['oauth2ClientSecret'] = self._normalize_value(oauth2_client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Tradeshift)


    def update_o_auth2_twitch(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Twitch:
        """
        Update the project OAuth2 Twitch configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Twitch OAuth2 app. For example: vvi0in000000000000000000ikmt9p
        client_secret : Optional[str]
            'Client Secret' of Twitch OAuth2 app. For example: pmapue000000000000000000zylw3v
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Twitch
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/twitch'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Twitch)


    def update_o_auth2_word_press(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2WordPress:
        """
        Update the project OAuth2 WordPress configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of WordPress OAuth2 app. For example: 130005
        client_secret : Optional[str]
            'Client Secret' of WordPress OAuth2 app. For example: PlBfJS0000000000000000000000000000000000000000000000000000EdUZJk
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2WordPress
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/wordpress'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2WordPress)


    def update_o_auth2_x(
        self,
        customer_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2X:
        """
        Update the project OAuth2 X configuration.

        Parameters
        ----------
        customer_key : Optional[str]
            'Customer Key' of X OAuth2 app. For example: slzZV0000000000000NFLaWT
        secret_key : Optional[str]
            'Secret Key' of X OAuth2 app. For example: tkEPkp00000000000000000000000000000000000000FTxbI9
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2X
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/x'
        api_params = {}

        if customer_key is not None:
            api_params['customerKey'] = self._normalize_value(customer_key)
        if secret_key is not None:
            api_params['secretKey'] = self._normalize_value(secret_key)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2X)


    def update_o_auth2_yahoo(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Yahoo:
        """
        Update the project OAuth2 Yahoo configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID, also known as Customer Key' of Yahoo OAuth2 app. For example: dj0yJm000000000000000000000000000000000000000000000000000000000000000000000000000000000000Z4PWRm
        client_secret : Optional[str]
            'Client Secret, also known as Customer Secret' of Yahoo OAuth2 app. For example: cf978f0000000000000000000000000000c5e2e9
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Yahoo
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/yahoo'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Yahoo)


    def update_o_auth2_yandex(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Yandex:
        """
        Update the project OAuth2 Yandex configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Yandex OAuth2 app. For example: 6a8a6a0000000000000000000091483c
        client_secret : Optional[str]
            'Client Secret' of Yandex OAuth2 app. For example: bbf98500000000000000000000c75a63
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Yandex
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/yandex'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Yandex)


    def update_o_auth2_zoho(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Zoho:
        """
        Update the project OAuth2 Zoho configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Zoho OAuth2 app. For example: 1000.83C178000000000000000000RPNX0B
        client_secret : Optional[str]
            'Client Secret' of Zoho OAuth2 app. For example: fb5cac000000000000000000000000000000a68f6e
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Zoho
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/zoho'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Zoho)


    def update_o_auth2_zoom(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> OAuth2Zoom:
        """
        Update the project OAuth2 Zoom configuration.

        Parameters
        ----------
        client_id : Optional[str]
            'Client ID' of Zoom OAuth2 app. For example: QMAC00000000000000w0AQ
        client_secret : Optional[str]
            'Client Secret' of Zoom OAuth2 app. For example: GAWsG4000000000000000000007U01ON
        enabled : Optional[bool]
            OAuth2 sign-in method status. Set to true to enable new session creation. Setting to true will trigger end-to-end credentials validation, and will throw if the credentials are invalid.
        
        Returns
        -------
        OAuth2Zoom
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/zoom'
        api_params = {}

        if client_id is not None:
            api_params['clientId'] = self._normalize_value(client_id)
        if client_secret is not None:
            api_params['clientSecret'] = self._normalize_value(client_secret)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OAuth2Zoom)


    def get_o_auth2_provider(
        self,
        provider_id: ProjectOAuthProviderId
    ) -> Union[OAuth2Github, OAuth2Discord, OAuth2Figma, OAuth2Dropbox, OAuth2Dailymotion, OAuth2Bitbucket, OAuth2Bitly, OAuth2Box, OAuth2Autodesk, OAuth2Google, OAuth2Zoom, OAuth2Zoho, OAuth2Yandex, OAuth2X, OAuth2WordPress, OAuth2Twitch, OAuth2Stripe, OAuth2Spotify, OAuth2Slack, OAuth2Podio, OAuth2Notion, OAuth2Salesforce, OAuth2Yahoo, OAuth2Linkedin, OAuth2Disqus, OAuth2Amazon, OAuth2Etsy, OAuth2Facebook, OAuth2Tradeshift, OAuth2Paypal, OAuth2Gitlab, OAuth2Authentik, OAuth2Auth0, OAuth2FusionAuth, OAuth2Keycloak, OAuth2Oidc, OAuth2Apple, OAuth2Okta, OAuth2Kick, OAuth2Microsoft]:
        """
        Get a single OAuth2 provider configuration. Credential fields (client secret, p8 file, key/team IDs) are write-only and always returned empty.

        Parameters
        ----------
        provider_id : ProjectOAuthProviderId
            OAuth2 provider key. For example: github, google, apple.
        
        Returns
        -------
        Union[OAuth2Github, OAuth2Discord, OAuth2Figma, OAuth2Dropbox, OAuth2Dailymotion, OAuth2Bitbucket, OAuth2Bitly, OAuth2Box, OAuth2Autodesk, OAuth2Google, OAuth2Zoom, OAuth2Zoho, OAuth2Yandex, OAuth2X, OAuth2WordPress, OAuth2Twitch, OAuth2Stripe, OAuth2Spotify, OAuth2Slack, OAuth2Podio, OAuth2Notion, OAuth2Salesforce, OAuth2Yahoo, OAuth2Linkedin, OAuth2Disqus, OAuth2Amazon, OAuth2Etsy, OAuth2Facebook, OAuth2Tradeshift, OAuth2Paypal, OAuth2Gitlab, OAuth2Authentik, OAuth2Auth0, OAuth2FusionAuth, OAuth2Keycloak, OAuth2Oidc, OAuth2Apple, OAuth2Okta, OAuth2Kick, OAuth2Microsoft]
            API response as one of the typed response models
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/oauth2/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)
        if not isinstance(response, dict):
            raise AppwriteException('Expected object response when hydrating a response model')

        if response.get('$id') == 'github':
            return self._parse_response(response, model=OAuth2Github)

        if response.get('$id') == 'discord':
            return self._parse_response(response, model=OAuth2Discord)

        if response.get('$id') == 'figma':
            return self._parse_response(response, model=OAuth2Figma)

        if response.get('$id') == 'dropbox':
            return self._parse_response(response, model=OAuth2Dropbox)

        if response.get('$id') == 'dailymotion':
            return self._parse_response(response, model=OAuth2Dailymotion)

        if response.get('$id') == 'bitbucket':
            return self._parse_response(response, model=OAuth2Bitbucket)

        if response.get('$id') == 'bitly':
            return self._parse_response(response, model=OAuth2Bitly)

        if response.get('$id') == 'box':
            return self._parse_response(response, model=OAuth2Box)

        if response.get('$id') == 'autodesk':
            return self._parse_response(response, model=OAuth2Autodesk)

        if response.get('$id') == 'google':
            return self._parse_response(response, model=OAuth2Google)

        if response.get('$id') == 'zoom':
            return self._parse_response(response, model=OAuth2Zoom)

        if response.get('$id') == 'zoho':
            return self._parse_response(response, model=OAuth2Zoho)

        if response.get('$id') == 'yandex':
            return self._parse_response(response, model=OAuth2Yandex)

        if response.get('$id') == 'x':
            return self._parse_response(response, model=OAuth2X)

        if response.get('$id') == 'wordpress':
            return self._parse_response(response, model=OAuth2WordPress)

        if response.get('$id') == 'twitch':
            return self._parse_response(response, model=OAuth2Twitch)

        if response.get('$id') == 'stripe':
            return self._parse_response(response, model=OAuth2Stripe)

        if response.get('$id') == 'spotify':
            return self._parse_response(response, model=OAuth2Spotify)

        if response.get('$id') == 'slack':
            return self._parse_response(response, model=OAuth2Slack)

        if response.get('$id') == 'podio':
            return self._parse_response(response, model=OAuth2Podio)

        if response.get('$id') == 'notion':
            return self._parse_response(response, model=OAuth2Notion)

        if response.get('$id') == 'salesforce':
            return self._parse_response(response, model=OAuth2Salesforce)

        if response.get('$id') == 'yahoo':
            return self._parse_response(response, model=OAuth2Yahoo)

        if response.get('$id') == 'linkedin':
            return self._parse_response(response, model=OAuth2Linkedin)

        if response.get('$id') == 'disqus':
            return self._parse_response(response, model=OAuth2Disqus)

        if response.get('$id') == 'amazon':
            return self._parse_response(response, model=OAuth2Amazon)

        if response.get('$id') == 'etsy':
            return self._parse_response(response, model=OAuth2Etsy)

        if response.get('$id') == 'facebook':
            return self._parse_response(response, model=OAuth2Facebook)

        if response.get('$id') == 'tradeshiftBox':
            return self._parse_response(response, model=OAuth2Tradeshift)

        if response.get('$id') == 'paypalSandbox':
            return self._parse_response(response, model=OAuth2Paypal)

        if response.get('$id') == 'gitlab':
            return self._parse_response(response, model=OAuth2Gitlab)

        if response.get('$id') == 'authentik':
            return self._parse_response(response, model=OAuth2Authentik)

        if response.get('$id') == 'auth0':
            return self._parse_response(response, model=OAuth2Auth0)

        if response.get('$id') == 'fusionauth':
            return self._parse_response(response, model=OAuth2FusionAuth)

        if response.get('$id') == 'keycloak':
            return self._parse_response(response, model=OAuth2Keycloak)

        if response.get('$id') == 'oidc':
            return self._parse_response(response, model=OAuth2Oidc)

        if response.get('$id') == 'apple':
            return self._parse_response(response, model=OAuth2Apple)

        if response.get('$id') == 'okta':
            return self._parse_response(response, model=OAuth2Okta)

        if response.get('$id') == 'kick':
            return self._parse_response(response, model=OAuth2Kick)

        if response.get('$id') == 'microsoft':
            return self._parse_response(response, model=OAuth2Microsoft)

        raise AppwriteException('Unable to match response to any known model')


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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_policies(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> PolicyList:
        """
        Get a list of all project policies and their current configuration.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        PolicyList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PolicyList)


    def update_deny_aliased_email_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Configures if aliased emails such as subaddresses and emails with suffixes are denied during new users sign-ups and email updates.

        Parameters
        ----------
        enabled : bool
            Set whether or not to block aliased emails during signup and email updates.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/deny-aliased-email'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_deny_corporate_email_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Configures if only corporate email addresses (non-free and non-disposable domains) are allowed during new user sign-ups and email updates.

        Parameters
        ----------
        enabled : bool
            Set whether or not to restrict sign-ups and email updates to corporate email addresses only.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/deny-corporate-email'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_deny_disposable_email_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Configures if disposable emails from known temporary domains are denied during new users sign-ups and email updates.

        Parameters
        ----------
        enabled : bool
            Set whether or not to block disposable email addresses during signup and email updates.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/deny-disposable-email'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_deny_free_email_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Configures if emails from free providers such as Gmail or Yahoo are denied during new users sign-ups and email updates.

        Parameters
        ----------
        enabled : bool
            Set whether or not to block free email addresses during signup and email updates.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/deny-free-email'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_membership_privacy_policy(
        self,
        user_id: Optional[bool] = None,
        user_email: Optional[bool] = None,
        user_phone: Optional[bool] = None,
        user_name: Optional[bool] = None,
        user_mfa: Optional[bool] = None,
        user_accessed_at: Optional[bool] = None
    ) -> ProjectModel:
        """
        Updating this policy allows you to control if team members can see other members information. When enabled, all team members can see ID, name, email, phone number, and MFA status of other members..

        Parameters
        ----------
        user_id : Optional[bool]
            Set to true if you want make user ID visible to all team members, or false to hide it.
        user_email : Optional[bool]
            Set to true if you want make user email visible to all team members, or false to hide it.
        user_phone : Optional[bool]
            Set to true if you want make user phone number visible to all team members, or false to hide it.
        user_name : Optional[bool]
            Set to true if you want make user name visible to all team members, or false to hide it.
        user_mfa : Optional[bool]
            Set to true if you want make user MFA status visible to all team members, or false to hide it.
        user_accessed_at : Optional[bool]
            Set to true if you want make user last access time visible to all team members, or false to hide it.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/membership-privacy'
        api_params = {}

        if user_id is not None:
            api_params['userId'] = self._normalize_value(user_id)
        if user_email is not None:
            api_params['userEmail'] = self._normalize_value(user_email)
        if user_phone is not None:
            api_params['userPhone'] = self._normalize_value(user_phone)
        if user_name is not None:
            api_params['userName'] = self._normalize_value(user_name)
        if user_mfa is not None:
            api_params['userMFA'] = self._normalize_value(user_mfa)
        if user_accessed_at is not None:
            api_params['userAccessedAt'] = self._normalize_value(user_accessed_at)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_password_dictionary_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Updating this policy allows you to control if new passwords are checked against most common passwords dictionary. When enabled, and user changes their password, password must not be contained in the dictionary.

        Parameters
        ----------
        enabled : bool
            Toggle password dictionary policy. Set to true if you want password change to block passwords in the dictionary, or false to allow them. When changing this policy, existing passwords remain valid.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/password-dictionary'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_password_history_policy(
        self,
        total: Optional[float]
    ) -> ProjectModel:
        """
        Updates one of password strength policies. Based on total length configured, previous password hashes are stored, and users cannot choose a new password that is already stored in the passwird history list, when updating an user password, or setting new one through password recovery.
        
        Keep in mind, while password history policy is disabled, the history is not being stored. Enabling the policy will not have any history on existing users, and it will only start to collect and enforce the policy on password changes since the policy is enabled.

        Parameters
        ----------
        total : Optional[float]
            Set the password history length per user. Value can be between 1 and 5000, or null to disable the limit.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/password-history'
        api_params = {}

        api_params['total'] = self._normalize_value(total)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_password_personal_data_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Updating this policy allows you to control if password strength is checked against personal data. When enabled, and user sets or changes their password, the password must not contain user ID, name, email or phone number.

        Parameters
        ----------
        enabled : bool
            Toggle password personal data policy. Set to true if you want to block passwords including user's personal data, or false to allow it. When changing this policy, existing passwords remain valid.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/password-personal-data'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_password_strength_policy(
        self,
        min: Optional[float] = None,
        uppercase: Optional[bool] = None,
        lowercase: Optional[bool] = None,
        number: Optional[bool] = None,
        symbols: Optional[bool] = None
    ) -> PolicyPasswordStrength:
        """
        Update the password strength requirements for users in the project.

        Parameters
        ----------
        min : Optional[float]
            Minimum password length. Value must be between 8 and 256. Default is 8.
        uppercase : Optional[bool]
            Whether passwords must include at least one uppercase letter.
        lowercase : Optional[bool]
            Whether passwords must include at least one lowercase letter.
        number : Optional[bool]
            Whether passwords must include at least one number.
        symbols : Optional[bool]
            Whether passwords must include at least one symbol.
        
        Returns
        -------
        PolicyPasswordStrength
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/password-strength'
        api_params = {}

        if min is not None:
            api_params['min'] = self._normalize_value(min)
        if uppercase is not None:
            api_params['uppercase'] = self._normalize_value(uppercase)
        if lowercase is not None:
            api_params['lowercase'] = self._normalize_value(lowercase)
        if number is not None:
            api_params['number'] = self._normalize_value(number)
        if symbols is not None:
            api_params['symbols'] = self._normalize_value(symbols)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PolicyPasswordStrength)


    def update_session_alert_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Updating this policy allows you to control if email alert is sent upon session creation. When enabled, and user signs into their account, they will be sent an email notification. There is an exception, the first session after a new sign up does not trigger an alert, even if the policy is enabled.

        Parameters
        ----------
        enabled : bool
            Toggle session alert policy. Set to true if you want users to receive email notifications when a sessions are created for their users, or false to not send email alerts.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/session-alert'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_session_duration_policy(
        self,
        duration: float
    ) -> ProjectModel:
        """
        Update maximum duration how long sessions created within a project should stay active for.

        Parameters
        ----------
        duration : float
            Maximum session length in seconds. Minium allowed value is 5 second, and maximum is 1 year, which is 31536000 seconds.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/session-duration'
        api_params = {}
        if duration is None:
            raise AppwriteException('Missing required parameter: "duration"')


        api_params['duration'] = self._normalize_value(duration)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_session_invalidation_policy(
        self,
        enabled: bool
    ) -> ProjectModel:
        """
        Updating this policy allows you to control if existing sessions should be invalidated when a password of a user is changed. When enabled, and user changes their password, they will be logged out of all their devices.

        Parameters
        ----------
        enabled : bool
            Toggle session invalidation policy. Set to true if you want password change to invalidate all sessions of an user, or false to keep sessions active.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/session-invalidation'
        api_params = {}
        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')


        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_session_limit_policy(
        self,
        total: Optional[float]
    ) -> ProjectModel:
        """
        Update the maximum number of sessions allowed per user. When the limit is hit, the oldest session will be deleted to make room for new one.

        Parameters
        ----------
        total : Optional[float]
            Set the maximum number of sessions allowed per user. Value can be between 1 and 5000, or null to disable the limit.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/session-limit'
        api_params = {}

        api_params['total'] = self._normalize_value(total)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_user_limit_policy(
        self,
        total: Optional[float]
    ) -> ProjectModel:
        """
        Update the maximum number of users in the project. When the limit is hit or amount of existing users already exceeded the limit, all users remain active, but new user sign up will be prohibited.

        Parameters
        ----------
        total : Optional[float]
            Set the maximum number of users allowed in the project. Value can be between 1 and 5000, or null to disable the limit.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/user-limit'
        api_params = {}

        api_params['total'] = self._normalize_value(total)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def get_policy(
        self,
        policy_id: ProjectPolicyId
    ) -> Union[PolicyPasswordDictionary, PolicyPasswordHistory, PolicyPasswordStrength, PolicyPasswordPersonalData, PolicySessionAlert, PolicySessionDuration, PolicySessionInvalidation, PolicySessionLimit, PolicyUserLimit, PolicyMembershipPrivacy, PolicyDenyAliasedEmail, PolicyDenyDisposableEmail, PolicyDenyFreeEmail, PolicyDenyCorporateEmail]:
        """
        Get a policy by its unique ID. This endpoint returns the current configuration for the requested project policy.

        Parameters
        ----------
        policy_id : ProjectPolicyId
            Policy ID. Can be one of: password-dictionary, password-history, password-strength, password-personal-data, session-alert, session-duration, session-invalidation, session-limit, user-limit, membership-privacy, deny-aliased-email, deny-disposable-email, deny-free-email, deny-corporate-email.
        
        Returns
        -------
        Union[PolicyPasswordDictionary, PolicyPasswordHistory, PolicyPasswordStrength, PolicyPasswordPersonalData, PolicySessionAlert, PolicySessionDuration, PolicySessionInvalidation, PolicySessionLimit, PolicyUserLimit, PolicyMembershipPrivacy, PolicyDenyAliasedEmail, PolicyDenyDisposableEmail, PolicyDenyFreeEmail, PolicyDenyCorporateEmail]
            API response as one of the typed response models
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/policies/{policyId}'
        api_params = {}
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')

        api_path = api_path.replace('{policyId}', str(self._normalize_value(policy_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)
        if not isinstance(response, dict):
            raise AppwriteException('Expected object response when hydrating a response model')

        if response.get('$id') == 'password-dictionary':
            return self._parse_response(response, model=PolicyPasswordDictionary)

        if response.get('$id') == 'password-history':
            return self._parse_response(response, model=PolicyPasswordHistory)

        if response.get('$id') == 'password-strength':
            return self._parse_response(response, model=PolicyPasswordStrength)

        if response.get('$id') == 'password-personal-data':
            return self._parse_response(response, model=PolicyPasswordPersonalData)

        if response.get('$id') == 'session-alert':
            return self._parse_response(response, model=PolicySessionAlert)

        if response.get('$id') == 'session-duration':
            return self._parse_response(response, model=PolicySessionDuration)

        if response.get('$id') == 'session-invalidation':
            return self._parse_response(response, model=PolicySessionInvalidation)

        if response.get('$id') == 'session-limit':
            return self._parse_response(response, model=PolicySessionLimit)

        if response.get('$id') == 'user-limit':
            return self._parse_response(response, model=PolicyUserLimit)

        if response.get('$id') == 'membership-privacy':
            return self._parse_response(response, model=PolicyMembershipPrivacy)

        if response.get('$id') == 'deny-aliased-email':
            return self._parse_response(response, model=PolicyDenyAliasedEmail)

        if response.get('$id') == 'deny-disposable-email':
            return self._parse_response(response, model=PolicyDenyDisposableEmail)

        if response.get('$id') == 'deny-free-email':
            return self._parse_response(response, model=PolicyDenyFreeEmail)

        if response.get('$id') == 'deny-corporate-email':
            return self._parse_response(response, model=PolicyDenyCorporateEmail)

        raise AppwriteException('Unable to match response to any known model')


    def update_protocol(
        self,
        protocol_id: ProjectProtocolId,
        enabled: bool
    ) -> ProjectModel:
        """
        Update properties of a specific protocol. Use this endpoint to enable or disable a protocol in your project. 

        Parameters
        ----------
        protocol_id : ProjectProtocolId
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

        api_path = '/project/protocols/{protocolId}'
        api_params = {}
        if protocol_id is None:
            raise AppwriteException('Missing required parameter: "protocol_id"')

        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')

        api_path = api_path.replace('{protocolId}', str(self._normalize_value(protocol_id)))

        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_service(
        self,
        service_id: ProjectServiceId,
        enabled: bool
    ) -> ProjectModel:
        """
        Update properties of a specific service. Use this endpoint to enable or disable a service in your project. 

        Parameters
        ----------
        service_id : ProjectServiceId
            Service name. Can be one of: account, avatars, databases, tablesdb, locale, health, project, storage, teams, users, vcs, sites, functions, proxy, graphql, migrations, messaging, advisor, oauth2
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

        api_path = '/project/services/{serviceId}'
        api_params = {}
        if service_id is None:
            raise AppwriteException('Missing required parameter: "service_id"')

        if enabled is None:
            raise AppwriteException('Missing required parameter: "enabled"')

        api_path = api_path.replace('{serviceId}', str(self._normalize_value(service_id)))

        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def update_smtp(
        self,
        host: Optional[str] = None,
        port: Optional[float] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        sender_email: Optional[str] = None,
        sender_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        secure: Optional[ProjectSMTPSecure] = None,
        enabled: Optional[bool] = None
    ) -> ProjectModel:
        """
        Update the SMTP configuration for your project. Use this endpoint to configure your project's SMTP provider with your custom settings for sending transactional emails.

        Parameters
        ----------
        host : Optional[str]
            SMTP server hostname (domain)
        port : Optional[float]
            SMTP server port
        username : Optional[str]
            SMTP server username. Pass an empty string to clear a previously set value.
        password : Optional[str]
            SMTP server password. Pass an empty string to clear a previously set value. This property is stored securely and cannot be read in future (write-only).
        sender_email : Optional[str]
            Email address shown in inbox as the sender of the email. Pass an empty string to clear a previously set value.
        sender_name : Optional[str]
            Name shown in inbox as the sender of the email. Pass an empty string to clear a previously set value.
        reply_to_email : Optional[str]
            Email used when user replies to the email. Pass an empty string to clear a previously set value.
        reply_to_name : Optional[str]
            Name used when user replies to the email. Pass an empty string to clear a previously set value.
        secure : Optional[ProjectSMTPSecure]
            Configures if communication with SMTP server is encrypted. Allowed values are: tls, ssl. Leave empty for no encryption.
        enabled : Optional[bool]
            Enable or disable custom SMTP. Custom SMTP is useful for branding purposes, but also allows use of custom email templates.
        
        Returns
        -------
        ProjectModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/smtp'
        api_params = {}

        if host is not None:
            api_params['host'] = self._normalize_value(host)
        if port is not None:
            api_params['port'] = self._normalize_value(port)
        if username is not None:
            api_params['username'] = self._normalize_value(username)
        if password is not None:
            api_params['password'] = self._normalize_value(password)
        if sender_email is not None:
            api_params['senderEmail'] = self._normalize_value(sender_email)
        if sender_name is not None:
            api_params['senderName'] = self._normalize_value(sender_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if secure is not None:
            api_params['secure'] = self._normalize_value(secure)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProjectModel)


    def create_smtp_test(
        self,
        emails: List[str]
    ) -> Dict[str, Any]:
        """
        Send a test email to verify SMTP configuration. 

        Parameters
        ----------
        emails : List[str]
            Array of emails to send test email to. Maximum of 10 emails are allowed.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/smtp/tests'
        api_params = {}
        if emails is None:
            raise AppwriteException('Missing required parameter: "emails"')


        api_params['emails'] = self._normalize_value(emails)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_email_templates(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> EmailTemplateList:
        """
        Get a list of all custom email templates configured for the project. This endpoint returns an array of all configured email templates and their locales.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        EmailTemplateList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/templates/email'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=EmailTemplateList)


    def update_email_template(
        self,
        template_id: ProjectEmailTemplateId,
        locale: Optional[ProjectEmailTemplateLocale] = None,
        subject: Optional[str] = None,
        message: Optional[str] = None,
        sender_name: Optional[str] = None,
        sender_email: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        reply_to_name: Optional[str] = None
    ) -> EmailTemplate:
        """
        Update a custom email template for the specified locale and type. Use this endpoint to modify the content of your email templates.

        Parameters
        ----------
        template_id : ProjectEmailTemplateId
            Custom email template type. Can be one of: verification, magicSession, recovery, invitation, mfaChallenge, sessionAlert, otpSession
        locale : Optional[ProjectEmailTemplateLocale]
            Custom email template locale. If left empty, the fallback locale (en) will be used.
        subject : Optional[str]
            Subject of the email template. Can be up to 255 characters.
        message : Optional[str]
            Plain or HTML body of the email template message. Can be up to 10MB of content.
        sender_name : Optional[str]
            Name of the email sender.
        sender_email : Optional[str]
            Email of the sender. Pass an empty string to clear a previously set value.
        reply_to_email : Optional[str]
            Reply to email. Pass an empty string to clear a previously set value.
        reply_to_name : Optional[str]
            Reply to name.
        
        Returns
        -------
        EmailTemplate
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/templates/email'
        api_params = {}
        if template_id is None:
            raise AppwriteException('Missing required parameter: "template_id"')


        api_params['templateId'] = self._normalize_value(template_id)
        if locale is not None:
            api_params['locale'] = self._normalize_value(locale)
        if subject is not None:
            api_params['subject'] = self._normalize_value(subject)
        if message is not None:
            api_params['message'] = self._normalize_value(message)
        if sender_name is not None:
            api_params['senderName'] = self._normalize_value(sender_name)
        if sender_email is not None:
            api_params['senderEmail'] = self._normalize_value(sender_email)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)

        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=EmailTemplate)


    def get_email_template(
        self,
        template_id: ProjectEmailTemplateId,
        locale: Optional[ProjectEmailTemplateLocale] = None
    ) -> EmailTemplate:
        """
        Get a custom email template for the specified locale and type. This endpoint returns the template content, subject, and other configuration details.

        Parameters
        ----------
        template_id : ProjectEmailTemplateId
            Custom email template type. Can be one of: verification, magicSession, recovery, invitation, mfaChallenge, sessionAlert, otpSession
        locale : Optional[ProjectEmailTemplateLocale]
            Custom email template locale. If left empty, the fallback locale (en) will be used.
        
        Returns
        -------
        EmailTemplate
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/templates/email/{templateId}'
        api_params = {}
        if template_id is None:
            raise AppwriteException('Missing required parameter: "template_id"')

        api_path = api_path.replace('{templateId}', str(self._normalize_value(template_id)))

        if locale is not None:
            api_params['locale'] = self._normalize_value(locale)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=EmailTemplate)


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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
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
            Variable unique ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            Variable unique ID.
        
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
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
            Variable unique ID.
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

        if key is not None:
            api_params['key'] = self._normalize_value(key)
        if value is not None:
            api_params['value'] = self._normalize_value(value)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('put', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
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
            Variable unique ID.
        
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
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response

