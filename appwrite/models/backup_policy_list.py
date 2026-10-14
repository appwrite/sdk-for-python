from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .backup_policy import BackupPolicy


class BackupPolicyList(AppwriteModel):
    """
    Backup policy list

    Attributes
    ----------
    total : float
        Total number of policies that matched your query.
    policies : List[BackupPolicy]
        List of policies.
    """

    total: float = Field(..., alias='total')
    policies: List[BackupPolicy] = Field(..., alias='policies')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'policies' not in data:
            data['policies'] = []
        return data
