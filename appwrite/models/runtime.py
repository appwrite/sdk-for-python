from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Runtime(AppwriteModel):
    """
    Runtime

    Attributes
    ----------
    id : str
        Runtime ID.
    key : str
        Parent runtime key.
    name : str
        Runtime Name.
    version : str
        Runtime version.
    base : str
        Base Docker image used to build the runtime.
    image : str
        Image name of Docker Hub.
    logo : str
        Name of the logo image.
    supports : List[Any]
        List of supported architectures.
    """
    id: str = Field(..., alias='$id')
    key: str = Field(..., alias='key')
    name: str = Field(..., alias='name')
    version: str = Field(..., alias='version')
    base: str = Field(..., alias='base')
    image: str = Field(..., alias='image')
    logo: str = Field(..., alias='logo')
    supports: List[Any] = Field(..., alias='supports')
