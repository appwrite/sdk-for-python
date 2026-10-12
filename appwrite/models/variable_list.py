from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .variable import Variable


class VariableList(AppwriteModel):
    """
    Variables List

    Attributes
    ----------
    total : float
        Total number of variables that matched your query.
    variables : List[Variable]
        List of variables.
    """

    total: float = Field(..., alias='total')
    variables: List[Variable] = Field(..., alias='variables')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
