from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.platform_type import PlatformType

class PlatformApple(AppwriteModel):
    """
    Platform Apple

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
    bundleidentifier : str
        Apple bundle identifier.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    type: PlatformType = Field(..., alias='type')
    bundleidentifier: str = Field(..., alias='bundleIdentifier')
