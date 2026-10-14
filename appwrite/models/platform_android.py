from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.platform_type import PlatformType


class PlatformAndroid(AppwriteModel):
    """
    Platform Android

    Attributes
    ----------
    id : str
        Platform ID.
    createdat : str
        Platform creation date in ISO 8601 format.
    updatedat : str
        Platform update date in ISO 8601 format.
    name : str
        Platform name.
    type : PlatformType
        Platform type. Possible values are: windows, apple, android, linux, web.
    applicationid : str
        Android application ID.
    fingerprints : List[Any]
        SHA-256 fingerprints of the certificates the app is signed with. Passkeys created in the app are accepted when its signature matches one.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    type: PlatformType = Field(..., alias='type')
    applicationid: str = Field(..., alias='applicationId')
    fingerprints: List[Any] = Field(..., alias='fingerprints')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'applicationId' not in data and 'applicationid' not in data:
            data['applicationId'] = ''
        if 'fingerprints' not in data:
            data['fingerprints'] = []
        return data
