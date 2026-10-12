from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    startedat : Optional[str]
        The restoration start time. Null until the restoration starts.
    migrationid : str
        Migration ID.
    services : List[Any]
        The services that are backed up by this policy.
    resources : List[Any]
        The resources that are backed up by this policy.
    options : Dict[str, Any]
        Restoration options as a key-value object.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    archiveid: str = Field(..., alias='archiveId')
    policyid: str = Field(..., alias='policyId')
    status: str = Field(..., alias='status')
    startedat: Optional[str] = Field(default=None, alias='startedAt')
    migrationid: str = Field(..., alias='migrationId')
    services: List[Any] = Field(..., alias='services')
    resources: List[Any] = Field(..., alias='resources')
    options: Dict[str, Any] = Field(..., alias='options')

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
        if 'archiveId' not in data and 'archiveid' not in data:
            data['archiveId'] = ''
        if 'policyId' not in data and 'policyid' not in data:
            data['policyId'] = ''
        if 'status' not in data:
            data['status'] = ''
        if 'migrationId' not in data and 'migrationid' not in data:
            data['migrationId'] = ''
        if 'options' not in data:
            data['options'] = []
        return data
