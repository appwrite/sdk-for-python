from ..service import Service
from typing import List
from ..exception import AppwriteException
from ..enums.browser import Browser;
from ..enums.credit_card import CreditCard;
from ..enums.flag import Flag;

class Avatars(Service):

    def __init__(self, client):
        super(Avatars, self).__init__(client)

    def get_browser(self, code: Browser, width: float = None, height: float = None, quality: float = None):
        """Get browser icon"""

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

    def get_credit_card(self, code: CreditCard, width: float = None, height: float = None, quality: float = None):
        """Get credit card icon"""

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

    def get_favicon(self, url: str):
        """Get favicon"""

        api_path = '/avatars/favicon'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_flag(self, code: Flag, width: float = None, height: float = None, quality: float = None):
        """Get country flag"""

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

    def get_image(self, url: str, width: float = None, height: float = None):
        """Get image from URL"""

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

    def get_initials(self, name: str = None, width: float = None, height: float = None, background: str = None):
        """Get user initials"""

        api_path = '/avatars/initials'
        api_params = {}

        api_params['name'] = name
        api_params['width'] = width
        api_params['height'] = height
        api_params['background'] = background

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_qr(self, text: str, size: float = None, margin: float = None, download: bool = None):
        """Get QR code"""

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
