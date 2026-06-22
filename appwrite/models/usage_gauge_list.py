from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .usage_metric import UsageMetric

class UsageGaugeList(AppwriteModel):
    """
    usageGaugeList

    Attributes
    ----------
    interval : str
        Time interval size (1h or 1d). Empty when the request omits `interval` — points then carry the request end time as their as-of marker.
    metrics : List[UsageMetric]
        One entry per requested metric, each carrying its own points[] time series (latest-snapshot per bucket / dimension via argMax over time).
    """
    interval: str = Field(..., alias='interval')
    metrics: List[UsageMetric] = Field(..., alias='metrics')
