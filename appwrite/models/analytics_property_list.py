from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .analytics_property import AnalyticsProperty


class AnalyticsPropertyList(AppwriteModel):
    """
    Analytics properties list

    Attributes
    ----------
    total : float
        Total number of properties that matched your query.
    properties : List[AnalyticsProperty]
        List of properties.
    """

    total: float = Field(..., alias='total')
    properties: List[AnalyticsProperty] = Field(..., alias='properties')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'properties' not in data:
            data['properties'] = []
        return data
