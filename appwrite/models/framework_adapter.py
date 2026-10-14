from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class FrameworkAdapter(AppwriteModel):
    """
    Framework Adapter

    Attributes
    ----------
    key : str
        Adapter key.
    installcommand : str
        Default command to download dependencies.
    buildcommand : str
        Default command to build site into output directory.
    outputdirectory : str
        Default output directory of build.
    fallbackfile : Optional[str]
        Name of fallback file to use instead of 404 page. If null, Appwrite 404 page will be displayed.
    """

    key: str = Field(..., alias='key')
    installcommand: str = Field(..., alias='installCommand')
    buildcommand: str = Field(..., alias='buildCommand')
    outputdirectory: str = Field(..., alias='outputDirectory')
    fallbackfile: Optional[str] = Field(default=None, alias='fallbackFile')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'key' not in data:
            data['key'] = ''
        if 'installCommand' not in data and 'installcommand' not in data:
            data['installCommand'] = ''
        if 'buildCommand' not in data and 'buildcommand' not in data:
            data['buildCommand'] = ''
        if 'outputDirectory' not in data and 'outputdirectory' not in data:
            data['outputDirectory'] = ''
        return data
