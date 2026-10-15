from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        Underlying engine of the dedicated backing: postgresql, mysql, or mongodb. A managed product (tablesdb, documentsdb, vectorsdb) reports the engine it runs on, so its type and engine can differ. Null when the database has no dedicated backing.
    specification : Optional[str]
        Compute specification identifier of the dedicated backing, e.g. s-2vcpu-2gb. Null when the database has no dedicated backing.
    replicas : Optional[float]
        Number of secondary high availability replicas, excluding the primary. Null when backing configuration is unavailable.
    error : Optional[str]
        Error message when the dedicated backing failed. Null when the database has no dedicated backing or has not failed.
    containerstatus : Optional[str]
        Container status of the dedicated backing: active, inactive, or failed (a wake was declined because the backing namespace is gone). Null when the database has no dedicated backing or the runtime has not reported one.
    lifecyclestate : Optional[str]
        Idle-lifecycle state of the dedicated backing: active, warm, cold, or hibernated. Null when the database has no dedicated backing or the runtime has not reported one.
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
    error: Optional[str] = Field(default=None, alias='error')
    containerstatus: Optional[str] = Field(default=None, alias='containerStatus')
    lifecyclestate: Optional[str] = Field(default=None, alias='lifecycleState')
    policies: Optional[List[BackupPolicy]] = Field(default=None, alias='policies')
    archives: Optional[List[BackupArchive]] = Field(default=None, alias='archives')

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
        if 'enabled' not in data:
            data['enabled'] = True
        if 'type' not in data:
            data['type'] = 'legacy'
        return data
