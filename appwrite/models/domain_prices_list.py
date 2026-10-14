from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .domain_price import DomainPrice


class DomainPricesList(AppwriteModel):
    """
    Domain prices list

    Attributes
    ----------
    total : float
        Total number of prices that matched your query.
    prices : List[DomainPrice]
        List of prices.
    """

    total: float = Field(..., alias='total')
    prices: List[DomainPrice] = Field(..., alias='prices')
