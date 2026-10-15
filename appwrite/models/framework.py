from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'key' not in data:
            data['key'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'buildRuntime' not in data and 'buildruntime' not in data:
            data['buildRuntime'] = ''
        if 'runtimes' not in data:
            data['runtimes'] = []
        if 'adapters' not in data:
            data['adapters'] = []
        return data
