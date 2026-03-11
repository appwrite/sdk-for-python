from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .country import Country

class CountryList(AppwriteModel):
    """
    Countries List

    Attributes
    ----------
    total : float
        Total number of countries that matched your query.
    countries : List[Country]
        List of countries.
    """
    total: float = Field(..., alias='total')
    countries: List[Country] = Field(..., alias='countries')
