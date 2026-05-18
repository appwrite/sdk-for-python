from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.usage_event_list import UsageEventList;
from ..models.usage_gauge_list import UsageGaugeList;

class Usage(Service):

    def __init__(self, client) -> None:
        super(Usage, self).__init__(client)

    def list_events(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> UsageEventList:
        """
        Query usage event metrics from the usage database. Returns individual event rows with full metadata. Pass Query objects as JSON strings to filter, paginate, and order results. Supported query methods: equal, greaterThanEqual, lessThanEqual, orderAsc, orderDesc, limit, offset. Supported filter attributes: metric, path, method, status, resource, resourceId, country, userAgent, time (these match the underlying column names — note that the response surfaces `resource` as `resourceType` and `country` as `countryCode`). When no time filter is supplied the endpoint defaults to the last 7 days. Default `limit(100)` is applied if none is given; user-supplied limits are capped at 500. The `total` field is capped at 5000 to keep counts predictable — pass `total=false` to skip the count entirely.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings as JSON. Supported: equal("metric", [...]), equal("path", [...]), equal("method", [...]), equal("status", [...]), equal("resource", [...]), equal("resourceId", [...]), equal("country", [...]), equal("userAgent", [...]), greaterThanEqual("time", "..."), lessThanEqual("time", "..."), orderAsc("time"), orderDesc("time"), limit(N), offset(N).
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        UsageEventList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/usage/events'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=UsageEventList)


    def list_gauges(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> UsageGaugeList:
        """
        Query usage gauge metrics (point-in-time resource snapshots) from the usage database. Returns individual gauge snapshots with metric, value, and timestamp. Pass Query objects as JSON strings to filter, paginate, and order results. Supported query methods: equal, greaterThanEqual, lessThanEqual, orderAsc, orderDesc, limit, offset. Supported filter attributes: metric, time. Use `orderDesc("time"), limit(1)` to fetch the most recent snapshot. When no time filter is supplied the endpoint defaults to the last 7 days. Default `limit(100)` is applied if none is given; user-supplied limits are capped at 500. The `total` field is capped at 5000 to keep counts predictable — pass `total=false` to skip the count entirely.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings as JSON. Supported: equal("metric", [...]), greaterThanEqual("time", "..."), lessThanEqual("time", "..."), orderAsc("time"), orderDesc("time"), limit(N), offset(N).
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        UsageGaugeList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/usage/gauges'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=UsageGaugeList)

