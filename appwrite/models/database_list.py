from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .database import Database


class DatabaseList(AppwriteModel):
    """
    Databases List

    Attributes
    ----------
    total : float
        Total number of databases that matched your query.
    databases : List[Database]
        List of databases.
    """

    total: float = Field(..., alias='total')
    databases: List[Database] = Field(..., alias='databases')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'databases' not in data:
            data['databases'] = []
        return data
