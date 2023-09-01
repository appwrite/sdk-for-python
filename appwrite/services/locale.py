from ..service import Service
from ..exception import AppwriteException

class Locale(Service):

    def __init__(self, client):
        super(Locale, self).__init__(client)

    def get(self):
        """Get User Locale"""

        
        api_path = '/locale'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_codes(self):
        """List Locale Codes"""

        
        api_path = '/locale/codes'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_continents(self):
        """List Continents"""

        
        api_path = '/locale/continents'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_countries(self):
        """List Countries"""

        
        api_path = '/locale/countries'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_countries_eu(self):
        """List EU Countries"""

        
        api_path = '/locale/countries/eu'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_countries_phones(self):
        """List Countries Phone Codes"""

        
        api_path = '/locale/countries/phones'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_currencies(self):
        """List Currencies"""

        
        api_path = '/locale/currencies'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_languages(self):
        """List Languages"""

        
        api_path = '/locale/languages'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)
