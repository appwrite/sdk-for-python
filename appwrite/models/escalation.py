from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .escalation_step import EscalationStep


class Escalation(AppwriteModel):
    """
    Escalation

    Attributes
    ----------
    id : str
        Escalation ID.
    createdat : str
        Escalation creation date in ISO 8601 format.
    updatedat : str
        Escalation update date in ISO 8601 format.
    name : str
        Escalation name.
    steps : List[EscalationStep]
        Who is notified of a firing alert, in order, until a member acknowledges it.
    repeat : float
        How many more times the steps run from the first, a monitor&#039;s cooldown after the last step, while nobody has acknowledged the alert.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    steps: List[EscalationStep] = Field(..., alias='steps')
    repeat: float = Field(..., alias='repeat')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'steps' not in data:
            data['steps'] = []
        if 'repeat' not in data:
            data['repeat'] = 0
        return data
