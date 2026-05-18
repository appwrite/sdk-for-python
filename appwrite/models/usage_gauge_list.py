from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .usage_gauge import UsageGauge

class UsageGaugeList(AppwriteModel):
    """
    Usage gauges list

    Attributes
    ----------
    total : float
        Total number of gauges that matched your query.
    gauges : List[UsageGauge]
        List of gauges.
    """
    total: float = Field(..., alias='total')
    gauges: List[UsageGauge] = Field(..., alias='gauges')
