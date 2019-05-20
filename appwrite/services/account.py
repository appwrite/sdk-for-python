from appwrite.service import Service


class Account(Service):

    def get(self):
        """Get Account"""
        pass

    def delete(self):
        """Delete Account"""
        pass

    def update_email(self, email, password):
        """Update Account Email"""
        pass

    def update_name(self, name):
        """Update Account Name"""
        pass

    def update_password(self, password, old_password):
        """Update Account Password"""
        pass

    def get_prefs(self):
        """Get Account Preferences"""
        pass

    def update_prefs(self, prefs):
        """Update Account Prefs"""
        pass

    def get_security(self):
        """Get Account Security Log"""
        pass

    def get_sessions(self):
        """Get Account Active Sessions"""
        pass
