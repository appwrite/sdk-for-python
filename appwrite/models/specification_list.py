from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .specification import Specification


class SpecificationList(AppwriteModel):
    """
    Specifications List

    Attributes
    ----------
    total : float
        Total number of specifications that matched your query.
    specifications : List[Specification]
        List of specifications.
    """

    total: float = Field(..., alias='total')
    specifications: List[Specification] = Field(..., alias='specifications')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'specifications' not in data:
            data['specifications'] = []
        return data
