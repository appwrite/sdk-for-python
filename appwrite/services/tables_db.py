from ..service import Service
from typing import List, Dict, Any, Optional
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.relationship_type import RelationshipType;
from ..enums.relation_mutate import RelationMutate;
from ..enums.index_type import IndexType;

class TablesDB(Service):

    def __init__(self, client) -> None:
        super(TablesDB, self).__init__(client)

    def list(self, queries: Optional[List[str]] = None, search: Optional[str] = None) -> Dict[str, Any]:
        """
        Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: name
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create(self, database_id: str, name: str, enabled: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['databaseId'] = database_id
        api_params['name'] = name
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_transactions(self, queries: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        List transactions across all databases.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/transactions'
        api_params = {}

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_transaction(self, ttl: Optional[float] = None) -> Dict[str, Any]:
        """
        Create a new transaction.

        Parameters
        ----------
        ttl : Optional[float]
            Seconds before the transaction expires.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/transactions'
        api_params = {}

        api_params['ttl'] = ttl

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_transaction(self, transaction_id: str) -> Dict[str, Any]:
        """
        Get a transaction by its unique ID.

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

        api_path = api_path.replace('{transactionId}', transaction_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_transaction(self, transaction_id: str, commit: Optional[bool] = None, rollback: Optional[bool] = None) -> Dict[str, Any]:
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

        api_path = api_path.replace('{transactionId}', transaction_id)

        api_params['commit'] = commit
        api_params['rollback'] = rollback

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_transaction(self, transaction_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{transactionId}', transaction_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_operations(self, transaction_id: str, operations: Optional[List[dict]] = None) -> Dict[str, Any]:
        """
        Create multiple operations in a single transaction.

        Parameters
        ----------
        transaction_id : str
            Transaction ID.
        operations : Optional[List[dict]]
            Array of staged operations.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/transactions/{transactionId}/operations'
        api_params = {}
        if transaction_id is None:
            raise AppwriteException('Missing required parameter: "transaction_id"')

        api_path = api_path.replace('{transactionId}', transaction_id)

        api_params['operations'] = operations

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get(self, database_id: str) -> Dict[str, Any]:
        """
        Get a database by its unique ID. This endpoint response returns a JSON object with the database metadata.

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

        api_path = api_path.replace('{databaseId}', database_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update(self, database_id: str, name: str, enabled: Optional[bool] = None) -> Dict[str, Any]:
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

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['name'] = name
        api_params['enabled'] = enabled

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, database_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_tables(self, database_id: str, queries: Optional[List[str]] = None, search: Optional[str] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/tablesdb/{databaseId}/tables'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create_table(self, database_id: str, table_id: str, name: str, permissions: Optional[List[str]] = None, row_security: Optional[bool] = None, enabled: Optional[bool] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['tableId'] = table_id
        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['rowSecurity'] = row_security
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_table(self, database_id: str, table_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_table(self, database_id: str, table_id: str, name: str, permissions: Optional[List[str]] = None, row_security: Optional[bool] = None, enabled: Optional[bool] = None) -> Dict[str, Any]:
        """
        Update a table by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        name : str
            Table name. Max length: 128 chars.
        permissions : Optional[List[str]]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        row_security : Optional[bool]
            Enables configuring permissions for individual rows. A user needs one of row or table level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : Optional[bool]
            Is table enabled? When set to 'disabled', users cannot access the table but Server SDKs with and API key can still read and write to the table. No data is lost when this is toggled.
        
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

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['rowSecurity'] = row_security
        api_params['enabled'] = enabled

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_table(self, database_id: str, table_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_columns(self, database_id: str, table_id: str, queries: Optional[List[str]] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_boolean_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[bool] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_boolean_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[bool], new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_datetime_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_datetime_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str], new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_email_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str], new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_enum_column(self, database_id: str, table_id: str, key: str, elements: List[str], required: bool, default: Optional[str] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['elements'] = elements
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_enum_column(self, database_id: str, table_id: str, key: str, elements: List[str], required: bool, default: Optional[str], new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['elements'] = elements
        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_float_column(self, database_id: str, table_id: str, key: str, required: bool, min: Optional[float] = None, max: Optional[float] = None, default: Optional[float] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_float_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[float], min: Optional[float] = None, max: Optional[float] = None, new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_integer_column(self, database_id: str, table_id: str, key: str, required: bool, min: Optional[float] = None, max: Optional[float] = None, default: Optional[float] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_integer_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[float], min: Optional[float] = None, max: Optional[float] = None, new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_ip_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_ip_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str], new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_line_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[List[Any]] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_line_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[List[Any]] = None, new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_point_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[List[Any]] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_point_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[List[Any]] = None, new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_polygon_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[List[Any]] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_polygon_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[List[Any]] = None, new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_relationship_column(self, database_id: str, table_id: str, related_table_id: str, type: RelationshipType, two_way: Optional[bool] = None, key: Optional[str] = None, two_way_key: Optional[str] = None, on_delete: Optional[RelationMutate] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['relatedTableId'] = related_table_id
        api_params['type'] = type
        api_params['twoWay'] = two_way
        api_params['key'] = key
        api_params['twoWayKey'] = two_way_key
        api_params['onDelete'] = on_delete

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_string_column(self, database_id: str, table_id: str, key: str, size: float, required: bool, default: Optional[str] = None, array: Optional[bool] = None, encrypt: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a string column.
        

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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['size'] = size
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array
        api_params['encrypt'] = encrypt

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_string_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str], size: Optional[float] = None, new_key: Optional[str] = None) -> Dict[str, Any]:
        """
        Update a string column. Changing the `default` value will not update already existing rows.
        

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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['size'] = size
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_url_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str] = None, array: Optional[bool] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_url_column(self, database_id: str, table_id: str, key: str, required: bool, default: Optional[str], new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_column(self, database_id: str, table_id: str, key: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_column(self, database_id: str, table_id: str, key: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_relationship_column(self, database_id: str, table_id: str, key: str, on_delete: Optional[RelationMutate] = None, new_key: Optional[str] = None) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)

        api_params['onDelete'] = on_delete
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_indexes(self, database_id: str, table_id: str, queries: Optional[List[str]] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_index(self, database_id: str, table_id: str, key: str, type: IndexType, columns: List[str], orders: Optional[List[str]] = None, lengths: Optional[List[float]] = None) -> Dict[str, Any]:
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
        type : IndexType
            Index type.
        columns : List[str]
            Array of columns to index. Maximum of 100 columns are allowed, each 32 characters long.
        orders : Optional[List[str]]
            Array of index orders. Maximum of 100 orders are allowed.
        lengths : Optional[List[float]]
            Length of index. Maximum of 100
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['key'] = key
        api_params['type'] = type
        api_params['columns'] = columns
        api_params['orders'] = orders
        api_params['lengths'] = lengths

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_index(self, database_id: str, table_id: str, key: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_index(self, database_id: str, table_id: str, key: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_rows(self, database_id: str, table_id: str, queries: Optional[List[str]] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['queries'] = queries
        api_params['transactionId'] = transaction_id

        return self.client.call('get', api_path, {
        }, api_params)

    def create_row(self, database_id: str, table_id: str, row_id: str, data: dict, permissions: Optional[List[str]] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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
        data : dict
            Row data as JSON object.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['rowId'] = row_id
        api_params['data'] = data
        api_params['permissions'] = permissions
        api_params['transactionId'] = transaction_id

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_rows(self, database_id: str, table_id: str, rows: List[dict], transaction_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create new Rows. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable). Make sure to define columns before creating rows.
        rows : List[dict]
            Array of rows data as JSON objects.
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

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if rows is None:
            raise AppwriteException('Missing required parameter: "rows"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['rows'] = rows
        api_params['transactionId'] = transaction_id

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def upsert_rows(self, database_id: str, table_id: str, rows: List[dict], transaction_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create or update Rows. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/references/cloud/server-dart/tablesDB#createTable) API or directly from your database console.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        rows : List[dict]
            Array of row data as JSON objects. May contain partial rows.
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

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        if rows is None:
            raise AppwriteException('Missing required parameter: "rows"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['rows'] = rows
        api_params['transactionId'] = transaction_id

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_rows(self, database_id: str, table_id: str, data: Optional[dict] = None, queries: Optional[List[str]] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Update all rows that match your queries, if no queries are submitted then all rows are updated. You can pass only specific fields to be updated.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        data : Optional[dict]
            Row data as JSON object. Include only column and value pairs to be updated.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
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

        api_path = '/tablesdb/{databaseId}/tables/{tableId}/rows'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if table_id is None:
            raise AppwriteException('Missing required parameter: "table_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['data'] = data
        api_params['queries'] = queries
        api_params['transactionId'] = transaction_id

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_rows(self, database_id: str, table_id: str, queries: Optional[List[str]] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)

        api_params['queries'] = queries
        api_params['transactionId'] = transaction_id

        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_row(self, database_id: str, table_id: str, row_id: str, queries: Optional[List[str]] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{rowId}', row_id)

        api_params['queries'] = queries
        api_params['transactionId'] = transaction_id

        return self.client.call('get', api_path, {
        }, api_params)

    def upsert_row(self, database_id: str, table_id: str, row_id: str, data: Optional[dict] = None, permissions: Optional[List[str]] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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
        data : Optional[dict]
            Row data as JSON object. Include all required columns of the row to be created or updated.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{rowId}', row_id)

        api_params['data'] = data
        api_params['permissions'] = permissions
        api_params['transactionId'] = transaction_id

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_row(self, database_id: str, table_id: str, row_id: str, data: Optional[dict] = None, permissions: Optional[List[str]] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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
        data : Optional[dict]
            Row data as JSON object. Include only columns and value pairs to be updated.
        permissions : Optional[List[str]]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{rowId}', row_id)

        api_params['data'] = data
        api_params['permissions'] = permissions
        api_params['transactionId'] = transaction_id

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_row(self, database_id: str, table_id: str, row_id: str, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{rowId}', row_id)

        api_params['transactionId'] = transaction_id

        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def decrement_row_column(self, database_id: str, table_id: str, row_id: str, column: str, value: Optional[float] = None, min: Optional[float] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{rowId}', row_id)
        api_path = api_path.replace('{column}', column)

        api_params['value'] = value
        api_params['min'] = min
        api_params['transactionId'] = transaction_id

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def increment_row_column(self, database_id: str, table_id: str, row_id: str, column: str, value: Optional[float] = None, max: Optional[float] = None, transaction_id: Optional[str] = None) -> Dict[str, Any]:
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
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{tableId}', table_id)
        api_path = api_path.replace('{rowId}', row_id)
        api_path = api_path.replace('{column}', column)

        api_params['value'] = value
        api_params['max'] = max
        api_params['transactionId'] = transaction_id

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)
