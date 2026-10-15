from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Specification(AppwriteModel):
    """
    Specification

    Attributes
    ----------
    memory : float
        Memory size in MB.
    cpus : float
        Number of CPUs.
    enabled : bool
        Is size enabled.
    slug : str
        Size slug.
    """

    memory: float = Field(..., alias='memory')
    cpus: float = Field(..., alias='cpus')
    enabled: bool = Field(..., alias='enabled')
    slug: str = Field(..., alias='slug')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'memory' not in data:
            data['memory'] = 0
        if 'cpus' not in data:
            data['cpus'] = 0
        if 'enabled' not in data:
            data['enabled'] = False
        if 'slug' not in data:
            data['slug'] = ''
        return data
