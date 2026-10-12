from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        return data
