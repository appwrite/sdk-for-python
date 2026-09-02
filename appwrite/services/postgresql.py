from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.dedicated_database_list import DedicatedDatabaseList
from ..models.dedicated_database import DedicatedDatabase
from ..models.dedicated_database_specification_list import DedicatedDatabaseSpecificationList
from ..models.dedicated_database_backup_list import DedicatedDatabaseBackupList
from ..models.dedicated_database_backup import DedicatedDatabaseBackup
from ..models.backup_policy_list import BackupPolicyList
from ..models.backup_policy import BackupPolicy
from ..models.dedicated_database_backup_storage import DedicatedDatabaseBackupStorage
from ..models.dedicated_database_branch_list import DedicatedDatabaseBranchList
from ..models.dedicated_database_operation import DedicatedDatabaseOperation
from ..models.dedicated_database_execution import DedicatedDatabaseExecution
from ..models.dedicated_database_extensions import DedicatedDatabaseExtensions
from ..models.dedicated_database_operation_list import DedicatedDatabaseOperationList
from ..models.dedicated_database_pitr_windows import DedicatedDatabasePITRWindows
from ..models.dedicated_database_pooler import DedicatedDatabasePooler
from ..models.dedicated_database_replicas import DedicatedDatabaseReplicas
from ..models.dedicated_database_restoration_list import DedicatedDatabaseRestorationList
from ..models.dedicated_database_restoration import DedicatedDatabaseRestoration
from ..models.database_status import DatabaseStatus


class Postgresql(Service):

    def __init__(self, client) -> None:
        super(Postgresql, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
    ) -> DedicatedDatabaseList:
        """
        List all dedicated databases. Results support pagination.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings.
        Returns
        -------
        DedicatedDatabaseList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseList)

    def create(
        self,
        database_id: str,
        name: str,
        version: Optional[str] = None,
        specification: Optional[str] = None,
        replicas: Optional[float] = None,
        sync_mode: Optional[str] = None,
        network_idle_timeout_seconds: Optional[float] = None,
        network_ip_allowlist: Optional[List[str]] = None,
        idle_timeout_minutes: Optional[float] = None,
        pitr: Optional[bool] = None,
        pitr_retention_days: Optional[float] = None,
        storage_autoscaling: Optional[bool] = None,
        storage_autoscaling_threshold_percent: Optional[float] = None,
        storage_autoscaling_max_gb: Optional[float] = None,
    ) -> DedicatedDatabase:
        """
        Create a new dedicated database with the chosen engine and configuration. Status will be 'provisioning' until the database is ready.

        Parameters
        ----------
        database_id : str
            Database ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Database display name. Max length: 128 chars.
        version : Optional[str]
            Database engine version. Defaults to latest for selected engine.
        specification : Optional[str]
            Specification identifier. Drives the allocated CPU, memory, storage, storage class, and connection ceiling.
        replicas : Optional[float]
            Number of high availability replicas (0-5). High availability is enabled when greater than 0.
        sync_mode : Optional[str]
            Replication sync mode preference. Allowed values: async, sync, quorum.
        network_idle_timeout_seconds : Optional[float]
            Connection idle timeout in seconds.
        network_ip_allowlist : Optional[List[str]]
            IP addresses/CIDR ranges allowed to connect.
        idle_timeout_minutes : Optional[float]
            Minutes of inactivity before container scales to zero.
        pitr : Optional[bool]
            Enable point-in-time recovery (PITR). Continuously archives changes so the database can be restored to any moment within the retention window.
        pitr_retention_days : Optional[float]
            Number of days to retain PITR data.
        storage_autoscaling : Optional[bool]
            Enable automatic storage expansion when usage exceeds threshold.
        storage_autoscaling_threshold_percent : Optional[float]
            Storage usage percentage (50-95) that triggers automatic expansion.
        storage_autoscaling_max_gb : Optional[float]
            Maximum storage size in GB for autoscaling. 0 means no limit.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_params['databaseId'] = self._normalize_value(database_id)
        api_params['name'] = self._normalize_value(name)
        if version is not None:
            api_params['version'] = self._normalize_value(version)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if replicas is not None:
            api_params['replicas'] = self._normalize_value(replicas)
        if sync_mode is not None:
            api_params['syncMode'] = self._normalize_value(sync_mode)
        if network_idle_timeout_seconds is not None:
            api_params['networkIdleTimeoutSeconds'] = self._normalize_value(network_idle_timeout_seconds)
        if network_ip_allowlist is not None:
            api_params['networkIPAllowlist'] = self._normalize_value(network_ip_allowlist)
        if idle_timeout_minutes is not None:
            api_params['idleTimeoutMinutes'] = self._normalize_value(idle_timeout_minutes)
        if pitr is not None:
            api_params['pitr'] = self._normalize_value(pitr)
        if pitr_retention_days is not None:
            api_params['pitrRetentionDays'] = self._normalize_value(pitr_retention_days)
        if storage_autoscaling is not None:
            api_params['storageAutoscaling'] = self._normalize_value(storage_autoscaling)
        if storage_autoscaling_threshold_percent is not None:
            api_params['storageAutoscalingThresholdPercent'] = self._normalize_value(
                storage_autoscaling_threshold_percent,
            )
        if storage_autoscaling_max_gb is not None:
            api_params['storageAutoscalingMaxGb'] = self._normalize_value(storage_autoscaling_max_gb)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def list_specifications(
        self,
    ) -> DedicatedDatabaseSpecificationList:
        """
        List the dedicated database specifications available on the current plan. Each specification reports its resource limits, pricing, and whether it is enabled for the organization.
        Returns
        -------
        DedicatedDatabaseSpecificationList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/specifications'
        api_params = {}

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseSpecificationList)

    def get(
        self,
        database_id: str,
    ) -> DedicatedDatabase:
        """
        Get a dedicated database by its unique ID. Returns the database configuration and current status.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def update(
        self,
        database_id: str,
        name: Optional[str] = None,
        status: Optional[str] = None,
        specification: Optional[str] = None,
        replicas: Optional[float] = None,
        sync_mode: Optional[str] = None,
        network_idle_timeout_seconds: Optional[float] = None,
        network_ip_allowlist: Optional[List[str]] = None,
        idle_timeout_minutes: Optional[float] = None,
        pitr: Optional[bool] = None,
        pitr_retention_days: Optional[float] = None,
        storage_autoscaling: Optional[bool] = None,
        storage_autoscaling_threshold_percent: Optional[float] = None,
        storage_autoscaling_max_gb: Optional[float] = None,
        metrics_trace_sample_rate: Optional[float] = None,
        metrics_slow_query_log_threshold_ms: Optional[float] = None,
        sql_api_enabled: Optional[bool] = None,
        sql_api_allowed_statements: Optional[List[str]] = None,
        sql_api_max_rows: Optional[float] = None,
        sql_api_max_bytes: Optional[float] = None,
        sql_api_timeout_seconds: Optional[float] = None,
    ) -> DedicatedDatabase:
        """
        Update a dedicated database configuration. All changes are applied with zero downtime. Specification changes (cpu, memory, storage) are handled via rolling cutover. Storage expansion is done online. All other settings are applied in-place.

        Parameters
        ----------
        database_id : str
            Database ID.
        name : Optional[str]
            Database display name.
        status : Optional[str]
            Database status. Allowed values: ready, paused, inactive. Set to "paused" to pause, "ready" to resume (also recovers a failed database whose infrastructure is healthy), or "inactive" to spin down a shared-pool database.
        specification : Optional[str]
            Specification. Changes cpu, memory, storage, connection ceiling, and node pool based on specification config. Resource changes are applied via rolling cutover with zero downtime.
        replicas : Optional[float]
            Number of high availability replicas (0-5). High availability is enabled when greater than 0.
        sync_mode : Optional[str]
            Replication sync mode preference. Allowed values: async, sync, quorum.
        network_idle_timeout_seconds : Optional[float]
            Connection idle timeout in seconds (60-86400).
        network_ip_allowlist : Optional[List[str]]
            IP addresses/CIDR ranges allowed to connect.
        idle_timeout_minutes : Optional[float]
            Minutes before container scales to zero.
        pitr : Optional[bool]
            Enable or disable point-in-time recovery (PITR).
        pitr_retention_days : Optional[float]
            Days to retain PITR data.
        storage_autoscaling : Optional[bool]
            Enable automatic storage expansion when usage exceeds threshold.
        storage_autoscaling_threshold_percent : Optional[float]
            Storage usage percentage (50-95) that triggers automatic expansion.
        storage_autoscaling_max_gb : Optional[float]
            Maximum storage size in GB for autoscaling. 0 means no limit.
        metrics_trace_sample_rate : Optional[float]
            Fraction of queries to trace (0.0–1.0). Forwarded to the sidecar.
        metrics_slow_query_log_threshold_ms : Optional[float]
            Threshold in ms above which queries are logged as slow. Forwarded to the sidecar.
        sql_api_enabled : Optional[bool]
            Enable the SQL API sidecar for this database.
        sql_api_allowed_statements : Optional[List[str]]
            Statement types the SQL API accepts. Allowed values: SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, TRUNCATE, GRANT, REVOKE.
        sql_api_max_rows : Optional[float]
            Maximum rows returned per SQL API execution (1-1000000).
        sql_api_max_bytes : Optional[float]
            Maximum serialised SQL API result payload in bytes (1024-104857600).
        sql_api_timeout_seconds : Optional[float]
            Per-call SQL API execution timeout in seconds (1-300).
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if replicas is not None:
            api_params['replicas'] = self._normalize_value(replicas)
        if sync_mode is not None:
            api_params['syncMode'] = self._normalize_value(sync_mode)
        if network_idle_timeout_seconds is not None:
            api_params['networkIdleTimeoutSeconds'] = self._normalize_value(network_idle_timeout_seconds)
        if network_ip_allowlist is not None:
            api_params['networkIPAllowlist'] = self._normalize_value(network_ip_allowlist)
        if idle_timeout_minutes is not None:
            api_params['idleTimeoutMinutes'] = self._normalize_value(idle_timeout_minutes)
        if pitr is not None:
            api_params['pitr'] = self._normalize_value(pitr)
        if pitr_retention_days is not None:
            api_params['pitrRetentionDays'] = self._normalize_value(pitr_retention_days)
        if storage_autoscaling is not None:
            api_params['storageAutoscaling'] = self._normalize_value(storage_autoscaling)
        if storage_autoscaling_threshold_percent is not None:
            api_params['storageAutoscalingThresholdPercent'] = self._normalize_value(
                storage_autoscaling_threshold_percent,
            )
        if storage_autoscaling_max_gb is not None:
            api_params['storageAutoscalingMaxGb'] = self._normalize_value(storage_autoscaling_max_gb)
        if metrics_trace_sample_rate is not None:
            api_params['metricsTraceSampleRate'] = self._normalize_value(metrics_trace_sample_rate)
        if metrics_slow_query_log_threshold_ms is not None:
            api_params['metricsSlowQueryLogThresholdMs'] = self._normalize_value(metrics_slow_query_log_threshold_ms)
        if sql_api_enabled is not None:
            api_params['sqlApiEnabled'] = self._normalize_value(sql_api_enabled)
        if sql_api_allowed_statements is not None:
            api_params['sqlApiAllowedStatements'] = self._normalize_value(sql_api_allowed_statements)
        if sql_api_max_rows is not None:
            api_params['sqlApiMaxRows'] = self._normalize_value(sql_api_max_rows)
        if sql_api_max_bytes is not None:
            api_params['sqlApiMaxBytes'] = self._normalize_value(sql_api_max_bytes)
        if sql_api_timeout_seconds is not None:
            api_params['sqlApiTimeoutSeconds'] = self._normalize_value(sql_api_timeout_seconds)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def delete(
        self,
        database_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a dedicated database. This action is irreversible. The database status will be set to 'deleting' and all resources will be cleaned up. Deletion is allowed from any state, and repeating the call re-dispatches the cleanup.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def list_backups(
        self,
        database_id: str,
        queries: Optional[List[str]] = None,
    ) -> DedicatedDatabaseBackupList:
        """
        List all backups for a dedicated database. Results can be filtered by status and type.

        Parameters
        ----------
        database_id : str
            Database ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: status, type, databaseId
        Returns
        -------
        DedicatedDatabaseBackupList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseBackupList)

    def create_backup(
        self,
        database_id: str,
        type: Optional[str] = None,
    ) -> DedicatedDatabaseBackup:
        """
        Create a manual backup of a dedicated database. The backup will be created asynchronously and its status can be checked via the get backup endpoint.

        Parameters
        ----------
        database_id : str
            Database ID.
        type : Optional[str]
            Backup type: full or incremental.
        Returns
        -------
        DedicatedDatabaseBackup
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseBackup)

    def list_backup_policies(
        self,
        database_id: str,
        queries: Optional[List[str]] = None,
    ) -> BackupPolicyList:
        """
        List scheduled backup policies for a dedicated database.

        Parameters
        ----------
        database_id : str
            Database ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK.
        Returns
        -------
        BackupPolicyList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/policies'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=BackupPolicyList)

    def create_backup_policy(
        self,
        database_id: str,
        policy_id: str,
        name: str,
        schedule: str,
        retention: float,
        type: Optional[str] = None,
        enabled: Optional[bool] = None,
    ) -> BackupPolicy:
        """
        Create a scheduled backup policy for a dedicated database.

        Parameters
        ----------
        database_id : str
            Database ID.
        policy_id : str
            Policy ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Policy name. Max length: 128 chars.
        schedule : str
            Schedule CRON syntax.
        retention : float
            Days to keep backups before deletion.
        type : Optional[str]
            Backup type: full or incremental.
        enabled : Optional[bool]
            Is policy enabled? When disabled, no backups will be taken.
        Returns
        -------
        BackupPolicy
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/policies'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if schedule is None:
            raise AppwriteException('Missing required parameter: "schedule"')
        if retention is None:
            raise AppwriteException('Missing required parameter: "retention"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['policyId'] = self._normalize_value(policy_id)
        api_params['name'] = self._normalize_value(name)
        api_params['schedule'] = self._normalize_value(schedule)
        api_params['retention'] = self._normalize_value(retention)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=BackupPolicy)

    def get_backup_policy(
        self,
        database_id: str,
        policy_id: str,
    ) -> BackupPolicy:
        """
        Get a scheduled backup policy for a dedicated database.

        Parameters
        ----------
        database_id : str
            Database ID.
        policy_id : str
            Policy ID.
        Returns
        -------
        BackupPolicy
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/policies/{policyId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{policyId}', str(self._normalize_value(policy_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=BackupPolicy)

    def update_backup_policy(
        self,
        database_id: str,
        policy_id: str,
        name: Optional[str] = None,
        schedule: Optional[str] = None,
        retention: Optional[float] = None,
        enabled: Optional[bool] = None,
    ) -> BackupPolicy:
        """
        Update a scheduled backup policy for a dedicated database.

        Parameters
        ----------
        database_id : str
            Database ID.
        policy_id : str
            Policy ID.
        name : Optional[str]
            Policy name. Max length: 128 chars.
        schedule : Optional[str]
            Schedule CRON syntax.
        retention : Optional[float]
            Days to keep backups before deletion.
        enabled : Optional[bool]
            Is policy enabled? When disabled, no backups will be taken.
        Returns
        -------
        BackupPolicy
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/policies/{policyId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{policyId}', str(self._normalize_value(policy_id)))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if schedule is not None:
            api_params['schedule'] = self._normalize_value(schedule)
        if retention is not None:
            api_params['retention'] = self._normalize_value(retention)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=BackupPolicy)

    def delete_backup_policy(
        self,
        database_id: str,
        policy_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a scheduled backup policy for a dedicated database. Backups already taken by the policy are kept until their retention expires.

        Parameters
        ----------
        database_id : str
            Database ID.
        policy_id : str
            Policy ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/policies/{policyId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{policyId}', str(self._normalize_value(policy_id)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def update_backup_storage(
        self,
        database_id: str,
        provider: str,
        bucket: str,
        access_key: str,
        secret_key: str,
        region: Optional[str] = None,
        prefix: Optional[str] = None,
        endpoint: Optional[str] = None,
    ) -> DedicatedDatabaseBackupStorage:
        """
        Configure off-cluster backup storage for a dedicated database. Supports S3, GCS, and Azure Blob Storage destinations. Backups will be stored to the configured destination in addition to on-cluster storage.

        Parameters
        ----------
        database_id : str
            Database ID.
        provider : str
            Storage provider for off-cluster backups. Allowed values: s3 (Amazon S3 or S3-compatible), gcs (Google Cloud Storage), azure (Azure Blob Storage).
        bucket : str
            Storage bucket or container name.
        access_key : str
            Access key or client ID for authentication.
        secret_key : str
            Secret key or service account JSON for authentication.
        region : Optional[str]
            Storage region.
        prefix : Optional[str]
            Object key prefix for backups.
        endpoint : Optional[str]
            Custom endpoint for S3-compatible storage (e.g. MinIO).
        Returns
        -------
        DedicatedDatabaseBackupStorage
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/storage'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if provider is None:
            raise AppwriteException('Missing required parameter: "provider"')
        if bucket is None:
            raise AppwriteException('Missing required parameter: "bucket"')
        if access_key is None:
            raise AppwriteException('Missing required parameter: "access_key"')
        if secret_key is None:
            raise AppwriteException('Missing required parameter: "secret_key"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['provider'] = self._normalize_value(provider)
        api_params['bucket'] = self._normalize_value(bucket)
        if region is not None:
            api_params['region'] = self._normalize_value(region)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if endpoint is not None:
            api_params['endpoint'] = self._normalize_value(endpoint)
        api_params['accessKey'] = self._normalize_value(access_key)
        api_params['secretKey'] = self._normalize_value(secret_key)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseBackupStorage)

    def get_backup(
        self,
        database_id: str,
        backup_id: str,
    ) -> DedicatedDatabaseBackup:
        """
        Get details of a specific database backup including its status, size, and timestamps.

        Parameters
        ----------
        database_id : str
            Database ID.
        backup_id : str
            Backup ID.
        Returns
        -------
        DedicatedDatabaseBackup
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/{backupId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if backup_id is None:
            raise AppwriteException('Missing required parameter: "backup_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{backupId}', str(self._normalize_value(backup_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseBackup)

    def delete_backup(
        self,
        database_id: str,
        backup_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a database backup. This will permanently remove the backup from storage and cannot be undone.

        Parameters
        ----------
        database_id : str
            Database ID.
        backup_id : str
            Backup ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/backups/{backupId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if backup_id is None:
            raise AppwriteException('Missing required parameter: "backup_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{backupId}', str(self._normalize_value(backup_id)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def list_branches(
        self,
        database_id: str,
    ) -> DedicatedDatabaseBranchList:
        """
        List all ephemeral branches for a dedicated database. Returns branch metadata including ID, name, namespace, and expiration time.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DedicatedDatabaseBranchList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/branches'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseBranchList)

    def create_branch(
        self,
        database_id: str,
        branch_id: Optional[str] = None,
        ttl: Optional[float] = None,
    ) -> DedicatedDatabase:
        """
        Create an ephemeral database branch from the primary via PVC snapshot. The branch is a full copy of the database at the current point in time, useful for testing schema migrations or running experiments without affecting production data. Branches expire after the configured TTL (default 24 hours). The branch is created asynchronously.

        Parameters
        ----------
        database_id : str
            Database ID.
        branch_id : Optional[str]
            Branch ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        ttl : Optional[float]
            Time-to-live in seconds before the branch expires. Min 300 (5 min), max 604800 (7 days). Default: 86400 (24h).
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/branches'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if branch_id is not None:
            api_params['branchId'] = self._normalize_value(branch_id)
        if ttl is not None:
            api_params['ttl'] = self._normalize_value(ttl)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def delete_branch(
        self,
        database_id: str,
        branch_id: str,
    ) -> DedicatedDatabase:
        """
        Delete an ephemeral database branch. This removes the branch namespace, its PVC, and the associated VolumeSnapshot. The deletion runs asynchronously and is irreversible.

        Parameters
        ----------
        database_id : str
            Database ID.
        branch_id : str
            Branch ID.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/branches/{branchId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if branch_id is None:
            raise AppwriteException('Missing required parameter: "branch_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{branchId}', str(self._normalize_value(branch_id)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def update_credentials(
        self,
        database_id: str,
    ) -> DedicatedDatabaseOperation:
        """
        Queue a rotation of the primary connection credentials for a dedicated database. A hibernated database is woken by the worker before rotation. List database operations until the returned operation reaches a terminal status, then fetch the database again for the refreshed connection string.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DedicatedDatabaseOperation
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/credentials'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseOperation)

    def create_execution(
        self,
        database_id: str,
        sql: str,
        bindings: Optional[Dict[str, Any]] = None,
        timeout_seconds: Optional[float] = None,
    ) -> DedicatedDatabaseExecution:
        """
        Execute SQL through the console-facing Cloud endpoint. Cloud proxies through the edge platform to the per-database SQL API sidecar. Application traffic should bypass cloud entirely and POST directly to the per-database hostname: `https://db-{project}-{db}.{region}.appwrite.center/v1/sql/executions` with an `X-Appwrite-Key` header — that path scales to the whole DB fleet without a per-query cloud round-trip. The statement type must be on the database's configured allow-list. Use bound parameters for any user-supplied values — the API does not interpolate raw strings.

        Parameters
        ----------
        database_id : str
            Database ID.
        sql : str
            SQL statement to execute. Exactly one statement per request.
        bindings : Optional[Dict[str, Any]]
            Optional bound parameters. Pass either a positional list or a name => value map matching the placeholder style used in the SQL.
        timeout_seconds : Optional[float]
            Per-call execution timeout override. Must be less than or equal to the database's configured sqlApiTimeoutSeconds.
        Returns
        -------
        DedicatedDatabaseExecution
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/executions'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if sql is None:
            raise AppwriteException('Missing required parameter: "sql"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['sql'] = self._normalize_value(sql)
        if bindings is not None:
            api_params['bindings'] = self._normalize_value(bindings)
        if timeout_seconds is not None:
            api_params['timeoutSeconds'] = self._normalize_value(timeout_seconds)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseExecution)

    def list_extensions(
        self,
        database_id: str,
    ) -> DedicatedDatabaseExtensions:
        """
        List installed and available extensions for a PostgreSQL database.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DedicatedDatabaseExtensions
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/extensions'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseExtensions)

    def create_extension(
        self,
        database_id: str,
        name: str,
    ) -> DedicatedDatabase:
        """
        Install a database extension. Only available for PostgreSQL databases. The install runs asynchronously; poll the extensions list endpoint for status.

        Parameters
        ----------
        database_id : str
            Database ID.
        name : str
            Extension name (e.g., pgvector, postgis, uuid-ossp).
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/extensions'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['name'] = self._normalize_value(name)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def delete_extension(
        self,
        database_id: str,
        extension_name: str,
    ) -> DedicatedDatabase:
        """
        Uninstall a database extension from a PostgreSQL database. The uninstall runs asynchronously; poll the extensions list endpoint for status.

        Parameters
        ----------
        database_id : str
            Database ID.
        extension_name : str
            Extension name to uninstall.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/extensions/{extensionName}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if extension_name is None:
            raise AppwriteException('Missing required parameter: "extension_name"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{extensionName}', str(self._normalize_value(extension_name)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def create_failover(
        self,
        database_id: str,
        target_replica_id: Optional[str] = None,
    ) -> DedicatedDatabase:
        """
        Trigger a manual failover for a dedicated database with high availability enabled. Promotes a replica to primary. The failover runs asynchronously; poll the database document for status updates. A database left mid-operation also accepts this call as a repair once nothing is driving the operation it is stuck in. Repairing a failover that did not finish, a `failed` database, a stranded upgrade or migrate, or a stranded compute resize additionally requires `targetReplicaId` to name the member to promote, because the default target may be the member that operation already promoted.

        Parameters
        ----------
        database_id : str
            Database ID.
        target_replica_id : Optional[str]
            Target replica ID to promote. If not specified, the healthiest replica is selected.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/failovers'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if target_replica_id is not None:
            api_params['targetReplicaId'] = self._normalize_value(target_replica_id)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def update_maintenance(
        self,
        database_id: str,
        day: str,
        hour_utc: float,
    ) -> DedicatedDatabase:
        """
        Update the maintenance window for a dedicated database. Maintenance operations like minor version upgrades will be performed during this window.

        Parameters
        ----------
        database_id : str
            Database ID.
        day : str
            Day of the week for the maintenance window. Allowed values: sun, mon, tue, wed, thu, fri, sat.
        hour_utc : float
            Hour in UTC (0-23) for maintenance window start.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/maintenance'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if day is None:
            raise AppwriteException('Missing required parameter: "day"')
        if hour_utc is None:
            raise AppwriteException('Missing required parameter: "hour_utc"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['day'] = self._normalize_value(day)
        api_params['hourUtc'] = self._normalize_value(hour_utc)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def create_migration(
        self,
        database_id: str,
        target_type: str,
        specification: Optional[str] = None,
    ) -> DedicatedDatabase:
        """
        Migrate a database between shared and dedicated types. Shared to dedicated provisions an always-on dedicated instance; dedicated to shared converts to a serverless instance that scales to zero when idle. Data is copied to the target with a brief read-only window during cutover.

        Parameters
        ----------
        database_id : str
            Database ID.
        target_type : str
            Target database type to migrate to. Allowed values: shared (serverless, scales to zero when idle), dedicated (always-on with persistent resources).
        specification : Optional[str]
            Target specification to provision when migrating to dedicated. Ignored for shared. Defaults to the database's current specification.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/migrations'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if target_type is None:
            raise AppwriteException('Missing required parameter: "target_type"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['targetType'] = self._normalize_value(target_type)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)

    def list_operations(
        self,
        database_id: str,
        status: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
    ) -> DedicatedDatabaseOperationList:
        """
        List the lifecycle operations recorded for a dedicated database, newest first. Every provision, update, restore, backup and replication action is recorded here with its outcome, including an attempt that was abandoned because another worker took over the database.

        Parameters
        ----------
        database_id : str
            Database ID.
        status : Optional[str]
            Filter by operation status.
        limit : Optional[float]
            Maximum number of operations to return.
        offset : Optional[float]
            Number of operations to skip.
        Returns
        -------
        DedicatedDatabaseOperationList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/operations'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseOperationList)

    def get_pitr(
        self,
        database_id: str,
    ) -> DedicatedDatabasePITRWindows:
        """
        Get available point-in-time recovery windows for a dedicated database. Returns the earliest and latest recovery points.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DedicatedDatabasePITRWindows
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/pitr'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabasePITRWindows)

    def get_pooler(
        self,
        database_id: str,
    ) -> DedicatedDatabasePooler:
        """
        Get the connection pooler configuration for a dedicated database. Returns pooler mode, max connections, and pool size settings.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DedicatedDatabasePooler
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/pooler'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabasePooler)

    def update_pooler(
        self,
        database_id: str,
        mode: Optional[str] = None,
        max_connections: Optional[float] = None,
        default_pool_size: Optional[float] = None,
        read_write_splitting: Optional[bool] = None,
        pooler_cpu_request: Optional[str] = None,
        pooler_cpu_limit: Optional[str] = None,
        pooler_memory_request: Optional[str] = None,
        pooler_memory_limit: Optional[str] = None,
    ) -> DedicatedDatabasePooler:
        """
        Update the connection pooler configuration for a dedicated database. Configure pool mode, max connections, and pool sizes.

        Parameters
        ----------
        database_id : str
            Database ID.
        mode : Optional[str]
            Connection pool mode. Allowed values: transaction, session. Transaction mode returns connections to the pool after each transaction; session mode holds connections for the entire session lifetime.
        max_connections : Optional[float]
            Client-connection ceiling the pooler accepts. Supported on MySQL and MariaDB only; the PostgreSQL pooler has no client cap, so set networkMaxConnections on the database instead.
        default_pool_size : Optional[float]
            Default pool size per user.
        read_write_splitting : Optional[bool]
            Route SELECTs to HA replicas, writes and locked reads to the primary. Defaults to true when HA is enabled.
        pooler_cpu_request : Optional[str]
            Pooler sidecar CPU request override (Kubernetes quantity, e.g. "250m" or "1"). Leave null for the proportional default (5% of DB CPU, floor 100m).
        pooler_cpu_limit : Optional[str]
            Pooler sidecar CPU limit override (Kubernetes quantity, e.g. "500m" or "1"). Leave null for the proportional default (10% of DB CPU, floor 200m). Changing this field rolls the database pod.
        pooler_memory_request : Optional[str]
            Pooler sidecar memory request override (Kubernetes quantity, e.g. "128Mi" or "1Gi"). Leave null for the proportional default (7.5% of DB memory, floor 64Mi).
        pooler_memory_limit : Optional[str]
            Pooler sidecar memory limit override (Kubernetes quantity, e.g. "256Mi" or "1Gi"). Leave null for the proportional default (15% of DB memory, floor 128Mi). Changing this field rolls the database pod.
        Returns
        -------
        DedicatedDatabasePooler
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/pooler'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if mode is not None:
            api_params['mode'] = self._normalize_value(mode)
        if max_connections is not None:
            api_params['maxConnections'] = self._normalize_value(max_connections)
        if default_pool_size is not None:
            api_params['defaultPoolSize'] = self._normalize_value(default_pool_size)
        if read_write_splitting is not None:
            api_params['readWriteSplitting'] = self._normalize_value(read_write_splitting)
        if pooler_cpu_request is not None:
            api_params['poolerCpuRequest'] = self._normalize_value(pooler_cpu_request)
        if pooler_cpu_limit is not None:
            api_params['poolerCpuLimit'] = self._normalize_value(pooler_cpu_limit)
        if pooler_memory_request is not None:
            api_params['poolerMemoryRequest'] = self._normalize_value(pooler_memory_request)
        if pooler_memory_limit is not None:
            api_params['poolerMemoryLimit'] = self._normalize_value(pooler_memory_limit)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabasePooler)

    def get_replicas(
        self,
        database_id: str,
    ) -> DedicatedDatabaseReplicas:
        """
        Get high availability status for a dedicated database. Returns replica statuses, replication lag, and sync mode.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DedicatedDatabaseReplicas
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/replicas'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseReplicas)

    def list_restorations(
        self,
        database_id: str,
        status: Optional[str] = None,
        type: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
    ) -> DedicatedDatabaseRestorationList:
        """
        List all restorations for a dedicated database. Results can be filtered by status and type.

        Parameters
        ----------
        database_id : str
            Database ID.
        status : Optional[str]
            Filter by restoration status.
        type : Optional[str]
            Filter by restoration type.
        limit : Optional[float]
            Maximum number of restorations to return.
        offset : Optional[float]
            Number of restorations to skip.
        Returns
        -------
        DedicatedDatabaseRestorationList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/restorations'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseRestorationList)

    def create_restoration(
        self,
        database_id: str,
        type: Optional[str] = None,
        backup_id: Optional[str] = None,
        target_database_id: Optional[str] = None,
        target_time: Optional[str] = None,
    ) -> DedicatedDatabaseRestoration:
        """
        Restore a database from a backup or to a specific point in time (PITR). For backup restoration, provide a backupId. For PITR, provide a targetTime as an ISO 8601 datetime. PITR requires the database to have PITR enabled and is only available for enterprise databases.

        Parameters
        ----------
        database_id : str
            Database ID.
        type : Optional[str]
            Restoration type. Allowed values: backup, pitr. Use "backup" to restore from a specific backup, or "pitr" for point-in-time recovery.
        backup_id : Optional[str]
            Backup ID to restore from (required for backup type).
        target_database_id : Optional[str]
            Existing database ID to restore into. The target must be distinct, ready, and use the same engine and version.
        target_time : Optional[str]
            Target time for PITR (required for pitr type) as an [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) datetime.
        Returns
        -------
        DedicatedDatabaseRestoration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/restorations'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if backup_id is not None:
            api_params['backupId'] = self._normalize_value(backup_id)
        if target_database_id is not None:
            api_params['targetDatabaseId'] = self._normalize_value(target_database_id)
        if target_time is not None:
            api_params['targetTime'] = self._normalize_value(target_time)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseRestoration)

    def get_restoration(
        self,
        database_id: str,
        restoration_id: str,
    ) -> DedicatedDatabaseRestoration:
        """
        Get details of a specific database restoration including its status, type, and timestamps.

        Parameters
        ----------
        database_id : str
            Database ID.
        restoration_id : str
            Restoration ID.
        Returns
        -------
        DedicatedDatabaseRestoration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/restorations/{restorationId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if restoration_id is None:
            raise AppwriteException('Missing required parameter: "restoration_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{restorationId}', str(self._normalize_value(restoration_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabaseRestoration)

    def get_status(
        self,
        database_id: str,
    ) -> DatabaseStatus:
        """
        Get real-time health and status information for a dedicated database. Returns health status, readiness, uptime, connection info, replica status, and volume information.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        DatabaseStatus
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/status'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DatabaseStatus)

    def create_upgrade(
        self,
        database_id: str,
        target_version: str,
    ) -> DedicatedDatabase:
        """
        Upgrade a dedicated database to a new engine version. Uses blue-green deployment for zero-downtime cutover.

        Parameters
        ----------
        database_id : str
            Database ID.
        target_version : str
            Target engine version to upgrade to.
        Returns
        -------
        DedicatedDatabase
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/postgresql/{databaseId}/upgrades'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if target_version is None:
            raise AppwriteException('Missing required parameter: "target_version"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['targetVersion'] = self._normalize_value(target_version)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DedicatedDatabase)
