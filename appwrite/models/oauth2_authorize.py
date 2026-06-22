from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2Authorize(AppwriteModel):
    """
    OAuth2 Authorize

    Attributes
    ----------
    grantid : str
        OAuth2 grant ID. Set when the user must give explicit consent; pass it to the approve or reject endpoint. Empty when a redirect URL is returned instead.
    redirecturl : str
        URL the end user should be redirected to when the flow can complete without consent. Empty when consent is still required.
    """
    grantid: str = Field(..., alias='grantId')
    redirecturl: str = Field(..., alias='redirectUrl')
