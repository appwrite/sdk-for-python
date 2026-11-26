from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class EscalationStep(AppwriteModel):
    """
    Escalation Step

    Attributes
    ----------
    delay : float
        Seconds to wait before notifying this step: after the alert fires for the first step, after the previous step for the others.
    roles : List[Any]
        Organization roles whose confirmed members this step notifies.
    userids : List[Any]
        IDs of the organization&#039;s members this step notifies, whatever their role.
    """

    delay: float = Field(..., alias='delay')
    roles: List[Any] = Field(..., alias='roles')
    userids: List[Any] = Field(..., alias='userIds')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'delay' not in data:
            data['delay'] = 0
        if 'roles' not in data:
            data['roles'] = []
        if 'userIds' not in data and 'userids' not in data:
            data['userIds'] = []
        return data
