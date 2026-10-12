from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .dedicated_database_restoration import DedicatedDatabaseRestoration


class DedicatedDatabaseRestorationList(AppwriteModel):
    """
    Dedicated database restorations list

    Attributes
    ----------
    total : float
        Total number of restorations that matched your query.
    restorations : List[DedicatedDatabaseRestoration]
        List of restorations.
    """

    total: float = Field(..., alias='total')
    restorations: List[DedicatedDatabaseRestoration] = Field(..., alias='restorations')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
