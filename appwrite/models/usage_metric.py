from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .usage_data_point import UsageDataPoint

class UsageMetric(AppwriteModel):
    """
    usageMetric

    Attributes
    ----------
    metric : str
        Metric key this series describes.
    points : List[UsageDataPoint]
        Data points for this metric, ordered by time ascending. With `interval`, each entry is one bucket; without, each entry is one row of the dimensional or aggregate breakdown.
    """
    metric: str = Field(..., alias='metric')
    points: List[UsageDataPoint] = Field(..., alias='points')
