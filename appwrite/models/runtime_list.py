from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .runtime import Runtime


class RuntimeList(AppwriteModel):
    """
    Runtimes List

    Attributes
    ----------
    total : float
        Total number of runtimes that matched your query.
    runtimes : List[Runtime]
        List of runtimes.
    """

    total: float = Field(..., alias='total')
    runtimes: List[Runtime] = Field(..., alias='runtimes')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
