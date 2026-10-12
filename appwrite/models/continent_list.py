from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .continent import Continent


class ContinentList(AppwriteModel):
    """
    Continents List

    Attributes
    ----------
    total : float
        Total number of continents that matched your query.
    continents : List[Continent]
        List of continents.
    """

    total: float = Field(..., alias='total')
    continents: List[Continent] = Field(..., alias='continents')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
