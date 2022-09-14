from ..service import Service
from ..exception import AppwriteException

class Account(Service):

    def __init__(self, client):
        super(Account, self).__init__(client)

    def get(self):
        """Get Account"""

        
        path = '/account'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_email(self, email, password):
        """Update Account Email"""

        
        path = '/account/email'
        params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['email'] = email
        params['password'] = password

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def list_logs(self, queries = None):
        """List Account Logs"""

        
        path = '/account/logs'
        params = {}

        params['queries'] = queries

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_name(self, name):
        """Update Account Name"""

        
        path = '/account/name'
        params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        params['name'] = name

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def update_password(self, password, old_password = None):
        """Update Account Password"""

        
        path = '/account/password'
        params = {}
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['password'] = password
        params['oldPassword'] = old_password

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def update_phone(self, phone, password):
        """Update Account Phone"""

        
        path = '/account/phone'
        params = {}
        if phone is None:
            raise AppwriteException('Missing required parameter: "phone"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')


        params['phone'] = phone
        params['password'] = password

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def get_prefs(self):
        """Get Account Preferences"""

        
        path = '/account/prefs'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_prefs(self, prefs):
        """Update Account Preferences"""

        
        path = '/account/prefs'
        params = {}
        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')


        params['prefs'] = prefs

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def create_recovery(self, email, url):
        """Create Password Recovery"""

        
        path = '/account/recovery'
        params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        params['email'] = email
        params['url'] = url

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def update_recovery(self, user_id, secret, password, password_again):
        """Create Password Recovery (confirmation)"""

        
        path = '/account/recovery'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        if password_again is None:
            raise AppwriteException('Missing required parameter: "password_again"')


        params['userId'] = user_id
        params['secret'] = secret
        params['password'] = password
        params['passwordAgain'] = password_again

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def list_sessions(self):
        """List Account Sessions"""

        
        path = '/account/sessions'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def delete_sessions(self):
        """Delete All Account Sessions"""

        
        path = '/account/sessions'
        params = {}

        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def get_session(self, session_id):
        """Get Session By ID"""

        
        path = '/account/sessions/{sessionId}'
        params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        path = path.replace('{sessionId}', session_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_session(self, session_id):
        """Update Session (Refresh Tokens)"""

        
        path = '/account/sessions/{sessionId}'
        params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        path = path.replace('{sessionId}', session_id)


        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def delete_session(self, session_id):
        """Delete Account Session"""

        
        path = '/account/sessions/{sessionId}'
        params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        path = path.replace('{sessionId}', session_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def update_status(self):
        """Update Account Status"""

        
        path = '/account/status'
        params = {}

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def create_verification(self, url):
        """Create Email Verification"""

        
        path = '/account/verification'
        params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        params['url'] = url

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def update_verification(self, user_id, secret):
        """Create Email Verification (confirmation)"""

        
        path = '/account/verification'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')


        params['userId'] = user_id
        params['secret'] = secret

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def create_phone_verification(self):
        """Create Phone Verification"""

        
        path = '/account/verification/phone'
        params = {}

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def update_phone_verification(self, user_id, secret):
        """Create Phone Verification (confirmation)"""

        
        path = '/account/verification/phone'
        params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')


        params['userId'] = user_id
        params['secret'] = secret

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)
