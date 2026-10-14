from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DedicatedDatabaseSpecification(AppwriteModel):
    """
    Specification

    Attributes
    ----------
    slug : str
        Specification slug. Use this value when creating a dedicated database.
    name : str
        Human readable specification name.
    price : float
        Monthly price of the specification in USD.
    storageoveragerate : Optional[float]
        Price per GB of storage above the included amount, per month, in USD.
    bandwidthoveragerate : Optional[float]
        Price per GB of bandwidth above the included amount, per month, in USD.
    replicarate : Optional[float]
        High availability replica price as a fraction of the specification price.
    pitrrate : Optional[float]
        Point-in-time recovery price as a fraction of the specification price.
    cpu : float
        Allocated CPU in millicores.
    memory : float
        Allocated memory in MB.
    maxconnections : float
        Maximum number of concurrent connections.
    includedstorage : float
        Included storage in GB before overage charges apply.
    includedbandwidth : float
        Included bandwidth in GB before overage charges apply.
    enabled : bool
        Whether the specification is available on the current plan.
    """

    slug: str = Field(..., alias='slug')
    name: str = Field(..., alias='name')
    price: float = Field(..., alias='price')
    storageoveragerate: Optional[float] = Field(default=None, alias='storageOverageRate')
    bandwidthoveragerate: Optional[float] = Field(default=None, alias='bandwidthOverageRate')
    replicarate: Optional[float] = Field(default=None, alias='replicaRate')
    pitrrate: Optional[float] = Field(default=None, alias='pitrRate')
    cpu: float = Field(..., alias='cpu')
    memory: float = Field(..., alias='memory')
    maxconnections: float = Field(..., alias='maxConnections')
    includedstorage: float = Field(..., alias='includedStorage')
    includedbandwidth: float = Field(..., alias='includedBandwidth')
    enabled: bool = Field(..., alias='enabled')
