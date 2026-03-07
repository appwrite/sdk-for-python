from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .health_status import HealthStatus

class HealthStatusList(AppwriteModel):
    """
    Status List

    Attributes
    ----------
    total : float
        Total number of statuses that matched your query.
    statuses : List[HealthStatus]
        List of statuses.
    """
    total: float = Field(..., alias='total')
    statuses: List[HealthStatus] = Field(..., alias='statuses')
