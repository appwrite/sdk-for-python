from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .database_status_connections import DatabaseStatusConnections
from .database_status_replica import DatabaseStatusReplica
from .database_status_volume import DatabaseStatusVolume


class DatabaseStatus(AppwriteModel):
    """
    Status

    Attributes
    ----------
    health : str
        Overall health status: healthy, degraded, unhealthy, or unknown when nothing could be measured.
    ready : bool
        Whether the database is ready to accept connections.
    engine : str
        Database engine: postgresql, mysql, or mongodb.
    version : str
        Database engine version.
    uptime : float
        Database uptime in seconds.
    connections : Optional[DatabaseStatusConnections]
        Connection statistics. Null when the database has not been probed.
    syncmode : str
        Requested replication sync mode. Possible values: async, sync, quorum. Compare with effectiveSyncMode for what the primary is enforcing.
    effectivesyncmode : Optional[str]
        Replication sync mode the primary is actually enforcing. Null when high availability is disabled or the state could not be read.
    syncdegraded : bool
        Whether the enforced replication is weaker than the requested syncMode.
    syncacknowledgements : float
        Number of standby acknowledgements the primary waits for before a write is committed.
    syncstandbycount : float
        Number of standbys registered with the primary for synchronous replication.
    syncstateconfirmed : Optional[bool]
        Whether the other sync fields are an engine reading rather than a recorded estimate. True when the primary answered what it is enforcing, including when that answer contradicted the record, in which case the contradicted values are replaced by the ones the engine reports. False when the reading could not be taken: the probe did not answer, there was no engine to ask, or the values describe a configuration change just applied rather than anything measured. Absent when no engine was asked at all, so an unprobed database is distinguishable from an unconfirmed one. False never means a standby was found lagging, because it is the absence of a reading rather than a negative one, so draw no conclusion about replication health from it or from a response that omits it.
    replicas : List[DatabaseStatusReplica]
        List of database replicas and their status. Every configured member appears, including one the backend has not brought up, which is reported as not healthy.
    volumes : List[DatabaseStatusVolume]
        Storage volume information.
    """

    health: str = Field(..., alias='health')
    ready: bool = Field(..., alias='ready')
    engine: str = Field(..., alias='engine')
    version: str = Field(..., alias='version')
    uptime: float = Field(..., alias='uptime')
    connections: Optional[DatabaseStatusConnections] = Field(default=None, alias='connections')
    syncmode: str = Field(..., alias='syncMode')
    effectivesyncmode: Optional[str] = Field(default=None, alias='effectiveSyncMode')
    syncdegraded: bool = Field(..., alias='syncDegraded')
    syncacknowledgements: float = Field(..., alias='syncAcknowledgements')
    syncstandbycount: float = Field(..., alias='syncStandbyCount')
    syncstateconfirmed: Optional[bool] = Field(default=None, alias='syncStateConfirmed')
    replicas: List[DatabaseStatusReplica] = Field(..., alias='replicas')
    volumes: List[DatabaseStatusVolume] = Field(..., alias='volumes')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'health' not in data:
            data['health'] = 'unknown'
        if 'ready' not in data:
            data['ready'] = False
        if 'engine' not in data:
            data['engine'] = 'postgresql'
        if 'version' not in data:
            data['version'] = ''
        if 'uptime' not in data:
            data['uptime'] = 0
        if 'syncMode' not in data and 'syncmode' not in data:
            data['syncMode'] = 'async'
        if 'syncDegraded' not in data and 'syncdegraded' not in data:
            data['syncDegraded'] = False
        if 'syncAcknowledgements' not in data and 'syncacknowledgements' not in data:
            data['syncAcknowledgements'] = 0
        if 'syncStandbyCount' not in data and 'syncstandbycount' not in data:
            data['syncStandbyCount'] = 0
        if 'replicas' not in data:
            data['replicas'] = []
        if 'volumes' not in data:
            data['volumes'] = []
        return data
