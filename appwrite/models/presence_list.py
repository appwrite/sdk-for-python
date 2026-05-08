from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .presence import Presence

T = TypeVar('T')

class PresenceList(AppwriteModel, Generic[T]):
    """
    Presences List

    Attributes
    ----------
    total : float
        Total number of presences that matched your query.
    presences : List[Presence[T]]
        List of presences.
    """
    total: float = Field(..., alias='total')
    presences: List[Presence[T]] = Field(..., alias='presences')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'PresenceList[T]':
        """Create PresenceList instance with typed data."""
        instance = cls.model_validate(data)
        if 'presences' in data and data['presences'] is not None:
            instance.presences = [
                Presence.with_data(row, model_type) 
                for row in data['presences']
            ]
        return instance
