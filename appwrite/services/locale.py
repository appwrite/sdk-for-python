from ..service import Service
from ..exception import AppwriteException

class Locale(Service):

    def __init__(self, client):
        super(Locale, self).__init__(client)

    def get(self):

        api_path = '/locale'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_codes(self):

        api_path = '/locale/codes'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_continents(self):

        api_path = '/locale/continents'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_countries(self):

        api_path = '/locale/countries'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_countries_eu(self):

        api_path = '/locale/countries/eu'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_countries_phones(self):

        api_path = '/locale/countries/phones'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_currencies(self):

        api_path = '/locale/currencies'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_languages(self):

        api_path = '/locale/languages'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)
