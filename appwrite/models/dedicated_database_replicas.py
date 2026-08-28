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
        Requested replication sync mode. Possible values: async (asynchronous, fastest), sync (synchronous, strong consistency), quorum (quorum-based, majority of replicas must confirm). This is what was asked for; compare it with effectiveSyncMode for what the primary is enforcing.
    effectivesyncmode : Optional[str]
        Replication sync mode the primary is actually enforcing. Null when high availability is disabled or the state could not be read. A value below the requested syncMode means writes are being acknowledged with weaker durability than configured.
    syncdegraded : bool
        Whether the enforced replication is weaker than the requested syncMode.
    syncacknowledgements : float
        Number of standby acknowledgements the primary waits for before a write is committed. Zero means writes are acknowledged locally.
    syncstandbycount : float
        Number of standbys registered with the primary for synchronous replication.
    syncstateconfirmed : Optional[bool]
        Whether the other sync fields are an engine reading rather than a recorded estimate. True when the primary answered what it is enforcing, including when that answer contradicted the record, in which case the contradicted values are replaced by the ones the engine reports. False when the reading could not be taken: the probe did not answer, there was no engine to ask, or the values describe a configuration change just applied rather than anything measured. Absent when no engine was asked at all, so an unprobed database is distinguishable from an unconfirmed one. False never means a standby was found lagging, because it is the absence of a reading rather than a negative one, so draw no conclusion about replication health from it or from a response that omits it.
    members : List[DedicatedDatabaseMember]
        Per-pod statuses for the primary and every replica.
    """

    replicas: float = Field(..., alias='replicas')
    syncmode: str = Field(..., alias='syncMode')
    effectivesyncmode: Optional[str] = Field(default=None, alias='effectiveSyncMode')
    syncdegraded: bool = Field(..., alias='syncDegraded')
    syncacknowledgements: float = Field(..., alias='syncAcknowledgements')
    syncstandbycount: float = Field(..., alias='syncStandbyCount')
    syncstateconfirmed: Optional[bool] = Field(default=None, alias='syncStateConfirmed')
    members: List[DedicatedDatabaseMember] = Field(..., alias='members')
