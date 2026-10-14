from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    nativeenabled : bool
        Native Sign in with Apple is active and can be used to create sessions from an ID token. Independent of enabled, which only controls the browser-based flow.
    nativeclientids : List[Any]
        App bundle IDs accepted as ID token audiences for native Sign in with Apple, next to the Services ID.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    serviceid: str = Field(..., alias='serviceId')
    keyid: str = Field(..., alias='keyId')
    teamid: str = Field(..., alias='teamId')
    p8file: str = Field(..., alias='p8File')
    nativeenabled: bool = Field(..., alias='nativeEnabled')
    nativeclientids: List[Any] = Field(..., alias='nativeClientIds')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'enabled' not in data:
            data['enabled'] = False
        if 'serviceId' not in data and 'serviceid' not in data:
            data['serviceId'] = ''
        if 'keyId' not in data and 'keyid' not in data:
            data['keyId'] = ''
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        if 'p8File' not in data and 'p8file' not in data:
            data['p8File'] = ''
        if 'nativeEnabled' not in data and 'nativeenabled' not in data:
            data['nativeEnabled'] = False
        if 'nativeClientIds' not in data and 'nativeclientids' not in data:
            data['nativeClientIds'] = []
        return data
