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
        Member role. Possible values: primary (accepts reads and writes), replica (read-only follower).
    status : str
        Member pod status. Possible values: provisioning (pod missing or Pending), starting (Running but not Ready), active (Running and Ready), failed (Failed phase or CrashLoopBackOff container), or the lowercased pod phase reported by the cluster.
    lagseconds : float
        Replication lag in seconds.
    """
    id: str = Field(..., alias='$id')
    role: str = Field(..., alias='role')
    status: str = Field(..., alias='status')
    lagseconds: float = Field(..., alias='lagSeconds')
