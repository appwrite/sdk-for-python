from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .migration import Migration


class MigrationList(AppwriteModel):
    """
    Migrations List

    Attributes
    ----------
    total : float
        Total number of migrations that matched your query.
    migrations : List[Migration]
        List of migrations.
    """

    total: float = Field(..., alias='total')
    migrations: List[Migration] = Field(..., alias='migrations')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'migrations' not in data:
            data['migrations'] = []
        return data
