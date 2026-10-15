from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    api : Optional[str]
        Product API that owns this database: tablesdb, documentsdb, vectorsdb, mysql, postgresql, or mongodb.
    engine : Optional[str]
        Database engine: postgresql, mysql, or mongodb. Null until the backing reports one.
    version : str
        Database engine version.
    specification : str
        Specification identifier.
    backend : str
        Database backend provider. Possible values: edge.
    hostname : str
        Database hostname for connections.
    connectionport : Optional[float]
        Database port for connections. Derived from the engine when the backing has not reported one yet.
    connectionuser : str
        Database username for connections.
    connectionpassword : str
        Database password for connections.
    credentialgeneration : Optional[float]
        Committed generation of the primary connection credentials. Null until the rotation contract has been initialized.
    connectionstring : str
        Full database connection string (URI format).
    ssl : bool
        Whether SSL/TLS is required for client connections.
    status : str
        Database status. Possible values: provisioning, ready, inactive, paused, failed, deleted, restoring, scaling.
    containerstatus : str
        Container status for lifecycle-managed database runtimes: active, inactive, or failed (a wake was declined because the backing namespace is gone).
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
    storagestatus : str
        Storage resize status. Possible values: idle (no resize in flight), resizing (the volume is growing towards storageTargetGb).
    storagetargetgb : float
        Size in GB the volume is growing towards while storageStatus is resizing. 0 when no resize is in flight.
    storageresizestartedat : Optional[str]
        Time the in-flight storage resize started, in ISO 8601 format.
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
    networkmaxconnections : float
        Maximum concurrent client connections. This is the limit a client pool may reach; the engine&#039;s own max_connections reported by the status endpoint is a smaller backend limit the pooler multiplexes onto and does not constrain a client pool.
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
        Maximum storage size in GB for autoscaling. Defaults to 3 times the specification&#039;s storage. 0 means no limit.
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
    api: Optional[str] = Field(default=None, alias='api')
    engine: Optional[str] = Field(default=None, alias='engine')
    version: str = Field(..., alias='version')
    specification: str = Field(..., alias='specification')
    backend: str = Field(..., alias='backend')
    hostname: str = Field(..., alias='hostname')
    connectionport: Optional[float] = Field(default=None, alias='connectionPort')
    connectionuser: str = Field(..., alias='connectionUser')
    connectionpassword: str = Field(..., alias='connectionPassword')
    credentialgeneration: Optional[float] = Field(default=None, alias='credentialGeneration')
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
    storagestatus: str = Field(..., alias='storageStatus')
    storagetargetgb: float = Field(..., alias='storageTargetGb')
    storageresizestartedat: Optional[str] = Field(default=None, alias='storageResizeStartedAt')
    storageclass: str = Field(..., alias='storageClass')
    storagemaxgb: float = Field(..., alias='storageMaxGb')
    nodepool: str = Field(..., alias='nodePool')
    replicas: float = Field(..., alias='replicas')
    syncmode: str = Field(..., alias='syncMode')
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
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'version' not in data:
            data['version'] = ''
        if 'specification' not in data:
            data['specification'] = ''
        if 'backend' not in data:
            data['backend'] = ''
        if 'hostname' not in data:
            data['hostname'] = ''
        if 'connectionUser' not in data and 'connectionuser' not in data:
            data['connectionUser'] = ''
        if 'connectionPassword' not in data and 'connectionpassword' not in data:
            data['connectionPassword'] = ''
        if 'connectionString' not in data and 'connectionstring' not in data:
            data['connectionString'] = ''
        if 'ssl' not in data:
            data['ssl'] = False
        if 'status' not in data:
            data['status'] = 'provisioning'
        if 'containerStatus' not in data and 'containerstatus' not in data:
            data['containerStatus'] = ''
        if 'lifecycleState' not in data and 'lifecyclestate' not in data:
            data['lifecycleState'] = ''
        if 'idleTimeoutMinutes' not in data and 'idletimeoutminutes' not in data:
            data['idleTimeoutMinutes'] = 15
        if 'cpu' not in data:
            data['cpu'] = 500
        if 'memory' not in data:
            data['memory'] = 512
        if 'storage' not in data:
            data['storage'] = 10
        if 'storageStatus' not in data and 'storagestatus' not in data:
            data['storageStatus'] = 'idle'
        if 'storageTargetGb' not in data and 'storagetargetgb' not in data:
            data['storageTargetGb'] = 0
        if 'storageClass' not in data and 'storageclass' not in data:
            data['storageClass'] = 'ssd'
        if 'storageMaxGb' not in data and 'storagemaxgb' not in data:
            data['storageMaxGb'] = 0
        if 'nodePool' not in data and 'nodepool' not in data:
            data['nodePool'] = ''
        if 'replicas' not in data:
            data['replicas'] = 0
        if 'syncMode' not in data and 'syncmode' not in data:
            data['syncMode'] = ''
        if 'networkMaxConnections' not in data and 'networkmaxconnections' not in data:
            data['networkMaxConnections'] = 100
        if 'networkIdleTimeoutSeconds' not in data and 'networkidletimeoutseconds' not in data:
            data['networkIdleTimeoutSeconds'] = 900
        if 'networkIPAllowlist' not in data and 'networkipallowlist' not in data:
            data['networkIPAllowlist'] = []
        if 'backupEnabled' not in data and 'backupenabled' not in data:
            data['backupEnabled'] = True
        if 'pitr' not in data:
            data['pitr'] = True
        if 'pitrRetentionDays' not in data and 'pitrretentiondays' not in data:
            data['pitrRetentionDays'] = 7
        if 'storageAutoscaling' not in data and 'storageautoscaling' not in data:
            data['storageAutoscaling'] = True
        if 'storageAutoscalingThresholdPercent' not in data and 'storageautoscalingthresholdpercent' not in data:
            data['storageAutoscalingThresholdPercent'] = 85
        if 'storageAutoscalingMaxGb' not in data and 'storageautoscalingmaxgb' not in data:
            data['storageAutoscalingMaxGb'] = 0
        if 'maintenanceWindowDay' not in data and 'maintenancewindowday' not in data:
            data['maintenanceWindowDay'] = 'sun'
        if 'maintenanceWindowHourUtc' not in data and 'maintenancewindowhourutc' not in data:
            data['maintenanceWindowHourUtc'] = 3
        if 'metricsEnabled' not in data and 'metricsenabled' not in data:
            data['metricsEnabled'] = False
        if 'sqlApiEnabled' not in data and 'sqlapienabled' not in data:
            data['sqlApiEnabled'] = True
        if 'sqlApiAllowedStatements' not in data and 'sqlapiallowedstatements' not in data:
            data['sqlApiAllowedStatements'] = ['SELECT', 'INSERT', 'UPDATE', 'DELETE']
        if 'sqlApiMaxRows' not in data and 'sqlapimaxrows' not in data:
            data['sqlApiMaxRows'] = 10000
        if 'sqlApiMaxBytes' not in data and 'sqlapimaxbytes' not in data:
            data['sqlApiMaxBytes'] = 10485760
        if 'sqlApiTimeoutSeconds' not in data and 'sqlapitimeoutseconds' not in data:
            data['sqlApiTimeoutSeconds'] = 30
        if 'error' not in data:
            data['error'] = ''
        return data
