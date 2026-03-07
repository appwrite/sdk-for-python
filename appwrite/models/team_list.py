from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .team import Team

class TeamList(AppwriteModel):
    """
    Teams List

    Attributes
    ----------
    total : float
        Total number of teams that matched your query.
    teams : List[Team]
        List of teams.
    """
    total: float = Field(..., alias='total')
    teams: List[Team] = Field(..., alias='teams')
