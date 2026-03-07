from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .framework_adapter import FrameworkAdapter

class Framework(AppwriteModel):
    """
    Framework

    Attributes
    ----------
    key : str
        Framework key.
    name : str
        Framework Name.
    buildruntime : str
        Default runtime version.
    runtimes : List[Any]
        List of supported runtime versions.
    adapters : List[FrameworkAdapter]
        List of supported adapters.
    """
    key: str = Field(..., alias='key')
    name: str = Field(..., alias='name')
    buildruntime: str = Field(..., alias='buildRuntime')
    runtimes: List[Any] = Field(..., alias='runtimes')
    adapters: List[FrameworkAdapter] = Field(..., alias='adapters')
