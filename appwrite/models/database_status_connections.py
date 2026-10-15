from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DatabaseStatusConnections(AppwriteModel):
    """
    Connections

    Attributes
    ----------
    current : float
        Current number of active connections.
    max : float
        The engine&#039;s own max_connections. On a pooled database this is the backend limit the pooler multiplexes onto, not the ceiling a client pool may reach — that is networkMaxConnections on the database resource.
    """

    current: float = Field(..., alias='current')
    max: float = Field(..., alias='max')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'current' not in data:
            data['current'] = 0
        if 'max' not in data:
            data['max'] = 100
        return data
