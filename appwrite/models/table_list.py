from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .table import Table


class TableList(AppwriteModel):
    """
    Tables List

    Attributes
    ----------
    total : float
        Total number of tables that matched your query.
    tables : List[Table]
        List of tables.
    """

    total: float = Field(..., alias='total')
    tables: List[Table] = Field(..., alias='tables')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
