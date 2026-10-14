from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class PolicyPasswordRotation(AppwriteModel):
    """
    Policy Password Rotation

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether expired passwords require a reset before email/password sign-in.
    maxage : float
        Maximum password age in seconds.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    maxage: float = Field(..., alias='maxAge')
