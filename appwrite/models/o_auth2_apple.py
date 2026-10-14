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
    nativeenabled : Optional[bool]
        Native Sign in with Apple is active and can be used to create sessions from an ID token. Independent of enabled, which only controls the browser-based flow.
    nativeclientids : Optional[List[Any]]
        App bundle IDs accepted as ID token audiences for native Sign in with Apple, next to the Services ID.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    serviceid: str = Field(..., alias='serviceId')
    keyid: str = Field(..., alias='keyId')
    teamid: str = Field(..., alias='teamId')
    p8file: str = Field(..., alias='p8File')
    nativeenabled: Optional[bool] = Field(default=None, alias='nativeEnabled')
    nativeclientids: Optional[List[Any]] = Field(default=None, alias='nativeClientIds')
