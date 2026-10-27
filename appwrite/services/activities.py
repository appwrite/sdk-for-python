from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.activity_event_list import ActivityEventList
from ..models.activity_event import ActivityEvent


class Activities(Service):

    def __init__(self, client) -> None:
        super(Activities, self).__init__(client)

    def list_events(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> ActivityEventList:
        """
        List all events for selected filters.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on attributes such as userId, teamId, etc.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
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
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=ActivityEventList)

    def get_event(
        self,
        event_id: str,
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
        if event_id is None or event_id == '':
            raise AppwriteException('Missing required parameter: "event_id"')
        api_path = api_path.replace('{eventId}', self._encode_path(event_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=ActivityEvent)
