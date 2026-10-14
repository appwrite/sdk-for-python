from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.o_auth2_auth0_prompt import OAuth2Auth0Prompt


class OAuth2Auth0(AppwriteModel):
    """
    OAuth2Auth0

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Auth0 OAuth2 client ID.
    clientsecret : str
        Auth0 OAuth2 client secret.
    prompt : List[OAuth2Auth0Prompt]
        Auth0 OAuth2 prompt values.
    endpoint : str
        Auth0 OAuth2 endpoint domain.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2Auth0Prompt] = Field(..., alias='prompt')
    endpoint: str = Field(..., alias='endpoint')

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
        if 'clientSecret' not in data and 'clientsecret' not in data:
            data['clientSecret'] = ''
        if 'prompt' not in data:
            data['prompt'] = []
        if 'endpoint' not in data:
            data['endpoint'] = ''
        return data
