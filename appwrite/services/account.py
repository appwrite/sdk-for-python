from ..service import Service
from ..exception import AppwriteException

class Account(Service):

    def __init__(self, client):
        super(Account, self).__init__(client)

    def get(self):
        """Get Account"""

        
        api_path = '/account'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email(self, email, password):
        """Update Email"""

        
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

    def list_identities(self, queries = None):
        """List Identities"""

        
        api_path = '/account/identities'
        api_params = {}

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_identity(self, identity_id):
        """Delete Identity"""

        
        api_path = '/account/identities/{identityId}'
        api_params = {}
        if identity_id is None:
            raise AppwriteException('Missing required parameter: "identity_id"')

        api_path = api_path.replace('{identityId}', identity_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_logs(self, queries = None):
        """List Logs"""

        
        api_path = '/account/logs'
        api_params = {}

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_name(self, name):
        """Update Name"""

        
        api_path = '/account/name'
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['name'] = name

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_password(self, password, old_password = None):
        """Update Password"""

        
        api_path = '/account/password'
        api_params = {}
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        api_params['password'] = password
        api_params['oldPassword'] = old_password

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_phone(self, phone, password):
        """Update Phone"""

        
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

    def get_prefs(self):
        """Get Account Preferences"""

        
        api_path = '/account/prefs'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_prefs(self, prefs):
        """Update Preferences"""

        
        api_path = '/account/prefs'
        api_params = {}
        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')


        api_params['prefs'] = prefs

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_recovery(self, email, url):
        """Create Password Recovery"""

        
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

    def update_recovery(self, user_id, secret, password, password_again):
        """Create Password Recovery (confirmation)"""

        
        api_path = '/account/recovery'
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        if password_again is None:
            raise AppwriteException('Missing required parameter: "password_again"')


        api_params['userId'] = user_id
        api_params['secret'] = secret
        api_params['password'] = password
        api_params['passwordAgain'] = password_again

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_sessions(self):
        """List Sessions"""

        
        api_path = '/account/sessions'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_sessions(self):
        """Delete Sessions"""

        
        api_path = '/account/sessions'
        api_params = {}

        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_session(self, session_id):
        """Get Session"""

        
        api_path = '/account/sessions/{sessionId}'
        api_params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace('{sessionId}', session_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_session(self, session_id):
        """Update OAuth Session (Refresh Tokens)"""

        
        api_path = '/account/sessions/{sessionId}'
        api_params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace('{sessionId}', session_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_session(self, session_id):
        """Delete Session"""

        
        api_path = '/account/sessions/{sessionId}'
        api_params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace('{sessionId}', session_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_status(self):
        """Update Status"""

        
        api_path = '/account/status'
        api_params = {}

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_verification(self, url):
        """Create Email Verification"""

        
        api_path = '/account/verification'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_verification(self, user_id, secret):
        """Create Email Verification (confirmation)"""

        
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

    def create_phone_verification(self):
        """Create Phone Verification"""

        
        api_path = '/account/verification/phone'
        api_params = {}

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_phone_verification(self, user_id, secret):
        """Create Phone Verification (confirmation)"""

        
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
