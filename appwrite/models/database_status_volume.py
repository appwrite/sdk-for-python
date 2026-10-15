from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DatabaseStatusVolume(AppwriteModel):
    """
    Volume

    Attributes
    ----------
    path : str
        Mount path of the volume.
    usedpercent : str
        Percentage of storage used.
    available : str
        Available storage space.
    mounted : bool
        Whether the volume is mounted.
    """

    path: str = Field(..., alias='path')
    usedpercent: str = Field(..., alias='usedPercent')
    available: str = Field(..., alias='available')
    mounted: bool = Field(..., alias='mounted')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'path' not in data:
            data['path'] = ''
        if 'usedPercent' not in data and 'usedpercent' not in data:
            data['usedPercent'] = '0%'
        if 'available' not in data:
            data['available'] = '0GB'
        if 'mounted' not in data:
            data['mounted'] = False
        return data
