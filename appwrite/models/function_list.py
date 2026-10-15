from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .function import Function


class FunctionList(AppwriteModel):
    """
    Functions List

    Attributes
    ----------
    total : float
        Total number of functions that matched your query.
    functions : List[Function]
        List of functions.
    """

    total: float = Field(..., alias='total')
    functions: List[Function] = Field(..., alias='functions')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'functions' not in data:
            data['functions'] = []
        return data
