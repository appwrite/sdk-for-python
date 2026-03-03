from ..service import Service
from typing import List, Dict, Any, Optional
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated

class Activities(Service):

    def __init__(self, client) -> None:
        super(Activities, self).__init__(client)

    def list_events(self, queries: Optional[str] = None) -> Dict[str, Any]:
        """
        List all events for selected filters.

        Parameters
        ----------
        queries : Optional[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on attributes such as userId, teamId, etc.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/activities/events'
        api_params = {}

        if queries is not None:
            api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def get_event(self, event_id: str) -> Dict[str, Any]:
        """
        Get event by ID.
        

        Parameters
        ----------
        event_id : str
            Event ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/activities/events/{eventId}'
        api_params = {}
        if event_id is None:
            raise AppwriteException('Missing required parameter: "event_id"')

        api_path = api_path.replace('{eventId}', event_id)


        return self.client.call('get', api_path, {
        }, api_params)
