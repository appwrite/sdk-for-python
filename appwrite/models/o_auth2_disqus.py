from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Disqus(AppwriteModel):
    """
    OAuth2Disqus

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    publickey : str
        Disqus OAuth2 public key.
    secretkey : str
        Disqus OAuth2 secret key.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    publickey: str = Field(..., alias='publicKey')
    secretkey: str = Field(..., alias='secretKey')
