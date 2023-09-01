from ..service import Service
from ..exception import AppwriteException

class Avatars(Service):

    def __init__(self, client):
        super(Avatars, self).__init__(client)

    def get_browser(self, code, width = None, height = None, quality = None):
        """Get Browser Icon"""

        
        api_path = '/avatars/browsers/{code}'
        api_params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        api_path = api_path.replace('{code}', code)

        api_params['width'] = width
        api_params['height'] = height
        api_params['quality'] = quality

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_credit_card(self, code, width = None, height = None, quality = None):
        """Get Credit Card Icon"""

        
        api_path = '/avatars/credit-cards/{code}'
        api_params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        api_path = api_path.replace('{code}', code)

        api_params['width'] = width
        api_params['height'] = height
        api_params['quality'] = quality

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_favicon(self, url):
        """Get Favicon"""

        
        api_path = '/avatars/favicon'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_flag(self, code, width = None, height = None, quality = None):
        """Get Country Flag"""

        
        api_path = '/avatars/flags/{code}'
        api_params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        api_path = api_path.replace('{code}', code)

        api_params['width'] = width
        api_params['height'] = height
        api_params['quality'] = quality

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_image(self, url, width = None, height = None):
        """Get Image from URL"""

        
        api_path = '/avatars/image'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url
        api_params['width'] = width
        api_params['height'] = height

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_initials(self, name = None, width = None, height = None, background = None):
        """Get User Initials"""

        
        api_path = '/avatars/initials'
        api_params = {}

        api_params['name'] = name
        api_params['width'] = width
        api_params['height'] = height
        api_params['background'] = background

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_qr(self, text, size = None, margin = None, download = None):
        """Get QR Code"""

        
        api_path = '/avatars/qr'
        api_params = {}
        if text is None:
            raise AppwriteException('Missing required parameter: "text"')


        api_params['text'] = text
        api_params['size'] = size
        api_params['margin'] = margin
        api_params['download'] = download

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)
