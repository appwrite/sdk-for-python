from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Paypal(AppwriteModel):
    """
    OAuth2Paypal

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        PayPal OAuth2 client ID.
    secretkey : str
        PayPal OAuth2 secret key.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    secretkey: str = Field(..., alias='secretKey')
