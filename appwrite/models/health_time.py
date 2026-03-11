from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class HealthTime(AppwriteModel):
    """
    Health Time

    Attributes
    ----------
    remotetime : float
        Current unix timestamp on trustful remote server.
    localtime : float
        Current unix timestamp of local server where Appwrite runs.
    diff : float
        Difference of unix remote and local timestamps in milliseconds.
    """
    remotetime: float = Field(..., alias='remoteTime')
    localtime: float = Field(..., alias='localTime')
    diff: float = Field(..., alias='diff')
