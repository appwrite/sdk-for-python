from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class UsageGauge(AppwriteModel):
    """
    usageGauge

    Attributes
    ----------
    metric : str
        The metric key.
    value : float
        The current snapshot value.
    time : str
        The snapshot timestamp.
    resourcetype : str
        The resource type.
    resourceid : str
        The resource ID.
    """
    metric: str = Field(..., alias='metric')
    value: float = Field(..., alias='value')
    time: str = Field(..., alias='time')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
