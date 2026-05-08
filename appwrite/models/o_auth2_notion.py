from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Notion(AppwriteModel):
    """
    OAuth2Notion

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    oauthclientid : str
        Notion OAuth2 client ID.
    oauthclientsecret : str
        Notion OAuth2 client secret.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    oauthclientid: str = Field(..., alias='oauthClientId')
    oauthclientsecret: str = Field(..., alias='oauthClientSecret')
