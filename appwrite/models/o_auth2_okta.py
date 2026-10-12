from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.o_auth2_okta_prompt import OAuth2OktaPrompt


class OAuth2Okta(AppwriteModel):
    """
    OAuth2Okta

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Okta OAuth2 client ID.
    clientsecret : str
        Okta OAuth2 client secret.
    prompt : List[OAuth2OktaPrompt]
        Okta OAuth2 prompt values.
    domain : str
        Okta OAuth2 domain.
    authorizationserverid : str
        Okta OAuth2 authorization server ID.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2OktaPrompt] = Field(..., alias='prompt')
    domain: str = Field(..., alias='domain')
    authorizationserverid: str = Field(..., alias='authorizationServerId')

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
        if 'domain' not in data:
            data['domain'] = ''
        if 'authorizationServerId' not in data and 'authorizationserverid' not in data:
            data['authorizationServerId'] = ''
        return data
