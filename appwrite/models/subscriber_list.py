from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
