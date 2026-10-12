from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class BackupPolicy(AppwriteModel):
    """
    backup

    Attributes
    ----------
    id : str
        Backup policy ID.
    name : str
        Backup policy name.
    createdat : str
        Policy creation date in ISO 8601 format.
    updatedat : str
        Policy update date in ISO 8601 format.
    services : List[Any]
        The services that are backed up by this policy.
    resources : List[Any]
        The resources that are backed up by this policy.
    resourceid : Optional[str]
        The resource ID to backup. Set only if this policy should backup a single resource.
    resourcetype : Optional[str]
        The resource type to backup. Set only if this policy should backup a single resource.
    retention : float
        How many days to keep the backup before it will be automatically deleted.
    schedule : str
        Policy backup schedule in CRON format.
    type : str
        Backup type. Possible values: full (complete database snapshot), incremental (changes since last backup).
    enabled : bool
        Is this policy enabled.
    """

    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    services: List[Any] = Field(..., alias='services')
    resources: List[Any] = Field(..., alias='resources')
    resourceid: Optional[str] = Field(default=None, alias='resourceId')
    resourcetype: Optional[str] = Field(default=None, alias='resourceType')
    retention: float = Field(..., alias='retention')
    schedule: str = Field(..., alias='schedule')
    type: str = Field(..., alias='type')
    enabled: bool = Field(..., alias='enabled')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'name' not in data:
            data['name'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'retention' not in data:
            data['retention'] = 1
        if 'schedule' not in data:
            data['schedule'] = '0 * * * *'
        if 'type' not in data:
            data['type'] = 'full'
        if 'enabled' not in data:
            data['enabled'] = False
        return data
