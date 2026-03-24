from ..service import Service
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.database_list import DatabaseList;
from ..models.database import Database;
from ..models.transaction_list import TransactionList;
from ..models.transaction import Transaction;
from ..models.collection_list import CollectionList;
from ..models.collection import Collection;
from ..models.document_list import DocumentList;
from ..models.document import Document;
from ..models.index_list import IndexList;
from ..enums.documents_db_index_type import DocumentsDBIndexType;
from ..enums.order_by import OrderBy;
from ..models.index import Index;

T = TypeVar('T')

class DocumentsDB(Service):

    def __init__(self, client) -> None:
        super(DocumentsDB, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> DatabaseList:
        """
        Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: name
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
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

        api_path = '/documentsdb'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=DatabaseList)


    def create(
        self,
        database_id: str,
        name: str,
        enabled: Optional[bool] = None
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
        
        Returns
        -------
        Database
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/documentsdb'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['databaseId'] = self._normalize_value(database_id)
        api_params['name'] = self._normalize_value(name)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Database)


    def list_transactions(
        self,
        queries: Optional[List[str]] = None
    ) -> TransactionList:
        """
        

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

        api_path = '/documentsdb/transactions'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=TransactionList)


    def create_transaction(
        self,
        ttl: Optional[float] = None
    ) -> Transaction:
        """
        

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

        api_path = '/documentsdb/transactions'
        api_params = {}

        if ttl is not None:
            api_params['ttl'] = self._normalize_value(ttl)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Transaction)


    def get_transaction(
        self,
        transaction_id: str
    ) -> Transaction:
        """
        

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

        api_path = '/documentsdb/transactions/{transactionId}'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')

        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Transaction)


    def update_transaction(
        self,
        transaction_id: str,
        commit: Optional[bool] = None,
        rollback: Optional[bool] = None
    ) -> Transaction:
        """
        

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

        api_path = '/documentsdb/transactions/{transactionId}'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')

        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))

        if commit is not None:
            api_params['commit'] = self._normalize_value(commit)
        if rollback is not None:
            api_params['rollback'] = self._normalize_value(rollback)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Transaction)


    def delete_transaction(
        self,
        transaction_id: str
    ) -> Dict[str, Any]:
        """
        

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

        api_path = '/documentsdb/transactions/{transactionId}'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')

        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def create_operations(
        self,
        transaction_id: str,
        operations: Optional[List[Dict[str, Any]]] = None
    ) -> Transaction:
        """
        

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

        api_path = '/documentsdb/transactions/{transactionId}/operations'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')

        api_path = api_path.replace('{transactionId}', str(self._normalize_value(transaction_id)))

        if operations is not None:
            api_params['operations'] = self._normalize_value(operations)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Transaction)


    def get(
        self,
        database_id: str
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

        api_path = '/documentsdb/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Database)


    def update(
        self,
        database_id: str,
        name: str,
        enabled: Optional[bool] = None
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
        
        Returns
        -------
        Database
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/documentsdb/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        api_params['name'] = self._normalize_value(name)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Database)


    def delete(
        self,
        database_id: str
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

        api_path = '/documentsdb/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_collections(
        self,
        database_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> CollectionList:
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
        CollectionList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/documentsdb/{databaseId}/collections'
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

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=CollectionList)


    def create_collection(
        self,
        database_id: str,
        collection_id: str,
        name: str,
        permissions: Optional[List[str]] = None,
        document_security: Optional[bool] = None,
        enabled: Optional[bool] = None,
        attributes: Optional[List[Dict[str, Any]]] = None,
        indexes: Optional[List[Dict[str, Any]]] = None
    ) -> Collection:
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
        permissions : Optional[List[str]]
            An array of permissions strings. By default, no user is granted with any permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        document_security : Optional[bool]
            Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.
        attributes : Optional[List[Dict[str, Any]]]
            Array of attribute definitions to create. Each attribute should contain: key (string), type (string: string, integer, float, boolean, datetime, relationship), size (integer, required for string type), required (boolean, optional), default (mixed, optional), array (boolean, optional), and type-specific options.
        indexes : Optional[List[Dict[str, Any]]]
            Array of index definitions to create. Each index should contain: key (string), type (string: key, fulltext, unique, spatial), attributes (array of attribute keys), orders (array of ASC/DESC, optional), and lengths (array of integers, optional).
        
        Returns
        -------
        Collection
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/documentsdb/{databaseId}/collections'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        api_params['collectionId'] = self._normalize_value(collection_id)
        api_params['name'] = self._normalize_value(name)
        api_params['permissions'] = self._normalize_value(permissions)
        if document_security is not None:
            api_params['documentSecurity'] = self._normalize_value(document_security)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if attributes is not None:
            api_params['attributes'] = self._normalize_value(attributes)
        if indexes is not None:
            api_params['indexes'] = self._normalize_value(indexes)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Collection)


    def get_collection(
        self,
        database_id: str,
        collection_id: str
    ) -> Collection:
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
        Collection
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Collection)


    def update_collection(
        self,
        database_id: str,
        collection_id: str,
        name: str,
        permissions: Optional[List[str]] = None,
        document_security: Optional[bool] = None,
        enabled: Optional[bool] = None
    ) -> Collection:
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
        permissions : Optional[List[str]]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        document_security : Optional[bool]
            Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.
        
        Returns
        -------
        Collection
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}'
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
        if permissions is not None:
            api_params['permissions'] = self._normalize_value(permissions)
        if document_security is not None:
            api_params['documentSecurity'] = self._normalize_value(document_security)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Collection)


    def delete_collection(
        self,
        database_id: str,
        collection_id: str
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_documents(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        total: Optional[bool] = None,
        ttl: Optional[float] = None,
        model_type: Type[T] = dict
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
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents'
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

        response = self.client.call('get', api_path, {
        }, api_params)

        return DocumentList.with_data(response, model_type)


    def create_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        data: Dict[str, Any],
        permissions: Optional[List[str]] = None,
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents'
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

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    def create_documents(
        self,
        database_id: str,
        collection_id: str,
        documents: List[Dict[str, Any]],
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents'
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

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    def upsert_documents(
        self,
        database_id: str,
        collection_id: str,
        documents: List[Dict[str, Any]],
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents'
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

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    def update_documents(
        self,
        database_id: str,
        collection_id: str,
        data: Optional[Dict[str, Any]] = None,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents'
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

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    def delete_documents(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents'
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

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    def get_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
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

        response = self.client.call('get', api_path, {
        }, api_params)

        return Document.with_data(response, model_type)


    def upsert_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        data: Optional[Dict[str, Any]] = None,
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
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

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    def update_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        data: Optional[Dict[str, Any]] = None,
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
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

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    def delete_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        transaction_id: Optional[str] = None
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents/{documentId}'
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

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def decrement_document_attribute(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        attribute: str,
        value: Optional[float] = None,
        min: Optional[float] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Document[T]:
        """
        Decrement a specific column of a row by a given value.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        document_id : str
            Document ID.
        attribute : str
            Attribute key.
        value : Optional[float]
            Value to decrement the attribute by. The value must be a number.
        min : Optional[float]
            Minimum value for the attribute. If the current value is lesser than this value, an exception will be thrown.
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents/{documentId}/{attribute}/decrement'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        if attribute is None:
            raise AppwriteException('Missing required parameter: "attribute"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))
        api_path = api_path.replace('{attribute}', str(self._normalize_value(attribute)))

        if value is not None:
            api_params['value'] = self._normalize_value(value)
        if min is not None:
            api_params['min'] = self._normalize_value(min)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    def increment_document_attribute(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        attribute: str,
        value: Optional[float] = None,
        max: Optional[float] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Document[T]:
        """
        Increment a specific column of a row by a given value.

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        document_id : str
            Document ID.
        attribute : str
            Attribute key.
        value : Optional[float]
            Value to increment the attribute by. The value must be a number.
        max : Optional[float]
            Maximum value for the attribute. If the current value is greater than this value, an error will be thrown.
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/documents/{documentId}/{attribute}/increment'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        if attribute is None:
            raise AppwriteException('Missing required parameter: "attribute"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{documentId}', str(self._normalize_value(document_id)))
        api_path = api_path.replace('{attribute}', str(self._normalize_value(attribute)))

        if value is not None:
            api_params['value'] = self._normalize_value(value)
        if max is not None:
            api_params['max'] = self._normalize_value(max)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    def list_indexes(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/indexes'
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

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=IndexList)


    def create_index(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        type: DocumentsDBIndexType,
        attributes: List[str],
        orders: Optional[List[OrderBy]] = None,
        lengths: Optional[List[float]] = None
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
        type : DocumentsDBIndexType
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/indexes'
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

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Index)


    def get_index(
        self,
        database_id: str,
        collection_id: str,
        key: str
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/indexes/{key}'
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


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Index)


    def delete_index(
        self,
        database_id: str,
        collection_id: str,
        key: str
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

        api_path = '/documentsdb/{databaseId}/collections/{collectionId}/indexes/{key}'
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


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

