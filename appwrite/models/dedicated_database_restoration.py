from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DedicatedDatabaseRestoration(AppwriteModel):
    """
    Restoration

    Attributes
    ----------
    id : str
        Restoration ID.
    createdat : str
        Restoration creation time in ISO 8601 format.
    databaseid : str
        Database ID being restored into.
    sourcedatabaseid : Optional[str]
        Source database ID when restoring a backup into another database.
    projectid : str
        Project ID.
    backupid : Optional[str]
        Backup ID used for restoration (null for PITR).
    type : str
        Restoration type. Possible values: backup (restore from a specific backup snapshot), pitr (point-in-time recovery to a specific timestamp).
    status : str
        Restoration status. Possible values: pending (queued for processing), running (currently in progress), completed (successfully finished), failed (encountered an error).
    targettime : Optional[str]
        Target time for PITR restoration in ISO 8601 format.
    startedat : Optional[str]
        Restoration start time in ISO 8601 format.
    completedat : Optional[str]
        Restoration completion time in ISO 8601 format.
    error : str
        Error message if restoration failed.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    databaseid: str = Field(..., alias='databaseId')
    sourcedatabaseid: Optional[str] = Field(default=None, alias='sourceDatabaseId')
    projectid: str = Field(..., alias='projectId')
    backupid: Optional[str] = Field(default=None, alias='backupId')
    type: str = Field(..., alias='type')
    status: str = Field(..., alias='status')
    targettime: Optional[str] = Field(default=None, alias='targetTime')
    startedat: Optional[str] = Field(default=None, alias='startedAt')
    completedat: Optional[str] = Field(default=None, alias='completedAt')
    error: str = Field(..., alias='error')

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
        if 'databaseId' not in data and 'databaseid' not in data:
            data['databaseId'] = ''
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'type' not in data:
            data['type'] = 'backup'
        if 'status' not in data:
            data['status'] = 'pending'
        if 'error' not in data:
            data['error'] = ''
        return data
