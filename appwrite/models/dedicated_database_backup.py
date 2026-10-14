from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DedicatedDatabaseBackup(AppwriteModel):
    """
    Backup

    Attributes
    ----------
    id : str
        Backup ID.
    createdat : str
        Backup creation time in ISO 8601 format.
    databaseid : str
        Database ID this backup belongs to.
    projectid : str
        Project ID.
    policyid : str
        Backup policy ID when the backup was created by a schedule.
    trigger : str
        Backup trigger. Possible values: manual, schedule.
    type : str
        Backup type. Possible values: full (complete database snapshot), incremental (changes since last backup), wal (write-ahead log continuous archival).
    requestedtype : str
        Backup type that was requested. Differs from `type` when the backend could not run the requested type and took a different one instead, in which case `fallbackReason` explains why. Empty for backups taken before the requested type was recorded.
    fallbackreason : str
        Why the backend ran a different backup type than the one requested. Empty when the backup ran as requested.
    status : str
        Backup status. Possible values: pending (queued for processing), running (currently in progress), completed (successfully finished), failed (encountered an error), verified (integrity check passed).
    sizebytes : float
        Backup size in bytes.
    startedat : Optional[str]
        Backup start time in ISO 8601 format.
    completedat : Optional[str]
        Backup completion time in ISO 8601 format.
    verifiedat : Optional[str]
        Backup verification time in ISO 8601 format.
    expiresat : Optional[str]
        Backup expiration time in ISO 8601 format.
    logposition : Optional[str]
        Transaction-log position the backup anchors at, in the engine&#039;s own notation: PostgreSQL `{walSegment}|{lsn}`, MySQL and MariaDB `{binlogFile}|{offset}`, MongoDB `{seconds}|{increment}`. Empty when the backup recorded no position, which is the case for backup types that carry none.
    error : str
        Error message if backup failed.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    databaseid: str = Field(..., alias='databaseId')
    projectid: str = Field(..., alias='projectId')
    policyid: str = Field(..., alias='policyId')
    trigger: str = Field(..., alias='trigger')
    type: str = Field(..., alias='type')
    requestedtype: str = Field(..., alias='requestedType')
    fallbackreason: str = Field(..., alias='fallbackReason')
    status: str = Field(..., alias='status')
    sizebytes: float = Field(..., alias='sizeBytes')
    startedat: Optional[str] = Field(default=None, alias='startedAt')
    completedat: Optional[str] = Field(default=None, alias='completedAt')
    verifiedat: Optional[str] = Field(default=None, alias='verifiedAt')
    expiresat: Optional[str] = Field(default=None, alias='expiresAt')
    logposition: Optional[str] = Field(default=None, alias='logPosition')
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
        if 'policyId' not in data and 'policyid' not in data:
            data['policyId'] = ''
        if 'trigger' not in data:
            data['trigger'] = 'manual'
        if 'type' not in data:
            data['type'] = 'full'
        if 'requestedType' not in data and 'requestedtype' not in data:
            data['requestedType'] = ''
        if 'fallbackReason' not in data and 'fallbackreason' not in data:
            data['fallbackReason'] = ''
        if 'status' not in data:
            data['status'] = 'pending'
        if 'sizeBytes' not in data and 'sizebytes' not in data:
            data['sizeBytes'] = 0
        if 'error' not in data:
            data['error'] = ''
        return data
