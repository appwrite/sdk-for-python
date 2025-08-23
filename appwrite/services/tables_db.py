from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException
from ..enums.relationship_type import RelationshipType;
from ..enums.relation_mutate import RelationMutate;
from ..enums.index_type import IndexType;

class TablesDB(Service):

    def __init__(self, client) -> None:
        super(TablesDB, self).__init__(client)

    def list(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: name
        search : str
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

    def create(self, database_id: str, name: str, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Database.
        

        Parameters
        ----------
        database_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Database name. Max length: 128 chars.
        enabled : bool
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

    def update(self, database_id: str, name: str, enabled: bool = None) -> Dict[str, Any]:
        """
        Update a database by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        name : str
            Database name. Max length: 128 chars.
        enabled : bool
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

    def list_tables(self, database_id: str, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all tables that belong to the provided databaseId. You can use the search parameter to filter your results.

        Parameters
        ----------
        database_id : str
            Database ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following columns: name, enabled, rowSecurity
        search : str
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

    def create_table(self, database_id: str, table_id: str, name: str, permissions: List[str] = None, row_security: bool = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Table. Before using this route, you should create a new database resource using either a [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreateTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Unique Id. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Table name. Max length: 128 chars.
        permissions : List[str]
            An array of permissions strings. By default, no user is granted with any permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        row_security : bool
            Enables configuring permissions for individual rows. A user needs one of row or table level permissions to access a row. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : bool
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

    def update_table(self, database_id: str, table_id: str, name: str, permissions: List[str] = None, row_security: bool = None, enabled: bool = None) -> Dict[str, Any]:
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
        permissions : List[str]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        row_security : bool
            Enables configuring permissions for individual rows. A user needs one of row or table level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : bool
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

    def list_columns(self, database_id: str, table_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        List columns in the table.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        queries : List[str]
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

    def create_boolean_column(self, database_id: str, table_id: str, key: str, required: bool, default: bool = None, array: bool = None) -> Dict[str, Any]:
        """
        Create a boolean column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : bool
            Default value for column when not provided. Cannot be set when column is required.
        array : bool
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

    def update_boolean_column(self, database_id: str, table_id: str, key: str, required: bool, default: bool, new_key: str = None) -> Dict[str, Any]:
        """
        Update a boolean column. Changing the `default` value will not update already existing rows.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : bool
            Default value for column when not provided. Cannot be set when column is required.
        new_key : str
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

    def create_datetime_column(self, database_id: str, table_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for the column in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Cannot be set when column is required.
        array : bool
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

    def update_datetime_column(self, database_id: str, table_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        new_key : str
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

    def create_email_column(self, database_id: str, table_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        array : bool
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

    def update_email_column(self, database_id: str, table_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        new_key : str
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

    def create_enum_column(self, database_id: str, table_id: str, key: str, elements: List[str], required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        array : bool
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

    def update_enum_column(self, database_id: str, table_id: str, key: str, elements: List[str], required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        new_key : str
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

    def create_float_column(self, database_id: str, table_id: str, key: str, required: bool, min: float = None, max: float = None, default: float = None, array: bool = None) -> Dict[str, Any]:
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
        min : float
            Minimum value
        max : float
            Maximum value
        default : float
            Default value. Cannot be set when required.
        array : bool
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

    def update_float_column(self, database_id: str, table_id: str, key: str, required: bool, default: float, min: float = None, max: float = None, new_key: str = None) -> Dict[str, Any]:
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
        default : float
            Default value. Cannot be set when required.
        min : float
            Minimum value
        max : float
            Maximum value
        new_key : str
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

    def create_integer_column(self, database_id: str, table_id: str, key: str, required: bool, min: float = None, max: float = None, default: float = None, array: bool = None) -> Dict[str, Any]:
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
        min : float
            Minimum value
        max : float
            Maximum value
        default : float
            Default value. Cannot be set when column is required.
        array : bool
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

    def update_integer_column(self, database_id: str, table_id: str, key: str, required: bool, default: float, min: float = None, max: float = None, new_key: str = None) -> Dict[str, Any]:
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
        default : float
            Default value. Cannot be set when column is required.
        min : float
            Minimum value
        max : float
            Maximum value
        new_key : str
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

    def create_ip_column(self, database_id: str, table_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value. Cannot be set when column is required.
        array : bool
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

    def update_ip_column(self, database_id: str, table_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value. Cannot be set when column is required.
        new_key : str
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

    def create_relationship_column(self, database_id: str, table_id: str, related_table_id: str, type: RelationshipType, two_way: bool = None, key: str = None, two_way_key: str = None, on_delete: RelationMutate = None) -> Dict[str, Any]:
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
        two_way : bool
            Is Two Way?
        key : str
            Column Key.
        two_way_key : str
            Two Way Column Key.
        on_delete : RelationMutate
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

    def create_string_column(self, database_id: str, table_id: str, key: str, size: float, required: bool, default: str = None, array: bool = None, encrypt: bool = None) -> Dict[str, Any]:
        """
        Create a string column.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        key : str
            Column Key.
        size : float
            Column size for text columns, in number of characters.
        required : bool
            Is column required?
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        array : bool
            Is column an array?
        encrypt : bool
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

    def update_string_column(self, database_id: str, table_id: str, key: str, required: bool, default: str, size: float = None, new_key: str = None) -> Dict[str, Any]:
        """
        Update a string column. Changing the `default` value will not update already existing rows.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        key : str
            Column Key.
        required : bool
            Is column required?
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        size : float
            Maximum size of the string column.
        new_key : str
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

    def create_url_column(self, database_id: str, table_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        array : bool
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

    def update_url_column(self, database_id: str, table_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for column when not provided. Cannot be set when column is required.
        new_key : str
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

    def update_relationship_column(self, database_id: str, table_id: str, key: str, on_delete: RelationMutate = None, new_key: str = None) -> Dict[str, Any]:
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
        on_delete : RelationMutate
            Constraints option
        new_key : str
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

    def list_indexes(self, database_id: str, table_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        List indexes on the table.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        queries : List[str]
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

    def create_index(self, database_id: str, table_id: str, key: str, type: IndexType, columns: List[str], orders: List[str] = None, lengths: List[float] = None) -> Dict[str, Any]:
        """
        Creates an index on the columns listed. Your index should include all the columns you will query in a single request.
        Type can be `key`, `fulltext`, or `unique`.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        key : str
            Index Key.
        type : IndexType
            Index type.
        columns : List[str]
            Array of columns to index. Maximum of 100 columns are allowed, each 32 characters long.
        orders : List[str]
            Array of index orders. Maximum of 100 orders are allowed.
        lengths : List[float]
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
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
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
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
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

    def list_rows(self, database_id: str, table_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get a list of all the user's rows in a given table. You can use the query params to filter your results.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the TableDB service [server integration](https://appwrite.io/docs/server/tablesdbdb#tablesdbCreate).
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        
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

        return self.client.call('get', api_path, {
        }, api_params)

    def create_row(self, database_id: str, table_id: str, row_id: str, data: dict, permissions: List[str] = None) -> Dict[str, Any]:
        """
        Create a new Row. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreateTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate). Make sure to define columns before creating rows.
        row_id : str
            Row ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        data : dict
            Row data as JSON object.
        permissions : List[str]
            An array of permissions strings. By default, only the current user is granted all permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        
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

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_rows(self, database_id: str, table_id: str, rows: List[dict]) -> Dict[str, Any]:
        """
        Create new Rows. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreateTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate). Make sure to define columns before creating rows.
        rows : List[dict]
            Array of documents data as JSON objects.
        
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

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def upsert_rows(self, database_id: str, table_id: str, rows: List[dict]) -> Dict[str, Any]:
        """
        Create or update Rows. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreateTable) API or directly from your database console.
        

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        rows : List[dict]
            Array of row data as JSON objects. May contain partial rows.
        
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

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_rows(self, database_id: str, table_id: str, data: dict = None, queries: List[str] = None) -> Dict[str, Any]:
        """
        Update all rows that match your queries, if no queries are submitted then all rows are updated. You can pass only specific fields to be updated.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        data : dict
            Row data as JSON object. Include only column and value pairs to be updated.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        
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

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_rows(self, database_id: str, table_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Bulk delete rows using queries, if no queries are passed then all rows are deleted.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        
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

        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_row(self, database_id: str, table_id: str, row_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get a row by its unique ID. This endpoint response returns a JSON object with the row data.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        row_id : str
            Row ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        
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

        return self.client.call('get', api_path, {
        }, api_params)

    def upsert_row(self, database_id: str, table_id: str, row_id: str, data: dict = None, permissions: List[str] = None) -> Dict[str, Any]:
        """
        Create or update a Row. Before using this route, you should create a new table resource using either a [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreateTable) API or directly from your database console.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID.
        row_id : str
            Row ID.
        data : dict
            Row data as JSON object. Include all required columns of the row to be created or updated.
        permissions : List[str]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        
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

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_row(self, database_id: str, table_id: str, row_id: str, data: dict = None, permissions: List[str] = None) -> Dict[str, Any]:
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
        data : dict
            Row data as JSON object. Include only columns and value pairs to be updated.
        permissions : List[str]
            An array of permissions strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        
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

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_row(self, database_id: str, table_id: str, row_id: str) -> Dict[str, Any]:
        """
        Delete a row by its unique ID.

        Parameters
        ----------
        database_id : str
            Database ID.
        table_id : str
            Table ID. You can create a new table using the Database service [server integration](https://appwrite.io/docs/server/tablesdb#tablesDBCreate).
        row_id : str
            Row ID.
        
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


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def decrement_row_column(self, database_id: str, table_id: str, row_id: str, column: str, value: float = None, min: float = None) -> Dict[str, Any]:
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
        value : float
            Value to increment the column by. The value must be a number.
        min : float
            Minimum value for the column. If the current value is lesser than this value, an exception will be thrown.
        
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

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def increment_row_column(self, database_id: str, table_id: str, row_id: str, column: str, value: float = None, max: float = None) -> Dict[str, Any]:
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
        value : float
            Value to increment the column by. The value must be a number.
        max : float
            Maximum value for the column. If the current value is greater than this value, an error will be thrown.
        
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

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)
