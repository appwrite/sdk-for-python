from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .index import Index


class IndexList(AppwriteModel):
    """
    Indexes List

    Attributes
    ----------
    total : float
        Total number of indexes that matched your query.
    indexes : List[Index]
        List of indexes.
    """

    total: float = Field(..., alias='total')
    indexes: List[Index] = Field(..., alias='indexes')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
