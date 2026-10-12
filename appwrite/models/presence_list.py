from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
