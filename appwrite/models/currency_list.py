from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .currency import Currency


class CurrencyList(AppwriteModel):
    """
    Currencies List

    Attributes
    ----------
    total : float
        Total number of currencies that matched your query.
    currencies : List[Currency]
        List of currencies.
    """

    total: float = Field(..., alias='total')
    currencies: List[Currency] = Field(..., alias='currencies')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
