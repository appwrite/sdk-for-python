from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicySessionDuration(AppwriteModel):
    """
    Policy Session Duration

    Attributes
    ----------
    id : str
        Policy ID.
    duration : float
        Session duration in seconds.
    """
    id: str = Field(..., alias='$id')
    duration: float = Field(..., alias='duration')
