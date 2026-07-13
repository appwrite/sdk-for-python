from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BillingPlanDedicatedDatabaseLimits(AppwriteModel):
    """
    dedicatedDatabaseLimits

    Attributes
    ----------
    mincpu : Optional[float]
        Minimum CPU allocation in millicores.
    maxcpu : Optional[float]
        Maximum CPU allocation in millicores.
    minmemorymb : Optional[float]
        Minimum memory allocation in megabytes.
    maxmemorymb : Optional[float]
        Maximum memory allocation in megabytes.
    minstoragegb : Optional[float]
        Minimum storage allocation in gigabytes.
    maxstoragegb : Optional[float]
        Maximum storage allocation in gigabytes.
    maxreplicas : Optional[float]
        Maximum number of high-availability replicas per dedicated database.
    maxconnections : Optional[float]
        Maximum number of client connections.
    maxipallowlistsize : Optional[float]
        Maximum number of entries allowed in the IP allowlist.
    maxextensions : Optional[float]
        Maximum number of database extensions that can be enabled.
    maxbackupretentiondays : Optional[float]
        Maximum number of days a backup can be retained.
    maxpitrretentiondays : Optional[float]
        Maximum number of days of point-in-time recovery data that can be retained.
    maxsqlapimaxrows : Optional[float]
        Maximum number of rows a single SQL API query can return.
    maxsqlapimaxbytes : Optional[float]
        Maximum response size in bytes for a single SQL API query.
    maxsqlapitimeoutseconds : Optional[float]
        Maximum execution time in seconds for a single SQL API query.
    maxsqlapiallowedstatements : Optional[float]
        Maximum number of SQL statement types that can be permitted through the SQL API.
    allowedsqlstatements : Optional[List[Any]]
        SQL statement types permitted through the SQL API.
    allowedstorageclasses : Optional[List[Any]]
        Storage classes available for dedicated databases.
    allowedsyncmodes : Optional[List[Any]]
        Replica synchronization modes available for dedicated databases.
    """
    mincpu: Optional[float] = Field(default=None, alias='minCpu')
    maxcpu: Optional[float] = Field(default=None, alias='maxCpu')
    minmemorymb: Optional[float] = Field(default=None, alias='minMemoryMb')
    maxmemorymb: Optional[float] = Field(default=None, alias='maxMemoryMb')
    minstoragegb: Optional[float] = Field(default=None, alias='minStorageGb')
    maxstoragegb: Optional[float] = Field(default=None, alias='maxStorageGb')
    maxreplicas: Optional[float] = Field(default=None, alias='maxReplicas')
    maxconnections: Optional[float] = Field(default=None, alias='maxConnections')
    maxipallowlistsize: Optional[float] = Field(default=None, alias='maxIpAllowlistSize')
    maxextensions: Optional[float] = Field(default=None, alias='maxExtensions')
    maxbackupretentiondays: Optional[float] = Field(default=None, alias='maxBackupRetentionDays')
    maxpitrretentiondays: Optional[float] = Field(default=None, alias='maxPitrRetentionDays')
    maxsqlapimaxrows: Optional[float] = Field(default=None, alias='maxSqlApiMaxRows')
    maxsqlapimaxbytes: Optional[float] = Field(default=None, alias='maxSqlApiMaxBytes')
    maxsqlapitimeoutseconds: Optional[float] = Field(default=None, alias='maxSqlApiTimeoutSeconds')
    maxsqlapiallowedstatements: Optional[float] = Field(default=None, alias='maxSqlApiAllowedStatements')
    allowedsqlstatements: Optional[List[Any]] = Field(default=None, alias='allowedSqlStatements')
    allowedstorageclasses: Optional[List[Any]] = Field(default=None, alias='allowedStorageClasses')
    allowedsyncmodes: Optional[List[Any]] = Field(default=None, alias='allowedSyncModes')
