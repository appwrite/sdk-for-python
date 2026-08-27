from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DedicatedDatabasePooler(AppwriteModel):
    """
    PoolerConfig

    Attributes
    ----------
    enabled : bool
        Whether connection pooling is enabled.
    mode : str
        Connection pool mode. Possible values: transaction (releases connections back to pool after each transaction), session (holds connections for the entire client session).
    maxconnections : float
        Client-connection ceiling the pooler accepts. Enforced on MySQL and MariaDB; on PostgreSQL the pooler has no client cap, so this reports the database&#039;s advertised networkMaxConnections and cannot be set here.
    defaultpoolsize : float
        Default pool size per user.
    port : float
        Pooler listening port.
    readwritesplitting : bool
        Whether SELECTs are routed to HA replicas while writes and locked reads stay on the primary. Active only when HA is enabled.
    poolercpurequest : str
        Effective CPU request applied to the pooler sidecar container (Kubernetes quantity). Returns the proportional default (5% of DB CPU, floor 100m) unless overridden.
    poolercpulimit : str
        Effective CPU limit applied to the pooler sidecar container (Kubernetes quantity). Returns the proportional default (10% of DB CPU, floor 200m) unless overridden.
    poolermemoryrequest : str
        Effective memory request applied to the pooler sidecar container (Kubernetes quantity). Returns the proportional default (7.5% of DB memory, floor 64Mi) unless overridden.
    poolermemorylimit : str
        Effective memory limit applied to the pooler sidecar container (Kubernetes quantity). Returns the proportional default (15% of DB memory, floor 128Mi) unless overridden.
    """

    enabled: bool = Field(..., alias='enabled')
    mode: str = Field(..., alias='mode')
    maxconnections: float = Field(..., alias='maxConnections')
    defaultpoolsize: float = Field(..., alias='defaultPoolSize')
    port: float = Field(..., alias='port')
    readwritesplitting: bool = Field(..., alias='readWriteSplitting')
    poolercpurequest: str = Field(..., alias='poolerCpuRequest')
    poolercpulimit: str = Field(..., alias='poolerCpuLimit')
    poolermemoryrequest: str = Field(..., alias='poolerMemoryRequest')
    poolermemorylimit: str = Field(..., alias='poolerMemoryLimit')
