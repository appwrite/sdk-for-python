from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicyDenyFreeEmail(AppwriteModel):
    """
    Policy Deny Free Email

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether the deny free email policy is enabled.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
