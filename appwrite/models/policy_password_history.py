from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicyPasswordHistory(AppwriteModel):
    """
    Policy Password History

    Attributes
    ----------
    id : str
        Policy ID.
    total : float
        Password history length. A value of 0 means the policy is disabled.
    """
    id: str = Field(..., alias='$id')
    total: float = Field(..., alias='total')
