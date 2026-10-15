from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DedicatedDatabasePITRWindows(AppwriteModel):
    """
    PITRWindows

    Attributes
    ----------
    earliest : str
        Earliest available recovery point.
    latest : str
        Latest available recovery point.
    """

    earliest: str = Field(..., alias='earliest')
    latest: str = Field(..., alias='latest')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'earliest' not in data:
            data['earliest'] = ''
        if 'latest' not in data:
            data['latest'] = ''
        return data
