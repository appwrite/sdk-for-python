from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .activity_event import ActivityEvent

class ActivityEventList(AppwriteModel):
    """
    Activity event list

    Attributes
    ----------
    total : float
        Total number of events that matched your query.
    events : List[ActivityEvent]
        List of events.
    """
    total: float = Field(..., alias='total')
    events: List[ActivityEvent] = Field(..., alias='events')
