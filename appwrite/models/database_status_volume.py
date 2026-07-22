from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DatabaseStatusVolume(AppwriteModel):
    """
    Volume

    Attributes
    ----------
    path : str
        Mount path of the volume.
    usedpercent : str
        Percentage of storage used.
    available : str
        Available storage space.
    mounted : bool
        Whether the volume is mounted.
    """
    path: str = Field(..., alias='path')
    usedpercent: str = Field(..., alias='usedPercent')
    available: str = Field(..., alias='available')
    mounted: bool = Field(..., alias='mounted')
