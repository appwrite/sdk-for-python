from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AlgoArgon2(AppwriteModel):
    """
    AlgoArgon2

    Attributes
    ----------
    type : str
        Algo type.
    memorycost : float
        Memory used to compute hash.
    timecost : float
        Amount of time consumed to compute hash
    threads : float
        Number of threads used to compute hash.
    """
    type: str = Field(..., alias='type')
    memorycost: float = Field(..., alias='memoryCost')
    timecost: float = Field(..., alias='timeCost')
    threads: float = Field(..., alias='threads')
