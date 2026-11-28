from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .analytics_metric import AnalyticsMetric


class AnalyticsMetricList(AppwriteModel):
    """
    AnalyticsMetricList

    Attributes
    ----------
    total : float
        Total number of metric rows returned.
    metrics : List[AnalyticsMetric]
        Metric rows: one per time bucket, one per dimension value, or a single row for the flat aggregate.
    """

    total: float = Field(..., alias='total')
    metrics: List[AnalyticsMetric] = Field(..., alias='metrics')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'metrics' not in data:
            data['metrics'] = []
        return data
