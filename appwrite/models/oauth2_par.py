from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2PAR(AppwriteModel):
    """
    OAuth2 PAR

    Attributes
    ----------
    request_uri : str
        Authorization request handle to pass to the authorize endpoint.
    expires_in : float
        Lifetime of the authorization request handle in seconds.
    """
    request_uri: str = Field(..., alias='request_uri')
    expires_in: float = Field(..., alias='expires_in')
