from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class AlgoScrypt(AppwriteModel):
    """
    AlgoScrypt

    Attributes
    ----------
    type : str
        Algo type.
    costcpu : float
        CPU complexity of computed hash.
    costmemory : float
        Memory complexity of computed hash.
    costparallel : float
        Parallelization of computed hash.
    length : float
        Length used to compute hash.
    """

    type: str = Field(..., alias='type')
    costcpu: float = Field(..., alias='costCpu')
    costmemory: float = Field(..., alias='costMemory')
    costparallel: float = Field(..., alias='costParallel')
    length: float = Field(..., alias='length')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'type' not in data:
            data['type'] = 'scrypt'
        if 'costCpu' not in data and 'costcpu' not in data:
            data['costCpu'] = 8
        if 'costMemory' not in data and 'costmemory' not in data:
            data['costMemory'] = 14
        if 'costParallel' not in data and 'costparallel' not in data:
            data['costParallel'] = 1
        if 'length' not in data:
            data['length'] = 64
        return data
