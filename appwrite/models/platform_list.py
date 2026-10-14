from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .platform_web import PlatformWeb
from .platform_apple import PlatformApple
from .platform_android import PlatformAndroid
from .platform_windows import PlatformWindows
from .platform_linux import PlatformLinux


class PlatformList(AppwriteModel):
    """
    Platforms List

    Attributes
    ----------
    total : float
        Total number of platforms in the given project.
    platforms : List[Union[PlatformWeb, PlatformApple, PlatformAndroid, PlatformWindows, PlatformLinux]]
        List of platforms.
    """

    total: float = Field(..., alias='total')
    platforms: List[
        Union[
            PlatformWeb,
            PlatformApple,
            PlatformAndroid,
            PlatformWindows,
            PlatformLinux,
        ]
    ] = Field(..., alias='platforms')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'platforms' not in data:
            data['platforms'] = []
        return data
