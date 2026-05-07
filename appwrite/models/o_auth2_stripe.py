from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Stripe(AppwriteModel):
    """
    OAuth2Stripe

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Stripe OAuth2 client ID.
    apisecretkey : str
        Stripe OAuth2 API secret key.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    apisecretkey: str = Field(..., alias='apiSecretKey')
