from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .dedicated_database_specification import DedicatedDatabaseSpecification


class DedicatedDatabaseSpecificationList(AppwriteModel):
    """
    SpecificationList

    Attributes
    ----------
    specifications : List[DedicatedDatabaseSpecification]
        List of dedicated database specifications.
    total : float
        Total number of specifications.
    """

    specifications: List[DedicatedDatabaseSpecification] = Field(..., alias='specifications')
    total: float = Field(..., alias='total')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
