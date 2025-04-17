from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException
from ..enums.authenticator_type import AuthenticatorType;
from ..enums.authentication_factor import AuthenticationFactor;
from ..enums.o_auth_provider import OAuthProvider;

class Account(Service):

    def __init__(self, client) -> None:
        super(Account, self).__init__(client)

    def get(self) -> Dict[str, Any]:
        """
        Get the currently logged in user.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def create(self, user_id: str, email: str, password: str, name: str = None) -> Dict[str, Any]:
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
        name : str
            User name. Max length: 128 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['email'] = email
        api_params['password'] = password
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email(self, email: str, password: str) -> Dict[str, Any]:
        """
        Update currently logged in user account email address. After changing user address, the user confirmation status will get reset. A new confirmation email is not sent automatically however you can use the send confirmation email endpoint again to send the confirmation email. For security measures, user password is required to complete this request.
        This endpoint can also be used to convert an anonymous account to a normal one, by passing an email address and a new password.
        

        Parameters
        ----------
        email : str
            User email.
        password : str
            User password. Must be at least 8 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['email'] = email
        api_params['password'] = password

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_identities(self, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get the list of identities for the currently logged in user.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, provider, providerUid, providerEmail, providerAccessTokenExpiry
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/identities'
        api_params = {}

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def delete_identity(self, identity_id: str) -> Dict[str, Any]:
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
        if identity_id is None:
            raise AppwriteException('Missing required parameter: "identity_id"')

        api_path = api_path.replace('{identityId}', identity_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_jwt(self) -> Dict[str, Any]:
        """
        Use this endpoint to create a JSON Web Token. You can use the resulting JWT to authenticate on behalf of the current user when working with the Appwrite server-side API and SDKs. The JWT secret is valid for 15 minutes from its creation and will be invalid if the user will logout in that time frame.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/jwts'
        api_params = {}

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_logs(self, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get the list of latest security activity logs for the currently logged in user. Each log returns user IP address, location and date and time of log.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/logs'
        api_params = {}

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def update_mfa(self, mfa: bool) -> Dict[str, Any]:
        """
        Enable or disable MFA on an account.

        Parameters
        ----------
        mfa : bool
            Enable or disable MFA.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa'
        api_params = {}
        if mfa is None:
            raise AppwriteException('Missing required parameter: "mfa"')


        api_params['mfa'] = mfa

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_mfa_authenticator(self, type: AuthenticatorType) -> Dict[str, Any]:
        """
        Add an authenticator app to be used as an MFA factor. Verify the authenticator using the [verify authenticator](/docs/references/cloud/client-web/account#updateMfaAuthenticator) method.

        Parameters
        ----------
        type : AuthenticatorType
            Type of authenticator. Must be `totp`
        
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

        api_path = api_path.replace('{type}', type)


        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_mfa_authenticator(self, type: AuthenticatorType, otp: str) -> Dict[str, Any]:
        """
        Verify an authenticator app after adding it using the [add authenticator](/docs/references/cloud/client-web/account#createMfaAuthenticator) method.

        Parameters
        ----------
        type : AuthenticatorType
            Type of authenticator.
        otp : str
            Valid verification token.
        
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

        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')

        api_path = api_path.replace('{type}', type)

        api_params['otp'] = otp

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_mfa_authenticator(self, type: AuthenticatorType) -> Dict[str, Any]:
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

        api_path = api_path.replace('{type}', type)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_mfa_challenge(self, factor: AuthenticationFactor) -> Dict[str, Any]:
        """
        Begin the process of MFA verification after sign-in. Finish the flow with [updateMfaChallenge](/docs/references/cloud/client-web/account#updateMfaChallenge) method.

        Parameters
        ----------
        factor : AuthenticationFactor
            Factor used for verification. Must be one of following: `email`, `phone`, `totp`, `recoveryCode`.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/challenge'
        api_params = {}
        if factor is None:
            raise AppwriteException('Missing required parameter: "factor"')


        api_params['factor'] = factor

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_mfa_challenge(self, challenge_id: str, otp: str) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/challenge'
        api_params = {}
        if challenge_id is None:
            raise AppwriteException('Missing required parameter: "challenge_id"')

        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')


        api_params['challengeId'] = challenge_id
        api_params['otp'] = otp

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_mfa_factors(self) -> Dict[str, Any]:
        """
        List the factors available on the account to be used as a MFA challange.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/factors'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_mfa_recovery_codes(self) -> Dict[str, Any]:
        """
        Get recovery codes that can be used as backup for MFA flow. Before getting codes, they must be generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to read recovery codes.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/recovery-codes'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def create_mfa_recovery_codes(self) -> Dict[str, Any]:
        """
        Generate recovery codes as backup for MFA flow. It's recommended to generate and show then immediately after user successfully adds their authehticator. Recovery codes can be used as a MFA verification type in [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/recovery-codes'
        api_params = {}

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_mfa_recovery_codes(self) -> Dict[str, Any]:
        """
        Regenerate recovery codes that can be used as backup for MFA flow. Before regenerating codes, they must be first generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method. An OTP challenge is required to regenreate recovery codes.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/mfa/recovery-codes'
        api_params = {}

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_name(self, name: str) -> Dict[str, Any]:
        """
        Update currently logged in user account name.

        Parameters
        ----------
        name : str
            User name. Max length: 128 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/name'
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['name'] = name

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_password(self, password: str, old_password: str = None) -> Dict[str, Any]:
        """
        Update currently logged in user password. For validation, user is required to pass in the new password, and the old password. For users created with OAuth, Team Invites and Magic URL, oldPassword is optional.

        Parameters
        ----------
        password : str
            New user password. Must be at least 8 chars.
        old_password : str
            Current user password. Must be at least 8 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/password'
        api_params = {}
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        api_params['password'] = password
        api_params['oldPassword'] = old_password

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_phone(self, phone: str, password: str) -> Dict[str, Any]:
        """
        Update the currently logged in user's phone number. After updating the phone number, the phone verification status will be reset. A confirmation SMS is not sent automatically, however you can use the [POST /account/verification/phone](https://appwrite.io/docs/references/cloud/client-web/account#createPhoneVerification) endpoint to send a confirmation SMS.

        Parameters
        ----------
        phone : str
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        password : str
            User password. Must be at least 8 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['phone'] = phone
        api_params['password'] = password

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_prefs(self) -> Dict[str, Any]:
        """
        Get the preferences as a key-value object for the currently logged in user.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/prefs'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def update_prefs(self, prefs: dict) -> Dict[str, Any]:
        """
        Update currently logged in user account preferences. The object you pass is stored as is, and replaces any previous value. The maximum allowed prefs size is 64kB and throws error if exceeded.

        Parameters
        ----------
        prefs : dict
            Prefs key-value JSON object.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/prefs'
        api_params = {}
        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')


        api_params['prefs'] = prefs

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_recovery(self, email: str, url: str) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['email'] = email
        api_params['url'] = url

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_recovery(self, user_id: str, secret: str, password: str) -> Dict[str, Any]:
        """
        Use this endpoint to complete the user account password reset. Both the **userId** and **secret** arguments will be passed as query parameters to the redirect URL you have provided when sending your request to the [POST /account/recovery](https://appwrite.io/docs/references/cloud/client-web/account#createRecovery) endpoint.
        
        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.

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
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['secret'] = secret
        api_params['password'] = password

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_sessions(self) -> Dict[str, Any]:
        """
        Get the list of active sessions across different devices for the currently logged in user.

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

        return self.client.call('get', api_path, {
        }, api_params)

    def delete_sessions(self) -> Dict[str, Any]:
        """
        Delete all sessions from the user account and remove any sessions cookies from the end client.

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

        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_anonymous_session(self) -> Dict[str, Any]:
        """
        Use this endpoint to allow a new user to register an anonymous account in your project. This route will also create a new session for the user. To allow the new user to convert an anonymous account to a normal account, you need to update its [email and password](https://appwrite.io/docs/references/cloud/client-web/account#updateEmail) or create an [OAuth2 session](https://appwrite.io/docs/references/cloud/client-web/account#CreateOAuth2Session).

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/sessions/anonymous'
        api_params = {}

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_email_password_session(self, email: str, password: str) -> Dict[str, Any]:
        """
        Allow the user to login into their account by providing a valid email and password combination. This route will create a new session for the user.
        
        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        email : str
            User email.
        password : str
            User password. Must be at least 8 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['email'] = email
        api_params['password'] = password

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_magic_url_session(self, user_id: str, secret: str) -> Dict[str, Any]:
        """
        Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        secret : str
            Valid verification token.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['secret'] = secret

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_phone_session(self, user_id: str, secret: str) -> Dict[str, Any]:
        """
        Use this endpoint to create a session from token. Provide the **userId** and **secret** parameters from the successful response of authentication flows initiated by token creation. For example, magic URL and phone login.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        secret : str
            Valid verification token.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['secret'] = secret

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_session(self, user_id: str, secret: str) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['secret'] = secret

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_session(self, session_id: str) -> Dict[str, Any]:
        """
        Use this endpoint to get a logged in user's session using a Session ID. Inputting 'current' will return the current session being used.

        Parameters
        ----------
        session_id : str
            Session ID. Use the string 'current' to get the current device session.
        
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
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace('{sessionId}', session_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_session(self, session_id: str) -> Dict[str, Any]:
        """
        Use this endpoint to extend a session's length. Extending a session is useful when session expiry is short. If the session was created using an OAuth provider, this endpoint refreshes the access token from the provider.

        Parameters
        ----------
        session_id : str
            Session ID. Use the string 'current' to update the current device session.
        
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
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace('{sessionId}', session_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_session(self, session_id: str) -> Dict[str, Any]:
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
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace('{sessionId}', session_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_status(self) -> Dict[str, Any]:
        """
        Block the currently logged in user account. Behind the scene, the user record is not deleted but permanently blocked from any access. To completely delete a user, use the Users API instead.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/status'
        api_params = {}

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_email_token(self, user_id: str, email: str, phrase: bool = None) -> Dict[str, Any]:
        """
        Sends the user an email with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's email is valid for 15 minutes.
        
        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        phrase : bool
            Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['email'] = email
        api_params['phrase'] = phrase

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_magic_url_token(self, user_id: str, email: str, url: str = None, phrase: bool = None) -> Dict[str, Any]:
        """
        Sends the user an email with a secret key for creating a session. If the provided user ID has not been registered, a new user will be created. When the user clicks the link in the email, the user is redirected back to the URL you provided with the secret key and userId values attached to the URL query string. Use the query string parameters to submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The link sent to the user's email address is valid for 1 hour.
        
        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).
        

        Parameters
        ----------
        user_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        url : str
            URL to redirect the user back to your app from the magic URL login. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        phrase : bool
            Toggle for security phrase. If enabled, email will be send with a randomly generated phrase and the phrase will also be included in the response. Confirming phrases match increases the security of your authentication flow.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['email'] = email
        api_params['url'] = url
        api_params['phrase'] = phrase

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_o_auth2_token(self, provider: OAuthProvider, success: str = None, failure: str = None, scopes: List[str] = None) -> str:
        """
        Allow the user to login to their account using the OAuth2 provider of their choice. Each OAuth2 provider should be enabled from the Appwrite console first. Use the success and failure arguments to provide a redirect URL's back to your app when login is completed. 
        
        If authentication succeeds, `userId` and `secret` of a token will be appended to the success URL as query parameters. These can be used to create a new session using the [Create session](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint.
        
        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        provider : OAuthProvider
            OAuth2 Provider. Currently, supported providers are: amazon, apple, auth0, authentik, autodesk, bitbucket, bitly, box, dailymotion, discord, disqus, dropbox, etsy, facebook, figma, github, gitlab, google, linkedin, microsoft, notion, oidc, okta, paypal, paypalSandbox, podio, salesforce, slack, spotify, stripe, tradeshift, tradeshiftBox, twitch, wordpress, yahoo, yammer, yandex, zoho, zoom.
        success : str
            URL to redirect back to your app after a successful login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        failure : str
            URL to redirect back to your app after a failed login attempt.  Only URLs from hostnames in your project's platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        scopes : List[str]
            A list of custom OAuth2 scopes. Check each provider internal docs for a list of supported scopes. Maximum of 100 scopes are allowed, each 4096 characters long.
        
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

        api_path = api_path.replace('{provider}', provider)

        api_params['success'] = success
        api_params['failure'] = failure
        api_params['scopes'] = scopes

        return self.client.call('get', api_path, {
        }, api_params, response_type='location')

    def create_phone_token(self, user_id: str, phone: str) -> Dict[str, Any]:
        """
        Sends the user an SMS with a secret key for creating a session. If the provided user ID has not be registered, a new user will be created. Use the returned user ID and secret and submit a request to the [POST /v1/account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process. The secret sent to the user's phone is valid for 15 minutes.
        
        A user is limited to 10 active sessions at a time by default. [Learn more about session limits](https://appwrite.io/docs/authentication-security#limits).

        Parameters
        ----------
        user_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        phone : str
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['userId'] = user_id
        api_params['phone'] = phone

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_verification(self, url: str) -> Dict[str, Any]:
        """
        Use this endpoint to send a verification message to your user email address to confirm they are the valid owners of that address. Both the **userId** and **secret** arguments will be passed as query parameters to the URL you have provided to be attached to the verification email. The provided URL should redirect the user back to your app and allow you to complete the verification process by verifying both the **userId** and **secret** parameters. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updateVerification). The verification link sent to the user's email address is valid for 7 days.
        
        Please note that in order to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md), the only valid redirect URLs are the ones from domains you have set when adding your platforms in the console interface.
        

        Parameters
        ----------
        url : str
            URL to redirect the user back to your app from the verification email. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verification'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_verification(self, user_id: str, secret: str) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verification'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')


        api_params['userId'] = user_id
        api_params['secret'] = secret

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_phone_verification(self) -> Dict[str, Any]:
        """
        Use this endpoint to send a verification SMS to the currently logged in user. This endpoint is meant for use after updating a user's phone number using the [accountUpdatePhone](https://appwrite.io/docs/references/cloud/client-web/account#updatePhone) endpoint. Learn more about how to [complete the verification process](https://appwrite.io/docs/references/cloud/client-web/account#updatePhoneVerification). The verification code sent to the user's phone number is valid for 15 minutes.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verification/phone'
        api_params = {}

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_phone_verification(self, user_id: str, secret: str) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/account/verification/phone'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')


        api_params['userId'] = user_id
        api_params['secret'] = secret

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)
