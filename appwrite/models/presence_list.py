from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .presence import Presence

class PresenceList(AppwriteModel):
    """
    Presences List

    Attributes
    ----------
    total : float
        Total number of presences that matched your query.
    presences : List[Presence]
        List of presences.
    """
    total: float = Field(..., alias='total')
    presences: List[Presence] = Field(..., alias='presences')
