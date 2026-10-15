from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        if 'clientId' not in data and 'clientid' not in data:
            data['clientId'] = ''
        if 'primaryClientSecret' not in data and 'primaryclientsecret' not in data:
            data['primaryClientSecret'] = ''
        return data
