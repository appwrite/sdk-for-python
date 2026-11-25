from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .alert import Alert


class AlertList(AppwriteModel):
    """
    Alerts List

    Attributes
    ----------
    total : float
        Total number of alerts that matched your query.
    alerts : List[Alert]
        List of alerts.
    """

    total: float = Field(..., alias='total')
    alerts: List[Alert] = Field(..., alias='alerts')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'alerts' not in data:
            data['alerts'] = []
        return data
