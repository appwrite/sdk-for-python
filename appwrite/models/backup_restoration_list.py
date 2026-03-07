from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .backup_restoration import BackupRestoration

class BackupRestorationList(AppwriteModel):
    """
    Backup restoration list

    Attributes
    ----------
    total : float
        Total number of restorations that matched your query.
    restorations : List[BackupRestoration]
        List of restorations.
    """
    total: float = Field(..., alias='total')
    restorations: List[BackupRestoration] = Field(..., alias='restorations')
