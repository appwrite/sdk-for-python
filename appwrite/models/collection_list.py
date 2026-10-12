from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .collection import Collection


class CollectionList(AppwriteModel):
    """
    Collections List

    Attributes
    ----------
    total : float
        Total number of collections that matched your query.
    collections : List[Collection]
        List of collections.
    """

    total: float = Field(..., alias='total')
    collections: List[Collection] = Field(..., alias='collections')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
