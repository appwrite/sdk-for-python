from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .subscriber import Subscriber


class SubscriberList(AppwriteModel):
    """
    Subscriber list

    Attributes
    ----------
    total : float
        Total number of subscribers that matched your query.
    subscribers : List[Subscriber]
        List of subscribers.
    """

    total: float = Field(..., alias='total')
    subscribers: List[Subscriber] = Field(..., alias='subscribers')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
