from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'prices' not in data:
            data['prices'] = []
        return data
