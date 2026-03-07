from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
