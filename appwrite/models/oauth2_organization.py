from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2Organization(AppwriteModel):
    """
    OAuth2 Organization

    Attributes
    ----------
    id : str
        Organization ID.
    """
    id: str = Field(..., alias='$id')
