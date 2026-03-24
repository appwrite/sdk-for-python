from ..service import Service
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.database_list import DatabaseList;
from ..models.database import Database;
from ..enums.model import Model;
from ..models.embedding_list import EmbeddingList;
from ..models.transaction_list import TransactionList;
from ..models.transaction import Transaction;
from ..models.vectorsdb_collection_list import VectorsdbCollectionList;
from ..models.vectorsdb_collection import VectorsdbCollection;
from ..models.document_list import DocumentList;
from ..models.document import Document;
from ..models.index_list import IndexList;
from ..enums.vectors_db_index_type import VectorsDBIndexType;
from ..enums.order_by import OrderBy;
from ..models.index import Index;

T = TypeVar('T')

class VectorsDB(Service):

    def __init__(self, client) -> None:
        super(VectorsDB, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> DatabaseList:
        """
        

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

        api_path = '/vectorsdb'
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

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Database)


    def create_text_embeddings(
        self,
        texts: List[str],
        model: Optional[Model] = None
    ) -> EmbeddingList:
        """
        

        Parameters
        ----------
        texts : List[str]
            Array of text to generate embeddings.
        model : Optional[Model]
            The embedding model to use for generating vector embeddings.
        
        Returns
        -------
        EmbeddingList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/vectorsdb/embeddings/text'
        api_params = {}
        if texts is None:
            raise AppwriteException('Missing required parameter: "texts"')


        api_params['texts'] = self._normalize_value(texts)
        if model is not None:
            api_params['model'] = self._normalize_value(model)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=EmbeddingList)


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

        api_path = '/vectorsdb/transactions'
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

        api_path = '/vectorsdb/transactions'
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

        api_path = '/vectorsdb/transactions/{transactionId}'
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

        api_path = '/vectorsdb/transactions/{transactionId}'
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

        api_path = '/vectorsdb/transactions/{transactionId}'
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

        api_path = '/vectorsdb/transactions/{transactionId}/operations'
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

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Database)


    def delete(
        self,
        database_id: str
    ) -> Dict[str, Any]:
        """
        

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
    ) -> VectorsdbCollectionList:
        """
        

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

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VectorsdbCollectionList)


    def create_collection(
        self,
        database_id: str,
        collection_id: str,
        name: str,
        dimension: float,
        permissions: Optional[List[str]] = None,
        document_security: Optional[bool] = None,
        enabled: Optional[bool] = None
    ) -> VectorsdbCollection:
        """
        

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

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=VectorsdbCollection)


    def get_collection(
        self,
        database_id: str,
        collection_id: str
    ) -> VectorsdbCollection:
        """
        

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


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VectorsdbCollection)


    def update_collection(
        self,
        database_id: str,
        collection_id: str,
        name: str,
        dimension: Optional[float] = None,
        permissions: Optional[List[str]] = None,
        document_security: Optional[bool] = None,
        enabled: Optional[bool] = None
    ) -> VectorsdbCollection:
        """
        

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

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=VectorsdbCollection)


    def delete_collection(
        self,
        database_id: str,
        collection_id: str
    ) -> Dict[str, Any]:
        """
        

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

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_indexes(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> IndexList:
        """
        

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

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=IndexList)


    def create_index(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        type: VectorsDBIndexType,
        attributes: List[str],
        orders: Optional[List[OrderBy]] = None,
        lengths: Optional[List[float]] = None
    ) -> Index:
        """
        

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


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

