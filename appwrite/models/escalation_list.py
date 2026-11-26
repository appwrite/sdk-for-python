from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .escalation import Escalation


class EscalationList(AppwriteModel):
    """
    Escalations List

    Attributes
    ----------
    total : float
        Total number of escalations that matched your query.
    escalations : List[Escalation]
        List of escalations.
    """

    total: float = Field(..., alias='total')
    escalations: List[Escalation] = Field(..., alias='escalations')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'escalations' not in data:
            data['escalations'] = []
        return data
