from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Locale(AppwriteModel):
    """
    Locale

    Attributes
    ----------
    ip : str
        User IP address.
    countrycode : str
        Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format
    country : str
        Country name. This field support localization.
    continentcode : str
        Continent code. A two character continent code &quot;AF&quot; for Africa, &quot;AN&quot; for Antarctica, &quot;AS&quot; for Asia, &quot;EU&quot; for Europe, &quot;NA&quot; for North America, &quot;OC&quot; for Oceania, and &quot;SA&quot; for South America.
    continent : str
        Continent name. This field support localization.
    eu : bool
        True if country is part of the European Union.
    currency : str
        Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format
    """
    ip: str = Field(..., alias='ip')
    countrycode: str = Field(..., alias='countryCode')
    country: str = Field(..., alias='country')
    continentcode: str = Field(..., alias='continentCode')
    continent: str = Field(..., alias='continent')
    eu: bool = Field(..., alias='eu')
    currency: str = Field(..., alias='currency')
