from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.analytics_property_list import AnalyticsPropertyList
from ..enums.analytics_property_type import AnalyticsPropertyType
from ..models.analytics_property import AnalyticsProperty
from ..models.analytics_annotation_list import AnalyticsAnnotationList
from ..models.analytics_annotation import AnalyticsAnnotation
from ..enums.analytics_interval import AnalyticsInterval
from ..enums.analytics_dimension import AnalyticsDimension
from ..models.analytics_metric_list import AnalyticsMetricList


class Analytics(Service):

    def __init__(self, client) -> None:
        super(Analytics, self).__init__(client)

    def list_properties(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None,
    ) -> AnalyticsPropertyList:
        """
        List analytics properties for the current project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, domain, enabled, type
        search : Optional[str]
            Search term to filter your list results. Matches the property ID, name and domain. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        AnalyticsPropertyList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
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

        return self._parse_response(response, model=AnalyticsPropertyList)

    def create_property(
        self,
        property_id: str,
        name: str,
        domain: Optional[str] = None,
        enabled: Optional[bool] = None,
        allowed_origins: Optional[List[str]] = None,
        identify_users: Optional[bool] = None,
        type: Optional[AnalyticsPropertyType] = None,
    ) -> AnalyticsProperty:
        """
        Create a new analytics property to track a website or application.

        Parameters
        ----------
        property_id : str
            Unique ID. Choose a custom ID or generate a random ID with `ID.unique()`. Max length is 36 chars.
        name : str
            Human-readable name for this property.
        domain : Optional[str]
            Primary domain to track (e.g. example.com). May be empty for mobile and agent properties.
        enabled : Optional[bool]
            Whether the property accepts events. Events sent to a disabled property are rejected as not found.
        allowed_origins : Optional[List[str]]
            Allowed origins for tracking. Use ["*"] to allow all.
        identify_users : Optional[bool]
            Record the signed-in user's ID on events sent from a client session, so traffic can be broken down and counted by user. Off by default.
        type : Optional[AnalyticsPropertyType]
            Kind of product this property tracks. Only changes which panels the dashboard shows; ingestion accepts the same events for every type.
        Returns
        -------
        AnalyticsProperty
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties'
        api_params = {}
        if property_id is None:
            raise AppwriteException('Missing required parameter: "property_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_params['propertyId'] = self._normalize_value(property_id)
        api_params['name'] = self._normalize_value(name)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if allowed_origins is not None:
            api_params['allowedOrigins'] = self._normalize_value(allowed_origins)
        if identify_users is not None:
            api_params['identifyUsers'] = self._normalize_value(identify_users)
        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=AnalyticsProperty)

    def get_property(
        self,
        property_id: str,
    ) -> AnalyticsProperty:
        """
        Get an analytics property by ID.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        Returns
        -------
        AnalyticsProperty
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=AnalyticsProperty)

    def update_property(
        self,
        property_id: str,
        name: Optional[str] = None,
        domain: Optional[str] = None,
        enabled: Optional[bool] = None,
        allowed_origins: Optional[List[str]] = None,
        identify_users: Optional[bool] = None,
        type: Optional[AnalyticsPropertyType] = None,
    ) -> AnalyticsProperty:
        """
        Update an analytics property. Only the attributes you pass are changed; omitted attributes keep their current value.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        name : Optional[str]
            Human-readable name for this property.
        domain : Optional[str]
            Primary domain to track (e.g. example.com). Pass an empty string to clear it.
        enabled : Optional[bool]
            Whether the property accepts events. Events sent to a disabled property are rejected as not found.
        allowed_origins : Optional[List[str]]
            Allowed origins for tracking. Use ["*"] to allow all. On a property linked to a site, Appwrite manages this list: it is rewritten from the site's production domains whenever they change.
        identify_users : Optional[bool]
            Record the signed-in user's ID on events sent from a client session, so traffic can be broken down and counted by user.
        type : Optional[AnalyticsPropertyType]
            Kind of product this property tracks. Only changes which panels the dashboard shows; stored events are kept.
        Returns
        -------
        AnalyticsProperty
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if allowed_origins is not None:
            api_params['allowedOrigins'] = self._normalize_value(allowed_origins)
        if identify_users is not None:
            api_params['identifyUsers'] = self._normalize_value(identify_users)
        if type is not None:
            api_params['type'] = self._normalize_value(type)

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

        return self._parse_response(response, model=AnalyticsProperty)

    def delete_property(
        self,
        property_id: str,
    ) -> Dict[str, Any]:
        """
        Delete an analytics property along with every event and session collected for it. This cannot be undone.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def list_annotations(
        self,
        property_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> AnalyticsAnnotationList:
        """
        List the annotations of an analytics property. Filter on `date` to fetch the annotations inside a chart's time range.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: date
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        AnalyticsAnnotationList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}/annotations'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
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

        return self._parse_response(response, model=AnalyticsAnnotationList)

    def create_annotation(
        self,
        property_id: str,
        annotation_id: str,
        date: str,
        content: str,
    ) -> AnalyticsAnnotation:
        """
        Create an annotation that marks a point in time on an analytics property's charts.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        annotation_id : str
            Unique ID. Choose a custom ID or generate a random ID with `ID.unique()`. Max length is 36 chars.
        date : str
            Point in time the annotation marks, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        content : str
            Annotation text. Max length: 512 chars.
        Returns
        -------
        AnalyticsAnnotation
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}/annotations'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        if annotation_id is None:
            raise AppwriteException('Missing required parameter: "annotation_id"')
        if date is None:
            raise AppwriteException('Missing required parameter: "date"')
        if content is None:
            raise AppwriteException('Missing required parameter: "content"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
        api_params['annotationId'] = self._normalize_value(annotation_id)
        api_params['date'] = self._normalize_value(date)
        api_params['content'] = self._normalize_value(content)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=AnalyticsAnnotation)

    def get_annotation(
        self,
        property_id: str,
        annotation_id: str,
    ) -> AnalyticsAnnotation:
        """
        Get an analytics annotation by ID.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        annotation_id : str
            Annotation unique ID.
        Returns
        -------
        AnalyticsAnnotation
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}/annotations/{annotationId}'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        if annotation_id is None or annotation_id == '':
            raise AppwriteException('Missing required parameter: "annotation_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
        api_path = api_path.replace('{annotationId}', self._encode_path(annotation_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=AnalyticsAnnotation)

    def update_annotation(
        self,
        property_id: str,
        annotation_id: str,
        date: Optional[str] = None,
        content: Optional[str] = None,
    ) -> AnalyticsAnnotation:
        """
        Update an analytics annotation. Only the attributes you pass are changed; omitted attributes keep their current value.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        annotation_id : str
            Annotation unique ID.
        date : Optional[str]
            Point in time the annotation marks, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        content : Optional[str]
            Annotation text. Max length: 512 chars.
        Returns
        -------
        AnalyticsAnnotation
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}/annotations/{annotationId}'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        if annotation_id is None or annotation_id == '':
            raise AppwriteException('Missing required parameter: "annotation_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
        api_path = api_path.replace('{annotationId}', self._encode_path(annotation_id))
        if date is not None:
            api_params['date'] = self._normalize_value(date)
        if content is not None:
            api_params['content'] = self._normalize_value(content)

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

        return self._parse_response(response, model=AnalyticsAnnotation)

    def delete_annotation(
        self,
        property_id: str,
        annotation_id: str,
    ) -> Dict[str, Any]:
        """
        Delete an analytics annotation.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        annotation_id : str
            Annotation unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}/annotations/{annotationId}'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        if annotation_id is None or annotation_id == '':
            raise AppwriteException('Missing required parameter: "annotation_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
        api_path = api_path.replace('{annotationId}', self._encode_path(annotation_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def create_event(
        self,
        property_id: str,
        name: str,
        url: str,
        domain: Optional[str] = None,
        referrer: Optional[str] = None,
        screen_width: Optional[float] = None,
        session_hash: Optional[str] = None,
        scroll_depth: Optional[float] = None,
        engagement_time: Optional[float] = None,
        props: Optional[List[str]] = None,
        user_id: Optional[str] = None,
        ip: Optional[str] = None,
        user_agent: Optional[str] = None,
        interactive: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Send a tracking event from a browser, native app, or server-side SDK.

        Parameters
        ----------
        property_id : str
            Analytics property ID.
        name : str
            Event name. "pageview" and "screen_view" are counted as views, every other name is a custom event.
        url : str
            Full page URL or screen identifier.
        domain : Optional[str]
            Hostname (e.g. example.com).
        referrer : Optional[str]
            Referrer URL.
        screen_width : Optional[float]
            Viewport width in CSS pixels.
        session_hash : Optional[str]
            Optional session hash (provided by SDK).
        scroll_depth : Optional[float]
            Scroll depth percentage 0-100.
        engagement_time : Optional[float]
            Engagement time in seconds, 0-4294967295.
        props : Optional[List[str]]
            Custom string properties as a flat key=value list (max 32 entries, alternating key,value).
        user_id : Optional[str]
            Override user ID. Pass an opaque ID, not personal data such as an email. Requires API-key auth with analytics.write scope.
        ip : Optional[str]
            Override IP address. Requires API-key auth with analytics.write scope.
        user_agent : Optional[str]
            Override user agent. Requires API-key auth with analytics.write scope.
        interactive : Optional[bool]
            Whether this event is a visitor interaction that ends a bounce. Set false for telemetry such as heartbeats or background syncs. Defaults to true for custom events and false for the automatic engagement, scroll and app lifecycle events. Ignored for views.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}/events'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
        api_params['name'] = self._normalize_value(name)
        api_params['url'] = self._normalize_value(url)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        if referrer is not None:
            api_params['referrer'] = self._normalize_value(referrer)
        if screen_width is not None:
            api_params['screenWidth'] = self._normalize_value(screen_width)
        if session_hash is not None:
            api_params['sessionHash'] = self._normalize_value(session_hash)
        if scroll_depth is not None:
            api_params['scrollDepth'] = self._normalize_value(scroll_depth)
        if engagement_time is not None:
            api_params['engagementTime'] = self._normalize_value(engagement_time)
        if props is not None:
            api_params['props'] = self._normalize_value(props)
        if user_id is not None:
            api_params['userId'] = self._normalize_value(user_id)
        if ip is not None:
            api_params['ip'] = self._normalize_value(ip)
        if user_agent is not None:
            api_params['userAgent'] = self._normalize_value(user_agent)
        if interactive is not None:
            api_params['interactive'] = self._normalize_value(interactive)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def list_metrics(
        self,
        property_id: str,
        queries: Optional[List[str]] = None,
        interval: Optional[AnalyticsInterval] = None,
        dimensions: Optional[List[AnalyticsDimension]] = None,
        prop_key: Optional[str] = None,
        date_range: Optional[str] = None,
        start_at: Optional[str] = None,
        end_at: Optional[str] = None,
        limit: Optional[float] = None,
        total: Optional[bool] = None,
    ) -> AnalyticsMetricList:
        """
        Read analytics metrics (visitors, sessions, pageviews, events, bounceRate, …) for a property over a date range.

        **Three response shapes**, chosen by `dimensions[]` and `interval`:
        - Neither: one row aggregating the whole window, with `value` and `date` null. Only this shape carries `visits`, `bounceRate`, `visitDuration`, `viewsPerVisit`, `scrollDepth` and `engagementTime`.
        - `dimensions[]`: one row per dimension value, ranked by visitors, with `value` set and `date` null.
        - `interval`: one row per time bucket in chronological order, with `date` set and `value` null.

        `pageviews` is carried by the flat aggregate and by `interval`, but not by a breakdown.

        `userId` and `users` cover identified traffic only: events sent with an API key's `userId`, or from a signed-in session on a property with `identifyUsers` on. A `userId` breakdown leaves out anonymous events; returned values are the project's user IDs.

        Custom event props: `dimensions[]=props` ranks the prop keys seen in the window, and adding `propKey` ranks the values of that one key. `queries[]` filters on a prop's value with the `props.<key>` attribute, e.g. `equal("props.plan", ["pro"])`.

        Combining `dimensions[]` with `interval` is not supported yet. `queries[]` filters the underlying events using standard Utopia query syntax.

        Parameters
        ----------
        property_id : str
            Analytics property unique ID.
        queries : Optional[List[str]]
            Up to 10 filter queries in Utopia syntax. Allowed attributes: country, region, city, browser, browserVersion, operatingSystem, operatingSystemVersion, device, screenSize, referrerSource, channel, utmSource, utmMedium, utmCampaign, utmContent, utmTerm, page, hostname, trafficType, botName, botCategory, userId, eventName, and `props.<key>` for a custom prop. page, userId, eventName and `props.<key>` are only accepted alongside `interval`, or with a breakdown on a dimension other than entryPage, exitPage. Allowed methods: equal, notEqual, contains, startsWith, endsWith. Example: `queries[]=equal("country", ["US"])`.
        interval : Optional[AnalyticsInterval]
            Time bucket size. Omit (null) for a flat aggregate over the whole window. Allowed: 1h, 1d, 1w, 1m.
        dimensions : Optional[List[AnalyticsDimension]]
            Dimension to break the metrics down by. One at most for now; the parameter is a list so that cap can be raised without a breaking change. Allowed: country, region, city, browser, browserVersion, operatingSystem, operatingSystemVersion, device, screenSize, referrerSource, channel, utmSource, utmMedium, utmCampaign, utmContent, utmTerm, page, hostname, entryPage, exitPage, trafficType, botName, botCategory, userId, eventName, props.
        prop_key : Optional[str]
            Custom prop key whose values to rank, with `dimensions[]=props`. Omit to rank the prop keys themselves.
        date_range : Optional[str]
            Date range shorthand (e.g. 7d, 30d). Ignored for any bound you supply explicitly via startAt/endAt.
        start_at : Optional[str]
            Explicit window start in ISO 8601. Defaults to endAt minus dateRange.
        end_at : Optional[str]
            Explicit window end in ISO 8601. Defaults to the current time.
        limit : Optional[float]
            Maximum number of ranked values to return.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        AnalyticsMetricList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/analytics/properties/{propertyId}/metrics'
        api_params = {}
        if property_id is None or property_id == '':
            raise AppwriteException('Missing required parameter: "property_id"')
        api_path = api_path.replace('{propertyId}', self._encode_path(property_id))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if dimensions is not None:
            api_params['dimensions'] = self._normalize_value(dimensions)
        if prop_key is not None:
            api_params['propKey'] = self._normalize_value(prop_key)
        if date_range is not None:
            api_params['dateRange'] = self._normalize_value(date_range)
        if start_at is not None:
            api_params['startAt'] = self._normalize_value(start_at)
        if end_at is not None:
            api_params['endAt'] = self._normalize_value(end_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
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

        return self._parse_response(response, model=AnalyticsMetricList)
