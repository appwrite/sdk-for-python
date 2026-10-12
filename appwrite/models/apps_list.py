from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .app import App


class AppsList(AppwriteModel):
    """
    Apps list

    Attributes
    ----------
    total : float
        Total number of apps that matched your query.
    apps : List[App]
        List of apps.
    """

    total: float = Field(..., alias='total')
    apps: List[App] = Field(..., alias='apps')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
