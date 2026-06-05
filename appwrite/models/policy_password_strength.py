from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicyPasswordStrength(AppwriteModel):
    """
    Policy Password Strength

    Attributes
    ----------
    id : str
        Policy ID.
    min : float
        Minimum password length required for user passwords.
    uppercase : bool
        Whether passwords must include at least one uppercase letter.
    lowercase : bool
        Whether passwords must include at least one lowercase letter.
    number : bool
        Whether passwords must include at least one number.
    symbols : bool
        Whether passwords must include at least one symbol.
    """
    id: str = Field(..., alias='$id')
    min: float = Field(..., alias='min')
    uppercase: bool = Field(..., alias='uppercase')
    lowercase: bool = Field(..., alias='lowercase')
    number: bool = Field(..., alias='number')
    symbols: bool = Field(..., alias='symbols')
