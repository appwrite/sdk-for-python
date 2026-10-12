from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .framework import Framework


class FrameworkList(AppwriteModel):
    """
    Frameworks List

    Attributes
    ----------
    total : float
        Total number of frameworks that matched your query.
    frameworks : List[Framework]
        List of frameworks.
    """

    total: float = Field(..., alias='total')
    frameworks: List[Framework] = Field(..., alias='frameworks')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
