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
    replicating : Optional[bool]
        Whether the engine reports this member&#039;s replication stream as up. Null when no reading was taken: a primary has no stream to report, and a member that is not healthy, or whose probe did not answer, has none yet. `healthy` is a reachability probe of the member itself and says nothing about replication, so a healthy member may still not be replicating.
    lagseconds : Optional[float]
        Replication lag in seconds (null for primary). Also null against `replicating: true`, for a member that is streaming but whose engine printed no numeric lag.
    """

    index: float = Field(..., alias='index')
    role: str = Field(..., alias='role')
    healthy: bool = Field(..., alias='healthy')
    replicating: Optional[bool] = Field(default=None, alias='replicating')
    lagseconds: Optional[float] = Field(default=None, alias='lagSeconds')
