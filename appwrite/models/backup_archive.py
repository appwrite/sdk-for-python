from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class BackupArchive(AppwriteModel):
    """
    Archive

    Attributes
    ----------
    id : str
        Archive ID.
    createdat : str
        Archive creation time in ISO 8601 format.
    updatedat : str
        Archive update date in ISO 8601 format.
    policyid : str
        Archive policy ID.
    size : Optional[float]
        Archive size in bytes. Null until the size is known.
    status : str
        The status of the archive creation. Possible values: pending, processing, uploading, completed, failed, skipped.
    startedat : Optional[str]
        The backup start time. Null until the backup starts.
    migrationid : str
        Migration ID.
    services : List[Any]
        The services that are backed up by this archive.
    resources : List[Any]
        The resources that are backed up by this archive.
    resourceid : Optional[str]
        The resource ID to backup. Set only if this archive should backup a single resource.
    resourcetype : Optional[str]
        The resource type to backup. Set only if this archive should backup a single resource.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    policyid: str = Field(..., alias='policyId')
    size: Optional[float] = Field(default=None, alias='size')
    status: str = Field(..., alias='status')
    startedat: Optional[str] = Field(default=None, alias='startedAt')
    migrationid: str = Field(..., alias='migrationId')
    services: List[Any] = Field(..., alias='services')
    resources: List[Any] = Field(..., alias='resources')
    resourceid: Optional[str] = Field(default=None, alias='resourceId')
    resourcetype: Optional[str] = Field(default=None, alias='resourceType')

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
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'policyId' not in data and 'policyid' not in data:
            data['policyId'] = ''
        if 'status' not in data:
            data['status'] = ''
        if 'migrationId' not in data and 'migrationid' not in data:
            data['migrationId'] = ''
        return data
