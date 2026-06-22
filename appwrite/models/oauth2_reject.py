from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2Reject(AppwriteModel):
    """
    OAuth2 Reject

    Attributes
    ----------
    redirecturl : str
        URL the end user should be redirected to after the grant is rejected, carrying an `access_denied` error.
    """
    redirecturl: str = Field(..., alias='redirectUrl')
