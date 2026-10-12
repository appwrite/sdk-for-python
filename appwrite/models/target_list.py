from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .target import Target


class TargetList(AppwriteModel):
    """
    Target list

    Attributes
    ----------
    total : float
        Total number of targets that matched your query.
    targets : List[Target]
        List of targets.
    """

    total: float = Field(..., alias='total')
    targets: List[Target] = Field(..., alias='targets')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
