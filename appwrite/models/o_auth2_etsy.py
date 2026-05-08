from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Etsy(AppwriteModel):
    """
    OAuth2Etsy

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    keystring : str
        Etsy OAuth2 keystring.
    sharedsecret : str
        Etsy OAuth2 shared secret.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    keystring: str = Field(..., alias='keyString')
    sharedsecret: str = Field(..., alias='sharedSecret')
