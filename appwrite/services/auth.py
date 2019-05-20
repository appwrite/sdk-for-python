from appwrite.service import Service


class Auth(Service):

    def login(self, email, password, success='', failure=''):
        """Login User"""
        pass

    def logout(self):
        """Logout Current Session"""
        pass

    def logout_by_session(self, user_id):
        """Logout Specific Session"""
        pass

    def recovery(self, email, redirect):
        """Password Recovery"""
        pass

    def recovery_reset(self, user_id, token, password_a, password_b):
        """Password Reset"""
        pass

    def register(self, email, password, redirect, name='', success='', failure=''):
        """Register User"""
        pass

    def confirm(self, user_id, token):
        """Confirm User"""
        pass

    def confirm_resend(self, redirect):
        """Resend Confirmation"""
        pass

    def oauth_callback(self, project_id, provider, code, state=''):
        """OAuth Callback"""
        pass

    def oauth(self, provider, success='', failure=''):
        """OAuth Login"""
        pass
