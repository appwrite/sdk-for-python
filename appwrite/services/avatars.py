from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException
from ..enums.browser import Browser;
from ..enums.credit_card import CreditCard;
from ..enums.flag import Flag;

class Avatars(Service):

    def __init__(self, client) -> None:
        super(Avatars, self).__init__(client)

    def get_browser(self, code: Browser, width: float = None, height: float = None, quality: float = None) -> bytes:
        """
        You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user [GET /account/sessions](https://appwrite.io/docs/references/cloud/client-web/account#getSessions) endpoint. Use width, height and quality arguments to change the output settings.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.

        Parameters
        ----------
        code : Browser
            Browser Code.
        width : float
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : float
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        quality : float
            Image quality. Pass an integer between 0 to 100. Defaults to keep existing image quality.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/browsers/{code}'
        api_params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        api_path = api_path.replace('{code}', code)

        api_params['width'] = width
        api_params['height'] = height
        api_params['quality'] = quality

        return self.client.call('get', api_path, {
        }, api_params)

    def get_credit_card(self, code: CreditCard, width: float = None, height: float = None, quality: float = None) -> bytes:
        """
        The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.
        

        Parameters
        ----------
        code : CreditCard
            Credit Card Code. Possible values: amex, argencard, cabal, cencosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro, rupay.
        width : float
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : float
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        quality : float
            Image quality. Pass an integer between 0 to 100. Defaults to keep existing image quality.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/credit-cards/{code}'
        api_params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        api_path = api_path.replace('{code}', code)

        api_params['width'] = width
        api_params['height'] = height
        api_params['quality'] = quality

        return self.client.call('get', api_path, {
        }, api_params)

    def get_favicon(self, url: str) -> bytes:
        """
        Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL.
        
        This endpoint does not follow HTTP redirects.

        Parameters
        ----------
        url : str
            Website URL which you want to fetch the favicon from.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/favicon'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url

        return self.client.call('get', api_path, {
        }, api_params)

    def get_flag(self, code: Flag, width: float = None, height: float = None, quality: float = None) -> bytes:
        """
        You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings. Country codes follow the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) standard.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.
        

        Parameters
        ----------
        code : Flag
            Country Code. ISO Alpha-2 country code format.
        width : float
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : float
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        quality : float
            Image quality. Pass an integer between 0 to 100. Defaults to keep existing image quality.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/flags/{code}'
        api_params = {}
        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        api_path = api_path.replace('{code}', code)

        api_params['width'] = width
        api_params['height'] = height
        api_params['quality'] = quality

        return self.client.call('get', api_path, {
        }, api_params)

    def get_image(self, url: str, width: float = None, height: float = None) -> bytes:
        """
        Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 400x400px.
        
        This endpoint does not follow HTTP redirects.

        Parameters
        ----------
        url : str
            Image URL which you want to crop.
        width : float
            Resize preview image width, Pass an integer between 0 to 2000. Defaults to 400.
        height : float
            Resize preview image height, Pass an integer between 0 to 2000. Defaults to 400.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/image'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url
        api_params['width'] = width
        api_params['height'] = height

        return self.client.call('get', api_path, {
        }, api_params)

    def get_initials(self, name: str = None, width: float = None, height: float = None, background: str = None) -> bytes:
        """
        Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the 'name' parameter. If no name is given and no user is logged, an empty avatar will be returned.
        
        You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user's initials when reloading the same theme will always return for the same initials.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.
        

        Parameters
        ----------
        name : str
            Full Name. When empty, current user name or email will be used. Max length: 128 chars.
        width : float
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : float
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        background : str
            Changes background color. By default a random color will be picked and stay will persistent to the given name.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/initials'
        api_params = {}

        api_params['name'] = name
        api_params['width'] = width
        api_params['height'] = height
        api_params['background'] = background

        return self.client.call('get', api_path, {
        }, api_params)

    def get_qr(self, text: str, size: float = None, margin: float = None, download: bool = None) -> bytes:
        """
        Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.
        

        Parameters
        ----------
        text : str
            Plain text to be converted to QR code image.
        size : float
            QR code size. Pass an integer between 1 to 1000. Defaults to 400.
        margin : float
            Margin from edge. Pass an integer between 0 to 10. Defaults to 1.
        download : bool
            Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/qr'
        api_params = {}
        if text is None:
            raise AppwriteException('Missing required parameter: "text"')


        api_params['text'] = text
        api_params['size'] = size
        api_params['margin'] = margin
        api_params['download'] = download

        return self.client.call('get', api_path, {
        }, api_params)
