from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
        Overall health status: healthy, degraded, or unhealthy.
    ready : bool
        Whether the database is ready to accept connections.
    engine : str
        Database engine: postgresql, mysql, mariadb, or mongodb.
    version : str
        Database engine version.
    uptime : float
        Database uptime in seconds.
    connections : DatabaseStatusConnections
        Connection statistics.
    replicas : List[DatabaseStatusReplica]
        List of database replicas and their status.
    volumes : List[DatabaseStatusVolume]
        Storage volume information.
    """
    health: str = Field(..., alias='health')
    ready: bool = Field(..., alias='ready')
    engine: str = Field(..., alias='engine')
    version: str = Field(..., alias='version')
    uptime: float = Field(..., alias='uptime')
    connections: DatabaseStatusConnections = Field(..., alias='connections')
    replicas: List[DatabaseStatusReplica] = Field(..., alias='replicas')
    volumes: List[DatabaseStatusVolume] = Field(..., alias='volumes')
