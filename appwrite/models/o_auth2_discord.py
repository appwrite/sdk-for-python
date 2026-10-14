from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.o_auth2_discord_prompt import OAuth2DiscordPrompt


class OAuth2Discord(AppwriteModel):
    """
    OAuth2Discord

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Discord OAuth2 client ID.
    clientsecret : str
        Discord OAuth2 client secret.
    prompt : Optional[List[OAuth2DiscordPrompt]]
        Discord OAuth2 prompt values.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: Optional[List[OAuth2DiscordPrompt]] = Field(default=None, alias='prompt')
