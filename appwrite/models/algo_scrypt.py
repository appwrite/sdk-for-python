from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
