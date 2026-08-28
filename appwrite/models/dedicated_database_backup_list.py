from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
