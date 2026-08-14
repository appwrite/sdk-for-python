from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DedicatedDatabaseMember(AppwriteModel):
    """
    Member

    Attributes
    ----------
    id : str
        Member identifier.
    role : str
        Member role. Possible values: primary (accepts reads and writes), replica (read-only follower), unknown (placement not established; reported while a transition is moving or restarting the topology and this member has not been probed, so no member can be named the write target).
    status : str
        Member pod status. Possible values: pending (configured but absent from the backend topology, so nothing is bringing it up), provisioning (pod missing or Pending), starting (Running but not Ready), active (Running and Ready), failed (Failed phase or CrashLoopBackOff container), or the lowercased pod phase reported by the cluster.
    lagseconds : Optional[float]
        Replication lag in seconds. Null when the lag is not known: a primary has none to report, and a member the backend has not probed has none yet.
    """
    id: str = Field(..., alias='$id')
    role: str = Field(..., alias='role')
    status: str = Field(..., alias='status')
    lagseconds: Optional[float] = Field(default=None, alias='lagSeconds')
