from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DedicatedDatabaseSpecificationPricing(AppwriteModel):
    """
    SpecificationPricing

    Attributes
    ----------
    storageoveragerate : float
        Price per GB of storage above the included amount, per month, in USD.
    bandwidthoveragerate : float
        Price per GB of bandwidth above the included amount, per month, in USD.
    replicarate : float
        High availability replica price as a fraction of the specification cost.
    crossregionreplicarate : float
        Cross-region replica price as a fraction of the specification cost.
    pitrrate : float
        Point-in-time recovery price as a fraction of the specification cost.
    """
    storageoveragerate: float = Field(..., alias='storageOverageRate')
    bandwidthoveragerate: float = Field(..., alias='bandwidthOverageRate')
    replicarate: float = Field(..., alias='replicaRate')
    crossregionreplicarate: float = Field(..., alias='crossRegionReplicaRate')
    pitrrate: float = Field(..., alias='pitrRate')
