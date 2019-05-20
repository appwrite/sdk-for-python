from appwrite.service import Service


class Avatars(Service):

    def get_browser(self, code, width=100, height=100, quality=100):
        """Get Browser Icon"""
        pass

    def get_credit_card(self, code, width=100, height=100, quality=100):
        """Get Credit Card Icon"""
        pass

    def get_favicon(self, url):
        """Get Favicon"""
        pass

    def get_flag(self, code, width=100, height=100, quality=100):
        """Get Country Flag"""
        pass

    def get_q_r(self, text, size=400, margin=1, download=0):
        """Text to QR Generator"""
        pass
