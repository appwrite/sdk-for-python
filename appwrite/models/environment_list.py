from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .environment import Environment


class EnvironmentList(AppwriteModel):
    """
    Environments list

    Attributes
    ----------
    total : float
        Total number of environments that matched your query.
    environments : List[Environment]
        List of environments.
    """

    total: float = Field(..., alias='total')
    environments: List[Environment] = Field(..., alias='environments')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'environments' not in data:
            data['environments'] = []
        return data
