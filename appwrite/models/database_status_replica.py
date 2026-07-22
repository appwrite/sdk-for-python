from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DatabaseStatusReplica(AppwriteModel):
    """
    Replica

    Attributes
    ----------
    index : float
        StatefulSet pod index (0 = primary, 1+ = replicas).
    role : str
        Replica role: primary or replica.
    healthy : bool
        Whether the replica is healthy.
    lagseconds : Optional[float]
        Replication lag in seconds (null for primary).
    """
    index: float = Field(..., alias='index')
    role: str = Field(..., alias='role')
    healthy: bool = Field(..., alias='healthy')
    lagseconds: Optional[float] = Field(default=None, alias='lagSeconds')
