from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Linkedin(AppwriteModel):
    """
    OAuth2Linkedin

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        LinkedIn OAuth2 client ID.
    primaryclientsecret : str
        LinkedIn OAuth2 primary client secret.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    primaryclientsecret: str = Field(..., alias='primaryClientSecret')
