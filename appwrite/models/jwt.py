from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Jwt(AppwriteModel):
    """
    JWT

    Attributes
    ----------
    jwt : str
        JWT encoded string.
    """
    jwt: str = Field(..., alias='jwt')
