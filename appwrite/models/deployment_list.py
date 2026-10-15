from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .deployment import Deployment


class DeploymentList(AppwriteModel):
    """
    Deployments List

    Attributes
    ----------
    total : float
        Total number of deployments that matched your query.
    deployments : List[Deployment]
        List of deployments.
    """

    total: float = Field(..., alias='total')
    deployments: List[Deployment] = Field(..., alias='deployments')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'deployments' not in data:
            data['deployments'] = []
        return data
