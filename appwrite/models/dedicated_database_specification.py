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
    cpu: float = Field(..., alias='cpu')
    memory: float = Field(..., alias='memory')
    maxconnections: float = Field(..., alias='maxConnections')
    includedstorage: float = Field(..., alias='includedStorage')
    includedbandwidth: float = Field(..., alias='includedBandwidth')
    enabled: bool = Field(..., alias='enabled')
