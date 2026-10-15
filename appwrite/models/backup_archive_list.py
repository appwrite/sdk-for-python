from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'archives' not in data:
            data['archives'] = []
        return data
