from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
    fallbackfile : str
        Name of fallback file to use instead of 404 page. If null, Appwrite 404 page will be displayed.
    """
    key: str = Field(..., alias='key')
    installcommand: str = Field(..., alias='installCommand')
    buildcommand: str = Field(..., alias='buildCommand')
    outputdirectory: str = Field(..., alias='outputDirectory')
    fallbackfile: str = Field(..., alias='fallbackFile')
