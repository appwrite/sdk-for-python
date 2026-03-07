from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.backup_archive_list import BackupArchiveList;
from ..enums.backup_services import BackupServices;
from ..models.backup_archive import BackupArchive;
from ..models.backup_policy_list import BackupPolicyList;
from ..models.backup_policy import BackupPolicy;
from ..models.backup_restoration import BackupRestoration;
from ..models.backup_restoration_list import BackupRestorationList;

class Backups(Service):

    def __init__(self, client) -> None:
        super(Backups, self).__init__(client)

    def list_archives(
        self,
        queries: Optional[List[str]] = None    ) -> BackupArchiveList:
        """
        List all archives for a project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        
        Returns
        -------
        BackupArchiveList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/archives'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=BackupArchiveList)


    def create_archive(
        self,
        services: List[BackupServices],
        resource_id: Optional[str] = None    ) -> BackupArchive:
        """
        Create a new archive asynchronously for a project.

        Parameters
        ----------
        services : List[BackupServices]
            Array of services to backup
        resource_id : Optional[str]
            Resource ID. When set, only this single resource will be backed up.
        
        Returns
        -------
        BackupArchive            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/archives'
        api_params = {}
        if services is None:
            raise AppwriteException('Missing required parameter: "services"')


        api_params['services'] = self._normalize_value(services)
        api_params['resourceId'] = self._normalize_value(resource_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=BackupArchive)


    def get_archive(
        self,
        archive_id: str    ) -> BackupArchive:
        """
        Get a backup archive using it's ID.

        Parameters
        ----------
        archive_id : str
            Archive ID. Choose a custom ID`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        
        Returns
        -------
        BackupArchive            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/archives/{archiveId}'
        api_params = {}
        if archive_id is None:
            raise AppwriteException('Missing required parameter: "archive_id"')

        api_path = api_path.replace('{archiveId}', str(self._normalize_value(archive_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=BackupArchive)


    def delete_archive(
        self,
        archive_id: str    ) -> Dict[str, Any]:
        """
        Delete an existing archive for a project.

        Parameters
        ----------
        archive_id : str
            Policy ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/archives/{archiveId}'
        api_params = {}
        if archive_id is None:
            raise AppwriteException('Missing required parameter: "archive_id"')

        api_path = api_path.replace('{archiveId}', str(self._normalize_value(archive_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_policies(
        self,
        queries: Optional[List[str]] = None    ) -> BackupPolicyList:
        """
        List all policies for a project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        
        Returns
        -------
        BackupPolicyList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/policies'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=BackupPolicyList)


    def create_policy(
        self,
        policy_id: str,
        services: List[BackupServices],
        retention: float,
        schedule: str,
        name: Optional[str] = None,
        resource_id: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> BackupPolicy:
        """
        Create a new backup policy.

        Parameters
        ----------
        policy_id : str
            Policy ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        services : List[BackupServices]
            Array of services to backup
        retention : float
            Days to keep backups before deletion
        schedule : str
            Schedule CRON syntax.
        name : Optional[str]
            Policy name. Max length: 128 chars.
        resource_id : Optional[str]
            Resource ID. When set, only this single resource will be backed up.
        enabled : Optional[bool]
            Is policy enabled? When set to 'disabled', no backups will be taken
        
        Returns
        -------
        BackupPolicy            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/policies'
        api_params = {}
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')

        if services is None:
            raise AppwriteException('Missing required parameter: "services"')

        if retention is None:
            raise AppwriteException('Missing required parameter: "retention"')

        if schedule is None:
            raise AppwriteException('Missing required parameter: "schedule"')


        api_params['policyId'] = self._normalize_value(policy_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['services'] = self._normalize_value(services)
        api_params['resourceId'] = self._normalize_value(resource_id)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['retention'] = self._normalize_value(retention)
        api_params['schedule'] = self._normalize_value(schedule)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=BackupPolicy)


    def get_policy(
        self,
        policy_id: str    ) -> BackupPolicy:
        """
        Get a backup policy using it's ID.

        Parameters
        ----------
        policy_id : str
            Policy ID. Choose a custom ID`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        
        Returns
        -------
        BackupPolicy            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/policies/{policyId}'
        api_params = {}
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')

        api_path = api_path.replace('{policyId}', str(self._normalize_value(policy_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=BackupPolicy)


    def update_policy(
        self,
        policy_id: str,
        name: Optional[str] = None,
        retention: Optional[float] = None,
        schedule: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> BackupPolicy:
        """
        Update an existing policy using it's ID.

        Parameters
        ----------
        policy_id : str
            Policy ID. Choose a custom ID`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : Optional[str]
            Policy name. Max length: 128 chars.
        retention : Optional[float]
            Days to keep backups before deletion
        schedule : Optional[str]
            Cron expression
        enabled : Optional[bool]
            Is Backup enabled? When set to 'disabled', No backup will be taken
        
        Returns
        -------
        BackupPolicy            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/policies/{policyId}'
        api_params = {}
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')

        api_path = api_path.replace('{policyId}', str(self._normalize_value(policy_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['retention'] = self._normalize_value(retention)
        if schedule is not None:
            api_params['schedule'] = self._normalize_value(schedule)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=BackupPolicy)


    def delete_policy(
        self,
        policy_id: str    ) -> Dict[str, Any]:
        """
        Delete a policy using it's ID.

        Parameters
        ----------
        policy_id : str
            Policy ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/policies/{policyId}'
        api_params = {}
        if policy_id is None:
            raise AppwriteException('Missing required parameter: "policy_id"')

        api_path = api_path.replace('{policyId}', str(self._normalize_value(policy_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def create_restoration(
        self,
        archive_id: str,
        services: List[BackupServices],
        new_resource_id: Optional[str] = None,
        new_resource_name: Optional[str] = None    ) -> BackupRestoration:
        """
        Create and trigger a new restoration for a backup on a project.

        Parameters
        ----------
        archive_id : str
            Backup archive ID to restore
        services : List[BackupServices]
            Array of services to restore
        new_resource_id : Optional[str]
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        new_resource_name : Optional[str]
            Database name. Max length: 128 chars.
        
        Returns
        -------
        BackupRestoration            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/restoration'
        api_params = {}
        if archive_id is None:
            raise AppwriteException('Missing required parameter: "archive_id"')

        if services is None:
            raise AppwriteException('Missing required parameter: "services"')


        api_params['archiveId'] = self._normalize_value(archive_id)
        api_params['services'] = self._normalize_value(services)
        if new_resource_id is not None:
            api_params['newResourceId'] = self._normalize_value(new_resource_id)
        if new_resource_name is not None:
            api_params['newResourceName'] = self._normalize_value(new_resource_name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=BackupRestoration)


    def list_restorations(
        self,
        queries: Optional[List[str]] = None    ) -> BackupRestorationList:
        """
        List all backup restorations for a project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        
        Returns
        -------
        BackupRestorationList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/restorations'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=BackupRestorationList)


    def get_restoration(
        self,
        restoration_id: str    ) -> BackupRestoration:
        """
        Get the current status of a backup restoration.

        Parameters
        ----------
        restoration_id : str
            Restoration ID. Choose a custom ID`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        
        Returns
        -------
        BackupRestoration            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/backups/restorations/{restorationId}'
        api_params = {}
        if restoration_id is None:
            raise AppwriteException('Missing required parameter: "restoration_id"')

        api_path = api_path.replace('{restorationId}', str(self._normalize_value(restoration_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=BackupRestoration)

