from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .preferences import Preferences

T = TypeVar('T')


class Team(AppwriteModel, Generic[T]):
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
    prefs : Preferences[T]
        Team preferences as a key-value object
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    total: float = Field(..., alias='total')
    prefs: Preferences[T] = Field(..., alias='prefs')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'total' not in data:
            data['total'] = 0
        return data

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Team[T]':
        """Create Team instance with typed data."""
        instance = cls.model_validate(data)
        if 'prefs' in data and data['prefs'] is not None:
            instance.prefs = Preferences.with_data(data['prefs'], model_type)
        return instance
