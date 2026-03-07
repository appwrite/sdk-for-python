from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .preferences import Preferences

class Team(AppwriteModel):
    """
    Team

    Attributes
    ----------
    id : str
        Team ID.
    createdat : str
        Team creation date in ISO 8601 format.
    updatedat : str
        Team update date in ISO 8601 format.
    name : str
        Team name.
    total : float
        Total number of team members.
    prefs : Preferences
        Team preferences as a key-value object
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    total: float = Field(..., alias='total')
    prefs: Preferences = Field(..., alias='prefs')
