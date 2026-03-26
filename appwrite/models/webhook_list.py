from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
