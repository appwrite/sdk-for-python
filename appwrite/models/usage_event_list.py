from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .usage_event import UsageEvent

class UsageEventList(AppwriteModel):
    """
    Usage events list

    Attributes
    ----------
    total : float
        Total number of events that matched your query.
    events : List[UsageEvent]
        List of events.
    """
    total: float = Field(..., alias='total')
    events: List[UsageEvent] = Field(..., alias='events')
