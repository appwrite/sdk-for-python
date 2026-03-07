from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
    enabled: bool = Field(..., alias='enabled')
