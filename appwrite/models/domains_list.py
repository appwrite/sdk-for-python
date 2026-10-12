from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .domain import Domain


class DomainsList(AppwriteModel):
    """
    Domains list

    Attributes
    ----------
    total : float
        Total number of domains that matched your query.
    domains : List[Domain]
        List of domains.
    """

    total: float = Field(..., alias='total')
    domains: List[Domain] = Field(..., alias='domains')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
