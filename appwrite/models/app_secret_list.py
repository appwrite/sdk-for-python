from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .app_secret import AppSecret


class AppSecretList(AppwriteModel):
    """
    App secrets list

    Attributes
    ----------
    total : float
        Total number of secrets that matched your query.
    secrets : List[AppSecret]
        List of secrets.
    """

    total: float = Field(..., alias='total')
    secrets: List[AppSecret] = Field(..., alias='secrets')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
