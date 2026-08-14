from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DatabaseStatusReplica(AppwriteModel):
    """
    Replica

    Attributes
    ----------
    index : float
        Member index within the database. Read `role` for which member accepts writes: a failover moves the primary without renumbering the indexes.
    role : str
        Member role. Possible values: primary (accepts reads and writes), replica (read-only follower), unknown (placement not established; reported while a transition is moving or restarting the topology, so no member can be named the write target).
    healthy : bool
        Whether the replica is healthy.
    lagseconds : Optional[float]
        Replication lag in seconds (null for primary).
    """
    index: float = Field(..., alias='index')
    role: str = Field(..., alias='role')
    healthy: bool = Field(..., alias='healthy')
    lagseconds: Optional[float] = Field(default=None, alias='lagSeconds')
