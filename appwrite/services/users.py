from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException
from ..enums.password_hash import PasswordHash;
from ..enums.authenticator_type import AuthenticatorType;
from ..enums.messaging_provider_type import MessagingProviderType;

class Users(Service):

    def __init__(self, client) -> None:
        super(Users, self).__init__(client)

    def list(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all the project's users. You can use the query params to filter your results.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, email, phone, status, passwordUpdate, registration, emailVerification, phoneVerification, labels
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create(self, user_id: str, email: str = None, phone: str = None, password: str = None, name: str = None) -> Dict[str, Any]:
        """
        Create a new user.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        phone : str
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        password : str
            Plain text user password. Must be at least 8 chars.
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

        api_path = '/users'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')


        api_params['userId'] = user_id
        api_params['email'] = email
        api_params['phone'] = phone
        api_params['password'] = password
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_argon2_user(self, user_id: str, email: str, password: str, name: str = None) -> Dict[str, Any]:
        """
        Create a new user. Password provided must be hashed with the [Argon2](https://en.wikipedia.org/wiki/Argon2) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            User password hashed using Argon2.
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

        api_path = '/users/argon2'
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

    def create_bcrypt_user(self, user_id: str, email: str, password: str, name: str = None) -> Dict[str, Any]:
        """
        Create a new user. Password provided must be hashed with the [Bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            User password hashed using Bcrypt.
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

        api_path = '/users/bcrypt'
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

    def list_identities(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get identities for all users.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, provider, providerUid, providerEmail, providerAccessTokenExpiry
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/identities'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

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

        api_path = '/users/identities/{identityId}'
        api_params = {}
        if identity_id is None:
            raise AppwriteException('Missing required parameter: "identity_id"')

        api_path = api_path.replace('{identityId}', identity_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_md5_user(self, user_id: str, email: str, password: str, name: str = None) -> Dict[str, Any]:
        """
        Create a new user. Password provided must be hashed with the [MD5](https://en.wikipedia.org/wiki/MD5) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            User password hashed using MD5.
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

        api_path = '/users/md5'
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

    def create_ph_pass_user(self, user_id: str, email: str, password: str, name: str = None) -> Dict[str, Any]:
        """
        Create a new user. Password provided must be hashed with the [PHPass](https://www.openwall.com/phpass/) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or pass the string `ID.unique()`to auto generate it. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            User password hashed using PHPass.
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

        api_path = '/users/phpass'
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

    def create_scrypt_user(self, user_id: str, email: str, password: str, password_salt: str, password_cpu: float, password_memory: float, password_parallel: float, password_length: float, name: str = None) -> Dict[str, Any]:
        """
        Create a new user. Password provided must be hashed with the [Scrypt](https://github.com/Tarsnap/scrypt) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            User password hashed using Scrypt.
        password_salt : str
            Optional salt used to hash password.
        password_cpu : float
            Optional CPU cost used to hash password.
        password_memory : float
            Optional memory cost used to hash password.
        password_parallel : float
            Optional parallelization cost used to hash password.
        password_length : float
            Optional hash length used to hash password.
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

        api_path = '/users/scrypt'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        if password_salt is None:
            raise AppwriteException('Missing required parameter: "password_salt"')

        if password_cpu is None:
            raise AppwriteException('Missing required parameter: "password_cpu"')

        if password_memory is None:
            raise AppwriteException('Missing required parameter: "password_memory"')

        if password_parallel is None:
            raise AppwriteException('Missing required parameter: "password_parallel"')

        if password_length is None:
            raise AppwriteException('Missing required parameter: "password_length"')


        api_params['userId'] = user_id
        api_params['email'] = email
        api_params['password'] = password
        api_params['passwordSalt'] = password_salt
        api_params['passwordCpu'] = password_cpu
        api_params['passwordMemory'] = password_memory
        api_params['passwordParallel'] = password_parallel
        api_params['passwordLength'] = password_length
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_scrypt_modified_user(self, user_id: str, email: str, password: str, password_salt: str, password_salt_separator: str, password_signer_key: str, name: str = None) -> Dict[str, Any]:
        """
        Create a new user. Password provided must be hashed with the [Scrypt Modified](https://gist.github.com/Meldiron/eecf84a0225eccb5a378d45bb27462cc) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            User password hashed using Scrypt Modified.
        password_salt : str
            Salt used to hash password.
        password_salt_separator : str
            Salt separator used to hash password.
        password_signer_key : str
            Signer key used to hash password.
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

        api_path = '/users/scrypt-modified'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        if password_salt is None:
            raise AppwriteException('Missing required parameter: "password_salt"')

        if password_salt_separator is None:
            raise AppwriteException('Missing required parameter: "password_salt_separator"')

        if password_signer_key is None:
            raise AppwriteException('Missing required parameter: "password_signer_key"')


        api_params['userId'] = user_id
        api_params['email'] = email
        api_params['password'] = password
        api_params['passwordSalt'] = password_salt
        api_params['passwordSaltSeparator'] = password_salt_separator
        api_params['passwordSignerKey'] = password_signer_key
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_sha_user(self, user_id: str, email: str, password: str, password_version: PasswordHash = None, name: str = None) -> Dict[str, Any]:
        """
        Create a new user. Password provided must be hashed with the [SHA](https://en.wikipedia.org/wiki/Secure_Hash_Algorithm) algorithm. Use the [POST /users](https://appwrite.io/docs/server/users#usersCreate) endpoint to create users with a plain text password.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        email : str
            User email.
        password : str
            User password hashed using SHA.
        password_version : PasswordHash
            Optional SHA version used to hash password. Allowed values are: 'sha1', 'sha224', 'sha256', 'sha384', 'sha512/224', 'sha512/256', 'sha512', 'sha3-224', 'sha3-256', 'sha3-384', 'sha3-512'
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

        api_path = '/users/sha'
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
        api_params['passwordVersion'] = password_version
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get(self, user_id: str) -> Dict[str, Any]:
        """
        Get a user by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete(self, user_id: str) -> Dict[str, Any]:
        """
        Delete a user by its unique ID, thereby releasing it's ID. Since ID is released and can be reused, all user-related resources like documents or storage files should be deleted before user deletion. If you want to keep ID reserved, use the [updateStatus](https://appwrite.io/docs/server/users#usersUpdateStatus) endpoint instead.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email(self, user_id: str, email: str) -> Dict[str, Any]:
        """
        Update the user email by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        email : str
            User email.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/email'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['email'] = email

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_jwt(self, user_id: str, session_id: str = None, duration: float = None) -> Dict[str, Any]:
        """
        Use this endpoint to create a JSON Web Token for user by its unique ID. You can use the resulting JWT to authenticate on behalf of the user. The JWT secret will become invalid if the session it uses gets deleted.

        Parameters
        ----------
        user_id : str
            User ID.
        session_id : str
            Session ID. Use the string 'recent' to use the most recent session. Defaults to the most recent session.
        duration : float
            Time in seconds before JWT expires. Default duration is 900 seconds, and maximum is 3600 seconds.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/jwts'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['sessionId'] = session_id
        api_params['duration'] = duration

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_labels(self, user_id: str, labels: List[str]) -> Dict[str, Any]:
        """
        Update the user labels by its unique ID. 
        
        Labels can be used to grant access to resources. While teams are a way for user's to share access to a resource, labels can be defined by the developer to grant access without an invitation. See the [Permissions docs](https://appwrite.io/docs/permissions) for more info.

        Parameters
        ----------
        user_id : str
            User ID.
        labels : List[str]
            Array of user labels. Replaces the previous labels. Maximum of 1000 labels are allowed, each up to 36 alphanumeric characters long.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/labels'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if labels is None:
            raise AppwriteException('Missing required parameter: "labels"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['labels'] = labels

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_logs(self, user_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get the user activity logs list by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
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

        api_path = '/users/{userId}/logs'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def list_memberships(self, user_id: str, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get the user membership list by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, teamId, invited, joined, confirm, roles
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/memberships'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def update_mfa(self, user_id: str, mfa: bool) -> Dict[str, Any]:
        """
        Enable or disable MFA on a user account.

        Parameters
        ----------
        user_id : str
            User ID.
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

        api_path = '/users/{userId}/mfa'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if mfa is None:
            raise AppwriteException('Missing required parameter: "mfa"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['mfa'] = mfa

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_mfa_authenticator(self, user_id: str, type: AuthenticatorType) -> Dict[str, Any]:
        """
        Delete an authenticator app.

        Parameters
        ----------
        user_id : str
            User ID.
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

        api_path = '/users/{userId}/mfa/authenticators/{type}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        api_path = api_path.replace('{userId}', user_id)
        api_path = api_path.replace('{type}', type)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_mfa_factors(self, user_id: str) -> Dict[str, Any]:
        """
        List the factors available on the account to be used as a MFA challange.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/mfa/factors'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def get_mfa_recovery_codes(self, user_id: str) -> Dict[str, Any]:
        """
        Get recovery codes that can be used as backup for MFA flow by User ID. Before getting codes, they must be generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/mfa/recovery-codes'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_mfa_recovery_codes(self, user_id: str) -> Dict[str, Any]:
        """
        Regenerate recovery codes that can be used as backup for MFA flow by User ID. Before regenerating codes, they must be first generated using [createMfaRecoveryCodes](/docs/references/cloud/client-web/account#createMfaRecoveryCodes) method.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/mfa/recovery-codes'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_mfa_recovery_codes(self, user_id: str) -> Dict[str, Any]:
        """
        Generate recovery codes used as backup for MFA flow for User ID. Recovery codes can be used as a MFA verification type in [createMfaChallenge](/docs/references/cloud/client-web/account#createMfaChallenge) method by client SDK.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/mfa/recovery-codes'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_name(self, user_id: str, name: str) -> Dict[str, Any]:
        """
        Update the user name by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
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

        api_path = '/users/{userId}/name'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['name'] = name

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_password(self, user_id: str, password: str) -> Dict[str, Any]:
        """
        Update the user password by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        password : str
            New user password. Must be at least 8 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/password'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['password'] = password

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_phone(self, user_id: str, number: str) -> Dict[str, Any]:
        """
        Update the user phone by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        number : str
            User phone number.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/phone'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if number is None:
            raise AppwriteException('Missing required parameter: "number"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['number'] = number

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_prefs(self, user_id: str) -> Dict[str, Any]:
        """
        Get the user preferences by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/prefs'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_prefs(self, user_id: str, prefs: dict) -> Dict[str, Any]:
        """
        Update the user preferences by its unique ID. The object you pass is stored as is, and replaces any previous value. The maximum allowed prefs size is 64kB and throws error if exceeded.

        Parameters
        ----------
        user_id : str
            User ID.
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

        api_path = '/users/{userId}/prefs'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['prefs'] = prefs

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_sessions(self, user_id: str) -> Dict[str, Any]:
        """
        Get the user sessions list by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/sessions'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def create_session(self, user_id: str) -> Dict[str, Any]:
        """
        Creates a session for a user. Returns an immediately usable session object.
        
        If you want to generate a token for a custom authentication flow, use the [POST /users/{userId}/tokens](https://appwrite.io/docs/server/users#createToken) endpoint.

        Parameters
        ----------
        user_id : str
            User ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/sessions'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_sessions(self, user_id: str) -> Dict[str, Any]:
        """
        Delete all user's sessions by using the user's unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/sessions'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_session(self, user_id: str, session_id: str) -> Dict[str, Any]:
        """
        Delete a user sessions by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        session_id : str
            Session ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/sessions/{sessionId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace('{userId}', user_id)
        api_path = api_path.replace('{sessionId}', session_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_status(self, user_id: str, status: bool) -> Dict[str, Any]:
        """
        Update the user status by its unique ID. Use this endpoint as an alternative to deleting a user if you want to keep user's ID reserved.

        Parameters
        ----------
        user_id : str
            User ID.
        status : bool
            User Status. To activate the user pass `true` and to block the user pass `false`.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/status'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if status is None:
            raise AppwriteException('Missing required parameter: "status"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['status'] = status

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_targets(self, user_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        List the messaging targets that are associated with a user.

        Parameters
        ----------
        user_id : str
            User ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, email, phone, status, passwordUpdate, registration, emailVerification, phoneVerification, labels
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/targets'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_target(self, user_id: str, target_id: str, provider_type: MessagingProviderType, identifier: str, provider_id: str = None, name: str = None) -> Dict[str, Any]:
        """
        Create a messaging target.

        Parameters
        ----------
        user_id : str
            User ID.
        target_id : str
            Target ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        provider_type : MessagingProviderType
            The target provider type. Can be one of the following: `email`, `sms` or `push`.
        identifier : str
            The target identifier (token, email, phone etc.)
        provider_id : str
            Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.
        name : str
            Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/targets'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if target_id is None:
            raise AppwriteException('Missing required parameter: "target_id"')

        if provider_type is None:
            raise AppwriteException('Missing required parameter: "provider_type"')

        if identifier is None:
            raise AppwriteException('Missing required parameter: "identifier"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['targetId'] = target_id
        api_params['providerType'] = provider_type
        api_params['identifier'] = identifier
        api_params['providerId'] = provider_id
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_target(self, user_id: str, target_id: str) -> Dict[str, Any]:
        """
        Get a user's push notification target by ID.

        Parameters
        ----------
        user_id : str
            User ID.
        target_id : str
            Target ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/targets/{targetId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if target_id is None:
            raise AppwriteException('Missing required parameter: "target_id"')

        api_path = api_path.replace('{userId}', user_id)
        api_path = api_path.replace('{targetId}', target_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_target(self, user_id: str, target_id: str, identifier: str = None, provider_id: str = None, name: str = None) -> Dict[str, Any]:
        """
        Update a messaging target.

        Parameters
        ----------
        user_id : str
            User ID.
        target_id : str
            Target ID.
        identifier : str
            The target identifier (token, email, phone etc.)
        provider_id : str
            Provider ID. Message will be sent to this target from the specified provider ID. If no provider ID is set the first setup provider will be used.
        name : str
            Target name. Max length: 128 chars. For example: My Awesome App Galaxy S23.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/targets/{targetId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if target_id is None:
            raise AppwriteException('Missing required parameter: "target_id"')

        api_path = api_path.replace('{userId}', user_id)
        api_path = api_path.replace('{targetId}', target_id)

        api_params['identifier'] = identifier
        api_params['providerId'] = provider_id
        api_params['name'] = name

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_target(self, user_id: str, target_id: str) -> Dict[str, Any]:
        """
        Delete a messaging target.

        Parameters
        ----------
        user_id : str
            User ID.
        target_id : str
            Target ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/targets/{targetId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if target_id is None:
            raise AppwriteException('Missing required parameter: "target_id"')

        api_path = api_path.replace('{userId}', user_id)
        api_path = api_path.replace('{targetId}', target_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_token(self, user_id: str, length: float = None, expire: float = None) -> Dict[str, Any]:
        """
        Returns a token with a secret key for creating a session. Use the user ID and secret and submit a request to the [PUT /account/sessions/token](https://appwrite.io/docs/references/cloud/client-web/account#createSession) endpoint to complete the login process.
        

        Parameters
        ----------
        user_id : str
            User ID.
        length : float
            Token length in characters. The default length is 6 characters
        expire : float
            Token expiration period in seconds. The default expiration is 15 minutes.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/tokens'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['length'] = length
        api_params['expire'] = expire

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email_verification(self, user_id: str, email_verification: bool) -> Dict[str, Any]:
        """
        Update the user email verification status by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        email_verification : bool
            User email verification status.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/verification'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email_verification is None:
            raise AppwriteException('Missing required parameter: "email_verification"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['emailVerification'] = email_verification

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_phone_verification(self, user_id: str, phone_verification: bool) -> Dict[str, Any]:
        """
        Update the user phone verification status by its unique ID.

        Parameters
        ----------
        user_id : str
            User ID.
        phone_verification : bool
            User phone verification status.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/users/{userId}/verification/phone'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if phone_verification is None:
            raise AppwriteException('Missing required parameter: "phone_verification"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['phoneVerification'] = phone_verification

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)
