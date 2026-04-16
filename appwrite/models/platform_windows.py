from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.platform_type import PlatformType

class PlatformWindows(AppwriteModel):
    """
    Platform Windows

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
    packageidentifiername : str
        Windows package identifier name.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    type: PlatformType = Field(..., alias='type')
    packageidentifiername: str = Field(..., alias='packageIdentifierName')
