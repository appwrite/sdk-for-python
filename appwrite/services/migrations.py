from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.migration_list import MigrationList
from ..enums.appwrite_migration_resource import AppwriteMigrationResource
from ..enums.on_duplicate import OnDuplicate
from ..models.migration import Migration
from ..enums.firebase_migration_resource import FirebaseMigrationResource
from ..enums.n_host_migration_resource import NHostMigrationResource
from ..enums.supabase_migration_resource import SupabaseMigrationResource


class Migrations(Service):

    def __init__(self, client) -> None:
        super(Migrations, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None,
    ) -> MigrationList:
        """
        List all migrations in the current project. This endpoint returns a list of all migrations including their status, progress, and any errors that occurred during the migration process.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: status, stage, source, destination, resources, resourceId, resourceInternalId, resourceType, parentResourceId, parentResourceInternalId, parentResourceType, destinationResourceId, destinationResourceInternalId, destinationResourceType, statusCounters, resourceData, errors
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        MigrationList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=MigrationList)

    def create_appwrite_migration(
        self,
        resources: List[AppwriteMigrationResource],
        endpoint: str,
        project_id: str,
        api_key: str,
        on_duplicate: Optional[OnDuplicate] = None,
    ) -> Migration:
        """
        Migrate data from another Appwrite project to your current project. This endpoint allows you to migrate resources like databases, collections, documents, users, and files from an existing Appwrite project.

        Parameters
        ----------
        resources : List[AppwriteMigrationResource]
            List of resources to migrate
        endpoint : str
            Source Appwrite endpoint
        project_id : str
            Source Project ID
        api_key : str
            Source API Key
        on_duplicate : Optional[OnDuplicate]
            Behavior when a row with an existing $id is encountered. "fail" (default): abort on first conflict. "skip": silently ignore. "overwrite": replace existing row.
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/appwrite'
        api_params = {}
        if resources is None:
            raise AppwriteException('Missing required parameter: "resources"')
        if endpoint is None:
            raise AppwriteException('Missing required parameter: "endpoint"')
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')
        if api_key is None:
            raise AppwriteException('Missing required parameter: "api_key"')
        api_params['resources'] = self._normalize_value(resources)
        api_params['endpoint'] = self._normalize_value(endpoint)
        api_params['projectId'] = self._normalize_value(project_id)
        api_params['apiKey'] = self._normalize_value(api_key)
        if on_duplicate is not None:
            api_params['onDuplicate'] = self._normalize_value(on_duplicate)

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

        return self._parse_response(response, model=Migration)

    def create_csv_export(
        self,
        database_id: str,
        collection_id: str,
        filename: str,
        columns: Optional[List[str]] = None,
        queries: Optional[List[str]] = None,
        delimiter: Optional[str] = None,
        enclosure: Optional[str] = None,
        escape: Optional[str] = None,
        header: Optional[bool] = None,
        notify: Optional[bool] = None,
    ) -> Migration:
        """
        Export documents to a CSV file from your Appwrite database. This endpoint allows you to export documents to a CSV file stored in a secure internal bucket. You'll receive an email with a download link when the export is complete.

        Parameters
        ----------
        database_id : str
            Database ID containing the source collection.
        collection_id : str
            Collection ID to export documents from.
        filename : str
            The name of the file to be created for the export, excluding the .csv extension.
        columns : Optional[List[str]]
            List of attributes to export. If empty, all attributes will be exported. You can use the `*` wildcard to export all attributes from the collection.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK to filter documents to export. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long.
        delimiter : Optional[str]
            The character that separates each column value. Default is comma.
        enclosure : Optional[str]
            The character that encloses each column value. Default is double quotes.
        escape : Optional[str]
            The escape character for the enclosure character. Default is double quotes.
        header : Optional[bool]
            Whether to include the header row with column names. Default is true.
        notify : Optional[bool]
            Set to true to receive an email when the export is complete. Default is true.
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/csv/exports'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if filename is None:
            raise AppwriteException('Missing required parameter: "filename"')
        api_params['databaseId'] = self._normalize_value(database_id)
        api_params['collectionId'] = self._normalize_value(collection_id)
        api_params['filename'] = self._normalize_value(filename)
        if columns is not None:
            api_params['columns'] = self._normalize_value(columns)
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if delimiter is not None:
            api_params['delimiter'] = self._normalize_value(delimiter)
        if enclosure is not None:
            api_params['enclosure'] = self._normalize_value(enclosure)
        if escape is not None:
            api_params['escape'] = self._normalize_value(escape)
        if header is not None:
            api_params['header'] = self._normalize_value(header)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)

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

        return self._parse_response(response, model=Migration)

    def create_csv_import(
        self,
        bucket_id: str,
        file_id: str,
        database_id: str,
        collection_id: str,
        internal_file: Optional[bool] = None,
        on_duplicate: Optional[OnDuplicate] = None,
    ) -> Migration:
        """
        Import documents from a CSV file into your Appwrite database. This endpoint allows you to import documents from a CSV file uploaded to Appwrite Storage bucket.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID.
        database_id : str
            Database ID containing the target collection.
        collection_id : str
            Collection ID to import documents into.
        internal_file : Optional[bool]
            Is the file stored in an internal bucket?
        on_duplicate : Optional[OnDuplicate]
            Behavior when a row with an existing $id is encountered. "fail" (default): abort on first conflict. "skip": silently ignore. "overwrite": replace existing row.
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/csv/imports'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')
        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_params['bucketId'] = self._normalize_value(bucket_id)
        api_params['fileId'] = self._normalize_value(file_id)
        api_params['databaseId'] = self._normalize_value(database_id)
        api_params['collectionId'] = self._normalize_value(collection_id)
        if internal_file is not None:
            api_params['internalFile'] = self._normalize_value(internal_file)
        if on_duplicate is not None:
            api_params['onDuplicate'] = self._normalize_value(on_duplicate)

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

        return self._parse_response(response, model=Migration)

    def create_firebase_migration(
        self,
        resources: List[FirebaseMigrationResource],
        service_account: str,
    ) -> Migration:
        """
        Migrate data from a Firebase project to your Appwrite project. This endpoint allows you to migrate resources like authentication and other supported services from a Firebase project.

        Parameters
        ----------
        resources : List[FirebaseMigrationResource]
            List of resources to migrate
        service_account : str
            JSON of the Firebase service account credentials
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/firebase'
        api_params = {}
        if resources is None:
            raise AppwriteException('Missing required parameter: "resources"')
        if service_account is None:
            raise AppwriteException('Missing required parameter: "service_account"')
        api_params['resources'] = self._normalize_value(resources)
        api_params['serviceAccount'] = self._normalize_value(service_account)

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

        return self._parse_response(response, model=Migration)

    def create_json_export(
        self,
        database_id: str,
        collection_id: str,
        filename: str,
        columns: Optional[List[str]] = None,
        queries: Optional[List[str]] = None,
        notify: Optional[bool] = None,
    ) -> Migration:
        """
        Export documents to a JSON file from your Appwrite database. This endpoint allows you to export documents to a JSON file stored in a secure internal bucket. You'll receive an email with a download link when the export is complete.

        Parameters
        ----------
        database_id : str
            Database ID containing the source collection.
        collection_id : str
            Collection ID to export documents from.
        filename : str
            The name of the file to be created for the export, excluding the .json extension.
        columns : Optional[List[str]]
            List of attributes to export. If empty, all attributes will be exported. You can use the `*` wildcard to export all attributes from the collection.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK to filter documents to export. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long.
        notify : Optional[bool]
            Set to true to receive an email when the export is complete. Default is true.
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/json/exports'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if filename is None:
            raise AppwriteException('Missing required parameter: "filename"')
        api_params['databaseId'] = self._normalize_value(database_id)
        api_params['collectionId'] = self._normalize_value(collection_id)
        api_params['filename'] = self._normalize_value(filename)
        if columns is not None:
            api_params['columns'] = self._normalize_value(columns)
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)

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

        return self._parse_response(response, model=Migration)

    def create_json_import(
        self,
        bucket_id: str,
        file_id: str,
        database_id: str,
        collection_id: str,
        internal_file: Optional[bool] = None,
        on_duplicate: Optional[OnDuplicate] = None,
    ) -> Migration:
        """
        Import documents from a JSON file into your Appwrite database. This endpoint allows you to import documents from a JSON file uploaded to Appwrite Storage bucket.

        Parameters
        ----------
        bucket_id : str
            Storage bucket unique ID. You can create a new storage bucket using the Storage service [server integration](https://appwrite.io/docs/server/storage#createBucket).
        file_id : str
            File ID.
        database_id : str
            Database ID containing the target collection.
        collection_id : str
            Collection ID to import documents into.
        internal_file : Optional[bool]
            Is the file stored in an internal bucket?
        on_duplicate : Optional[OnDuplicate]
            Behavior when a row with an existing $id is encountered. "fail" (default): abort on first conflict. "skip": silently ignore. "overwrite": replace existing row.
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/json/imports'
        api_params = {}
        if bucket_id is None:
            raise AppwriteException('Missing required parameter: "bucket_id"')
        if file_id is None:
            raise AppwriteException('Missing required parameter: "file_id"')
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_params['bucketId'] = self._normalize_value(bucket_id)
        api_params['fileId'] = self._normalize_value(file_id)
        api_params['databaseId'] = self._normalize_value(database_id)
        api_params['collectionId'] = self._normalize_value(collection_id)
        if internal_file is not None:
            api_params['internalFile'] = self._normalize_value(internal_file)
        if on_duplicate is not None:
            api_params['onDuplicate'] = self._normalize_value(on_duplicate)

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

        return self._parse_response(response, model=Migration)

    def create_n_host_migration(
        self,
        resources: List[NHostMigrationResource],
        subdomain: str,
        region: str,
        admin_secret: str,
        database: str,
        username: str,
        password: str,
        port: Optional[float] = None,
    ) -> Migration:
        """
        Migrate data from an NHost project to your Appwrite project. This endpoint allows you to migrate resources like authentication, databases, and other supported services from an NHost project.

        Parameters
        ----------
        resources : List[NHostMigrationResource]
            List of resources to migrate
        subdomain : str
            Source's Subdomain
        region : str
            Source's Region
        admin_secret : str
            Source's Admin Secret
        database : str
            Source's Database Name
        username : str
            Source's Database Username
        password : str
            Source's Database Password
        port : Optional[float]
            Source's Database Port
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/nhost'
        api_params = {}
        if resources is None:
            raise AppwriteException('Missing required parameter: "resources"')
        if subdomain is None:
            raise AppwriteException('Missing required parameter: "subdomain"')
        if region is None:
            raise AppwriteException('Missing required parameter: "region"')
        if admin_secret is None:
            raise AppwriteException('Missing required parameter: "admin_secret"')
        if database is None:
            raise AppwriteException('Missing required parameter: "database"')
        if username is None:
            raise AppwriteException('Missing required parameter: "username"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['resources'] = self._normalize_value(resources)
        api_params['subdomain'] = self._normalize_value(subdomain)
        api_params['region'] = self._normalize_value(region)
        api_params['adminSecret'] = self._normalize_value(admin_secret)
        api_params['database'] = self._normalize_value(database)
        api_params['username'] = self._normalize_value(username)
        api_params['password'] = self._normalize_value(password)
        if port is not None:
            api_params['port'] = self._normalize_value(port)

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

        return self._parse_response(response, model=Migration)

    def create_supabase_migration(
        self,
        resources: List[SupabaseMigrationResource],
        endpoint: str,
        api_key: str,
        database_host: str,
        username: str,
        password: str,
        port: Optional[float] = None,
    ) -> Migration:
        """
        Migrate data from a Supabase project to your Appwrite project. This endpoint allows you to migrate resources like authentication, databases, and other supported services from a Supabase project.

        Parameters
        ----------
        resources : List[SupabaseMigrationResource]
            List of resources to migrate
        endpoint : str
            Source's Supabase Endpoint
        api_key : str
            Source's API Key
        database_host : str
            Source's Database Host
        username : str
            Source's Database Username
        password : str
            Source's Database Password
        port : Optional[float]
            Source's Database Port
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/supabase'
        api_params = {}
        if resources is None:
            raise AppwriteException('Missing required parameter: "resources"')
        if endpoint is None:
            raise AppwriteException('Missing required parameter: "endpoint"')
        if api_key is None:
            raise AppwriteException('Missing required parameter: "api_key"')
        if database_host is None:
            raise AppwriteException('Missing required parameter: "database_host"')
        if username is None:
            raise AppwriteException('Missing required parameter: "username"')
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')
        api_params['resources'] = self._normalize_value(resources)
        api_params['endpoint'] = self._normalize_value(endpoint)
        api_params['apiKey'] = self._normalize_value(api_key)
        api_params['databaseHost'] = self._normalize_value(database_host)
        api_params['username'] = self._normalize_value(username)
        api_params['password'] = self._normalize_value(password)
        if port is not None:
            api_params['port'] = self._normalize_value(port)

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

        return self._parse_response(response, model=Migration)

    def get(
        self,
        migration_id: str,
    ) -> Migration:
        """
        Get a migration by its unique ID. This endpoint returns detailed information about a specific migration including its current status, progress, and any errors that occurred during the migration process.

        Parameters
        ----------
        migration_id : str
            Migration unique ID.
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/{migrationId}'
        api_params = {}
        if migration_id is None or migration_id == '':
            raise AppwriteException('Missing required parameter: "migration_id"')
        api_path = api_path.replace('{migrationId}', self._encode_path(migration_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Migration)

    def retry(
        self,
        migration_id: str,
    ) -> Migration:
        """
        Retry a failed migration. This endpoint allows you to retry a migration that has previously failed.

        Parameters
        ----------
        migration_id : str
            Migration unique ID.
        Returns
        -------
        Migration
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/{migrationId}'
        api_params = {}
        if migration_id is None or migration_id == '':
            raise AppwriteException('Missing required parameter: "migration_id"')
        api_path = api_path.replace('{migrationId}', self._encode_path(migration_id))

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

        return self._parse_response(response, model=Migration)

    def delete(
        self,
        migration_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a migration by its unique ID. This endpoint allows you to remove a migration from your project's migration history.

        Parameters
        ----------
        migration_id : str
            Migration ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/migrations/{migrationId}'
        api_params = {}
        if migration_id is None or migration_id == '':
            raise AppwriteException('Missing required parameter: "migration_id"')
        api_path = api_path.replace('{migrationId}', self._encode_path(migration_id))

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
