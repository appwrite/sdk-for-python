from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .membership import Membership


class MembershipList(AppwriteModel):
    """
    Memberships List

    Attributes
    ----------
    total : float
        Total number of memberships that matched your query.
    memberships : List[Membership]
        List of memberships.
    """

    total: float = Field(..., alias='total')
    memberships: List[Membership] = Field(..., alias='memberships')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'memberships' not in data:
            data['memberships'] = []
        return data
