from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_member import DedicatedDatabaseMember

class DedicatedDatabaseReplicas(AppwriteModel):
    """
    Replicas

    Attributes
    ----------
    replicas : float
        Number of configured replicas. Zero means high availability is disabled.
    syncmode : str
        Replication sync mode. Possible values: async (asynchronous, fastest), sync (synchronous, strong consistency), quorum (quorum-based, majority of replicas must confirm).
    members : List[DedicatedDatabaseMember]
        Per-pod statuses for the primary and every replica.
    """
    replicas: float = Field(..., alias='replicas')
    syncmode: str = Field(..., alias='syncMode')
    members: List[DedicatedDatabaseMember] = Field(..., alias='members')
