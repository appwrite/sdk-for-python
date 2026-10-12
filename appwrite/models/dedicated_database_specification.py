from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    storageoveragerate : float
        Price per GB of storage above the included amount, per month, in USD.
    bandwidthoveragerate : float
        Price per GB of bandwidth above the included amount, per month, in USD.
    replicarate : float
        High availability replica price as a fraction of the specification price.
    pitrrate : float
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
    storageoveragerate: float = Field(..., alias='storageOverageRate')
    bandwidthoveragerate: float = Field(..., alias='bandwidthOverageRate')
    replicarate: float = Field(..., alias='replicaRate')
    pitrrate: float = Field(..., alias='pitrRate')
    cpu: float = Field(..., alias='cpu')
    memory: float = Field(..., alias='memory')
    maxconnections: float = Field(..., alias='maxConnections')
    includedstorage: float = Field(..., alias='includedStorage')
    includedbandwidth: float = Field(..., alias='includedBandwidth')
    enabled: bool = Field(..., alias='enabled')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'slug' not in data:
            data['slug'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'price' not in data:
            data['price'] = 0
        if 'storageOverageRate' not in data and 'storageoveragerate' not in data:
            data['storageOverageRate'] = 0
        if 'bandwidthOverageRate' not in data and 'bandwidthoveragerate' not in data:
            data['bandwidthOverageRate'] = 0
        if 'replicaRate' not in data and 'replicarate' not in data:
            data['replicaRate'] = 0
        if 'pitrRate' not in data and 'pitrrate' not in data:
            data['pitrRate'] = 0
        if 'cpu' not in data:
            data['cpu'] = 0
        if 'memory' not in data:
            data['memory'] = 0
        if 'maxConnections' not in data and 'maxconnections' not in data:
            data['maxConnections'] = 0
        if 'includedStorage' not in data and 'includedstorage' not in data:
            data['includedStorage'] = 0
        if 'includedBandwidth' not in data and 'includedbandwidth' not in data:
            data['includedBandwidth'] = 0
        if 'enabled' not in data:
            data['enabled'] = False
        return data
