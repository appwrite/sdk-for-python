from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MfaFactors(AppwriteModel):
    """
    MFAFactors

    Attributes
    ----------
    totp : bool
        Can TOTP be used for MFA challenge for this account.
    phone : bool
        Can phone (SMS) be used for MFA challenge for this account.
    email : bool
        Can email be used for MFA challenge for this account.
    recoverycode : bool
        Can recovery code be used for MFA challenge for this account.
    """
    totp: bool = Field(..., alias='totp')
    phone: bool = Field(..., alias='phone')
    email: bool = Field(..., alias='email')
    recoverycode: bool = Field(..., alias='recoveryCode')
