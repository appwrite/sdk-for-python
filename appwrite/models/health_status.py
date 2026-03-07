from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from ..enums.health_check_status import HealthCheckStatus

class HealthStatus(AppwriteModel):
    """
    Health Status

    Attributes
    ----------
    name : str
        Name of the service.
    ping : float
        Duration in milliseconds how long the health check took.
    status : HealthCheckStatus
        Service status. Possible values are: `pass`, `fail`
    """
    name: str = Field(..., alias='name')
    ping: float = Field(..., alias='ping')
    status: HealthCheckStatus = Field(..., alias='status')
