from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DedicatedDatabase(AppwriteModel):
    """
    DedicatedDatabase

    Attributes
    ----------
    id : str
        Dedicated database ID.
    createdat : str
        Database creation time in ISO 8601 format.
    updatedat : str
        Database update date in ISO 8601 format.
    projectid : str
        Project ID that owns this database.
    name : str
        Database display name.
    api : str
        Product API that owns this database: tablesdb, documentsdb, vectorsdb, mysql, postgresql, or mongodb.
    engine : str
        Database engine: postgresql, mysql, mariadb, or mongodb.
    version : str
        Database engine version.
    specification : str
        Specification identifier.
    backend : str
        Database backend provider. Possible values: prisma, edge.
    hostname : str
        Database hostname for connections.
    connectionport : float
        Database port for connections.
    connectionuser : str
        Database username for connections.
    connectionpassword : str
        Database password for connections.
    connectionstring : str
        Full database connection string (URI format).
    ssl : bool
        Whether SSL/TLS is required for client connections.
    status : str
        Database status. Possible values: provisioning, ready, inactive, paused, failed, deleted, restoring, scaling.
    containerstatus : str
        Container status for lifecycle-managed database runtimes: active or inactive.
    lastaccessedat : Optional[str]
        Last activity timestamp in ISO 8601 format.
    idleuntil : Optional[str]
        Display-only timestamp when the database is expected to be considered idle (ISO 8601 format). Derived from last activity; lifecycle transitions are driven by lifecycleState.
    lifecyclestate : str
        Idle-lifecycle state of the database. Possible values: active, warm, cold, hibernated.
    idletimeoutminutes : float
        Minutes of inactivity before container scales to zero.
    cpu : float
        CPU allocated in millicores.
    memory : float
        Memory allocated in MB.
    storage : float
        Storage allocated in GB.
    storageclass : str
        Storage class. Currently always &#039;ssd&#039;; DigitalOcean exposes a single block-storage class.
    storagemaxgb : float
        Maximum storage allowed in GB. 0 means use system default.
    nodepool : str
        Kubernetes node pool where the database is scheduled.
    replicas : float
        Number of high availability replicas. High availability is enabled when greater than 0.
    syncmode : str
        Replication sync mode: async, sync, or quorum.
    crossregionreplicas : float
        Number of cross-region replicas. Cross-region availability is enabled when greater than 0.
    networkmaxconnections : float
        Maximum concurrent connections.
    networkidletimeoutseconds : float
        Connection idle timeout in seconds.
    networkipallowlist : List[Any]
        IP addresses/CIDR ranges allowed to connect.
    backupenabled : bool
        Whether automatic backups are enabled.
    pitr : bool
        Whether point-in-time recovery is enabled.
    pitrretentiondays : float
        Number of days to retain PITR data.
    storageautoscaling : bool
        Whether automatic storage expansion is enabled.
    storageautoscalingthresholdpercent : float
        Storage usage percentage that triggers automatic expansion.
    storageautoscalingmaxgb : float
        Maximum storage size in GB for autoscaling. 0 means no limit.
    maintenancewindowday : str
        Day of the week for the maintenance window. Possible values: sun, mon, tue, wed, thu, fri, sat.
    maintenancewindowhourutc : float
        Hour in UTC (0-23) when the maintenance window starts.
    metricsenabled : bool
        Whether metrics collection is enabled.
    sqlapienabled : bool
        Whether the SQL API sidecar is enabled for this database.
    sqlapiallowedstatements : List[Any]
        Statement types accepted by the SQL API. Defaults to read/write DML only; DDL/DCL types (CREATE, ALTER, DROP, TRUNCATE, GRANT, REVOKE) are opt-in per database. Allowed values: SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, TRUNCATE, GRANT, REVOKE.
    sqlapimaxrows : float
        Maximum rows returned per SQL API execution. Results larger than this are truncated.
    sqlapimaxbytes : float
        Maximum serialised SQL API result payload in bytes. Results larger than this are truncated.
    sqlapitimeoutseconds : float
        Maximum server-side SQL API execution time in seconds before the query is cancelled.
    error : str
        Error message if status is failed.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    projectid: str = Field(..., alias='projectId')
    name: str = Field(..., alias='name')
    api: str = Field(..., alias='api')
    engine: str = Field(..., alias='engine')
    version: str = Field(..., alias='version')
    specification: str = Field(..., alias='specification')
    backend: str = Field(..., alias='backend')
    hostname: str = Field(..., alias='hostname')
    connectionport: float = Field(..., alias='connectionPort')
    connectionuser: str = Field(..., alias='connectionUser')
    connectionpassword: str = Field(..., alias='connectionPassword')
    connectionstring: str = Field(..., alias='connectionString')
    ssl: bool = Field(..., alias='ssl')
    status: str = Field(..., alias='status')
    containerstatus: str = Field(..., alias='containerStatus')
    lastaccessedat: Optional[str] = Field(default=None, alias='lastAccessedAt')
    idleuntil: Optional[str] = Field(default=None, alias='idleUntil')
    lifecyclestate: str = Field(..., alias='lifecycleState')
    idletimeoutminutes: float = Field(..., alias='idleTimeoutMinutes')
    cpu: float = Field(..., alias='cpu')
    memory: float = Field(..., alias='memory')
    storage: float = Field(..., alias='storage')
    storageclass: str = Field(..., alias='storageClass')
    storagemaxgb: float = Field(..., alias='storageMaxGb')
    nodepool: str = Field(..., alias='nodePool')
    replicas: float = Field(..., alias='replicas')
    syncmode: str = Field(..., alias='syncMode')
    crossregionreplicas: float = Field(..., alias='crossRegionReplicas')
    networkmaxconnections: float = Field(..., alias='networkMaxConnections')
    networkidletimeoutseconds: float = Field(..., alias='networkIdleTimeoutSeconds')
    networkipallowlist: List[Any] = Field(..., alias='networkIPAllowlist')
    backupenabled: bool = Field(..., alias='backupEnabled')
    pitr: bool = Field(..., alias='pitr')
    pitrretentiondays: float = Field(..., alias='pitrRetentionDays')
    storageautoscaling: bool = Field(..., alias='storageAutoscaling')
    storageautoscalingthresholdpercent: float = Field(..., alias='storageAutoscalingThresholdPercent')
    storageautoscalingmaxgb: float = Field(..., alias='storageAutoscalingMaxGb')
    maintenancewindowday: str = Field(..., alias='maintenanceWindowDay')
    maintenancewindowhourutc: float = Field(..., alias='maintenanceWindowHourUtc')
    metricsenabled: bool = Field(..., alias='metricsEnabled')
    sqlapienabled: bool = Field(..., alias='sqlApiEnabled')
    sqlapiallowedstatements: List[Any] = Field(..., alias='sqlApiAllowedStatements')
    sqlapimaxrows: float = Field(..., alias='sqlApiMaxRows')
    sqlapimaxbytes: float = Field(..., alias='sqlApiMaxBytes')
    sqlapitimeoutseconds: float = Field(..., alias='sqlApiTimeoutSeconds')
    error: str = Field(..., alias='error')
