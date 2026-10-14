from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Oauth2Project(AppwriteModel):
    """
    OAuth2 Project

    Attributes
    ----------
    id : str
        Project ID.
    region : str
        Region ID the project is deployed in.
    endpoint : str
        API endpoint of the region the project is deployed in. Empty when the region has no public hostname configured.
    """

    id: str = Field(..., alias='$id')
    region: str = Field(..., alias='region')
    endpoint: str = Field(..., alias='endpoint')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'region' not in data:
            data['region'] = ''
        if 'endpoint' not in data:
            data['endpoint'] = ''
        return data
