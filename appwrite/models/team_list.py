from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .team import Team

T = TypeVar('T')

class TeamList(AppwriteModel, Generic[T]):
    """
    Teams List

    Attributes
    ----------
    total : float
        Total number of teams that matched your query.
    teams : List[Team[T]]
        List of teams.
    """
    total: float = Field(..., alias='total')
    teams: List[Team[T]] = Field(..., alias='teams')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'TeamList[T]':
        """Create TeamList instance with typed data."""
        instance = cls.model_validate(data)
        if 'teams' in data and data['teams'] is not None:
            instance.teams = [
                Team.with_data(row, model_type) 
                for row in data['teams']
            ]
        return instance
