from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .backup_archive import BackupArchive

class BackupArchiveList(AppwriteModel):
    """
    Backup archive list

    Attributes
    ----------
    total : float
        Total number of archives that matched your query.
    archives : List[BackupArchive]
        List of archives.
    """
    total: float = Field(..., alias='total')
    archives: List[BackupArchive] = Field(..., alias='archives')
