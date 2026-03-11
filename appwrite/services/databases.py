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
from ..models.attribute_list import AttributeList;
from ..models.attribute_boolean import AttributeBoolean;
from ..models.attribute_datetime import AttributeDatetime;
from ..models.attribute_email import AttributeEmail;
from ..models.attribute_enum import AttributeEnum;
from ..models.attribute_float import AttributeFloat;
from ..models.attribute_integer import AttributeInteger;
from ..models.attribute_ip import AttributeIp;
from ..models.attribute_line import AttributeLine;
from ..models.attribute_longtext import AttributeLongtext;
from ..models.attribute_mediumtext import AttributeMediumtext;
from ..models.attribute_point import AttributePoint;
from ..models.attribute_polygon import AttributePolygon;
from ..enums.relationship_type import RelationshipType;
from ..enums.relation_mutate import RelationMutate;
from ..models.attribute_relationship import AttributeRelationship;
from ..models.attribute_string import AttributeString;
from ..models.attribute_text import AttributeText;
from ..models.attribute_url import AttributeUrl;
from ..models.attribute_varchar import AttributeVarchar;
from ..models.document_list import DocumentList;
from ..models.document import Document;
from ..models.index_list import IndexList;
from ..enums.index_type import IndexType;
from ..enums.order_by import OrderBy;
from ..models.index import Index;

T = TypeVar('T')

class Databases(Service):

    def __init__(self, client) -> None:
        super(Databases, self).__init__(client)

    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.list` instead.")
    def list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> DatabaseList:
        """
        Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.list` instead.
        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name
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

        api_path = '/databases'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create` instead.")
    def create(
        self,
        database_id: str,
        name: str,
        enabled: Optional[bool] = None
    ) -> Database:
        """
        Create a new Database.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create` instead.
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

        api_path = '/databases'
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

        api_path = '/databases/transactions'
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

        api_path = '/databases/transactions'
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

        api_path = '/databases/transactions/{transactionId}'
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

        api_path = '/databases/transactions/{transactionId}'
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

        api_path = '/databases/transactions/{transactionId}'
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

        api_path = '/databases/transactions/{transactionId}/operations'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.get` instead.")
    def get(
        self,
        database_id: str
    ) -> Database:
        """
        Get a database by its unique ID. This endpoint response returns a JSON object with the database metadata.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.get` instead.
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

        api_path = '/databases/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Database)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update` instead.")
    def update(
        self,
        database_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> Database:
        """
        Update a database by its unique ID.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        name : Optional[str]
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

        api_path = '/databases/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Database)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.delete` instead.")
    def delete(
        self,
        database_id: str
    ) -> Dict[str, Any]:
        """
        Delete a database by its unique ID. Only API keys with with databases.write scope can delete a database.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.delete` instead.
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

        api_path = '/databases/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.list_tables` instead.")
    def list_collections(
        self,
        database_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> CollectionList:
        """
        Get a list of all collections that belong to the provided databaseId. You can use the search parameter to filter your results.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.list_tables` instead.
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

        api_path = '/databases/{databaseId}/collections'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_table` instead.")
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
        Create a new Collection. Before using this route, you should create a new database resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_table` instead.
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
            Array of attribute definitions to create. Each attribute should contain: key (string), type (string: string, integer, float, boolean, datetime), size (integer, required for string type), required (boolean, optional), default (mixed, optional), array (boolean, optional), and type-specific options.
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

        api_path = '/databases/{databaseId}/collections'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.get_table` instead.")
    def get_collection(
        self,
        database_id: str,
        collection_id: str
    ) -> Collection:
        """
        Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.get_table` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_table` instead.")
    def update_collection(
        self,
        database_id: str,
        collection_id: str,
        name: Optional[str] = None,
        permissions: Optional[List[str]] = None,
        document_security: Optional[bool] = None,
        enabled: Optional[bool] = None
    ) -> Collection:
        """
        Update a collection by its unique ID.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_table` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        name : Optional[str]
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

        api_path = '/databases/{databaseId}/collections/{collectionId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['permissions'] = self._normalize_value(permissions)
        if document_security is not None:
            api_params['documentSecurity'] = self._normalize_value(document_security)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Collection)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.delete_table` instead.")
    def delete_collection(
        self,
        database_id: str,
        collection_id: str
    ) -> Dict[str, Any]:
        """
        Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.delete_table` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.list_columns` instead.")
    def list_attributes(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> AttributeList:
        """
        List attributes in the collection.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.list_columns` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, size, required, array, status, error
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        AttributeList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes'
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

        return self._parse_response(response, model=AttributeList)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_boolean_column` instead.")
    def create_boolean_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[bool] = None,
        array: Optional[bool] = None
    ) -> AttributeBoolean:
        """
        Create a boolean attribute.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_boolean_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[bool]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeBoolean
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/boolean'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeBoolean)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_boolean_column` instead.")
    def update_boolean_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[bool],
        new_key: Optional[str] = None
    ) -> AttributeBoolean:
        """
        Update a boolean attribute. Changing the `default` value will not update already existing documents.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_boolean_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#createCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[bool]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New attribute key.
        
        Returns
        -------
        AttributeBoolean
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/boolean/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeBoolean)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_datetime_column` instead.")
    def create_datetime_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> AttributeDatetime:
        """
        Create a date time attribute according to the ISO 8601 standard.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_datetime_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#createCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for the attribute in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeDatetime
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/datetime'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeDatetime)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_datetime_column` instead.")
    def update_datetime_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeDatetime:
        """
        Update a date time attribute. Changing the `default` value will not update already existing documents.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_datetime_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New attribute key.
        
        Returns
        -------
        AttributeDatetime
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/datetime/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeDatetime)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_email_column` instead.")
    def create_email_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> AttributeEmail:
        """
        Create an email attribute.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_email_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeEmail
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/email'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeEmail)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_email_column` instead.")
    def update_email_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeEmail:
        """
        Update an email attribute. Changing the `default` value will not update already existing documents.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_email_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeEmail
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/email/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeEmail)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_enum_column` instead.")
    def create_enum_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        elements: List[str],
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> AttributeEnum:
        """
        Create an enum attribute. The `elements` param acts as a white-list of accepted values for this attribute. 
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_enum_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        elements : List[str]
            Array of enum values.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeEnum
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/enum'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None:
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['elements'] = self._normalize_value(elements)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeEnum)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_enum_column` instead.")
    def update_enum_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        elements: List[str],
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeEnum:
        """
        Update an enum attribute. Changing the `default` value will not update already existing documents.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_enum_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        elements : List[str]
            Updated list of enum values.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeEnum
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/enum/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None:
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['elements'] = self._normalize_value(elements)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeEnum)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_float_column` instead.")
    def create_float_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        min: Optional[float] = None,
        max: Optional[float] = None,
        default: Optional[float] = None,
        array: Optional[bool] = None
    ) -> AttributeFloat:
        """
        Create a float attribute. Optionally, minimum and maximum values can be provided.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_float_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        min : Optional[float]
            Minimum value.
        max : Optional[float]
            Maximum value.
        default : Optional[float]
            Default value. Cannot be set when required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeFloat
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/float'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['min'] = self._normalize_value(min)
        api_params['max'] = self._normalize_value(max)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeFloat)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_float_column` instead.")
    def update_float_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[float],
        min: Optional[float] = None,
        max: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> AttributeFloat:
        """
        Update a float attribute. Changing the `default` value will not update already existing documents.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_float_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[float]
            Default value. Cannot be set when required.
        min : Optional[float]
            Minimum value.
        max : Optional[float]
            Maximum value.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeFloat
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['min'] = self._normalize_value(min)
        api_params['max'] = self._normalize_value(max)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeFloat)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_integer_column` instead.")
    def create_integer_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        min: Optional[float] = None,
        max: Optional[float] = None,
        default: Optional[float] = None,
        array: Optional[bool] = None
    ) -> AttributeInteger:
        """
        Create an integer attribute. Optionally, minimum and maximum values can be provided.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_integer_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        min : Optional[float]
            Minimum value
        max : Optional[float]
            Maximum value
        default : Optional[float]
            Default value. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeInteger
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/integer'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['min'] = self._normalize_value(min)
        api_params['max'] = self._normalize_value(max)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeInteger)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_integer_column` instead.")
    def update_integer_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[float],
        min: Optional[float] = None,
        max: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> AttributeInteger:
        """
        Update an integer attribute. Changing the `default` value will not update already existing documents.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_integer_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[float]
            Default value. Cannot be set when attribute is required.
        min : Optional[float]
            Minimum value
        max : Optional[float]
            Maximum value
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeInteger
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/integer/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['min'] = self._normalize_value(min)
        api_params['max'] = self._normalize_value(max)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeInteger)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_ip_column` instead.")
    def create_ip_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> AttributeIp:
        """
        Create IP address attribute.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_ip_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeIp
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/ip'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeIp)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_ip_column` instead.")
    def update_ip_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeIp:
        """
        Update an ip attribute. Changing the `default` value will not update already existing documents.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_ip_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value. Cannot be set when attribute is required.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeIp
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/ip/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeIp)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_line_column` instead.")
    def create_line_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None
    ) -> AttributeLine:
        """
        Create a geometric line attribute.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_line_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[List[Any]]
            Default value for attribute when not provided, two-dimensional array of coordinate pairs, [[longitude, latitude], [longitude, latitude], …], listing the vertices of the line in order. Cannot be set when attribute is required.
        
        Returns
        -------
        AttributeLine
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/line'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeLine)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_line_column` instead.")
    def update_line_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None,
        new_key: Optional[str] = None
    ) -> AttributeLine:
        """
        Update a line attribute. Changing the `default` value will not update already existing documents.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_line_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#createCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[List[Any]]
            Default value for attribute when not provided, two-dimensional array of coordinate pairs, [[longitude, latitude], [longitude, latitude], …], listing the vertices of the line in order. Cannot be set when attribute is required.
        new_key : Optional[str]
            New attribute key.
        
        Returns
        -------
        AttributeLine
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/line/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeLine)


    def create_longtext_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> AttributeLongtext:
        """
        Create a longtext attribute.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        encrypt : Optional[bool]
            Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.
        
        Returns
        -------
        AttributeLongtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/longtext'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)
        if encrypt is not None:
            api_params['encrypt'] = self._normalize_value(encrypt)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeLongtext)


    def update_longtext_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeLongtext:
        """
        Update a longtext attribute. Changing the `default` value will not update already existing documents.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeLongtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/longtext/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeLongtext)


    def create_mediumtext_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> AttributeMediumtext:
        """
        Create a mediumtext attribute.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        encrypt : Optional[bool]
            Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.
        
        Returns
        -------
        AttributeMediumtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/mediumtext'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)
        if encrypt is not None:
            api_params['encrypt'] = self._normalize_value(encrypt)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeMediumtext)


    def update_mediumtext_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeMediumtext:
        """
        Update a mediumtext attribute. Changing the `default` value will not update already existing documents.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeMediumtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/mediumtext/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeMediumtext)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_point_column` instead.")
    def create_point_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None
    ) -> AttributePoint:
        """
        Create a geometric point attribute.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_point_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[List[Any]]
            Default value for attribute when not provided, array of two numbers [longitude, latitude], representing a single coordinate. Cannot be set when attribute is required.
        
        Returns
        -------
        AttributePoint
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/point'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributePoint)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_point_column` instead.")
    def update_point_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None,
        new_key: Optional[str] = None
    ) -> AttributePoint:
        """
        Update a point attribute. Changing the `default` value will not update already existing documents.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_point_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#createCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[List[Any]]
            Default value for attribute when not provided, array of two numbers [longitude, latitude], representing a single coordinate. Cannot be set when attribute is required.
        new_key : Optional[str]
            New attribute key.
        
        Returns
        -------
        AttributePoint
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/point/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributePoint)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_polygon_column` instead.")
    def create_polygon_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None
    ) -> AttributePolygon:
        """
        Create a geometric polygon attribute.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_polygon_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[List[Any]]
            Default value for attribute when not provided, three-dimensional array where the outer array holds one or more linear rings, [[[longitude, latitude], …], …], the first ring is the exterior boundary, any additional rings are interior holes, and each ring must start and end with the same coordinate pair. Cannot be set when attribute is required.
        
        Returns
        -------
        AttributePolygon
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/polygon'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributePolygon)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_polygon_column` instead.")
    def update_polygon_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None,
        new_key: Optional[str] = None
    ) -> AttributePolygon:
        """
        Update a polygon attribute. Changing the `default` value will not update already existing documents.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_polygon_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#createCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[List[Any]]
            Default value for attribute when not provided, three-dimensional array where the outer array holds one or more linear rings, [[[longitude, latitude], …], …], the first ring is the exterior boundary, any additional rings are interior holes, and each ring must start and end with the same coordinate pair. Cannot be set when attribute is required.
        new_key : Optional[str]
            New attribute key.
        
        Returns
        -------
        AttributePolygon
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/polygon/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributePolygon)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_relationship_column` instead.")
    def create_relationship_attribute(
        self,
        database_id: str,
        collection_id: str,
        related_collection_id: str,
        type: RelationshipType,
        two_way: Optional[bool] = None,
        key: Optional[str] = None,
        two_way_key: Optional[str] = None,
        on_delete: Optional[RelationMutate] = None
    ) -> AttributeRelationship:
        """
        Create relationship attribute. [Learn more about relationship attributes](https://appwrite.io/docs/databases-relationships#relationship-attributes).
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_relationship_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        related_collection_id : str
            Related Collection ID.
        type : RelationshipType
            Relation type
        two_way : Optional[bool]
            Is Two Way?
        key : Optional[str]
            Attribute Key.
        two_way_key : Optional[str]
            Two Way Attribute Key.
        on_delete : Optional[RelationMutate]
            Constraints option
        
        Returns
        -------
        AttributeRelationship
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/relationship'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if related_collection_id is None:
            raise AppwriteException('Missing required parameter: "related_collection_id"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['relatedCollectionId'] = self._normalize_value(related_collection_id)
        api_params['type'] = self._normalize_value(type)
        if two_way is not None:
            api_params['twoWay'] = self._normalize_value(two_way)
        api_params['key'] = self._normalize_value(key)
        api_params['twoWayKey'] = self._normalize_value(two_way_key)
        if on_delete is not None:
            api_params['onDelete'] = self._normalize_value(on_delete)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeRelationship)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_relationship_column` instead.")
    def update_relationship_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        on_delete: Optional[RelationMutate] = None,
        new_key: Optional[str] = None
    ) -> AttributeRelationship:
        """
        Update relationship attribute. [Learn more about relationship attributes](https://appwrite.io/docs/databases-relationships#relationship-attributes).
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_relationship_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        on_delete : Optional[RelationMutate]
            Constraints option
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeRelationship
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/relationship/{key}'
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

        if on_delete is not None:
            api_params['onDelete'] = self._normalize_value(on_delete)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeRelationship)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_string_column` instead.")
    def create_string_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        size: float,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> AttributeString:
        """
        Create a string attribute.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_string_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        size : float
            Attribute size for text attributes, in number of characters.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        encrypt : Optional[bool]
            Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.
        
        Returns
        -------
        AttributeString
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/string'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if size is None:
            raise AppwriteException('Missing required parameter: "size"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['size'] = self._normalize_value(size)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)
        if encrypt is not None:
            api_params['encrypt'] = self._normalize_value(encrypt)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeString)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_string_column` instead.")
    def update_string_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        size: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> AttributeString:
        """
        Update a string attribute. Changing the `default` value will not update already existing documents.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_string_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        size : Optional[float]
            Maximum size of the string attribute.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeString
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/string/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['size'] = self._normalize_value(size)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeString)


    def create_text_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> AttributeText:
        """
        Create a text attribute.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        encrypt : Optional[bool]
            Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.
        
        Returns
        -------
        AttributeText
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/text'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)
        if encrypt is not None:
            api_params['encrypt'] = self._normalize_value(encrypt)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeText)


    def update_text_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeText:
        """
        Update a text attribute. Changing the `default` value will not update already existing documents.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeText
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/text/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeText)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_url_column` instead.")
    def create_url_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> AttributeUrl:
        """
        Create a URL attribute.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_url_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        
        Returns
        -------
        AttributeUrl
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/url'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeUrl)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_url_column` instead.")
    def update_url_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> AttributeUrl:
        """
        Update an url attribute. Changing the `default` value will not update already existing documents.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_url_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeUrl
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/url/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeUrl)


    def create_varchar_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        size: float,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> AttributeVarchar:
        """
        Create a varchar attribute.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        size : float
            Attribute size for varchar attributes, in number of characters. Maximum size is 16381.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : Optional[bool]
            Is attribute an array?
        encrypt : Optional[bool]
            Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.
        
        Returns
        -------
        AttributeVarchar
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/varchar'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if size is None:
            raise AppwriteException('Missing required parameter: "size"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['size'] = self._normalize_value(size)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)
        if encrypt is not None:
            api_params['encrypt'] = self._normalize_value(encrypt)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeVarchar)


    def update_varchar_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        size: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> AttributeVarchar:
        """
        Update a varchar attribute. Changing the `default` value will not update already existing documents.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Attribute Key.
        required : bool
            Is attribute required?
        default : Optional[str]
            Default value for attribute when not provided. Cannot be set when attribute is required.
        size : Optional[float]
            Maximum size of the varchar attribute.
        new_key : Optional[str]
            New Attribute Key.
        
        Returns
        -------
        AttributeVarchar
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/varchar/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['size'] = self._normalize_value(size)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=AttributeVarchar)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.get_column` instead.")
    def get_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str
    ) -> Union[AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributeString]:
        """
        Get attribute by ID.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.get_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        
        Returns
        -------
        Union[AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributeString]
            API response as one of the typed response models
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
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

        return self._parse_response(response, union_models=(AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributeString, ))


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.delete_column` instead.")
    def delete_attribute(
        self,
        database_id: str,
        collection_id: str,
        key: str
    ) -> Dict[str, Any]:
        """
        Deletes an attribute.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.delete_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        key : str
            Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.list_rows` instead.")
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

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.list_rows` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_row` instead.")
    def create_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        data: Dict[str, Any],
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Document[T]:
        """
        Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_row` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
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
        api_params['permissions'] = self._normalize_value(permissions)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_rows` instead.")
    def create_documents(
        self,
        database_id: str,
        collection_id: str,
        documents: List[Dict[str, Any]],
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> DocumentList[T]:
        """
        Create new Documents. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_rows` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
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
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.upsert_rows` instead.")
    def upsert_documents(
        self,
        database_id: str,
        collection_id: str,
        documents: List[Dict[str, Any]],
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> DocumentList[T]:
        """
        Create or update Documents. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.upsert_rows` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
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
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_rows` instead.")
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

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_rows` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
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
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.delete_rows` instead.")
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

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.delete_rows` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{collectionId}', str(self._normalize_value(collection_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return DocumentList.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.get_row` instead.")
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

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.get_row` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.upsert_row` instead.")
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
        Create or update a Document. Before using this route, you should create a new collection resource using either a [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection) API or directly from your database console.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.upsert_row` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        document_id : str
            Document ID.
        data : Optional[Dict[str, Any]]
            Document data as JSON object. Include all required attributes of the document to be created or updated.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
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
        api_params['permissions'] = self._normalize_value(permissions)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_row` instead.")
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

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_row` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID.
        document_id : str
            Document ID.
        data : Optional[Dict[str, Any]]
            Document data as JSON object. Include only attribute and value pairs to be updated.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
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
        api_params['permissions'] = self._normalize_value(permissions)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.delete_row` instead.")
    def delete_document(
        self,
        database_id: str,
        collection_id: str,
        document_id: str,
        transaction_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Delete a document by its unique ID.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.delete_row` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
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

        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.decrement_row_column` instead.")
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
        Decrement a specific attribute of a document by a given value.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.decrement_row_column` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}/{attribute}/decrement'
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
        api_params['min'] = self._normalize_value(min)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.increment_row_column` instead.")
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
        Increment a specific attribute of a document by a given value.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.increment_row_column` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}/{attribute}/increment'
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
        api_params['max'] = self._normalize_value(max)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Document.with_data(response, model_type)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.list_indexes` instead.")
    def list_indexes(
        self,
        database_id: str,
        collection_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> IndexList:
        """
        List indexes in the collection.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.list_indexes` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.create_index` instead.")
    def create_index(
        self,
        database_id: str,
        collection_id: str,
        key: str,
        type: IndexType,
        attributes: List[str],
        orders: Optional[List[OrderBy]] = None,
        lengths: Optional[List[float]] = None
    ) -> Index:
        """
        Creates an index on the attributes listed. Your index should include all the attributes you will query in a single request.
        Attributes can be `key`, `fulltext`, and `unique`.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_index` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        collection_id : str
            Collection ID. You can create a new collection using the Database service [server integration](https://appwrite.io/docs/server/databases#databasesCreateCollection).
        key : str
            Index Key.
        type : IndexType
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.get_index` instead.")
    def get_index(
        self,
        database_id: str,
        collection_id: str,
        key: str
    ) -> Index:
        """
        Get an index by its unique ID.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.get_index` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
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


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.delete_index` instead.")
    def delete_index(
        self,
        database_id: str,
        collection_id: str,
        key: str
    ) -> Dict[str, Any]:
        """
        Delete an index.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.delete_index` instead.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/indexes/{key}'
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

