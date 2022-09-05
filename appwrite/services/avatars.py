from ..service import Service
from ..exception import AppwriteException

class Avatars(Service):

    def __init__(self, client):
        super(Avatars, self).__init__(client)

    def get_browser(self, code, width = None, height = None, quality = None):
        """Get Browser Icon"""

        
        path = '/avatars/browsers/{code}'
        params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        path = path.replace('{code}', code)

        params['width'] = width
        params['height'] = height
        params['quality'] = quality

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_credit_card(self, code, width = None, height = None, quality = None):
        """Get Credit Card Icon"""

        
        path = '/avatars/credit-cards/{code}'
        params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        path = path.replace('{code}', code)

        params['width'] = width
        params['height'] = height
        params['quality'] = quality

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_favicon(self, url):
        """Get Favicon"""

        
        path = '/avatars/favicon'
        params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        params['url'] = url

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_flag(self, code, width = None, height = None, quality = None):
        """Get Country Flag"""

        
        path = '/avatars/flags/{code}'
        params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        path = path.replace('{code}', code)

        params['width'] = width
        params['height'] = height
        params['quality'] = quality

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_image(self, url, width = None, height = None):
        """Get Image from URL"""

        
        path = '/avatars/image'
        params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        params['url'] = url
        params['width'] = width
        params['height'] = height

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_initials(self, name = None, width = None, height = None, background = None):
        """Get User Initials"""

        
        path = '/avatars/initials'
        params = {}

        params['name'] = name
        params['width'] = width
        params['height'] = height
        params['background'] = background

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_qr(self, text, size = None, margin = None, download = None):
        """Get QR Code"""

        
        path = '/avatars/qr'
        params = {}
        if text is None:
            raise AppwriteException('Missing required parameter: "text"')


        params['text'] = text
        params['size'] = size
        params['margin'] = margin
        params['download'] = download

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
