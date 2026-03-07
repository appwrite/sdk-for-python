from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.locale import Locale as LocaleModel;
from ..models.locale_code_list import LocaleCodeList;
from ..models.continent_list import ContinentList;
from ..models.country_list import CountryList;
from ..models.phone_list import PhoneList;
from ..models.currency_list import CurrencyList;
from ..models.language_list import LanguageList;

class Locale(Service):

    def __init__(self, client) -> None:
        super(Locale, self).__init__(client)

    def get(
        self
    ) -> LocaleModel:
        """
        Get the current user location based on IP. Returns an object with user country code, country name, continent name, continent code, ip address and suggested currency. You can use the locale header to get the data in a supported language.
        
        ([IP Geolocation by DB-IP](https://db-ip.com))

        Returns
        -------
        LocaleModel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LocaleModel)


    def list_codes(
        self
    ) -> LocaleCodeList:
        """
        List of all locale codes in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

        Returns
        -------
        LocaleCodeList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/codes'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LocaleCodeList)


    def list_continents(
        self
    ) -> ContinentList:
        """
        List of all continents. You can use the locale header to get the data in a supported language.

        Returns
        -------
        ContinentList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/continents'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ContinentList)


    def list_countries(
        self
    ) -> CountryList:
        """
        List of all countries. You can use the locale header to get the data in a supported language.

        Returns
        -------
        CountryList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/countries'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=CountryList)


    def list_countries_eu(
        self
    ) -> CountryList:
        """
        List of all countries that are currently members of the EU. You can use the locale header to get the data in a supported language.

        Returns
        -------
        CountryList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/countries/eu'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=CountryList)


    def list_countries_phones(
        self
    ) -> PhoneList:
        """
        List of all countries phone codes. You can use the locale header to get the data in a supported language.

        Returns
        -------
        PhoneList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/countries/phones'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PhoneList)


    def list_currencies(
        self
    ) -> CurrencyList:
        """
        List of all currencies, including currency symbol, name, plural, and decimal digits for all major and minor currencies. You can use the locale header to get the data in a supported language.

        Returns
        -------
        CurrencyList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/currencies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=CurrencyList)


    def list_languages(
        self
    ) -> LanguageList:
        """
        List of all languages classified by ISO 639-1 including 2-letter code, name in English, and name in the respective language.

        Returns
        -------
        LanguageList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/locale/languages'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LanguageList)

