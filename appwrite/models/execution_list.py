from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .execution import Execution


class ExecutionList(AppwriteModel):
    """
    Executions List

    Attributes
    ----------
    total : float
        Total number of executions that matched your query.
    executions : List[Execution]
        List of executions.
    """

    total: float = Field(..., alias='total')
    executions: List[Execution] = Field(..., alias='executions')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'executions' not in data:
            data['executions'] = []
        return data
