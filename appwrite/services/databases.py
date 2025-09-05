from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException
from ..enums.relationship_type import RelationshipType;
from ..enums.relation_mutate import RelationMutate;
from ..enums.index_type import IndexType;

class Databases(Service):

    def __init__(self, client) -> None:
        super(Databases, self).__init__(client)

    def list(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all databases from the current Appwrite project. You can use the search parameter to filter your results.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.list` instead.
        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name
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

        api_path = '/databases'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create(self, database_id: str, name: str, enabled: bool = None) -> Dict[str, Any]:
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

        api_path = '/databases'
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

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.get` instead.
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

        api_path = api_path.replace('{databaseId}', database_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update(self, database_id: str, name: str, enabled: bool = None) -> Dict[str, Any]:
        """
        Update a database by its unique ID.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.update` instead.
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

        api_path = '/databases/{databaseId}'
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

        api_path = api_path.replace('{databaseId}', database_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_collections(self, database_id: str, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all collections that belong to the provided databaseId. You can use the search parameter to filter your results.

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.list_tables` instead.
        Parameters
        ----------
        database_id : str
            Database ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, documentSecurity
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

        api_path = '/databases/{databaseId}/collections'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create_collection(self, database_id: str, collection_id: str, name: str, permissions: List[str] = None, document_security: bool = None, enabled: bool = None) -> Dict[str, Any]:
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
        permissions : List[str]
            An array of permissions strings. By default, no user is granted with any permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
        document_security : bool
            Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : bool
            Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)

        api_params['collectionId'] = collection_id
        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['documentSecurity'] = document_security
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_collection(self, database_id: str, collection_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_collection(self, database_id: str, collection_id: str, name: str, permissions: List[str] = None, document_security: bool = None, enabled: bool = None) -> Dict[str, Any]:
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
        name : str
            Collection name. Max length: 128 chars.
        permissions : List[str]
            An array of permission strings. By default, the current permissions are inherited. [Learn more about permissions](https://appwrite.io/docs/permissions).
        document_security : bool
            Enables configuring permissions for individual documents. A user needs one of document or collection level permissions to access a document. [Learn more about permissions](https://appwrite.io/docs/permissions).
        enabled : bool
            Is collection enabled? When set to 'disabled', users cannot access the collection but Server SDKs with and API key can still read and write to the collection. No data is lost when this is toggled.
        
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

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['name'] = name
        api_params['permissions'] = permissions
        api_params['documentSecurity'] = document_security
        api_params['enabled'] = enabled

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_collection(self, database_id: str, collection_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_attributes(self, database_id: str, collection_id: str, queries: List[str] = None) -> Dict[str, Any]:
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
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, size, required, array, status, error
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_boolean_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: bool = None, array: bool = None) -> Dict[str, Any]:
        """
        Create a boolean attribute.
        

        .. deprecated::1.8.0
            This API has been deprecated since 1.8.0. Please use `tablesDB.create_boolean_column` instead.
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
        default : bool
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_boolean_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: bool, new_key: str = None) -> Dict[str, Any]:
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
        default : bool
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : str
            New attribute key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_datetime_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for the attribute in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_datetime_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : str
            New attribute key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_email_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_enum_attribute(self, database_id: str, collection_id: str, key: str, elements: List[str], required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['elements'] = elements
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_enum_attribute(self, database_id: str, collection_id: str, key: str, elements: List[str], required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['elements'] = elements
        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_float_attribute(self, database_id: str, collection_id: str, key: str, required: bool, min: float = None, max: float = None, default: float = None, array: bool = None) -> Dict[str, Any]:
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
        min : float
            Minimum value.
        max : float
            Maximum value.
        default : float
            Default value. Cannot be set when required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_float_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: float, min: float = None, max: float = None, new_key: str = None) -> Dict[str, Any]:
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
        default : float
            Default value. Cannot be set when required.
        min : float
            Minimum value.
        max : float
            Maximum value.
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_integer_attribute(self, database_id: str, collection_id: str, key: str, required: bool, min: float = None, max: float = None, default: float = None, array: bool = None) -> Dict[str, Any]:
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
        min : float
            Minimum value
        max : float
            Maximum value
        default : float
            Default value. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_integer_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: float, min: float = None, max: float = None, new_key: str = None) -> Dict[str, Any]:
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
        default : float
            Default value. Cannot be set when attribute is required.
        min : float
            Minimum value
        max : float
            Maximum value
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['min'] = min
        api_params['max'] = max
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_ip_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_ip_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value. Cannot be set when attribute is required.
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_line_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: List[Any] = None) -> Dict[str, Any]:
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
        default : List[Any]
            Default value for attribute when not provided, two-dimensional array of coordinate pairs, [[longitude, latitude], [longitude, latitude], …], listing the vertices of the line in order. Cannot be set when attribute is required.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_line_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: List[Any] = None, new_key: str = None) -> Dict[str, Any]:
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
        default : List[Any]
            Default value for attribute when not provided, two-dimensional array of coordinate pairs, [[longitude, latitude], [longitude, latitude], …], listing the vertices of the line in order. Cannot be set when attribute is required.
        new_key : str
            New attribute key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_point_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: List[Any] = None) -> Dict[str, Any]:
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
        default : List[Any]
            Default value for attribute when not provided, array of two numbers [longitude, latitude], representing a single coordinate. Cannot be set when attribute is required.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_point_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: List[Any] = None, new_key: str = None) -> Dict[str, Any]:
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
        default : List[Any]
            Default value for attribute when not provided, array of two numbers [longitude, latitude], representing a single coordinate. Cannot be set when attribute is required.
        new_key : str
            New attribute key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_polygon_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: List[Any] = None) -> Dict[str, Any]:
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
        default : List[Any]
            Default value for attribute when not provided, three-dimensional array where the outer array holds one or more linear rings, [[[longitude, latitude], …], …], the first ring is the exterior boundary, any additional rings are interior holes, and each ring must start and end with the same coordinate pair. Cannot be set when attribute is required.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_polygon_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: List[Any] = None, new_key: str = None) -> Dict[str, Any]:
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
        default : List[Any]
            Default value for attribute when not provided, three-dimensional array where the outer array holds one or more linear rings, [[[longitude, latitude], …], …], the first ring is the exterior boundary, any additional rings are interior holes, and each ring must start and end with the same coordinate pair. Cannot be set when attribute is required.
        new_key : str
            New attribute key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_relationship_attribute(self, database_id: str, collection_id: str, related_collection_id: str, type: RelationshipType, two_way: bool = None, key: str = None, two_way_key: str = None, on_delete: RelationMutate = None) -> Dict[str, Any]:
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
        two_way : bool
            Is Two Way?
        key : str
            Attribute Key.
        two_way_key : str
            Two Way Attribute Key.
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['relatedCollectionId'] = related_collection_id
        api_params['type'] = type
        api_params['twoWay'] = two_way
        api_params['key'] = key
        api_params['twoWayKey'] = two_way_key
        api_params['onDelete'] = on_delete

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_string_attribute(self, database_id: str, collection_id: str, key: str, size: float, required: bool, default: str = None, array: bool = None, encrypt: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        encrypt : bool
            Toggle encryption for the attribute. Encryption enhances security by not storing any plain text values in the database. However, encrypted attributes cannot be queried.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['size'] = size
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array
        api_params['encrypt'] = encrypt

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_string_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str, size: float = None, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        size : float
            Maximum size of the string attribute.
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['size'] = size
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_url_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        array : bool
            Is attribute an array?
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['required'] = required
        api_params['default'] = default
        api_params['array'] = array

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_url_attribute(self, database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> Dict[str, Any]:
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
        default : str
            Default value for attribute when not provided. Cannot be set when attribute is required.
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['required'] = required
        api_params['default'] = default
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_attribute(self, database_id: str, collection_id: str, key: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_attribute(self, database_id: str, collection_id: str, key: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_relationship_attribute(self, database_id: str, collection_id: str, key: str, on_delete: RelationMutate = None, new_key: str = None) -> Dict[str, Any]:
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
        on_delete : RelationMutate
            Constraints option
        new_key : str
            New Attribute Key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/databases/{databaseId}/collections/{collectionId}/attributes/{key}/relationship'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)

        api_params['onDelete'] = on_delete
        api_params['newKey'] = new_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_documents(self, database_id: str, collection_id: str, queries: List[str] = None) -> Dict[str, Any]:
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_document(self, database_id: str, collection_id: str, document_id: str, data: dict, permissions: List[str] = None) -> Dict[str, Any]:
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
        data : dict
            Document data as JSON object.
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['documentId'] = document_id
        api_params['data'] = data
        api_params['permissions'] = permissions

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_documents(self, database_id: str, collection_id: str, documents: List[dict]) -> Dict[str, Any]:
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
        documents : List[dict]
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if documents is None:
            raise AppwriteException('Missing required parameter: "documents"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['documents'] = documents

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def upsert_documents(self, database_id: str, collection_id: str, documents: List[dict]) -> Dict[str, Any]:
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
        documents : List[dict]
            Array of document data as JSON objects. May contain partial documents.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['documents'] = documents

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_documents(self, database_id: str, collection_id: str, data: dict = None, queries: List[str] = None) -> Dict[str, Any]:
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
        data : dict
            Document data as JSON object. Include only attribute and value pairs to be updated.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['data'] = data
        api_params['queries'] = queries

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_documents(self, database_id: str, collection_id: str, queries: List[str] = None) -> Dict[str, Any]:
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['queries'] = queries

        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_document(self, database_id: str, collection_id: str, document_id: str, queries: List[str] = None) -> Dict[str, Any]:
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def upsert_document(self, database_id: str, collection_id: str, document_id: str, data: dict, permissions: List[str] = None) -> Dict[str, Any]:
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
        data : dict
            Document data as JSON object. Include all required attributes of the document to be created or updated.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        if data is None:
            raise AppwriteException('Missing required parameter: "data"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)

        api_params['data'] = data
        api_params['permissions'] = permissions

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_document(self, database_id: str, collection_id: str, document_id: str, data: dict = None, permissions: List[str] = None) -> Dict[str, Any]:
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
        data : dict
            Document data as JSON object. Include only attribute and value pairs to be updated.
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

        api_path = '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}'
        api_params = {}
        if database_id is None:
            raise AppwriteException('Missing required parameter: "database_id"')

        if collection_id is None:
            raise AppwriteException('Missing required parameter: "collection_id"')

        if document_id is None:
            raise AppwriteException('Missing required parameter: "document_id"')

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)

        api_params['data'] = data
        api_params['permissions'] = permissions

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_document(self, database_id: str, collection_id: str, document_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def decrement_document_attribute(self, database_id: str, collection_id: str, document_id: str, attribute: str, value: float = None, min: float = None) -> Dict[str, Any]:
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
        value : float
            Value to increment the attribute by. The value must be a number.
        min : float
            Minimum value for the attribute. If the current value is lesser than this value, an exception will be thrown.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)
        api_path = api_path.replace('{attribute}', attribute)

        api_params['value'] = value
        api_params['min'] = min

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def increment_document_attribute(self, database_id: str, collection_id: str, document_id: str, attribute: str, value: float = None, max: float = None) -> Dict[str, Any]:
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
        value : float
            Value to increment the attribute by. The value must be a number.
        max : float
            Maximum value for the attribute. If the current value is greater than this value, an error will be thrown.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{documentId}', document_id)
        api_path = api_path.replace('{attribute}', attribute)

        api_params['value'] = value
        api_params['max'] = max

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_indexes(self, database_id: str, collection_id: str, queries: List[str] = None) -> Dict[str, Any]:
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
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, type, status, attributes, error
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def create_index(self, database_id: str, collection_id: str, key: str, type: IndexType, attributes: List[str], orders: List[str] = None, lengths: List[float] = None) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)

        api_params['key'] = key
        api_params['type'] = type
        api_params['attributes'] = attributes
        api_params['orders'] = orders
        api_params['lengths'] = lengths

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_index(self, database_id: str, collection_id: str, key: str) -> Dict[str, Any]:
        """
        Get index by ID.

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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_index(self, database_id: str, collection_id: str, key: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{databaseId}', database_id)
        api_path = api_path.replace('{collectionId}', collection_id)
        api_path = api_path.replace('{key}', key)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)
