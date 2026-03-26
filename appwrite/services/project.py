from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.variable_list import VariableList;
from ..models.variable import Variable;

class Project(Service):

    def __init__(self, client) -> None:
        super(Project, self).__init__(client)

    def list_variables(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> VariableList:
        """
        Get a list of all project environment variables.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: key, resourceType, resourceId, secret
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        VariableList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VariableList)


    def create_variable(
        self,
        variable_id: str,
        key: str,
        value: str,
        secret: Optional[bool] = None
    ) -> Variable:
        """
        Create a new project environment variable. These variables can be accessed by all functions and sites in the project.

        Parameters
        ----------
        variable_id : str
            Variable ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        key : str
            Variable key. Max length: 255 chars.
        value : str
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only projects can read them during build and runtime.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if value is None:
            raise AppwriteException('Missing required parameter: "value"')


        api_params['variableId'] = self._normalize_value(variable_id)
        api_params['key'] = self._normalize_value(key)
        api_params['value'] = self._normalize_value(value)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def get_variable(
        self,
        variable_id: str
    ) -> Variable:
        """
        Get a variable by its unique ID. 

        Parameters
        ----------
        variable_id : str
            Variable ID.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables/{variableId}'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Variable)


    def update_variable(
        self,
        variable_id: str,
        key: Optional[str] = None,
        value: Optional[str] = None,
        secret: Optional[bool] = None
    ) -> Variable:
        """
        Update variable by its unique ID.

        Parameters
        ----------
        variable_id : str
            Variable ID.
        key : Optional[str]
            Variable key. Max length: 255 chars.
        value : Optional[str]
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only projects can read them during build and runtime.
        
        Returns
        -------
        Variable
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables/{variableId}'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['value'] = self._normalize_value(value)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def delete_variable(
        self,
        variable_id: str
    ) -> Dict[str, Any]:
        """
        Delete a variable by its unique ID. 

        Parameters
        ----------
        variable_id : str
            Variable ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/project/variables/{variableId}'
        api_params = {}
        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

