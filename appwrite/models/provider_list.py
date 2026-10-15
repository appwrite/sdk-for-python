from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .provider import Provider


class ProviderList(AppwriteModel):
    """
    Provider list

    Attributes
    ----------
    total : float
        Total number of providers that matched your query.
    providers : List[Provider]
        List of providers.
    """

    total: float = Field(..., alias='total')
    providers: List[Provider] = Field(..., alias='providers')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'providers' not in data:
            data['providers'] = []
        return data
