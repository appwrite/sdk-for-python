from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'key' not in data:
            data['key'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'version' not in data:
            data['version'] = ''
        if 'base' not in data:
            data['base'] = ''
        if 'image' not in data:
            data['image'] = ''
        if 'logo' not in data:
            data['logo'] = ''
        if 'supports' not in data:
            data['supports'] = []
        return data
