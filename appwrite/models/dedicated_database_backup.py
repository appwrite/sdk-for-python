from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
