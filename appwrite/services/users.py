from ..service import Service
from ..exception import AppwriteException

class Users(Service):

    def __init__(self, client):
        super(Users, self).__init__(client)

    def list(self, queries = None, search = None):
        """List Users"""

        
        path = '/users'
        params = {}

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create(self, user_id, email = None, phone = None, password = None, name = None):
        """Create User"""

        
        path = '/users'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')


        params['userId'] = user_id
        params['email'] = email
        params['phone'] = phone
        params['password'] = password
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_argon2_user(self, user_id, email, password, name = None):
        """Create User with Argon2 Password"""

        
        path = '/users/argon2'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['userId'] = user_id
        params['email'] = email
        params['password'] = password
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_bcrypt_user(self, user_id, email, password, name = None):
        """Create User with Bcrypt Password"""

        
        path = '/users/bcrypt'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['userId'] = user_id
        params['email'] = email
        params['password'] = password
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_md5_user(self, user_id, email, password, name = None):
        """Create User with MD5 Password"""

        
        path = '/users/md5'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['userId'] = user_id
        params['email'] = email
        params['password'] = password
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_ph_pass_user(self, user_id, email, password, name = None):
        """Create User with PHPass Password"""

        
        path = '/users/phpass'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['userId'] = user_id
        params['email'] = email
        params['password'] = password
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_scrypt_user(self, user_id, email, password, password_salt, password_cpu, password_memory, password_parallel, password_length, name = None):
        """Create User with Scrypt Password"""

        
        path = '/users/scrypt'
        params = {}
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


        params['userId'] = user_id
        params['email'] = email
        params['password'] = password
        params['passwordSalt'] = password_salt
        params['passwordCpu'] = password_cpu
        params['passwordMemory'] = password_memory
        params['passwordParallel'] = password_parallel
        params['passwordLength'] = password_length
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_scrypt_modified_user(self, user_id, email, password, password_salt, password_salt_separator, password_signer_key, name = None):
        """Create User with Scrypt Modified Password"""

        
        path = '/users/scrypt-modified'
        params = {}
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


        params['userId'] = user_id
        params['email'] = email
        params['password'] = password
        params['passwordSalt'] = password_salt
        params['passwordSaltSeparator'] = password_salt_separator
        params['passwordSignerKey'] = password_signer_key
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def create_sha_user(self, user_id, email, password, password_version = None, name = None):
        """Create User with SHA Password"""

        
        path = '/users/sha'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['userId'] = user_id
        params['email'] = email
        params['password'] = password
        params['passwordVersion'] = password_version
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get(self, user_id):
        """Get User"""

        
        path = '/users/{userId}'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        path = path.replace('{userId}', user_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete(self, user_id):
        """Delete User"""

        
        path = '/users/{userId}'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        path = path.replace('{userId}', user_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def update_email(self, user_id, email):
        """Update Email"""

        
        path = '/users/{userId}/email'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        path = path.replace('{userId}', user_id)

        params['email'] = email

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def list_logs(self, user_id, queries = None):
        """List User Logs"""

        
        path = '/users/{userId}/logs'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        path = path.replace('{userId}', user_id)

        params['queries'] = queries

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def list_memberships(self, user_id):
        """List User Memberships"""

        
        path = '/users/{userId}/memberships'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        path = path.replace('{userId}', user_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_name(self, user_id, name):
        """Update Name"""

        
        path = '/users/{userId}/name'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        path = path.replace('{userId}', user_id)

        params['name'] = name

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def update_password(self, user_id, password):
        """Update Password"""

        
        path = '/users/{userId}/password'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        path = path.replace('{userId}', user_id)

        params['password'] = password

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def update_phone(self, user_id, number):
        """Update Phone"""

        
        path = '/users/{userId}/phone'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if number is None:
            raise AppwriteException('Missing required parameter: "number"')

        path = path.replace('{userId}', user_id)

        params['number'] = number

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def get_prefs(self, user_id):
        """Get User Preferences"""

        
        path = '/users/{userId}/prefs'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        path = path.replace('{userId}', user_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_prefs(self, user_id, prefs):
        """Update User Preferences"""

        
        path = '/users/{userId}/prefs'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')

        path = path.replace('{userId}', user_id)

        params['prefs'] = prefs

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def list_sessions(self, user_id):
        """List User Sessions"""

        
        path = '/users/{userId}/sessions'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        path = path.replace('{userId}', user_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_sessions(self, user_id):
        """Delete User Sessions"""

        
        path = '/users/{userId}/sessions'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        path = path.replace('{userId}', user_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def delete_session(self, user_id, session_id):
        """Delete User Session"""

        
        path = '/users/{userId}/sessions/{sessionId}'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        path = path.replace('{userId}', user_id)
        path = path.replace('{sessionId}', session_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def update_status(self, user_id, status):
        """Update User Status"""

        
        path = '/users/{userId}/status'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if status is None:
            raise AppwriteException('Missing required parameter: "status"')

        path = path.replace('{userId}', user_id)

        params['status'] = status

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def update_email_verification(self, user_id, email_verification):
        """Update Email Verification"""

        
        path = '/users/{userId}/verification'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email_verification is None:
            raise AppwriteException('Missing required parameter: "email_verification"')

        path = path.replace('{userId}', user_id)

        params['emailVerification'] = email_verification

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def update_phone_verification(self, user_id, phone_verification):
        """Update Phone Verification"""

        
        path = '/users/{userId}/verification/phone'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if phone_verification is None:
            raise AppwriteException('Missing required parameter: "phone_verification"')

        path = path.replace('{userId}', user_id)

        params['phoneVerification'] = phone_verification

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)
