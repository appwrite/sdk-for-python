from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .dedicated_database_backup import DedicatedDatabaseBackup


class DedicatedDatabaseBackupList(AppwriteModel):
    """
    BackupList

    Attributes
    ----------
    total : float
        Total number of backups.
    backups : List[DedicatedDatabaseBackup]
        List of backups.
    """

    total: float = Field(..., alias='total')
    backups: List[DedicatedDatabaseBackup] = Field(..., alias='backups')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
