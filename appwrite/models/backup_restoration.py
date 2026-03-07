from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class BackupRestoration(AppwriteModel):
    """
    Restoration

    Attributes
    ----------
    id : str
        Restoration ID.
    createdat : str
        Restoration creation time in ISO 8601 format.
    updatedat : str
        Restoration update date in ISO 8601 format.
    archiveid : str
        Backup archive ID.
    policyid : str
        Backup policy ID.
    status : str
        The status of the restoration. Possible values: pending, downloading, processing, completed, failed.
    startedat : str
        The backup start time.
    migrationid : str
        Migration ID.
    services : List[Any]
        The services that are backed up by this policy.
    resources : List[Any]
        The resources that are backed up by this policy.
    options : str
        Optional data in key-value object. 
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    archiveid: str = Field(..., alias='archiveId')
    policyid: str = Field(..., alias='policyId')
    status: str = Field(..., alias='status')
    startedat: str = Field(..., alias='startedAt')
    migrationid: str = Field(..., alias='migrationId')
    services: List[Any] = Field(..., alias='services')
    resources: List[Any] = Field(..., alias='resources')
    options: str = Field(..., alias='options')
