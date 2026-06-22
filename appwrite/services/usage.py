from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.usage_event_list import UsageEventList
from ..models.usage_gauge_list import UsageGaugeList

class Usage(Service):

    def __init__(self, client) -> None:
        super(Usage, self).__init__(client)

    def list_events(
        self,
        metrics: List[str],
        resource: Optional[str] = None,
        resource_id: Optional[str] = None,
        interval: Optional[str] = None,
        dimensions: Optional[List[str]] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        order_by: Optional[str] = None,
        order_dir: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None
    ) -> UsageEventList:
        """
        Aggregate usage event metrics. `metrics[]` (1-10) is required; the response always contains one entry per requested metric, each with its own `points[]` time series.
        
        **Two response shapes**:
        - Omit `interval` for a flat top-N table — one point per dimension combination, no time axis. Useful for "top 10 paths by bandwidth in the last 7 days".
        - Pass `interval` (`1m`, `15m`, `30m`, `1h`, `1d`) for a time series — one point per (time bucket × dimension combination).
        
        `dimensions[]` breaks each point down by one or more attributes (service, path, status, country, …). Pass multiple metrics to render stacked charts in one round-trip. `resource` and `resourceId` filter the underlying events. `orderBy=value`+`orderDir=desc`+`limit=N` returns the top-N by aggregated value. When `startAt` is omitted, the default window adapts to `interval` (or 7d when interval is omitted).

        Parameters
        ----------
        metrics : List[str]
            One to ten metric names. Single-metric callers pass a one-element array. Example: `metrics[]=executions` or `metrics[]=executions&metrics[]=executions.compute` for stacked charts.
        resource : Optional[str]
            Resource type filter (singular form). Common values: function, site, database, bucket, file, webhook, team, user, project.
        resource_id : Optional[str]
            Resource id filter.
        interval : Optional[str]
            Time interval size. Omit (null) for a flat aggregate over the whole window. Allowed: 1m, 15m, 30m, 1h, 1d.
        dimensions : Optional[List[str]]
            Break-down dimensions (max 10). Allowed: path, method, status, service, country, region, hostname, osName, clientType, clientName, deviceName, teamId, resourceId.
        start_at : Optional[str]
            Range start in ISO 8601. Defaults adapt to interval (7d for the no-interval aggregate).
        end_at : Optional[str]
            Range end in ISO 8601. Defaults to the current time.
        order_by : Optional[str]
            Column to order by. Allowed: time, value. Default time when an interval is set; otherwise value.
        order_dir : Optional[str]
            Sort direction: asc or desc. Default desc — paired with the default limit, returns the most recent / highest-value groups first.
        limit : Optional[float]
            Maximum rows to return (1-5000).
        offset : Optional[float]
            Pagination offset (0-100000).
        
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
        if metrics is None:
            raise AppwriteException('Missing required parameter: "metrics"')


        api_params['metrics'] = self._normalize_value(metrics)
        if resource is not None:
            api_params['resource'] = self._normalize_value(resource)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if dimensions is not None:
            api_params['dimensions'] = self._normalize_value(dimensions)
        if start_at is not None:
            api_params['startAt'] = self._normalize_value(start_at)
        if end_at is not None:
            api_params['endAt'] = self._normalize_value(end_at)
        if order_by is not None:
            api_params['orderBy'] = self._normalize_value(order_by)
        if order_dir is not None:
            api_params['orderDir'] = self._normalize_value(order_dir)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=UsageEventList)


    def list_gauges(
        self,
        metrics: List[str],
        resource_id: Optional[str] = None,
        team_id: Optional[str] = None,
        interval: Optional[str] = None,
        dimensions: Optional[List[str]] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        order_by: Optional[str] = None,
        order_dir: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None
    ) -> UsageGaugeList:
        """
        Aggregate usage gauge snapshots. Gauges are point-in-time values (storage totals, resource counts, …); each point carries the latest snapshot in its interval via `argMax(value, time)`. `metrics[]` (1-10) is required; the response always contains one entry per requested metric, each with its own `points[]` time series.
        
        **Two response shapes**:
        - Omit `interval` for a flat top-N table — `argMax(value, time)` per dimension combination over the whole window, no time axis. Useful for "top 10 resources by current storage".
        - Pass `interval` (`1m`, `15m`, `30m`, `1h`, `1d`) for a time series — one snapshot per (time bucket × dimension combination).
        
        `dimensions[]` breaks each point down further. Supported on gauges: `resourceId`, `teamId`, `service`, `resource`. `service` and `resource` enable per-service / per-resource-type panels (e.g. storage-by-service: group `files.storage`, `deployments.storage`, `builds.storage`, `databases.storage` by `service`). Pass multiple metrics to render stacked charts in one round-trip. `resourceId` and `teamId` parameters filter the underlying rows. `orderBy=value`+`orderDir=desc`+`limit=N` returns the top-N. When `startAt` is omitted, the default window adapts to interval (or 7d when interval is omitted).

        Parameters
        ----------
        metrics : List[str]
            One to ten metric names. Single-metric callers pass a one-element array. Example: `metrics[]=files.storage` or `metrics[]=files.storage&metrics[]=deployments.storage` for stacked charts.
        resource_id : Optional[str]
            Resource id filter.
        team_id : Optional[str]
            Team id filter.
        interval : Optional[str]
            Time interval size. Omit (null) for a flat aggregate over the whole window. Allowed: 1m, 15m, 30m, 1h, 1d.
        dimensions : Optional[List[str]]
            Break-down dimensions. Allowed: resourceId, teamId, service, resource.
        start_at : Optional[str]
            Range start in ISO 8601. Defaults to endAt - 7d.
        end_at : Optional[str]
            Range end in ISO 8601. Defaults to the current time.
        order_by : Optional[str]
            Column to order by. Allowed: time, value. Default time.
        order_dir : Optional[str]
            Sort direction: asc or desc. Default desc — paired with the default limit, this returns the most recent groups first. Pass asc for chronological charting.
        limit : Optional[float]
            Maximum rows to return (1-5000).
        offset : Optional[float]
            Pagination offset (0-100000).
        
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
        if metrics is None:
            raise AppwriteException('Missing required parameter: "metrics"')


        api_params['metrics'] = self._normalize_value(metrics)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if team_id is not None:
            api_params['teamId'] = self._normalize_value(team_id)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if dimensions is not None:
            api_params['dimensions'] = self._normalize_value(dimensions)
        if start_at is not None:
            api_params['startAt'] = self._normalize_value(start_at)
        if end_at is not None:
            api_params['endAt'] = self._normalize_value(end_at)
        if order_by is not None:
            api_params['orderBy'] = self._normalize_value(order_by)
        if order_dir is not None:
            api_params['orderDir'] = self._normalize_value(order_dir)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=UsageGaugeList)

