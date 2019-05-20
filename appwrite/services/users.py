from appwrite.service import Service


class Users(Service):

    def list_users(self, search='', limit=25, offset=0, order_type='ASC'):
        """List Users"""
        pass

    def create_user(self, email, password, name=''):
        """Create User"""
        pass

    def get_user(self, user_id):
        """Get User"""
        pass

    def get_user_logs(self, user_id):
        """Get User Logs"""
        pass

    def get_user_prefs(self, user_id):
        """Get User Prefs"""
        pass

    def get_user_sessions(self, user_id):
        """Get User Sessions"""
        pass

    def delete_user_sessions(self, user_id):
        """Delete User Sessions"""
        pass

    def delete_users_session(self, user_id, session_id):
        """Delete User Session"""
        pass

    def update_user_status(self, user_id, status):
        """Block User"""
        pass
