from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
