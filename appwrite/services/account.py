from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.user import User
from ..models.oauth2_consent_list import Oauth2ConsentList
from ..models.oauth2_consent import Oauth2Consent
from ..models.oauth2_consent_token_list import Oauth2ConsentTokenList
from ..models.oauth2_consent_token import Oauth2ConsentToken
from ..models.identity_list import IdentityList
from ..models.membership_list import MembershipList
from ..enums.authenticator_type import AuthenticatorType
from ..models.mfa_type import MfaType
from ..enums.authentication_factor import AuthenticationFactor
from ..models.mfa_challenge import MfaChallenge
from ..models.session import Session
from ..models.mfa_factors import MfaFactors
from ..models.mfa_recovery_codes import MfaRecoveryCodes
from ..models.passkey_list import PasskeyList
from ..models.passkey_challenge import PasskeyChallenge
from ..models.passkey import Passkey
from ..models.preferences import Preferences
from ..models.token import Token
from ..models.session_list import SessionList
from ..enums.id_token_provider import IdTokenProvider
from ..enums.o_auth_provider import OAuthProvider
from ..models.token_secret import TokenSecret

T = TypeVar('T')


class Account(Service):

    def __init__(self, client) -> None:
        super(Account, self).__init__(client)

    def get(
        self,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Get the currently logged in user.

        Parameters
        ----------
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account'
        api_params = {}

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def create(
        self,
        user_id: str,
        email: str,
        password: str,
        name: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Use this endpoint to allow a new user to register a new account in your project. After the user registration completes successfully, you can use the [/account/verfication](https://appwrite.io/docs/references/cloud/client-web/account#createVerification) route to start verifying the user email address. To allow the new user to login to their new account, you need to create a new [account session](https://appwrite.io/docs/references/cloud/client-web/account#createEmailSession).

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            New user password. Must be between 8 and 256 chars.
        name : Optional[str]
            User name. Max length: 128 chars.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['email'] = self._normalize_value(email)
        api_params['password'] = self._normalize_value(password)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def list_consents(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> Oauth2ConsentList:
        """
        Get a list of the OAuth2 consents the current user has given to third-party apps.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        Oauth2ConsentList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/consents'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Oauth2ConsentList)

    def get_consent(
        self,
        consent_id: str,
    ) -> Oauth2Consent:
        """
        Get an OAuth2 consent the current user has given to a third-party app by its unique ID.

        Parameters
        ----------
        consent_id : str
            Consent unique ID.
        Returns
        -------
        Oauth2Consent
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/consents/{consentId}'
        api_params = {}
        if consent_id is None or consent_id == '':
            raise AppwriteException('Missing required parameter: "consent_id"')
        api_path = api_path.replace('{consentId}', self._encode_path(consent_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Oauth2Consent)

    def delete_consent(
        self,
        consent_id: str,
    ) -> Dict[str, Any]:
        """
        Delete an OAuth2 consent by its unique ID. All token families issued under the consent are revoked, and the app must ask for consent again to regain access.

        Parameters
        ----------
        consent_id : str
            Consent unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/consents/{consentId}'
        api_params = {}
        if consent_id is None or consent_id == '':
            raise AppwriteException('Missing required parameter: "consent_id"')
        api_path = api_path.replace('{consentId}', self._encode_path(consent_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def list_consent_tokens(
        self,
        consent_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> Oauth2ConsentTokenList:
        """
        Get a list of the token families issued under an OAuth2 consent. Each entry represents one authorized device or session; the token secrets themselves are never returned.

        Parameters
        ----------
        consent_id : str
            Consent unique ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        Oauth2ConsentTokenList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/consents/{consentId}/tokens'
        api_params = {}
        if consent_id is None or consent_id == '':
            raise AppwriteException('Missing required parameter: "consent_id"')
        api_path = api_path.replace('{consentId}', self._encode_path(consent_id))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Oauth2ConsentTokenList)

    def get_consent_token(
        self,
        consent_id: str,
        token_id: str,
    ) -> Oauth2ConsentToken:
        """
        Get a token family issued under an OAuth2 consent by its unique ID. The token secrets themselves are never returned.

        Parameters
        ----------
        consent_id : str
            Consent unique ID.
        token_id : str
            Token unique ID.
        Returns
        -------
        Oauth2ConsentToken
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/consents/{consentId}/tokens/{tokenId}'
        api_params = {}
        if consent_id is None or consent_id == '':
            raise AppwriteException('Missing required parameter: "consent_id"')
        if token_id is None or token_id == '':
            raise AppwriteException('Missing required parameter: "token_id"')
        api_path = api_path.replace('{consentId}', self._encode_path(consent_id))
        api_path = api_path.replace('{tokenId}', self._encode_path(token_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Oauth2ConsentToken)

    def delete_consent_token(
        self,
        consent_id: str,
        token_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a token family issued under an OAuth2 consent by its unique ID. The access and refresh tokens of the family stop working immediately; other token families and the consent itself are unaffected.

        Parameters
        ----------
        consent_id : str
            Consent unique ID.
        token_id : str
            Token unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/consents/{consentId}/tokens/{tokenId}'
        api_params = {}
        if consent_id is None or consent_id == '':
            raise AppwriteException('Missing required parameter: "consent_id"')
        if token_id is None or token_id == '':
            raise AppwriteException('Missing required parameter: "token_id"')
        api_path = api_path.replace('{consentId}', self._encode_path(consent_id))
        api_path = api_path.replace('{tokenId}', self._encode_path(token_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def update_email(
        self,
        email: str,
        password: str,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Update currently logged in user account email address. After changing user address, the user confirmation status will get reset. A new confirmation email is not sent automatically however you can use the send confirmation email endpoint again to send the confirmation email. For security measures, user password is required to complete this request.
        This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.

        Parameters
        ----------
        email : str
            User email.
        password : str
            User password. Must be at least 8 chars.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/email'
        api_params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['email'] = self._normalize_value(email)
        api_params['password'] = self._normalize_value(password)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def list_identities(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> IdentityList:
        """
        Get the list of identities for the currently logged in user.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, provider, providerUid, providerEmail, providerAccessTokenExpiry
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        IdentityList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/identities'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=IdentityList)

    def delete_identity(
        self,
        identity_id: str,
    ) -> Dict[str, Any]:
        """
        Delete an identity by its unique ID.

        Parameters
        ----------
        identity_id : str
            Identity ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/identities/{identityId}'
        api_params = {}
        if identity_id is None or identity_id == '':
            raise AppwriteException('Missing required parameter: "identity_id"')
        api_path = api_path.replace('{identityId}', self._encode_path(identity_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def list_memberships(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> MembershipList:
        """
        Get the team memberships of the currently logged in user.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, teamId, invited, joined, confirm, roles
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

        api_path = '/account/memberships'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MembershipList)

    def update_mfa(
        self,
        mfa: bool,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Enable or disable MFA on an account.

        Parameters
        ----------
        mfa : bool
            Enable or disable MFA.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa'
        api_params = {}
        if mfa is None:
            raise AppwriteException('Missing required parameter: "mfa"')
        api_params['mfa'] = self._normalize_value(mfa)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def create_mfa_authenticator(
        self,
        type: AuthenticatorType,
    ) -> MfaType:
        """
        Add an authenticator app to be used as an MFA factor. Verify the authenticator using the [verify authenticator](/docs/references/cloud/client-web/account#updateMfaAuthenticator) method.

        Parameters
        ----------
        type : AuthenticatorType
            Type of authenticator. Must be `totp`
        Returns
        -------
        MfaType
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/authenticators/{type}'
        api_params = {}
        if type is None:
            raise AppwriteException('Missing required parameter: "type"')
        api_path = api_path.replace('{type}', self._encode_path(type))

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MfaType)

    def update_mfa_authenticator(
        self,
        type: AuthenticatorType,
        otp: str,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Verify an authenticator app after adding it using the [add authenticator](/docs/references/cloud/client-web/account#createMfaAuthenticator) method.

        Parameters
        ----------
        type : AuthenticatorType
            Type of authenticator.
        otp : str
            Valid verification token.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/authenticators/{type}'
        api_params = {}
        if type is None:
            raise AppwriteException('Missing required parameter: "type"')
        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')
        api_path = api_path.replace('{type}', self._encode_path(type))
        api_params['otp'] = self._normalize_value(otp)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def delete_mfa_authenticator(
        self,
        type: AuthenticatorType,
    ) -> Dict[str, Any]:
        """
        Delete an authenticator for a user by ID.

        Parameters
        ----------
        type : AuthenticatorType
            Type of authenticator.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/authenticators/{type}'
        api_params = {}
        if type is None:
            raise AppwriteException('Missing required parameter: "type"')
        api_path = api_path.replace('{type}', self._encode_path(type))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def create_mfa_challenge(
        self,
        factor: AuthenticationFactor,
    ) -> MfaChallenge:
        """
        Begin the process of MFA verification after sign-in. Finish the flow with [updateMfaChallenge](/docs/references/cloud/client-web/account#updateMfaChallenge) method.

        Parameters
        ----------
        factor : AuthenticationFactor
            Factor used for verification. Must be one of following: `email`, `phone`, `totp`, `recoveryCode`, `custom`.
        Returns
        -------
        MfaChallenge
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/challenges'
        api_params = {}
        if factor is None:
            raise AppwriteException('Missing required parameter: "factor"')
        api_params['factor'] = self._normalize_value(factor)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MfaChallenge)

    def update_mfa_challenge(
        self,
        challenge_id: str,
        otp: str,
    ) -> Session:
        """
        Complete the MFA challenge by providing the one-time password. Finish the process of MFA verification by providing the one-time password. To begin the flow, use [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method.

        Parameters
        ----------
        challenge_id : str
            ID of the challenge.
        otp : str
            Valid verification token.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/challenges'
        api_params = {}
        if challenge_id is None:
            raise AppwriteException('Missing required parameter: "challenge_id"')
        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')
        api_params['challengeId'] = self._normalize_value(challenge_id)
        api_params['otp'] = self._normalize_value(otp)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    def list_mfa_factors(
        self,
    ) -> MfaFactors:
        """
        List the factors available on the account to be used as a MFA challange.
        Returns
        -------
        MfaFactors
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/factors'
        api_params = {}

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MfaFactors)

    def get_mfa_recovery_codes(
        self,
    ) -> MfaRecoveryCodes:
        """
        Get recovery codes that can be used as backup for MFA flow. Before getting codes, they must be generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to read recovery codes.
        Returns
        -------
        MfaRecoveryCodes
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/recovery-codes'
        api_params = {}

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MfaRecoveryCodes)

    def create_mfa_recovery_codes(
        self,
    ) -> MfaRecoveryCodes:
        """
        Generate recovery codes as backup for MFA flow. It's recommended to generate and show then immediately after user successfully adds their authehticator. Recovery codes can be used as a MFA verification type in [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method.
        Returns
        -------
        MfaRecoveryCodes
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/recovery-codes'
        api_params = {}

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MfaRecoveryCodes)

    def update_mfa_recovery_codes(
        self,
    ) -> MfaRecoveryCodes:
        """
        Regenerate recovery codes that can be used as backup for MFA flow. Before regenerating codes, they must be first generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to regenreate recovery codes.
        Returns
        -------
        MfaRecoveryCodes
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/recovery-codes'
        api_params = {}

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MfaRecoveryCodes)

    def update_name(
        self,
        name: str,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Update currently logged in user account name.

        Parameters
        ----------
        name : str
            User name. Max length: 128 chars.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/name'
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_params['name'] = self._normalize_value(name)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def list_passkeys(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> PasskeyList:
        """
        Get the list of verified passkeys registered by the currently logged in user.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter and order on the following attributes: $id, $createdAt, $updatedAt, name, accessedAt
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        PasskeyList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/passkeys'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=PasskeyList)

    def create_passkey(
        self,
        passkey_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> PasskeyChallenge:
        """
        Start registering a passkey for the currently logged in user. The session must have signed in or completed an MFA challenge within the last 10 minutes. Pass the returned `publicKey` options to `navigator.credentials.create()`, then complete the registration with [Update passkey verification](/docs/references/cloud/client-web/account#updatePasskeyVerification). The passkey stays pending until verified, and the challenge expires after 5 minutes.

        Parameters
        ----------
        passkey_id : Optional[str]
            Passkey ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : Optional[str]
            Passkey name, shown when listing passkeys. Max length: 128 chars.
        Returns
        -------
        PasskeyChallenge
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/passkeys'
        api_params = {}
        if passkey_id is not None:
            api_params['passkeyId'] = self._normalize_value(passkey_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=PasskeyChallenge)

    def get_passkey(
        self,
        passkey_id: str,
    ) -> Passkey:
        """
        Get a verified passkey of the currently logged in user by its unique ID.

        Parameters
        ----------
        passkey_id : str
            Passkey ID.
        Returns
        -------
        Passkey
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/passkeys/{passkeyId}'
        api_params = {}
        if passkey_id is None or passkey_id == '':
            raise AppwriteException('Missing required parameter: "passkey_id"')
        api_path = api_path.replace('{passkeyId}', self._encode_path(passkey_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Passkey)

    def update_passkey(
        self,
        passkey_id: str,
        name: str,
    ) -> Passkey:
        """
        Rename a passkey of the currently logged in user.

        Parameters
        ----------
        passkey_id : str
            Passkey ID.
        name : str
            Passkey name. Max length: 128 chars.
        Returns
        -------
        Passkey
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/passkeys/{passkeyId}'
        api_params = {}
        if passkey_id is None or passkey_id == '':
            raise AppwriteException('Missing required parameter: "passkey_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_path = api_path.replace('{passkeyId}', self._encode_path(passkey_id))
        api_params['name'] = self._normalize_value(name)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Passkey)

    def delete_passkey(
        self,
        passkey_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a passkey from the currently logged in user. The passkey can no longer be used to sign in, although it may remain stored on the user's device. The session must have signed in or completed an MFA challenge within the last 10 minutes.

        Parameters
        ----------
        passkey_id : str
            Passkey ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/passkeys/{passkeyId}'
        api_params = {}
        if passkey_id is None or passkey_id == '':
            raise AppwriteException('Missing required parameter: "passkey_id"')
        api_path = api_path.replace('{passkeyId}', self._encode_path(passkey_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def update_passkey_verification(
        self,
        passkey_id: str,
        credential: Dict[str, Any],
    ) -> Passkey:
        """
        Complete a passkey registration started with [Create passkey](/docs/references/cloud/client-web/account#createPasskey). Pass the JSON form of the credential returned by `navigator.credentials.create()`, for example `credential.toJSON()`. Each registration can be verified once; a failed attempt requires starting it again.

        Parameters
        ----------
        passkey_id : str
            Passkey ID.
        credential : Dict[str, Any]
            Registration credential returned by the authenticator, in the JSON form produced by `PublicKeyCredential.toJSON()`.
        Returns
        -------
        Passkey
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/passkeys/{passkeyId}/verification'
        api_params = {}
        if passkey_id is None or passkey_id == '':
            raise AppwriteException('Missing required parameter: "passkey_id"')
        if credential is None:
            raise AppwriteException('Missing required parameter: "credential"')
        api_path = api_path.replace('{passkeyId}', self._encode_path(passkey_id))
        api_params['credential'] = self._normalize_value(credential)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Passkey)

    def update_password(
        self,
        password: str,
        old_password: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth, Team Invites and Magic URL, oldPassword is optional.

        Parameters
        ----------
        password : str
            New user password. Must be at least 8 chars.
        old_password : Optional[str]
            Current user password. Max length: 256 chars.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/password'
        api_params = {}
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['password'] = self._normalize_value(password)
        if old_password is not None:
            api_params['oldPassword'] = self._normalize_value(old_password)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def update_phone(
        self,
        phone: str,
        password: str,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Update the currently logged in user's phone number. After updating the phone number, the phone verification status will be reset. A confirmation SMS is not sent automatically, however you can use the [POST /account/verification/phone](https://appwrite.io/docs/references/cloud/client-web/account#createPhoneVerification) endpoint to send a confirmation SMS.

        Parameters
        ----------
        phone : str
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        password : str
            User password. Must be at least 8 chars.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/phone'
        api_params = {}
        if phone is None:
            raise AppwriteException('Missing required parameter: "phone"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['phone'] = self._normalize_value(phone)
        api_params['password'] = self._normalize_value(password)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def get_prefs(
        self,
        model_type: Type[T] = dict,
    ) -> Preferences[T]:
        """
        Get the preferences as a key-value object for the currently logged in user.

        Parameters
        ----------
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        Preferences[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/prefs'
        api_params = {}

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return Preferences.with_data(response, model_type)

    def update_prefs(
        self,
        prefs: Dict[str, Any],
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Update currently logged in user account preferences. The object you pass is stored as is, and replaces any previous value. The maximum allowed prefs size is 64kB and throws error if exceeded.

        Parameters
        ----------
        prefs : Dict[str, Any]
            Prefs key-value JSON object.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/prefs'
        api_params = {}
        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')
        api_params['prefs'] = self._normalize_value(prefs)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def create_recovery(
        self,
        email: str,
        url: str,
    ) -> Token:
        """
        Sends the user an email with a temporary secret key for password reset. When the user clicks the confirmation link he is redirected back to your app password reset URL with the secret key and email address values attached to the URL query string. Use the query string params to submit a request to the [PUT /account/recovery](https://appwrite.io/docs/references/cloud/client-web/account#updateRecovery) endpoint to complete the process. The verification link sent to the user's email address is valid for 1 hour.

        Parameters
        ----------
        email : str
            User email.
        url : str
            URL to redirect the user back to your app from the recovery email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/recovery'
        api_params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')
        api_params['email'] = self._normalize_value(email)
        api_params['url'] = self._normalize_value(url)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def update_recovery(
        self,
        user_id: str,
        secret: str,
        password: str,
    ) -> Token:
        """
        Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](https://appwrite.io/docs/references/cloud/client-web/account#createRecovery) endpoint.

        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

        The new password must satisfy the project's enabled password policies, including custom deny lists. Dictionary entries match the entire password case-sensitively; personal-data terms match substrings case-insensitively. Personal-data validation runs after token verification against the recovered user's ID, name, email, and phone, closing the previous recovery gap for profile-based checks. A rejected password leaves the existing credentials unchanged and the recovery token usable.

        Parameters
        ----------
        user_id : str
            User ID.
        secret : str
            Valid reset token.
        password : str
            New user password. Must be between 8 and 256 chars.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/recovery'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)
        api_params['password'] = self._normalize_value(password)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def create_recovery_otp(
        self,
        email: str,
        phrase: Optional[bool] = None,
    ) -> Token:
        """
        Use this endpoint to send a 6-digit password recovery code to the user's email address. Unlike [createRecovery](https://appwrite.io/docs/references/cloud/client-web/account#createRecovery), this method requires no redirect URL, which makes it suitable for mobile and desktop apps that cannot host a recovery page. Learn more about how to [complete the recovery process](https://appwrite.io/docs/references/cloud/client-web/account#updateRecoveryOTP). The code sent to the user's email address is valid for 15 minutes.

        Enable the **phrase** parameter to include a randomly generated security phrase in both the email and the response. Showing that phrase in your app lets the user confirm the email genuinely came from your request, which helps protect against phishing.

        Parameters
        ----------
        email : str
            User email.
        phrase : Optional[bool]
            Toggle for security phrase. If enabled, email will be sent with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/recovery/otp'
        api_params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')
        api_params['email'] = self._normalize_value(email)
        if phrase is not None:
            api_params['phrase'] = self._normalize_value(phrase)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def update_recovery_otp(
        self,
        user_id: str,
        secret: str,
        password: str,
    ) -> Token:
        """
        Use this endpoint to complete the user password recovery process using the 6-digit code that was emailed by [createRecoveryOTP](https://appwrite.io/docs/references/cloud/client-web/account#createRecoveryOTP). Pass the **userId** of the user along with the **secret** code from the email and the new **password** to set. If confirmed, this route will return a 200 status code, the code is consumed and the user's password is updated.

        The new password must satisfy the project's enabled password policies, including custom deny lists. Dictionary entries match the entire password case-sensitively; personal-data terms match substrings case-insensitively. Personal-data validation runs after token verification against the recovered user's ID, name, email, and phone, closing the previous recovery gap for profile-based checks. A rejected password leaves the existing credentials unchanged and the recovery token usable.

        Parameters
        ----------
        user_id : str
            User ID.
        secret : str
            Valid recovery OTP code.
        password : str
            New user password. Must be between 8 and 256 chars.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/recovery/otp'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)
        api_params['password'] = self._normalize_value(password)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def list_sessions(
        self,
        total: Optional[bool] = None,
    ) -> SessionList:
        """
        Get the list of active sessions across different devices for the currently logged in user.

        Parameters
        ----------
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        SessionList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions'
        api_params = {}
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=SessionList)

    def delete_sessions(
        self,
        current: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Delete all sessions from the user account and remove any sessions cookies from the end client. Pass `current` as false to keep the session making the request and sign out of every other session.

        Parameters
        ----------
        current : Optional[bool]
            Delete the current session too. Use false to sign out of every other session while staying signed in on this one.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions'
        api_params = {}
        if current is not None:
            api_params['current'] = self._normalize_value(current)

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def create_anonymous_session(
        self,
    ) -> Session:
        """
        Use this endpoint to allow a new user to register an anonymous account in your project. This route will also create a new session for the user. To allow the new user to convert an anonymous account to a normal account, you need to update its [email and password](https://appwrite.io/docs/references/cloud/client-web/account#updateEmail) or create an [OAuth2 session](https://appwrite.io/docs/references/cloud/client-web/account#CreateOAuth2Session).
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/anonymous'
        api_params = {}

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    def create_email_password_session(
        self,
        email: str,
        password: str,
        duration: Optional[float] = None,
    ) -> Session:
        """
        Allow the user to login into their account by providing a valid email and password combination. This route will create a new session for the user. Use the optional `duration` parameter to create a shorter session, for example when the user doesn't choose "remember me". It must be at least 60 seconds and cannot exceed the project maximum session length.

        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        email : str
            User email.
        password : str
            User password. Must be at least 8 chars.
        duration : Optional[float]
            Session length in seconds. Minimum is 60 seconds, and it cannot exceed the project maximum session length. Defaults to the project maximum session length.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/email'
        api_params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['email'] = self._normalize_value(email)
        api_params['password'] = self._normalize_value(password)
        if duration is not None:
            api_params['duration'] = self._normalize_value(duration)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    def create_id_token_session(
        self,
        provider: IdTokenProvider,
        id_token: str,
        nonce: Optional[str] = None,
        access_token: Optional[str] = None,
        access_token_expiry: Optional[float] = None,
        name: Optional[str] = None,
    ) -> Session:
        """
        Allow the user to login to their account using an OpenID Connect ID token obtained natively from the OAuth2 provider, for example via Google Credential Manager on Android or Sign in with Apple on iOS. No browser or redirect is involved: the ID token is verified against the provider's published signing keys and a session is created in a single request.

        Native sign-in is switched on per provider with its nativeEnabled setting. It is independent of the browser-based flow's enabled setting, which has no effect on this endpoint. The token's audience must match the provider's configured client ID or one of its native client IDs; tokens issued for any other client ID are rejected. For Sign in with Apple, register your app's bundle ID as a native client ID. For Google, the web client ID used by Credential Manager is usually the configured client ID; add your Android and iOS client IDs as native client IDs if your app requests tokens for them.

        Pass the raw nonce used when requesting the ID token so it can be validated against the token's nonce claim. When signing in with Apple, the nonce is required: hash it with SHA-256 before passing it to the Apple SDK, and send the raw value here - Apple tokens requested without a nonce are rejected. For Google the nonce is optional: it is validated whenever the token carries one, and ignored when the provider issued the token without one. Apple only returns the user's name on the first authorization, and never inside the ID token - capture it on the client and pass it via the name parameter.

        If there is already an active session, the new session will be attached to the logged-in account. If there are no active sessions, the server will attempt to look for a user with the same email address as the verified email received from the provider and attach the new session to the existing user. If no matching user is found - the server will create a new user.

        This flow does not return provider refresh tokens. You may pass an access token the provider handed your client, along with its lifetime, to store it on the session - but Appwrite cannot renew it once it expires. If your app needs long-lived access to provider APIs, use the browser-based OAuth2 flow instead.

        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        provider : IdTokenProvider
            OAuth2 provider that issued the ID token. Currently, supported providers are: apple, google.
        id_token : str
            OpenID Connect ID token (JWT) obtained natively from the provider, for example via Google Credential Manager or Sign in with Apple.
        nonce : Optional[str]
            Raw nonce used when requesting the ID token. Required for Apple, and whenever the token carries a nonce claim, which must match it. Ignored when the provider issued the token without a nonce.
        access_token : Optional[str]
            Provider access token to store alongside the session for calling provider APIs. Never used for authentication.
        access_token_expiry : Optional[float]
            Seconds until the provider access token expires, as reported by the provider. Stored so clients can tell when the stored token goes stale.
        name : Optional[str]
            User name. Only used when creating a new user and the ID token has no name claim, such as on the first Sign in with Apple authorization.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/id-token'
        api_params = {}
        if provider is None:
            raise AppwriteException('Missing required parameter: "provider"')
        if id_token is None:
            raise AppwriteException('Missing required parameter: "id_token"')
        api_params['provider'] = self._normalize_value(provider)
        api_params['idToken'] = self._normalize_value(id_token)
        if nonce is not None:
            api_params['nonce'] = self._normalize_value(nonce)
        if access_token is not None:
            api_params['accessToken'] = self._normalize_value(access_token)
        if access_token_expiry is not None:
            api_params['accessTokenExpiry'] = self._normalize_value(access_token_expiry)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    @deprecated("This API has been deprecated since 1.6.0. Please use `account.create_session` instead.")
    def update_magic_url_session(
        self,
        user_id: str,
        secret: str,
    ) -> Session:
        """
        Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

        .. deprecated::1.6.0
            This API has been deprecated since 1.6.0. Please use `account.create_session` instead.
        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        secret : str
            Valid verification token.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/magic-url'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    @deprecated("This API has been deprecated since 1.6.0. Please use `account.create_session` instead.")
    def update_phone_session(
        self,
        user_id: str,
        secret: str,
    ) -> Session:
        """
        Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

        .. deprecated::1.6.0
            This API has been deprecated since 1.6.0. Please use `account.create_session` instead.
        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        secret : str
            Valid verification token.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/phone'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    def create_session(
        self,
        user_id: str,
        secret: str,
    ) -> Session:
        """
        Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        secret : str
            Secret of a token generated by login methods. For example, the `createMagicURLToken` or `createPhoneToken` methods.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/token'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    def get_session(
        self,
        session_id: str,
    ) -> Session:
        """
        Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will return the current session being used.

        Parameters
        ----------
        session_id : str
            Session ID. Use the string 'current' to get the current device session.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/{sessionId}'
        api_params = {}
        if session_id is None or session_id == '':
            raise AppwriteException('Missing required parameter: "session_id"')
        api_path = api_path.replace('{sessionId}', self._encode_path(session_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    def update_session(
        self,
        session_id: str,
    ) -> Session:
        """
        Use this endpoint to extend a session's length. Extending a session is useful when session expiry is short. If the session was created using an OAuth provider, this endpoint refreshes the access token from the provider.

        Parameters
        ----------
        session_id : str
            Session ID. Use the string 'current' to update the current device session.
        Returns
        -------
        Session
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/{sessionId}'
        api_params = {}
        if session_id is None or session_id == '':
            raise AppwriteException('Missing required parameter: "session_id"')
        api_path = api_path.replace('{sessionId}', self._encode_path(session_id))

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Session)

    def delete_session(
        self,
        session_id: str,
    ) -> Dict[str, Any]:
        """
        Logout the user. Use 'current' as the session ID to logout on this device, use a session ID to logout on another device. If you're looking to logout the user on all devices, use [Delete Sessions](https://appwrite.io/docs/references/cloud/client-web/account#deleteSessions) instead.

        Parameters
        ----------
        session_id : str
            Session ID. Use the string 'current' to delete the current device session.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/{sessionId}'
        api_params = {}
        if session_id is None or session_id == '':
            raise AppwriteException('Missing required parameter: "session_id"')
        api_path = api_path.replace('{sessionId}', self._encode_path(session_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def update_status(
        self,
        model_type: Type[T] = dict,
    ) -> User[T]:
        """
        Block the currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. To completely delete a user, use the Users API instead.

        Parameters
        ----------
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        User[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/status'
        api_params = {}

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return User.with_data(response, model_type)

    def create_email_token(
        self,
        user_id: str,
        email: str,
        phrase: Optional[bool] = None,
    ) -> Token:
        """
        Sends the user an email with a secret key for creating a session. If the email address has never been used, a **new account is created** using the provided `userId`. Otherwise, if the email address is already attached to an account, the **user ID is ignored**. Then, the user will receive an email with the one-time password. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's email is valid for 15 minutes.

        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars. If the email address has never been used, a new account is created using the provided userId. Otherwise, if the email address is already attached to an account, the user ID is ignored.
        email : str
            User email.
        phrase : Optional[bool]
            Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/tokens/email'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['email'] = self._normalize_value(email)
        if phrase is not None:
            api_params['phrase'] = self._normalize_value(phrase)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def create_magic_url_token(
        self,
        user_id: str,
        email: str,
        url: Optional[str] = None,
        phrase: Optional[bool] = None,
    ) -> Token:
        """
        Sends the user an email with a secret key for creating a session. If the provided user ID has not been registered, a new user will be created. When the user clicks the link in the email, the user is redirected back to the URL you provided with the secret key and userId values attached to the URL query string. Use the query string parameters to submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The link sent to the user's email address is valid for 1 hour.

        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        user_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars. If the email address has never been used, a new account is created using the provided userId. Otherwise, if the email address is already attached to an account, the user ID is ignored.
        email : str
            User email.
        url : Optional[str]
            URL to redirect the user back to your app from the magic URL login. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        phrase : Optional[bool]
            Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/tokens/magic-url'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['email'] = self._normalize_value(email)
        if url is not None:
            api_params['url'] = self._normalize_value(url)
        if phrase is not None:
            api_params['phrase'] = self._normalize_value(phrase)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def create_o_auth2_token(
        self,
        provider: OAuthProvider,
        success: Optional[str] = None,
        failure: Optional[str] = None,
        scopes: Optional[List[str]] = None,
        state: Optional[str] = None,
    ) -> str:
        """
        Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2 provider should be enabled from the Appwrite console first. Use the success and failure arguments to provide a redirect URL's back to your app when login is completed.

        If authentication succeeds, `userId` and `secret` of a token will be appended to the success URL as query parameters. These can be used to create a new session using the [Create session](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint.

        If there is already an active session, the OAuth2 identity is attached to the logged-in account and that session stays active until the token is exchanged for a new one.

        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        provider : OAuthProvider
            OAuth2 Provider. Currently, supported providers are: amazon, apple, appwrite, auth0, authentik, autodesk, bitbucket, bitly, box, cloudflare, dailymotion, discord, disqus, dropbox, etsy, facebook, figma, fusionauth, github, gitlab, google, huggingface, kakao, keycloak, kick, linkedin, microsoft, notion, oidc, okta, paypal, paypalSandbox, podio, resend, salesforce, slack, spotify, stripe, tiktok, tradeshift, tradeshiftBox, twitch, webflow, wordpress, x, yahoo, yammer, yandex, zoho, zoom.
        success : Optional[str]
            URL to redirect back to your app after a successful login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        failure : Optional[str]
            URL to redirect back to your app after a failed login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        scopes : Optional[List[str]]
            A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes. Maximum of 100 scopes are allowed, each 4096 characters long.
        state : Optional[str]
            An opaque value your app generates and keeps, for example in a cookie. It is returned unchanged as the `state` query parameter on the success and failure URLs, so your app can check that the sign-in it receives is one it started. Printable ASCII only (RFC 6749 Appendix A.5). Max length: 256 chars.
        Returns
        -------
        str
            Authentication response as a string

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/tokens/oauth2/{provider}'
        api_params = {}
        if provider is None:
            raise AppwriteException('Missing required parameter: "provider"')
        api_path = api_path.replace('{provider}', self._encode_path(provider))
        if success is not None:
            api_params['success'] = self._normalize_value(success)
        if failure is not None:
            api_params['failure'] = self._normalize_value(failure)
        if scopes is not None:
            api_params['scopes'] = self._normalize_value(scopes)
        if state is not None:
            api_params['state'] = self._normalize_value(state)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'text/html',
            },
            api_params,
            response_type='location',
        )

        return response

    def create_passkey_token(
        self,
    ) -> PasskeyChallenge:
        """
        Start signing in with a passkey. No email or user ID is needed: pass the returned `publicKey` options to `navigator.credentials.get()` and the user picks one of their passkeys. Then call [Update passkey token](/docs/references/cloud/client-web/account#updatePasskeyToken) with the credential to receive a token, and exchange it with [Create session](/docs/references/cloud/client-web/account#createSession). The challenge expires after 5 minutes.
        Returns
        -------
        PasskeyChallenge
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/tokens/passkey'
        api_params = {}

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=PasskeyChallenge)

    def update_passkey_token(
        self,
        challenge_id: str,
        credential: Dict[str, Any],
    ) -> TokenSecret:
        """
        Complete a passkey sign-in started with [Create passkey token](/docs/references/cloud/client-web/account#createPasskeyToken). Pass the challenge ID and the JSON form of the credential returned by `navigator.credentials.get()`, for example `credential.toJSON()`. The returned token includes its secret and expires after 1 minute: exchange it for a session with [Create session](/docs/references/cloud/client-web/account#createSession). Passkeys require user verification, so the session also satisfies MFA. Each challenge can only be used once.

        Parameters
        ----------
        challenge_id : str
            Challenge ID returned by createPasskeyToken.
        credential : Dict[str, Any]
            Authentication credential returned by the authenticator, in the JSON form produced by `PublicKeyCredential.toJSON()`.
        Returns
        -------
        TokenSecret
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/tokens/passkey'
        api_params = {}
        if challenge_id is None:
            raise AppwriteException('Missing required parameter: "challenge_id"')
        if credential is None:
            raise AppwriteException('Missing required parameter: "credential"')
        api_params['challengeId'] = self._normalize_value(challenge_id)
        api_params['credential'] = self._normalize_value(credential)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=TokenSecret)

    def create_phone_token(
        self,
        user_id: str,
        phone: str,
    ) -> Token:
        """
        Sends the user an SMS with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's phone is valid for 15 minutes.

        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        user_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars. If the phone number has never been used, a new account is created using the provided userId. Otherwise, if the phone number is already attached to an account, the user ID is ignored.
        phone : str
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/tokens/phone'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if phone is None:
            raise AppwriteException('Missing required parameter: "phone"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['phone'] = self._normalize_value(phone)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def create_email_verification(
        self,
        url: str,
    ) -> Token:
        """
        Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updateVerification). The verification link sent to the user's email address is valid for 7 days.

        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

        Parameters
        ----------
        url : str
            URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/email'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')
        api_params['url'] = self._normalize_value(url)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    @deprecated("This API has been deprecated since 1.8.0. Please use `account.create_email_verification` instead.")
    def create_verification(
        self,
        url: str,
    ) -> Token:
        """
        Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updateVerification). The verification link sent to the user's email address is valid for 7 days.

        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `account.create_email_verification` instead.
        Parameters
        ----------
        url : str
            URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/email'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')
        api_params['url'] = self._normalize_value(url)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def update_email_verification(
        self,
        user_id: str,
        secret: str,
    ) -> Token:
        """
        Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

        Parameters
        ----------
        user_id : str
            User ID.
        secret : str
            Valid verification token.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/email'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    @deprecated("This API has been deprecated since 1.8.0. Please use `account.update_email_verification` instead.")
    def update_verification(
        self,
        user_id: str,
        secret: str,
    ) -> Token:
        """
        Use this endpoint to complete the user email verification process. Use both the **userId** and **secret** parameters that were attached to your app URL to verify the user email ownership. If confirmed this route will return a 200 status code.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `account.update_email_verification` instead.
        Parameters
        ----------
        user_id : str
            User ID.
        secret : str
            Valid verification token.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/email'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def create_email_verification_otp(
        self,
        phrase: Optional[bool] = None,
    ) -> Token:
        """
        Use this endpoint to send a 6-digit verification code to the currently logged in user's email address. Unlike [createEmailVerification](https://appwrite.io/docs/references/cloud/client-web/account#createEmailVerification), this method requires no redirect URL, which makes it suitable for mobile and desktop apps that cannot host a verification page. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updateEmailVerificationOTP). The code sent to the user's email address is valid for 15 minutes.

        Enable the **phrase** parameter to include a randomly generated security phrase in both the email and the response. Showing that phrase in your app lets the user confirm the email genuinely came from your request, which helps protect against phishing.

        Parameters
        ----------
        phrase : Optional[bool]
            Toggle for security phrase. If enabled, email will be sent with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/email/otp'
        api_params = {}
        if phrase is not None:
            api_params['phrase'] = self._normalize_value(phrase)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def update_email_verification_otp(
        self,
        user_id: str,
        secret: str,
    ) -> Token:
        """
        Use this endpoint to complete the user email verification process using the 6-digit code that was emailed by [createEmailVerificationOTP](https://appwrite.io/docs/references/cloud/client-web/account#createEmailVerificationOTP). Pass the **userId** of the user being verified along with the **secret** code from the email. If confirmed, this route will return a 200 status code and the code is consumed.

        Parameters
        ----------
        user_id : str
            User ID.
        secret : str
            Valid verification OTP code.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/email/otp'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def create_phone_verification(
        self,
    ) -> Token:
        """
        Use this endpoint to send a verification SMS to the currently logged in user. This endpoint is meant for use after updating a user's phone number using the [accountUpdatePhone](https://appwrite.io/docs/references/cloud/client-web/account#updatePhone) endpoint. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updatePhoneVerification). The verification code sent to the user's phone number is valid for 15 minutes.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/phone'
        api_params = {}

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)

    def update_phone_verification(
        self,
        user_id: str,
        secret: str,
    ) -> Token:
        """
        Use this endpoint to complete the user phone verification process. Use the **userId** and **secret** that were sent to your user's phone number to verify the user email ownership. If confirmed this route will return a 200 status code.

        Parameters
        ----------
        user_id : str
            User ID.
        secret : str
            Valid verification token.
        Returns
        -------
        Token
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verifications/phone'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')
        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')
        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Token)
