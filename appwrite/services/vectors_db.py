from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.database_list import DatabaseList
from ..models.database import Database
from ..models.dedicated_database_specification_list import DedicatedDatabaseSpecificationList
from ..models.transaction_list import TransactionList
from ..models.transaction import Transaction
from ..models.vectorsdb_collection_list import VectorsdbCollectionList
from ..models.vectorsdb_collection import VectorsdbCollection
from ..models.document_list import DocumentList
from ..models.document import Document
from ..models.index_list import IndexList
from ..enums.vectors_db_index_type import VectorsDBIndexType
from ..enums.order_by import OrderBy
from ..models.index import Index
from ..models.dedicated_database import DedicatedDatabase
from ..models.dedicated_database_operation_list import DedicatedDatabaseOperationList
from ..models.dedicated_database_replicas import DedicatedDatabaseReplicas
from ..models.database_status import DatabaseStatus

T = TypeVar('T')


class VectorsDB(Service):

    def __init__(self, client) -> None:
        super(VectorsDB, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> DatabaseList:
        """
        Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: name
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        DatabaseList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
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

        return self._parse_response(response, model=DatabaseList)

    def create(
        self,
        database_id: str,
        name: str,
        enabled: Optional[bool] = None,
        specification: Optional[str] = None,
        replicas: Optional[float] = None,
        sync_mode: Optional[str] = None,
    ) -> Database:
        """
        Create a new Database.

        Parameters
        ----------
        database_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Database name. Max length: 128 chars.
        enabled : Optional[bool]
            Is the database enabled? When set to 'disabled', users cannot access the database but Server SDKs with an API key can still read and write to the database. No data is lost when this is toggled.
        specification : Optional[str]
            Database specification. Defaults to `serverless`, which creates the database on the shared pool. Any other value provisions a dedicated database on that specification.
        replicas : Optional[float]
            Number of high availability replicas (0-5) for the dedicated database backing this database. Requires a dedicated `specification`; must be 0 for a serverless database. High availability is enabled when greater than 0.
        sync_mode : Optional[str]
            Replication sync mode for the dedicated database backing this database. Requires a dedicated `specification`; the mode is only in force once there is at least one replica. Allowed values: async, sync, quorum.
        Returns
        -------
        Database
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_params['databaseId'] = self._normalize_value(database_id)
        api_params['name'] = self._normalize_value(name)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if replicas is not None:
            api_params['replicas'] = self._normalize_value(replicas)
        if sync_mode is not None:
            api_params['syncMode'] = self._normalize_value(sync_mode)

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

        return self._parse_response(response, model=Database)

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

        api_path = '/vectorsdb/specifications'
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

    def list_transactions(
        self,
        queries: Optional[List[str]] = None,
    ) -> TransactionList:
        """
        List transactions across all databases.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries).
        Returns
        -------
        TransactionList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/transactions'
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

        return self._parse_response(response, model=TransactionList)

    def create_transaction(
        self,
        ttl: Optional[float] = None,
    ) -> Transaction:
        """
        Create a new transaction.

        Parameters
        ----------
        ttl : Optional[float]
            Seconds before the transaction expires.
        Returns
        -------
        Transaction
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/transactions'
        api_params = {}
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

        return self._parse_response(response, model=Transaction)

    def get_transaction(
        self,
        transaction_id: str,
    ) -> Transaction:
        """
        Get a transaction by its unique ID.

        Parameters
        ----------
        transaction_id : str
            Transaction ID.
        Returns
        -------
        Transaction
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/transactions/{transactionId}'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')
        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Transaction)

    def update_transaction(
        self,
        transaction_id: str,
        commit: Optional[bool] = None,
        rollback: Optional[bool] = None,
    ) -> Transaction:
        """
        Update a transaction, to either commit or roll back its operations.

        Parameters
        ----------
        transaction_id : str
            Transaction ID.
        commit : Optional[bool]
            Commit transaction?
        rollback : Optional[bool]
            Rollback transaction?
        Returns
        -------
        Transaction
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/transactions/{transactionId}'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')
        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))
        if commit is not None:
            api_params['commit'] = self._normalize_value(commit)
        if rollback is not None:
            api_params['rollback'] = self._normalize_value(rollback)

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

        return self._parse_response(response, model=Transaction)

    def delete_transaction(
        self,
        transaction_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a transaction by its unique ID.

        Parameters
        ----------
        transaction_id : str
            Transaction ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/transactions/{transactionId}'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')
        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
            },
            api_params,
        )

        return response

    def create_operations(
        self,
        transaction_id: str,
        operations: Optional[List[Dict[str, Any]]] = None,
    ) -> Transaction:
        """
        Create multiple operations in a single transaction.

        Parameters
        ----------
        transaction_id : str
            Transaction ID.
        operations : Optional[List[Dict[str, Any]]]
            Array of staged operations.
        Returns
        -------
        Transaction
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/transactions/{transactionId}/operations'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')
        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))
        if operations is not None:
            api_params['operations'] = self._normalize_value(operations)

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

        return self._parse_response(response, model=Transaction)

    def get(
        self,
        database_id: str,
    ) -> Database:
        """
        Get a database by its unique ID. This endpoint response returns a JSON object with the database metadata.

        Parameters
        ----------
        database_id : str
            Database ID.
        Returns
        -------
        Database
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}'
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

        return self._parse_response(response, model=Database)

    def update(
        self,
        database_id: str,
        name: str,
        enabled: Optional[bool] = None,
        specification: Optional[str] = None,
        replicas: Optional[float] = None,
        sync_mode: Optional[str] = None,
    ) -> Database:
        """
        Update a database by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        name : str
            Database name. Max length: 128 chars.
        enabled : Optional[bool]
            Is database enabled? When set to 'disabled', users cannot access the database but Server SDKs with an API key can still read and write to the database. No data is lost when this is toggled.
        specification : Optional[str]
            Database specification. Resizing between dedicated specifications changes cpu, memory, storage and the connection ceiling via a rolling cutover with zero downtime. Moving a `serverless` database onto a dedicated specification is a data migration, not a resize.
        replicas : Optional[float]
            Number of high availability replicas (0-5) for the dedicated database backing this database. Only valid when the database is backed by a dedicated specification. High availability is enabled when greater than 0.
        sync_mode : Optional[str]
            Replication sync mode for the dedicated database backing this database. Only valid when the database is backed by a dedicated specification; the mode is only in force once there is at least one replica. Allowed values: async, sync, quorum.
        Returns
        -------
        Database
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['name'] = self._normalize_value(name)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)
        if replicas is not None:
            api_params['replicas'] = self._normalize_value(replicas)
        if sync_mode is not None:
            api_params['syncMode'] = self._normalize_value(sync_mode)

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

        return self._parse_response(response, model=Database)

    def delete(
        self,
        database_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a database by its unique ID. Only API keys with with databases.write scope can delete a database.

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

        api_path = '/vectorsdb/{databaseId}'
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
            },
            api_params,
        )

        return response

    def list_collections(
        self,
        database_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None,
    ) -> VectorsdbCollectionList:
        """
        Get a list of all collections that belong to the provided databaseId. You can use the search parameter to filter your results.

        Parameters
        ----------
        database_id : str
            Database ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, documentSecurity
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        VectorsdbCollectionList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
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

        return self._parse_response(response, model=VectorsdbCollectionList)

    def create_collection(
        self,
        database_id: str,
        collection_id: str,
        name: str,
        dimension: float,
        permissions: Optional[List[str]] = None,
        document_security: Optional[bool] = None,
        enabled: Optional[bool] = None,
    ) -> VectorsdbCollection:
        """
        Create a new Collection. Before using this route, you should create a new database resource using either a [server integration](https://appwrite.io/docs/server/databases#documentsDBCreateCollection) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Collection name. Max length: 128 chars.
        dimension : float
            Embedding dimension.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, no user is granted with any permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        document_security : Optional[bool]
            Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.
        Returns
        -------
        VectorsdbCollection
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if dimension is None:
            raise AppwriteException('Missing required parameter: "dimension"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_params['collectionId'] = self._normalize_value(collection_id)
        api_params['name'] = self._normalize_value(name)
        api_params['dimension'] = self._normalize_value(dimension)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if document_security is not None:
            api_params['documentSecurity'] = self._normalize_value(document_security)
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

        return self._parse_response(response, model=VectorsdbCollection)

    def get_collection(
        self,
        database_id: str,
        collection_id: str,
    ) -> VectorsdbCollection:
        """
        Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        Returns
        -------
        VectorsdbCollection
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=VectorsdbCollection)

    def update_collection(
        self,
        database_id: str,
        collection_id: str,
        name: str,
        dimension: Optional[float] = None,
        permissions: Optional[List[str]] = None,
        document_security: Optional[bool] = None,
        enabled: Optional[bool] = None,
    ) -> VectorsdbCollection:
        """
        Update a collection by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        name : str
            Collection name. Max length: 128 chars.
        dimension : Optional[float]
            Embedding dimensions.
        permissions : Optional[List[str]]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        document_security : Optional[bool]
            Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.
        Returns
        -------
        VectorsdbCollection
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_params['name'] = self._normalize_value(name)
        if dimension is not None:
            api_params['dimension'] = self._normalize_value(dimension)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if document_security is not None:
            api_params['documentSecurity'] = self._normalize_value(document_security)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

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

        return self._parse_response(response, model=VectorsdbCollection)

    def delete_collection(
        self,
        database_id: str,
        collection_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
            },
            api_params,
        )

        return response

    def list_documents(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        total: Optional[bool] = None,
        ttl: Optional[float] = None,
        model_type: Type[T] = dict,
    ) -> DocumentList[T]:
        """
        Get a list of all the user's documents in a given collection. You can use the query params to filter your results.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 524288 characters long.
        transaction_id : Optional[str]
            Transaction ID to read uncommitted changes within the transaction.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        ttl : Optional[float]
            TTL (seconds) for cached responses when caching is enabled for select queries. Must be between 0 and 86400 (24 hours).
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        DocumentList[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)
        if total is not None:
            api_params['total'] = self._normalize_value(total)
        if ttl is not None:
            api_params['ttl'] = self._normalize_value(ttl)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return DocumentList.with_data(response, model_type)

    def create_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        data: Dict[str, Any],
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> Document[T]:
        """
        Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#documentsDBCreateCollection) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection). Make sure to define attributes before creating documents.
        document_id : str
            Document ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        data : Dict[str, Any]
            Document data as JSON object.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        Document[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')
        if data is None:
            raise AppwriteException('Missing required parameter: "data"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_params['documentId'] = self._normalize_value(document_id)
        api_params['data'] = self._normalize_value(data)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

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

        return Document.with_data(response, model_type)

    def create_documents(
        self,
        database_id: str,
        collection_id: str,
        documents: List[Dict[str, Any]],
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> DocumentList[T]:
        """
        Create new Documents. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#documentsDBCreateCollection) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection). Make sure to define attributes before creating documents.
        documents : List[Dict[str, Any]]
            Array of documents data as JSON objects.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        DocumentList[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if documents is None:
            raise AppwriteException('Missing required parameter: "documents"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_params['documents'] = self._normalize_value(documents)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

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

        return DocumentList.with_data(response, model_type)

    def upsert_documents(
        self,
        database_id: str,
        collection_id: str,
        documents: List[Dict[str, Any]],
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> DocumentList[T]:
        """
        Create or update Documents. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#documentsDBCreateCollection) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        documents : List[Dict[str, Any]]
            Array of document data as JSON objects. May contain partial documents.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        DocumentList[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if documents is None:
            raise AppwriteException('Missing required parameter: "documents"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_params['documents'] = self._normalize_value(documents)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

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

        return DocumentList.with_data(response, model_type)

    def update_documents(
        self,
        database_id: str,
        collection_id: str,
        data: Optional[Dict[str, Any]] = None,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> DocumentList[T]:
        """
        Update all documents that match your queries, if no queries are submitted then all documents are updated. You can pass only specific fields to be updated.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        data : Optional[Dict[str, Any]]
            Document data as JSON object. Include only attribute and value pairs to be updated.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        DocumentList[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

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

        return DocumentList.with_data(response, model_type)

    def delete_documents(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> DocumentList[T]:
        """
        Bulk delete documents using queries, if no queries are passed then all documents are deleted.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        DocumentList[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

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

        return DocumentList.with_data(response, model_type)

    def create_query(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        total: Optional[bool] = None,
        ttl: Optional[float] = None,
        model_type: Type[T] = dict,
    ) -> DocumentList[T]:
        """
        Get a list of all the user's documents in a given collection using a POST request. This behaves identically to the list documents endpoint but accepts the queries in the request body, allowing much larger `queries` arrays than can fit in a URL query string.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 524288 characters long.
        transaction_id : Optional[str]
            Transaction ID to read uncommitted changes within the transaction.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        ttl : Optional[float]
            TTL (seconds) for cached responses when caching is enabled for select queries. Must be between 0 and 86400 (24 hours).
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        DocumentList[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents/query'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)
        if total is not None:
            api_params['total'] = self._normalize_value(total)
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

        return DocumentList.with_data(response, model_type)

    def get_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> Document[T]:
        """
        Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        document_id : str
            Document ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        transaction_id : Optional[str]
            Transaction ID to read uncommitted changes within the transaction.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        Document[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return Document.with_data(response, model_type)

    def upsert_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        data: Optional[Dict[str, Any]] = None,
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> Document[T]:
        """
        Create or update a Document. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#documentsDBCreateCollection) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        document_id : str
            Document ID.
        data : Optional[Dict[str, Any]]
            Document data as JSON object. Include all required fields of the document to be created or updated.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        Document[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))
        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

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

        return Document.with_data(response, model_type)

    def update_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        data: Optional[Dict[str, Any]] = None,
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict,
    ) -> Document[T]:
        """
        Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        document_id : str
            Document ID.
        data : Optional[Dict[str, Any]]
            Document data as JSON object. Include only fields and value pairs to be updated.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.

        Returns
        -------
        Document[T]
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))
        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

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

        return Document.with_data(response, model_type)

    def delete_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        transaction_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Delete a document by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        document_id : str
            Document ID.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
            },
            api_params,
        )

        return response

    def list_indexes(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> IndexList:
        """
        List indexes in the collection.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, status, attributes, error
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        IndexList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/indexes'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
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

        return self._parse_response(response, model=IndexList)

    def create_index(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        type: VectorsDBIndexType,
        attributes: List[str],
        orders: Optional[List[OrderBy]] = None,
        lengths: Optional[List[float]] = None,
    ) -> Index:
        """
        Creates an index on the attributes listed. Your index should include all the attributes you will query in a single request.
        Attributes can be `key`, `fulltext`, and `unique`.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Index Key.
        type : VectorsDBIndexType
            Index type.
        attributes : List[str]
            Array of attributes to index. Maximum of 100 attributes are allowed, each 32 characters long.
        orders : Optional[List[OrderBy]]
            Array of index orders. Maximum of 100 orders are allowed.
        lengths : Optional[List[float]]
            Length of index. Maximum of 100
        Returns
        -------
        Index
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/indexes'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if key is None:
            raise AppwriteException('Missing required parameter: "key"')
        if type is None:
            raise AppwriteException('Missing required parameter: "type"')
        if attributes is None:
            raise AppwriteException('Missing required parameter: "attributes"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_params['key'] = self._normalize_value(key)
        api_params['type'] = self._normalize_value(type)
        api_params['attributes'] = self._normalize_value(attributes)
        if orders is not None:
            api_params['orders'] = self._normalize_value(orders)
        if lengths is not None:
            api_params['lengths'] = self._normalize_value(lengths)

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

        return self._parse_response(response, model=Index)

    def get_index(
        self,
        database_id: str,
        collection_id: str,
        key: str,
    ) -> Index:
        """
        Get index by ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Index Key.
        Returns
        -------
        Index
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/indexes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if key is None:
            raise AppwriteException('Missing required parameter: "key"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Index)

    def delete_index(
        self,
        database_id: str,
        collection_id: str,
        key: str,
    ) -> Dict[str, Any]:
        """
        Delete an index.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Index Key.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/{databaseId}/collections/{collectionId}/indexes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')
        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')
        if key is None:
            raise AppwriteException('Missing required parameter: "key"')
        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
            },
            api_params,
        )

        return response

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

        api_path = '/vectorsdb/{databaseId}/failovers'
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

        api_path = '/vectorsdb/{databaseId}/operations'
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

        api_path = '/vectorsdb/{databaseId}/replicas'
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

        api_path = '/vectorsdb/{databaseId}/status'
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
