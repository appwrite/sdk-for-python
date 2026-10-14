from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .dedicated_database_operation import DedicatedDatabaseOperation


class DedicatedDatabaseOperationList(AppwriteModel):
    """
    OperationList

    Attributes
    ----------
    total : float
        Total number of operations.
    operations : List[DedicatedDatabaseOperation]
        List of operations.
    """

    total: float = Field(..., alias='total')
    operations: List[DedicatedDatabaseOperation] = Field(..., alias='operations')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'operations' not in data:
            data['operations'] = []
        return data
