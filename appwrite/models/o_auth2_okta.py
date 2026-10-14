from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
    prompt : Optional[List[OAuth2OktaPrompt]]
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
    prompt: Optional[List[OAuth2OktaPrompt]] = Field(default=None, alias='prompt')
    domain: str = Field(..., alias='domain')
    authorizationserverid: str = Field(..., alias='authorizationServerId')
