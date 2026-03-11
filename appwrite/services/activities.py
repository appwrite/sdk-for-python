from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.activity_event_list import ActivityEventList;
from ..models.activity_event import ActivityEvent;

class Activities(Service):

    def __init__(self, client) -> None:
        super(Activities, self).__init__(client)

    def list_events(
        self,
        queries: Optional[str] = None
    ) -> ActivityEventList:
        """
        List all events for selected filters.

        Parameters
        ----------
        queries : Optional[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on attributes such as userId, teamId, etc.
        
        Returns
        -------
        ActivityEventList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/activities/events'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ActivityEventList)


    def get_event(
        self,
        event_id: str
    ) -> ActivityEvent:
        """
        Get event by ID.
        

        Parameters
        ----------
        event_id : str
            Event ID.
        
        Returns
        -------
        ActivityEvent
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/activities/events/{eventId}'
        api_params = {}
        if event_id is None:
            raise AppwriteException('Missing required parameter: "event_id"')

        api_path = api_path.replace('{eventId}', str(self._normalize_value(event_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ActivityEvent)

