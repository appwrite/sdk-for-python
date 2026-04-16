from ..service import Service
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.database_list import DatabaseList;
from ..models.database import Database;
from ..models.transaction_list import TransactionList;
from ..models.transaction import Transaction;
from ..models.table_list import TableList;
from ..models.table import Table;
from ..models.column_list import ColumnList;
from ..models.column_boolean import ColumnBoolean;
from ..models.column_datetime import ColumnDatetime;
from ..models.column_email import ColumnEmail;
from ..models.column_enum import ColumnEnum;
from ..models.column_float import ColumnFloat;
from ..models.column_integer import ColumnInteger;
from ..models.column_ip import ColumnIp;
from ..models.column_line import ColumnLine;
from ..models.column_longtext import ColumnLongtext;
from ..models.column_mediumtext import ColumnMediumtext;
from ..models.column_point import ColumnPoint;
from ..models.column_polygon import ColumnPolygon;
from ..enums.relationship_type import RelationshipType;
from ..enums.relation_mutate import RelationMutate;
from ..models.column_relationship import ColumnRelationship;
from ..models.column_string import ColumnString;
from ..models.column_text import ColumnText;
from ..models.column_url import ColumnUrl;
from ..models.column_varchar import ColumnVarchar;
from ..models.column_index_list import ColumnIndexList;
from ..enums.tables_db_index_type import TablesDBIndexType;
from ..enums.order_by import OrderBy;
from ..models.column_index import ColumnIndex;
from ..models.row_list import RowList;
from ..models.row import Row;

T = TypeVar('T')

class TablesDB(Service):

    def __init__(self, client) -> None:
        super(TablesDB, self).__init__(client)

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

        api_path = '/tablesdb'
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

        api_path = '/tablesdb'
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

        api_path = '/tablesdb/transactions'
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

        api_path = '/tablesdb/transactions'
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

        api_path = '/tablesdb/transactions/{transactionId}'
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

        api_path = '/tablesdb/transactions/{transactionId}'
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

        api_path = '/tablesdb/transactions/{transactionId}'
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

        api_path = '/tablesdb/transactions/{transactionId}/operations'
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

        api_path = '/tablesdb/{databaseId}'
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
        name: Optional[str] = None,
        enabled: Optional[bool] = None
    ) -> Database:
        """
        Update a database by its unique ID.

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

        api_path = '/tablesdb/{databaseId}'
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

        api_path = '/tablesdb/{databaseId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_tables(
        self,
        database_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None
    ) -> TableList:
        """
        Get a list of all tables that belong to the provided databaseId. You can use the search parameter to filter your results.

        Parameters
        ----------
        database_id : str
            Database ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: name, enabled, rowSecurity
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        TableList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables'
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

        return self._parse_response(response, model=TableList)


    def create_table(
        self,
        database_id: str,
        table_id: str,
        name: str,
        permissions: Optional[List[str]] = None,
        row_security: Optional[bool] = None,
        enabled: Optional[bool] = None,
        columns: Optional[List[Dict[str, Any]]] = None,
        indexes: Optional[List[Dict[str, Any]]] = None
    ) -> Table:
        """
        Create a new Table. Before using this route, you should create a new database resource using either a [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Table name. Max length: 128 chars.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, no user is granted with any permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        row_security : Optional[bool]
            Enables configuring permissions for individual rows. A user needs one of row or table level permissions to access a row. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is table enabled? When set to 'disabled', users cannot access the table but Server SDKs with and API key can still read and write to the table. No data is lost when this is toggled.
        columns : Optional[List[Dict[str, Any]]]
            Array of column definitions to create. Each column should contain: key (string), type (string: string, integer, float, boolean, datetime, relationship), size (integer, required for string type), required (boolean, optional), default (mixed, optional), array (boolean, optional), and type-specific options.
        indexes : Optional[List[Dict[str, Any]]]
            Array of index definitions to create. Each index should contain: key (string), type (string: key, fulltext, unique, spatial), attributes (array of column keys), orders (array of ASC/DESC, optional), and lengths (array of integers, optional).
        
        Returns
        -------
        Table
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))

        api_params['tableId'] = self._normalize_value(table_id)
        api_params['name'] = self._normalize_value(name)
        api_params['permissions'] = self._normalize_value(permissions)
        if row_security is not None:
            api_params['rowSecurity'] = self._normalize_value(row_security)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if columns is not None:
            api_params['columns'] = self._normalize_value(columns)
        if indexes is not None:
            api_params['indexes'] = self._normalize_value(indexes)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Table)


    def get_table(
        self,
        database_id: str,
        table_id: str
    ) -> Table:
        """
        Get a table by its unique ID. This endpoint response returns a JSON object with the table metadata.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        
        Returns
        -------
        Table
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Table)


    def update_table(
        self,
        database_id: str,
        table_id: str,
        name: Optional[str] = None,
        permissions: Optional[List[str]] = None,
        row_security: Optional[bool] = None,
        enabled: Optional[bool] = None,
        purge: Optional[bool] = None
    ) -> Table:
        """
        Update a table by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        name : Optional[str]
            Table name. Max length: 128 chars.
        permissions : Optional[List[str]]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        row_security : Optional[bool]
            Enables configuring permissions for individual rows. A user needs one of row or table-level permissions to access a row. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is table enabled? When set to 'disabled', users cannot access the table but Server SDKs with and API key can still read and write to the table. No data is lost when this is toggled.
        purge : Optional[bool]
            When true, purge all cached list responses for this table as part of the update. Use this to force readers to see fresh data immediately instead of waiting for the cache TTL to expire.
        
        Returns
        -------
        Table
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['permissions'] = self._normalize_value(permissions)
        if row_security is not None:
            api_params['rowSecurity'] = self._normalize_value(row_security)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if purge is not None:
            api_params['purge'] = self._normalize_value(purge)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Table)


    def delete_table(
        self,
        database_id: str,
        table_id: str
    ) -> Dict[str, Any]:
        """
        Delete a table by its unique ID. Only users with write permissions have access to delete this resource.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_columns(
        self,
        database_id: str,
        table_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> ColumnList:
        """
        List columns in the table.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: key, type, size, required, array, status, error
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ColumnList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ColumnList)


    def create_boolean_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[bool] = None,
        array: Optional[bool] = None
    ) -> ColumnBoolean:
        """
        Create a boolean column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[bool]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnBoolean
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/boolean'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnBoolean)


    def update_boolean_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[bool],
        new_key: Optional[str] = None
    ) -> ColumnBoolean:
        """
        Update a boolean column. Changing the `default` value will not update already existing rows.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[bool]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnBoolean
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/boolean/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnBoolean)


    def create_datetime_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> ColumnDatetime:
        """
        Create a date time column according to the ISO 8601 standard.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for the column in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnDatetime
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/datetime'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnDatetime)


    def update_datetime_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnDatetime:
        """
        Update a date time column. Changing the `default` value will not update already existing rows.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnDatetime
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/datetime/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnDatetime)


    def create_email_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> ColumnEmail:
        """
        Create an email column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnEmail
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/email'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnEmail)


    def update_email_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnEmail:
        """
        Update an email column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnEmail
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/email/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnEmail)


    def create_enum_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        elements: List[str],
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> ColumnEnum:
        """
        Create an enumeration column. The `elements` param acts as a white-list of accepted values for this column.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        elements : List[str]
            Array of enum values.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnEnum
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/enum'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None:
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['elements'] = self._normalize_value(elements)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnEnum)


    def update_enum_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        elements: List[str],
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnEnum:
        """
        Update an enum column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        elements : List[str]
            Updated list of enum values.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnEnum
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/enum/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if elements is None:
            raise AppwriteException('Missing required parameter: "elements"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['elements'] = self._normalize_value(elements)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnEnum)


    def create_float_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        min: Optional[float] = None,
        max: Optional[float] = None,
        default: Optional[float] = None,
        array: Optional[bool] = None
    ) -> ColumnFloat:
        """
        Create a float column. Optionally, minimum and maximum values can be provided.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        min : Optional[float]
            Minimum value
        max : Optional[float]
            Maximum value
        default : Optional[float]
            Default value. Cannot be set when required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnFloat
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/float'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return self._parse_response(response, model=ColumnFloat)


    def update_float_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[float],
        min: Optional[float] = None,
        max: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> ColumnFloat:
        """
        Update a float column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[float]
            Default value. Cannot be set when required.
        min : Optional[float]
            Minimum value
        max : Optional[float]
            Maximum value
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnFloat
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/float/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['min'] = self._normalize_value(min)
        api_params['max'] = self._normalize_value(max)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnFloat)


    def create_integer_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        min: Optional[float] = None,
        max: Optional[float] = None,
        default: Optional[float] = None,
        array: Optional[bool] = None
    ) -> ColumnInteger:
        """
        Create an integer column. Optionally, minimum and maximum values can be provided.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        min : Optional[float]
            Minimum value
        max : Optional[float]
            Maximum value
        default : Optional[float]
            Default value. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnInteger
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/integer'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return self._parse_response(response, model=ColumnInteger)


    def update_integer_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[float],
        min: Optional[float] = None,
        max: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> ColumnInteger:
        """
        Update an integer column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[float]
            Default value. Cannot be set when column is required.
        min : Optional[float]
            Minimum value
        max : Optional[float]
            Maximum value
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnInteger
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/integer/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['min'] = self._normalize_value(min)
        api_params['max'] = self._normalize_value(max)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnInteger)


    def create_ip_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> ColumnIp:
        """
        Create IP address column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnIp
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/ip'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnIp)


    def update_ip_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnIp:
        """
        Update an ip column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnIp
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/ip/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnIp)


    def create_line_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None
    ) -> ColumnLine:
        """
        Create a geometric line column.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[List[Any]]
            Default value for column when not provided, two-dimensional array of coordinate pairs, [[longitude, latitude], [longitude, latitude], …], listing the vertices of the line in order. Cannot be set when column is required.
        
        Returns
        -------
        ColumnLine
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/line'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnLine)


    def update_line_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None,
        new_key: Optional[str] = None
    ) -> ColumnLine:
        """
        Update a line column. Changing the `default` value will not update already existing rows.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[List[Any]]
            Default value for column when not provided, two-dimensional array of coordinate pairs, [[longitude, latitude], [longitude, latitude], …], listing the vertices of the line in order. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnLine
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/line/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnLine)


    def create_longtext_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> ColumnLongtext:
        """
        Create a longtext column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        encrypt : Optional[bool]
            Toggle encryption for the column. Encryption enhances security by not storing any plain text values in the database. However, encrypted columns cannot be queried.
        
        Returns
        -------
        ColumnLongtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/longtext'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return self._parse_response(response, model=ColumnLongtext)


    def update_longtext_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnLongtext:
        """
        Update a longtext column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnLongtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/longtext/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnLongtext)


    def create_mediumtext_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> ColumnMediumtext:
        """
        Create a mediumtext column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        encrypt : Optional[bool]
            Toggle encryption for the column. Encryption enhances security by not storing any plain text values in the database. However, encrypted columns cannot be queried.
        
        Returns
        -------
        ColumnMediumtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/mediumtext'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return self._parse_response(response, model=ColumnMediumtext)


    def update_mediumtext_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnMediumtext:
        """
        Update a mediumtext column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnMediumtext
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/mediumtext/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnMediumtext)


    def create_point_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None
    ) -> ColumnPoint:
        """
        Create a geometric point column.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[List[Any]]
            Default value for column when not provided, array of two numbers [longitude, latitude], representing a single coordinate. Cannot be set when column is required.
        
        Returns
        -------
        ColumnPoint
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/point'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnPoint)


    def update_point_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None,
        new_key: Optional[str] = None
    ) -> ColumnPoint:
        """
        Update a point column. Changing the `default` value will not update already existing rows.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[List[Any]]
            Default value for column when not provided, array of two numbers [longitude, latitude], representing a single coordinate. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnPoint
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/point/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnPoint)


    def create_polygon_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None
    ) -> ColumnPolygon:
        """
        Create a geometric polygon column.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[List[Any]]
            Default value for column when not provided, three-dimensional array where the outer array holds one or more linear rings, [[[longitude, latitude], …], …], the first ring is the exterior boundary, any additional rings are interior holes, and each ring must start and end with the same coordinate pair. Cannot be set when column is required.
        
        Returns
        -------
        ColumnPolygon
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/polygon'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnPolygon)


    def update_polygon_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[List[Any]] = None,
        new_key: Optional[str] = None
    ) -> ColumnPolygon:
        """
        Update a polygon column. Changing the `default` value will not update already existing rows.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[List[Any]]
            Default value for column when not provided, three-dimensional array where the outer array holds one or more linear rings, [[[longitude, latitude], …], …], the first ring is the exterior boundary, any additional rings are interior holes, and each ring must start and end with the same coordinate pair. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnPolygon
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/polygon/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnPolygon)


    def create_relationship_column(
        self,
        database_id: str,
        table_id: str,
        related_table_id: str,
        type: RelationshipType,
        two_way: Optional[bool] = None,
        key: Optional[str] = None,
        two_way_key: Optional[str] = None,
        on_delete: Optional[RelationMutate] = None
    ) -> ColumnRelationship:
        """
        Create relationship column. [Learn more about relationship columns](https://appwrite.io/docs/databases-relationships#relationship-columns).
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        related_table_id : str
            Related Table ID.
        type : RelationshipType
            Relation type
        two_way : Optional[bool]
            Is Two Way?
        key : Optional[str]
            Column Key.
        two_way_key : Optional[str]
            Two Way Column Key.
        on_delete : Optional[RelationMutate]
            Constraints option
        
        Returns
        -------
        ColumnRelationship
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/relationship'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if related_table_id is None:
            raise AppwriteException('Missing required parameter: "related_table_id"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['relatedTableId'] = self._normalize_value(related_table_id)
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

        return self._parse_response(response, model=ColumnRelationship)


    @deprecated("This API has been deprecated since 1.9.0. Please use `tablesDB.create_text_column` instead.")
    def create_string_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        size: float,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> ColumnString:
        """
        Create a string column.
        

        .. deprecated::1.9.0
            This API has been deprecated since 1.9.0. Please use `tablesDB.create_text_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        size : float
            Column size for text columns, in number of characters.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        encrypt : Optional[bool]
            Toggle encryption for the column. Encryption enhances security by not storing any plain text values in the database. However, encrypted columns cannot be queried.
        
        Returns
        -------
        ColumnString
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/string'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if size is None:
            raise AppwriteException('Missing required parameter: "size"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return self._parse_response(response, model=ColumnString)


    @deprecated("This API has been deprecated since 1.8.0. Please use `tablesDB.update_text_column` instead.")
    def update_string_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        size: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> ColumnString:
        """
        Update a string column. Changing the `default` value will not update already existing rows.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update_text_column` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        size : Optional[float]
            Maximum size of the string column.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnString
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/string/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['size'] = self._normalize_value(size)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnString)


    def create_text_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> ColumnText:
        """
        Create a text column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        encrypt : Optional[bool]
            Toggle encryption for the column. Encryption enhances security by not storing any plain text values in the database. However, encrypted columns cannot be queried.
        
        Returns
        -------
        ColumnText
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/text'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return self._parse_response(response, model=ColumnText)


    def update_text_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnText:
        """
        Update a text column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnText
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/text/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnText)


    def create_url_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None
    ) -> ColumnUrl:
        """
        Create a URL column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        
        Returns
        -------
        ColumnUrl
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/url'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        if array is not None:
            api_params['array'] = self._normalize_value(array)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnUrl)


    def update_url_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        new_key: Optional[str] = None
    ) -> ColumnUrl:
        """
        Update an url column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnUrl
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/url/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnUrl)


    def create_varchar_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        size: float,
        required: bool,
        default: Optional[str] = None,
        array: Optional[bool] = None,
        encrypt: Optional[bool] = None
    ) -> ColumnVarchar:
        """
        Create a varchar column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        size : float
            Column size for varchar columns, in number of characters. Maximum size is 16381.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        array : Optional[bool]
            Is column an array?
        encrypt : Optional[bool]
            Toggle encryption for the column. Encryption enhances security by not storing any plain text values in the database. However, encrypted columns cannot be queried.
        
        Returns
        -------
        ColumnVarchar
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/varchar'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if size is None:
            raise AppwriteException('Missing required parameter: "size"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return self._parse_response(response, model=ColumnVarchar)


    def update_varchar_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        required: bool,
        default: Optional[str],
        size: Optional[float] = None,
        new_key: Optional[str] = None
    ) -> ColumnVarchar:
        """
        Update a varchar column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : Optional[str]
            Default value for column when not provided. Cannot be set when column is required.
        size : Optional[float]
            Maximum size of the varchar column.
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnVarchar
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/varchar/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if required is None:
            raise AppwriteException('Missing required parameter: "required"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['required'] = self._normalize_value(required)
        api_params['default'] = self._normalize_value(default)
        api_params['size'] = self._normalize_value(size)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnVarchar)


    def get_column(
        self,
        database_id: str,
        table_id: str,
        key: str
    ) -> Union[ColumnBoolean, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnString]:
        """
        Get column by ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        
        Returns
        -------
        Union[ColumnBoolean, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnString]
            API response as one of the typed response models
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ColumnBoolean)


    def delete_column(
        self,
        database_id: str,
        table_id: str,
        key: str
    ) -> Dict[str, Any]:
        """
        Deletes a column.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_relationship_column(
        self,
        database_id: str,
        table_id: str,
        key: str,
        on_delete: Optional[RelationMutate] = None,
        new_key: Optional[str] = None
    ) -> ColumnRelationship:
        """
        Update relationship column. [Learn more about relationship columns](https://appwrite.io/docs/databases-relationships#relationship-columns).
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        key : str
            Column Key.
        on_delete : Optional[RelationMutate]
            Constraints option
        new_key : Optional[str]
            New Column Key.
        
        Returns
        -------
        ColumnRelationship
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/columns/{key}/relationship'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))

        api_params['onDelete'] = self._normalize_value(on_delete)
        api_params['newKey'] = self._normalize_value(new_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnRelationship)


    def list_indexes(
        self,
        database_id: str,
        table_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> ColumnIndexList:
        """
        List indexes on the table.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: key, type, status, attributes, error
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ColumnIndexList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/indexes'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ColumnIndexList)


    def create_index(
        self,
        database_id: str,
        table_id: str,
        key: str,
        type: TablesDBIndexType,
        columns: List[str],
        orders: Optional[List[OrderBy]] = None,
        lengths: Optional[List[float]] = None
    ) -> ColumnIndex:
        """
        Creates an index on the columns listed. Your index should include all the columns you will query in a single request.
        Type can be `key`, `fulltext`, or `unique`.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Index Key.
        type : TablesDBIndexType
            Index type.
        columns : List[str]
            Array of columns to index. Maximum of 100 columns are allowed, each 32 characters long.
        orders : Optional[List[OrderBy]]
            Array of index orders. Maximum of 100 orders are allowed.
        lengths : Optional[List[float]]
            Length of index. Maximum of 100
        
        Returns
        -------
        ColumnIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/indexes'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if columns is None:
            raise AppwriteException('Missing required parameter: "columns"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['type'] = self._normalize_value(type)
        api_params['columns'] = self._normalize_value(columns)
        if orders is not None:
            api_params['orders'] = self._normalize_value(orders)
        if lengths is not None:
            api_params['lengths'] = self._normalize_value(lengths)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ColumnIndex)


    def get_index(
        self,
        database_id: str,
        table_id: str,
        key: str
    ) -> ColumnIndex:
        """
        Get index by ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        key : str
            Index Key.
        
        Returns
        -------
        ColumnIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/indexes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ColumnIndex)


    def delete_index(
        self,
        database_id: str,
        table_id: str,
        key: str
    ) -> Dict[str, Any]:
        """
        Delete an index.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
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

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/indexes/{key}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{key}', str(self._normalize_value(key)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_rows(
        self,
        database_id: str,
        table_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        total: Optional[bool] = None,
        ttl: Optional[float] = None,
        model_type: Type[T] = dict
    ) -> RowList[T]:
        """
        Get a list of all the user's rows in a given table. You can use the query params to filter your results.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TablesDB service [server integration](https://appwrite.io/docs/products/databases/tables#create-table).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        transaction_id : Optional[str]
            Transaction ID to read uncommitted changes within the transaction.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        ttl : Optional[float]
            TTL (seconds) for caching list responses. Responses are stored in an in-memory key-value cache, keyed per project, table, schema version (columns and indexes), caller authorization roles, and the exact query — so users with different permissions never share cached entries. Schema changes invalidate cached entries automatically; row writes do not, so choose a TTL you are comfortable serving as stale data. Set to 0 to disable caching. Must be between 0 and 86400 (24 hours).
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        RowList[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

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

        return RowList.with_data(response, model_type)


    def create_row(
        self,
        database_id: str,
        table_id: str,
        row_id: str,
        data: Dict[str, Any],
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Row[T]:
        """
        Create a new Row. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable). Make sure to define columns before creating rows.
        row_id : str
            Row ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        data : Dict[str, Any]
            Row data as JSON object.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Row[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if row_id is None:
            raise AppwriteException('Missing required parameter: "row_id"')

        if data is None:
            raise AppwriteException('Missing required parameter: "data"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['rowId'] = self._normalize_value(row_id)
        api_params['data'] = self._normalize_value(data)
        api_params['permissions'] = self._normalize_value(permissions)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Row.with_data(response, model_type)


    def create_rows(
        self,
        database_id: str,
        table_id: str,
        rows: List[Dict[str, Any]],
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> RowList[T]:
        """
        Create new Rows. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable). Make sure to define columns before creating rows.
        rows : List[Dict[str, Any]]
            Array of rows data as JSON objects.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        RowList[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if rows is None:
            raise AppwriteException('Missing required parameter: "rows"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['rows'] = self._normalize_value(rows)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return RowList.with_data(response, model_type)


    def upsert_rows(
        self,
        database_id: str,
        table_id: str,
        rows: List[Dict[str, Any]],
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> RowList[T]:
        """
        Create or update Rows. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable) API or directly from your database console.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        rows : List[Dict[str, Any]]
            Array of row data as JSON objects. May contain partial rows.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        RowList[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if rows is None:
            raise AppwriteException('Missing required parameter: "rows"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        api_params['rows'] = self._normalize_value(rows)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return RowList.with_data(response, model_type)


    def update_rows(
        self,
        database_id: str,
        table_id: str,
        data: Optional[Dict[str, Any]] = None,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> RowList[T]:
        """
        Update all rows that match your queries, if no queries are submitted then all rows are updated. You can pass only specific fields to be updated.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        data : Optional[Dict[str, Any]]
            Row data as JSON object. Include only column and value pairs to be updated.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        RowList[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        if data is not None:
            api_params['data'] = self._normalize_value(data)
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return RowList.with_data(response, model_type)


    def delete_rows(
        self,
        database_id: str,
        table_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> RowList[T]:
        """
        Bulk delete rows using queries, if no queries are passed then all rows are deleted.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        RowList[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return RowList.with_data(response, model_type)


    def get_row(
        self,
        database_id: str,
        table_id: str,
        row_id: str,
        queries: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Row[T]:
        """
        Get a row by its unique ID. This endpoint response returns a JSON object with the row data.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        row_id : str
            Row ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        transaction_id : Optional[str]
            Transaction ID to read uncommitted changes within the transaction.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Row[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows/{rowId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if row_id is None:
            raise AppwriteException('Missing required parameter: "row_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{rowId}', str(self._normalize_value(row_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if transaction_id is not None:
            api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('get', api_path, {
        }, api_params)

        return Row.with_data(response, model_type)


    def upsert_row(
        self,
        database_id: str,
        table_id: str,
        row_id: str,
        data: Optional[Dict[str, Any]] = None,
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Row[T]:
        """
        Create or update a Row. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        row_id : str
            Row ID.
        data : Optional[Dict[str, Any]]
            Row data as JSON object. Include all required columns of the row to be created or updated.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Row[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows/{rowId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if row_id is None:
            raise AppwriteException('Missing required parameter: "row_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{rowId}', str(self._normalize_value(row_id)))

        if data is not None:
            api_params['data'] = self._normalize_value(data)
        api_params['permissions'] = self._normalize_value(permissions)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Row.with_data(response, model_type)


    def update_row(
        self,
        database_id: str,
        table_id: str,
        row_id: str,
        data: Optional[Dict[str, Any]] = None,
        permissions: Optional[List[str]] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Row[T]:
        """
        Update a row by its unique ID. Using the patch method you can pass only specific fields that will get updated.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        row_id : str
            Row ID.
        data : Optional[Dict[str, Any]]
            Row data as JSON object. Include only columns and value pairs to be updated.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Row[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows/{rowId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if row_id is None:
            raise AppwriteException('Missing required parameter: "row_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{rowId}', str(self._normalize_value(row_id)))

        if data is not None:
            api_params['data'] = self._normalize_value(data)
        api_params['permissions'] = self._normalize_value(permissions)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Row.with_data(response, model_type)


    def delete_row(
        self,
        database_id: str,
        table_id: str,
        row_id: str,
        transaction_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Delete a row by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable).
        row_id : str
            Row ID.
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

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows/{rowId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if row_id is None:
            raise AppwriteException('Missing required parameter: "row_id"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{rowId}', str(self._normalize_value(row_id)))

        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def decrement_row_column(
        self,
        database_id: str,
        table_id: str,
        row_id: str,
        column: str,
        value: Optional[float] = None,
        min: Optional[float] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Row[T]:
        """
        Decrement a specific column of a row by a given value.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        row_id : str
            Row ID.
        column : str
            Column key.
        value : Optional[float]
            Value to increment the column by. The value must be a number.
        min : Optional[float]
            Minimum value for the column. If the current value is lesser than this value, an exception will be thrown.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Row[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows/{rowId}/{column}/decrement'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if row_id is None:
            raise AppwriteException('Missing required parameter: "row_id"')

        if column is None:
            raise AppwriteException('Missing required parameter: "column"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{rowId}', str(self._normalize_value(row_id)))
        api_path = api_path.replace('{column}', str(self._normalize_value(column)))

        if value is not None:
            api_params['value'] = self._normalize_value(value)
        api_params['min'] = self._normalize_value(min)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Row.with_data(response, model_type)


    def increment_row_column(
        self,
        database_id: str,
        table_id: str,
        row_id: str,
        column: str,
        value: Optional[float] = None,
        max: Optional[float] = None,
        transaction_id: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> Row[T]:
        """
        Increment a specific column of a row by a given value.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        row_id : str
            Row ID.
        column : str
            Column key.
        value : Optional[float]
            Value to increment the column by. The value must be a number.
        max : Optional[float]
            Maximum value for the column. If the current value is greater than this value, an error will be thrown.
        transaction_id : Optional[str]
            Transaction ID for staging the operation.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Row[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows/{rowId}/{column}/increment'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if row_id is None:
            raise AppwriteException('Missing required parameter: "row_id"')

        if column is None:
            raise AppwriteException('Missing required parameter: "column"')

        api_path = api_path.replace('{databaseId}', str(self._normalize_value(database_id)))
        api_path = api_path.replace('{tableId}', str(self._normalize_value(table_id)))
        api_path = api_path.replace('{rowId}', str(self._normalize_value(row_id)))
        api_path = api_path.replace('{column}', str(self._normalize_value(column)))

        if value is not None:
            api_params['value'] = self._normalize_value(value)
        api_params['max'] = self._normalize_value(max)
        api_params['transactionId'] = self._normalize_value(transaction_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Row.with_data(response, model_type)

