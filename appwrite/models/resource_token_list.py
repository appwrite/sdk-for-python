from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .resource_token import ResourceToken


class ResourceTokenList(AppwriteModel):
    """
    Resource Tokens List

    Attributes
    ----------
    total : float
        Total number of tokens that matched your query.
    tokens : List[ResourceToken]
        List of tokens.
    """

    total: float = Field(..., alias='total')
    tokens: List[ResourceToken] = Field(..., alias='tokens')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
