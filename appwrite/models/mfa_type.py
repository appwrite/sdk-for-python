from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class MfaType(AppwriteModel):
    """
    MFAType

    Attributes
    ----------
    secret : str
        Secret token used for TOTP factor.
    uri : str
        URI for authenticator apps.
    """
    secret: str = Field(..., alias='secret')
    uri: str = Field(..., alias='uri')
