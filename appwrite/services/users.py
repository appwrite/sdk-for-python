from ..service import Service
from ..exception import AppwriteException

class Users(Service):

    def __init__(self, client):
        super(Users, self).__init__(client)

    def list(self, queries = None, search = None):
        """List users"""

        
        api_path = '/users'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create(self, user_id, email = None, phone = None, password = None, name = None):
        """Create user"""

        
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

    def create_argon2_user(self, user_id, email, password, name = None):
        """Create user with Argon2 password"""

        
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

    def create_bcrypt_user(self, user_id, email, password, name = None):
        """Create user with bcrypt password"""

        
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

    def list_identities(self, queries = None, search = None):
        """List identities"""

        
        api_path = '/users/identities'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_identity(self, identity_id):
        """Delete identity"""

        
        api_path = '/users/identities/{identityId}'
        api_params = {}
        if identity_id is None:
            raise AppwriteException('Missing required parameter: "identity_id"')

        api_path = api_path.replace('{identityId}', identity_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_md5_user(self, user_id, email, password, name = None):
        """Create user with MD5 password"""

        
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

    def create_ph_pass_user(self, user_id, email, password, name = None):
        """Create user with PHPass password"""

        
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

    def create_scrypt_user(self, user_id, email, password, password_salt, password_cpu, password_memory, password_parallel, password_length, name = None):
        """Create user with Scrypt password"""

        
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

    def create_scrypt_modified_user(self, user_id, email, password, password_salt, password_salt_separator, password_signer_key, name = None):
        """Create user with Scrypt modified password"""

        
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

    def create_sha_user(self, user_id, email, password, password_version = None, name = None):
        """Create user with SHA password"""

        
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

    def get(self, user_id):
        """Get user"""

        
        api_path = '/users/{userId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, user_id):
        """Delete user"""

        
        api_path = '/users/{userId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email(self, user_id, email):
        """Update email"""

        
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

    def create_jwt(self, user_id, session_id = None, duration = None):
        """Create user JWT"""

        
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

    def update_labels(self, user_id, labels):
        """Update user labels"""

        
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

    def list_logs(self, user_id, queries = None):
        """List user logs"""

        
        api_path = '/users/{userId}/logs'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_memberships(self, user_id):
        """List user memberships"""

        
        api_path = '/users/{userId}/memberships'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_mfa(self, user_id, mfa):
        """Update MFA"""

        
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

    def delete_mfa_authenticator(self, user_id, type):
        """Delete authenticator"""

        
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

    def list_mfa_factors(self, user_id):
        """List factors"""

        
        api_path = '/users/{userId}/mfa/factors'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_mfa_recovery_codes(self, user_id):
        """Get MFA recovery codes"""

        
        api_path = '/users/{userId}/mfa/recovery-codes'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_mfa_recovery_codes(self, user_id):
        """Regenerate MFA recovery codes"""

        
        api_path = '/users/{userId}/mfa/recovery-codes'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_mfa_recovery_codes(self, user_id):
        """Create MFA recovery codes"""

        
        api_path = '/users/{userId}/mfa/recovery-codes'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_name(self, user_id, name):
        """Update name"""

        
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

    def update_password(self, user_id, password):
        """Update password"""

        
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

    def update_phone(self, user_id, number):
        """Update phone"""

        
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

    def get_prefs(self, user_id):
        """Get user preferences"""

        
        api_path = '/users/{userId}/prefs'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_prefs(self, user_id, prefs):
        """Update user preferences"""

        
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

    def list_sessions(self, user_id):
        """List user sessions"""

        
        api_path = '/users/{userId}/sessions'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_session(self, user_id):
        """Create session"""

        
        api_path = '/users/{userId}/sessions'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_sessions(self, user_id):
        """Delete user sessions"""

        
        api_path = '/users/{userId}/sessions'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_session(self, user_id, session_id):
        """Delete user session"""

        
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

    def update_status(self, user_id, status):
        """Update user status"""

        
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

    def list_targets(self, user_id, queries = None):
        """List user targets"""

        
        api_path = '/users/{userId}/targets'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        api_path = api_path.replace('{userId}', user_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_target(self, user_id, target_id, provider_type, identifier, provider_id = None, name = None):
        """Create user target"""

        
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

    def get_target(self, user_id, target_id):
        """Get user target"""

        
        api_path = '/users/{userId}/targets/{targetId}'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if target_id is None:
            raise AppwriteException('Missing required parameter: "target_id"')

        api_path = api_path.replace('{userId}', user_id)
        api_path = api_path.replace('{targetId}', target_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_target(self, user_id, target_id, identifier = None, provider_id = None, name = None):
        """Update user target"""

        
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

    def delete_target(self, user_id, target_id):
        """Delete user target"""

        
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

    def create_token(self, user_id, length = None, expire = None):
        """Create token"""

        
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

    def update_email_verification(self, user_id, email_verification):
        """Update email verification"""

        
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

    def update_phone_verification(self, user_id, phone_verification):
        """Update phone verification"""

        
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
