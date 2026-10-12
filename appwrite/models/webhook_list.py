from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .webhook import Webhook


class WebhookList(AppwriteModel):
    """
    Webhooks List

    Attributes
    ----------
    total : float
        Total number of webhooks that matched your query.
    webhooks : List[Webhook]
        List of webhooks.
    """

    total: float = Field(..., alias='total')
    webhooks: List[Webhook] = Field(..., alias='webhooks')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
