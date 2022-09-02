from ..service import Service
from ..exception import AppwriteException

class Locale(Service):

    def __init__(self, client):
        super(Locale, self).__init__(client)

    def get(self):
        """Get User Locale"""

        
        path = '/locale'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_continents(self):
        """List Continents"""

        
        path = '/locale/continents'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_countries(self):
        """List Countries"""

        
        path = '/locale/countries'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_countries_eu(self):
        """List EU Countries"""

        
        path = '/locale/countries/eu'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_countries_phones(self):
        """List Countries Phone Codes"""

        
        path = '/locale/countries/phones'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_currencies(self):
        """List Currencies"""

        
        path = '/locale/currencies'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_languages(self):
        """List Languages"""

        
        path = '/locale/languages'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
