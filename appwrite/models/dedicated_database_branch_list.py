from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .dedicated_database_branch import DedicatedDatabaseBranch


class DedicatedDatabaseBranchList(AppwriteModel):
    """
    BranchList

    Attributes
    ----------
    total : float
        Total number of branches.
    branches : List[DedicatedDatabaseBranch]
        List of branches.
    """

    total: float = Field(..., alias='total')
    branches: List[DedicatedDatabaseBranch] = Field(..., alias='branches')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
