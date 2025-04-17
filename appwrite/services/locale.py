from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException

class Locale(Service):

    def __init__(self, client) -> None:
        super(Locale, self).__init__(client)

    def get(self) -> Dict[str, Any]:
        """
        Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.
        
        ([IP Geolocation by DB-IP](https://db-ip.com))

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_codes(self) -> Dict[str, Any]:
        """
        List of all locale codes in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/codes'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_continents(self) -> Dict[str, Any]:
        """
        List of all continents. You can use the locale header to get the data in a supported language.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/continents'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_countries(self) -> Dict[str, Any]:
        """
        List of all countries. You can use the locale header to get the data in a supported language.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/countries'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_countries_eu(self) -> Dict[str, Any]:
        """
        List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/countries/eu'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_countries_phones(self) -> Dict[str, Any]:
        """
        List of all countries phone codes. You can use the locale header to get the data in a supported language.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/countries/phones'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_currencies(self) -> Dict[str, Any]:
        """
        List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/currencies'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_languages(self) -> Dict[str, Any]:
        """
        List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/languages'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)
