from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
