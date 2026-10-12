from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .insight import Insight


class InsightList(AppwriteModel):
    """
    Insights List

    Attributes
    ----------
    total : float
        Total number of insights that matched your query.
    insights : List[Insight]
        List of insights.
    """

    total: float = Field(..., alias='total')
    insights: List[Insight] = Field(..., alias='insights')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
