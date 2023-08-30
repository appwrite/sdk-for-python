from ..service import Service
from ..exception import AppwriteException

class Locale(Service):

    def __init__(self, client):
        super(Locale, self).__init__(client)

    def get(self):
        """Get User Locale"""

        
        api_path = '/locale'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_codes(self):
        """List Locale Codes"""

        
        api_path = '/locale/codes'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_continents(self):
        """List Continents"""

        
        api_path = '/locale/continents'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_countries(self):
        """List Countries"""

        
        api_path = '/locale/countries'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_countries_eu(self):
        """List EU Countries"""

        
        api_path = '/locale/countries/eu'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_countries_phones(self):
        """List Countries Phone Codes"""

        
        api_path = '/locale/countries/phones'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_currencies(self):
        """List Currencies"""

        
        api_path = '/locale/currencies'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def list_languages(self):
        """List Languages"""

        
        api_path = '/locale/languages'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)
