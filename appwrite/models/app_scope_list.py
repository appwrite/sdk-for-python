from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .app_scope import AppScope


class AppScopeList(AppwriteModel):
    """
    App scopes list

    Attributes
    ----------
    total : float
        Total number of scopes that matched your query.
    scopes : List[AppScope]
        List of scopes.
    """

    total: float = Field(..., alias='total')
    scopes: List[AppScope] = Field(..., alias='scopes')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'scopes' not in data:
            data['scopes'] = []
        return data
