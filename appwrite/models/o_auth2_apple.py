from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Apple(AppwriteModel):
    """
    OAuth2Apple

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    serviceid : str
        Apple OAuth2 service ID.
    keyid : str
        Apple OAuth2 key ID.
    teamid : str
        Apple OAuth2 team ID.
    p8file : str
        Apple OAuth2 .p8 private key file contents. The secret key wrapped by the PEM markers is 200 characters long.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    serviceid: str = Field(..., alias='serviceId')
    keyid: str = Field(..., alias='keyId')
    teamid: str = Field(..., alias='teamId')
    p8file: str = Field(..., alias='p8File')
