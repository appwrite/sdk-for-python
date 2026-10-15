from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class AlgoArgon2(AppwriteModel):
    """
    AlgoArgon2

    Attributes
    ----------
    type : str
        Algo type.
    memorycost : float
        Memory used to compute hash.
    timecost : float
        Amount of time consumed to compute hash
    threads : float
        Number of threads used to compute hash.
    """

    type: str = Field(..., alias='type')
    memorycost: float = Field(..., alias='memoryCost')
    timecost: float = Field(..., alias='timeCost')
    threads: float = Field(..., alias='threads')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'type' not in data:
            data['type'] = 'argon2'
        if 'memoryCost' not in data and 'memorycost' not in data:
            data['memoryCost'] = 0
        if 'timeCost' not in data and 'timecost' not in data:
            data['timeCost'] = 0
        if 'threads' not in data:
            data['threads'] = 0
        return data
