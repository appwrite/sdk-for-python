from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .dedicated_database import DedicatedDatabase


class DedicatedDatabaseList(AppwriteModel):
    """
    Dedicated databases list

    Attributes
    ----------
    total : float
        Total number of databases that matched your query.
    databases : List[DedicatedDatabase]
        List of databases.
    """

    total: float = Field(..., alias='total')
    databases: List[DedicatedDatabase] = Field(..., alias='databases')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
