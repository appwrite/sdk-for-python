from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
