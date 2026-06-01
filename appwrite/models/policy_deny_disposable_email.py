from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicyDenyDisposableEmail(AppwriteModel):
    """
    Policy Deny Disposable Email

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether the deny disposable email policy is enabled.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
