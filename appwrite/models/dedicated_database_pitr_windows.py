from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DedicatedDatabasePITRWindows(AppwriteModel):
    """
    PITRWindows

    Attributes
    ----------
    earliest : str
        Earliest available recovery point.
    latest : str
        Latest available recovery point.
    """

    earliest: str = Field(..., alias='earliest')
    latest: str = Field(..., alias='latest')
