from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated

class Graphql(Service):

    def __init__(self, client) -> None:
        super(Graphql, self).__init__(client)

    def query(
        self,
        query: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute a GraphQL mutation.

        Parameters
        ----------
        query : Dict[str, Any]
            The query or queries to execute.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/graphql'
        api_params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        api_params['query'] = self._normalize_value(query)

        response = self.client.call('post', api_path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, api_params)

        return response


    def mutation(
        self,
        query: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute a GraphQL mutation.

        Parameters
        ----------
        query : Dict[str, Any]
            The query or queries to execute.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/graphql/mutation'
        api_params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        api_params['query'] = self._normalize_value(query)

        response = self.client.call('post', api_path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, api_params)

        return response

