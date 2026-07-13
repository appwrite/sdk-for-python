from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.database_type import DatabaseType
from ..enums.database_status import DatabaseStatus
from .backup_policy import BackupPolicy
from .backup_archive import BackupArchive

class Database(AppwriteModel):
    """
    Database

    Attributes
    ----------
    id : str
        Database ID.
    name : str
        Database name.
    createdat : str
        Database creation date in ISO 8601 format.
    updatedat : str
        Database update date in ISO 8601 format.
    enabled : bool
        If database is enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the database is inaccessible to users, but remains accessible to Server SDKs using API keys.
    type : DatabaseType
        Database type.
    status : Optional[DatabaseStatus]
        Database status. Possible values: `provisioning`, `ready` or `failed`
    policies : List[BackupPolicy]
        Database backup policies.
    archives : List[BackupArchive]
        Database backup archives.
    """
    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    enabled: bool = Field(..., alias='enabled')
    type: DatabaseType = Field(..., alias='type')
    status: Optional[DatabaseStatus] = Field(default=None, alias='status')
    policies: List[BackupPolicy] = Field(..., alias='policies')
    archives: List[BackupArchive] = Field(..., alias='archives')
