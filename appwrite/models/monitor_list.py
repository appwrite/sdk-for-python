from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .monitor import Monitor


class MonitorList(AppwriteModel):
    """
    Monitors List

    Attributes
    ----------
    total : float
        Total number of monitors that matched your query.
    monitors : List[Monitor]
        List of monitors.
    """

    total: float = Field(..., alias='total')
    monitors: List[Monitor] = Field(..., alias='monitors')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'monitors' not in data:
            data['monitors'] = []
        return data
