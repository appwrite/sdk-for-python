from ..service import Service
from typing import List, Dict, Any, Optional
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.browser import Browser;
from ..enums.credit_card import CreditCard;
from ..enums.flag import Flag;
from ..enums.theme import Theme;
from ..enums.timezone import Timezone;
from ..enums.output import Output;

class Avatars(Service):

    def __init__(self, client) -> None:
        super(Avatars, self).__init__(client)

    def get_browser(self, code: Browser, width: Optional[float] = None, height: Optional[float] = None, quality: Optional[float] = None) -> bytes:
        """
        You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user [GET /account/sessions](https://appwrite.io/docs/references/cloud/client-web/account#getSessions) endpoint. Use width, height and quality arguments to change the output settings.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.

        Parameters
        ----------
        code : Browser
            Browser Code.
        width : Optional[float]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : Optional[float]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        quality : Optional[float]
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

        if width is not None:
            api_params['width'] = width
        if height is not None:
            api_params['height'] = height
        if quality is not None:
            api_params['quality'] = quality

        return self.client.call('get', api_path, {
        }, api_params)

    def get_credit_card(self, code: CreditCard, width: Optional[float] = None, height: Optional[float] = None, quality: Optional[float] = None) -> bytes:
        """
        The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.
        

        Parameters
        ----------
        code : CreditCard
            Credit Card Code. Possible values: amex, argencard, cabal, cencosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, unionpay, visa, mir, maestro, rupay.
        width : Optional[float]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : Optional[float]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        quality : Optional[float]
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

        if width is not None:
            api_params['width'] = width
        if height is not None:
            api_params['height'] = height
        if quality is not None:
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

    def get_flag(self, code: Flag, width: Optional[float] = None, height: Optional[float] = None, quality: Optional[float] = None) -> bytes:
        """
        You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings. Country codes follow the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) standard.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.
        

        Parameters
        ----------
        code : Flag
            Country Code. ISO Alpha-2 country code format.
        width : Optional[float]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : Optional[float]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        quality : Optional[float]
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

        if width is not None:
            api_params['width'] = width
        if height is not None:
            api_params['height'] = height
        if quality is not None:
            api_params['quality'] = quality

        return self.client.call('get', api_path, {
        }, api_params)

    def get_image(self, url: str, width: Optional[float] = None, height: Optional[float] = None) -> bytes:
        """
        Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 400x400px.
        
        This endpoint does not follow HTTP redirects.

        Parameters
        ----------
        url : str
            Image URL which you want to crop.
        width : Optional[float]
            Resize preview image width, Pass an integer between 0 to 2000. Defaults to 400.
        height : Optional[float]
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
        if width is not None:
            api_params['width'] = width
        if height is not None:
            api_params['height'] = height

        return self.client.call('get', api_path, {
        }, api_params)

    def get_initials(self, name: Optional[str] = None, width: Optional[float] = None, height: Optional[float] = None, background: Optional[str] = None) -> bytes:
        """
        Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the 'name' parameter. If no name is given and no user is logged, an empty avatar will be returned.
        
        You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user's initials when reloading the same theme will always return for the same initials.
        
        When one dimension is specified and the other is 0, the image is scaled with preserved aspect ratio. If both dimensions are 0, the API provides an image at source quality. If dimensions are not specified, the default size of image returned is 100x100px.
        

        Parameters
        ----------
        name : Optional[str]
            Full Name. When empty, current user name or email will be used. Max length: 128 chars.
        width : Optional[float]
            Image width. Pass an integer between 0 to 2000. Defaults to 100.
        height : Optional[float]
            Image height. Pass an integer between 0 to 2000. Defaults to 100.
        background : Optional[str]
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

        if name is not None:
            api_params['name'] = name
        if width is not None:
            api_params['width'] = width
        if height is not None:
            api_params['height'] = height
        if background is not None:
            api_params['background'] = background

        return self.client.call('get', api_path, {
        }, api_params)

    def get_qr(self, text: str, size: Optional[float] = None, margin: Optional[float] = None, download: Optional[bool] = None) -> bytes:
        """
        Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.
        

        Parameters
        ----------
        text : str
            Plain text to be converted to QR code image.
        size : Optional[float]
            QR code size. Pass an integer between 1 to 1000. Defaults to 400.
        margin : Optional[float]
            Margin from edge. Pass an integer between 0 to 10. Defaults to 1.
        download : Optional[bool]
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
        if size is not None:
            api_params['size'] = size
        if margin is not None:
            api_params['margin'] = margin
        if download is not None:
            api_params['download'] = download

        return self.client.call('get', api_path, {
        }, api_params)

    def get_screenshot(self, url: str, headers: Optional[dict] = None, viewport_width: Optional[float] = None, viewport_height: Optional[float] = None, scale: Optional[float] = None, theme: Optional[Theme] = None, user_agent: Optional[str] = None, fullpage: Optional[bool] = None, locale: Optional[str] = None, timezone: Optional[Timezone] = None, latitude: Optional[float] = None, longitude: Optional[float] = None, accuracy: Optional[float] = None, touch: Optional[bool] = None, permissions: Optional[List[str]] = None, sleep: Optional[float] = None, width: Optional[float] = None, height: Optional[float] = None, quality: Optional[float] = None, output: Optional[Output] = None) -> bytes:
        """
        Use this endpoint to capture a screenshot of any website URL. This endpoint uses a headless browser to render the webpage and capture it as an image.
        
        You can configure the browser viewport size, theme, user agent, geolocation, permissions, and more. Capture either just the viewport or the full page scroll.
        
        When width and height are specified, the image is resized accordingly. If both dimensions are 0, the API provides an image at original size. If dimensions are not specified, the default viewport size is 1280x720px.

        Parameters
        ----------
        url : str
            Website URL which you want to capture.
        headers : Optional[dict]
            HTTP headers to send with the browser request. Defaults to empty.
        viewport_width : Optional[float]
            Browser viewport width. Pass an integer between 1 to 1920. Defaults to 1280.
        viewport_height : Optional[float]
            Browser viewport height. Pass an integer between 1 to 1080. Defaults to 720.
        scale : Optional[float]
            Browser scale factor. Pass a number between 0.1 to 3. Defaults to 1.
        theme : Optional[Theme]
            Browser theme. Pass "light" or "dark". Defaults to "light".
        user_agent : Optional[str]
            Custom user agent string. Defaults to browser default.
        fullpage : Optional[bool]
            Capture full page scroll. Pass 0 for viewport only, or 1 for full page. Defaults to 0.
        locale : Optional[str]
            Browser locale (e.g., "en-US", "fr-FR"). Defaults to browser default.
        timezone : Optional[Timezone]
            IANA timezone identifier (e.g., "America/New_York", "Europe/London"). Defaults to browser default.
        latitude : Optional[float]
            Geolocation latitude. Pass a number between -90 to 90. Defaults to 0.
        longitude : Optional[float]
            Geolocation longitude. Pass a number between -180 to 180. Defaults to 0.
        accuracy : Optional[float]
            Geolocation accuracy in meters. Pass a number between 0 to 100000. Defaults to 0.
        touch : Optional[bool]
            Enable touch support. Pass 0 for no touch, or 1 for touch enabled. Defaults to 0.
        permissions : Optional[List[str]]
            Browser permissions to grant. Pass an array of permission names like ["geolocation", "camera", "microphone"]. Defaults to empty.
        sleep : Optional[float]
            Wait time in seconds before taking the screenshot. Pass an integer between 0 to 10. Defaults to 0.
        width : Optional[float]
            Output image width. Pass 0 to use original width, or an integer between 1 to 2000. Defaults to 0 (original width).
        height : Optional[float]
            Output image height. Pass 0 to use original height, or an integer between 1 to 2000. Defaults to 0 (original height).
        quality : Optional[float]
            Screenshot quality. Pass an integer between 0 to 100. Defaults to keep existing image quality.
        output : Optional[Output]
            Output format type (jpeg, jpg, png, gif and webp).
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/avatars/screenshots'
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')


        api_params['url'] = url
        if headers is not None:
            api_params['headers'] = headers
        if viewport_width is not None:
            api_params['viewportWidth'] = viewport_width
        if viewport_height is not None:
            api_params['viewportHeight'] = viewport_height
        if scale is not None:
            api_params['scale'] = scale
        if theme is not None:
            api_params['theme'] = theme
        if user_agent is not None:
            api_params['userAgent'] = user_agent
        if fullpage is not None:
            api_params['fullpage'] = fullpage
        if locale is not None:
            api_params['locale'] = locale
        if timezone is not None:
            api_params['timezone'] = timezone
        if latitude is not None:
            api_params['latitude'] = latitude
        if longitude is not None:
            api_params['longitude'] = longitude
        if accuracy is not None:
            api_params['accuracy'] = accuracy
        if touch is not None:
            api_params['touch'] = touch
        if permissions is not None:
            api_params['permissions'] = permissions
        if sleep is not None:
            api_params['sleep'] = sleep
        if width is not None:
            api_params['width'] = width
        if height is not None:
            api_params['height'] = height
        if quality is not None:
            api_params['quality'] = quality
        if output is not None:
            api_params['output'] = output

        return self.client.call('get', api_path, {
        }, api_params)
