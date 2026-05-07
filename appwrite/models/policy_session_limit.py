from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicySessionLimit(AppwriteModel):
    """
    Policy Session Limit

    Attributes
    ----------
    id : str
        Policy ID.
    total : float
        Maximum number of sessions allowed per user. A value of 0 means the policy is disabled.
    """
    id: str = Field(..., alias='$id')
    total: float = Field(..., alias='total')
