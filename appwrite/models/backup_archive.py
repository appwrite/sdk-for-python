from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
    size : float
        Archive size in bytes.
    status : str
        The status of the archive creation. Possible values: pending, processing, uploading, completed, failed.
    startedat : str
        The backup start time.
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
    size: float = Field(..., alias='size')
    status: str = Field(..., alias='status')
    startedat: str = Field(..., alias='startedAt')
    migrationid: str = Field(..., alias='migrationId')
    services: List[Any] = Field(..., alias='services')
    resources: List[Any] = Field(..., alias='resources')
    resourceid: Optional[str] = Field(default=None, alias='resourceId')
    resourcetype: Optional[str] = Field(default=None, alias='resourceType')
