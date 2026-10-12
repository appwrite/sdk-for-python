from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .session import Session


class SessionList(AppwriteModel):
    """
    Sessions List

    Attributes
    ----------
    total : float
        Total number of sessions that matched your query.
    sessions : List[Session]
        List of sessions.
    """

    total: float = Field(..., alias='total')
    sessions: List[Session] = Field(..., alias='sessions')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
