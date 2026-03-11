from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MfaRecoveryCodes(AppwriteModel):
    """
    MFA Recovery Codes

    Attributes
    ----------
    recoverycodes : List[Any]
        Recovery codes.
    """
    recoverycodes: List[Any] = Field(..., alias='recoveryCodes')
