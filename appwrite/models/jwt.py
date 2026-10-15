from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'jwt' not in data:
            data['jwt'] = ''
        return data
