from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Bitbucket(AppwriteModel):
    """
    OAuth2Bitbucket

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    key : str
        Bitbucket OAuth2 key.
    secret : str
        Bitbucket OAuth2 secret.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    key: str = Field(..., alias='key')
    secret: str = Field(..., alias='secret')
