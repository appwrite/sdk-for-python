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
        Dedicated database lifecycle status. Null when the database has no valid dedicated backing.
    engine : Optional[str]
        Underlying engine of the dedicated backing: postgresql, mysql, mariadb, or mongodb. A managed product (tablesdb, documentsdb, vectorsdb) reports the engine it runs on, so its type and engine can differ. Null when the database has no dedicated backing.
    specification : Optional[str]
        Compute specification identifier of the dedicated backing, e.g. s-2vcpu-2gb. Null when the database has no dedicated backing.
    replicas : Optional[float]
        Number of secondary high availability replicas, excluding the primary. Null when backing configuration is unavailable.
    policies : Optional[List[BackupPolicy]]
        Database backup policies.
    archives : Optional[List[BackupArchive]]
        Database backup archives.
    """
    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    enabled: bool = Field(..., alias='enabled')
    type: DatabaseType = Field(..., alias='type')
    status: Optional[DatabaseStatus] = Field(default=None, alias='status')
    engine: Optional[str] = Field(default=None, alias='engine')
    specification: Optional[str] = Field(default=None, alias='specification')
    replicas: Optional[float] = Field(default=None, alias='replicas')
    policies: Optional[List[BackupPolicy]] = Field(default=None, alias='policies')
    archives: Optional[List[BackupArchive]] = Field(default=None, alias='archives')
