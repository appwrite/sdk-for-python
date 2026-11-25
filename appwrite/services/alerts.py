from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.alert_list import AlertList
from ..models.alert import Alert


class Alerts(Service):

    def __init__(self, client) -> None:
        super(Alerts, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> AlertList:
        """
        Get a list of the alerts the project's monitors raised, open and resolved. An alert is created when a monitor starts firing and resolved when it recovers. Use queries to filter by monitor, status, type or resource, order by `$createdAt` for the latest first, and `Query.search('search', term)` to search alert and monitor IDs, names and metrics.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: monitorId, name, status, type, resourceType, resourceId, metric, resolvedAt, search
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        AlertList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/alerts'
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

        return self._parse_response(response, model=AlertList)

    def get(
        self,
        alert_id: str,
    ) -> Alert:
        """
        Get an alert by its unique ID: the monitor that raised it, when it fired and resolved, and the readings while it fired.

        Parameters
        ----------
        alert_id : str
            Alert ID.
        Returns
        -------
        Alert
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/alerts/{alertId}'
        api_params = {}
        if alert_id is None or alert_id == '':
            raise AppwriteException('Missing required parameter: "alert_id"')
        api_path = api_path.replace('{alertId}', self._encode_path(alert_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Alert)

    def update(
        self,
        alert_id: str,
        acknowledged: bool,
    ) -> Alert:
        """
        Acknowledge a firing alert, or undo that. Everyone who can read the alert sees who acknowledged it and when. The alert keeps firing until its monitor recovers; a resolved alert keeps its acknowledgement and cannot be changed.

        Parameters
        ----------
        alert_id : str
            Alert ID.
        acknowledged : bool
            Whether the alert is acknowledged. False undoes an acknowledgement.
        Returns
        -------
        Alert
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/alerts/{alertId}'
        api_params = {}
        if alert_id is None or alert_id == '':
            raise AppwriteException('Missing required parameter: "alert_id"')
        if acknowledged is None:
            raise AppwriteException('Missing required parameter: "acknowledged"')
        api_path = api_path.replace('{alertId}', self._encode_path(alert_id))
        api_params['acknowledged'] = self._normalize_value(acknowledged)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Alert)
