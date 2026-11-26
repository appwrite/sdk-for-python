from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.monitor_list import MonitorList
from ..enums.monitor_record import MonitorRecord
from ..enums.monitor_severity import MonitorSeverity
from ..models.monitor import Monitor
from ..enums.monitor_method import MonitorMethod
from ..enums.monitor_tls_mode import MonitorTlsMode


class Monitors(Service):

    def __init__(self, client) -> None:
        super(Monitors, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> MonitorList:
        """
        Get a list of the project's monitors of every type. Use queries to filter by type, resource, severity or status, and `Query.search('search', term)` to search monitor IDs, names, metrics and resources.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, type, resourceType, resourceId, enabled, severity, escalationId, status, evaluatedAt, triggeredAt, search
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        MonitorList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors'
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

        return self._parse_response(response, model=MonitorList)

    def create_dns_monitor(
        self,
        monitor_id: str,
        name: str,
        domain: str,
        record: Optional[MonitorRecord] = None,
        resolver: Optional[str] = None,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Create a DNS monitor. It asks a resolver for a domain's records of one type on its own interval, and opens an alert when the resolver fails, or when its rules match the answers, by default when there is no such record. Each alert fires the `monitors.[monitorId].alerts.[alertId].create` event when it opens and `.update` when a check passes again, for project webhooks, functions and realtime, and notifies the organization's members by email and in the console.

        Parameters
        ----------
        monitor_id : str
            Monitor ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Monitor name. Max length: 128 chars.
        domain : str
            Domain to query, such as `example.com`.
        record : Optional[MonitorRecord]
            Record type to query: `A`, `AAAA`, `CNAME`, `MX`, `TXT` or `NS`. Defaults to `A`.
        resolver : Optional[str]
            Resolver to query, as an IP address with an optional port, such as `1.1.1.1` or `[2606:4700:4700::1111]:53`. Defaults to the server's DNS resolver.
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `answer` (the first record returned, compared lowercased without the trailing dot), `answers` (number of records returned), `latency` (milliseconds the check took). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. `answer` takes `equal` and `notEqual` only. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires when the resolver returns no answers.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Defaults to 60, or to the shortest interval your plan allows when that is longer. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Set to false to create the monitor without checking it.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Defaults to owners; pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Leave empty to notify the `notify` roles once.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/dns'
        api_params = {}
        if monitor_id is None:
            raise AppwriteException('Missing required parameter: "monitor_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')
        api_params['monitorId'] = self._normalize_value(monitor_id)
        api_params['name'] = self._normalize_value(name)
        api_params['domain'] = self._normalize_value(domain)
        if record is not None:
            api_params['record'] = self._normalize_value(record)
        if resolver is not None:
            api_params['resolver'] = self._normalize_value(resolver)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def update_dns_monitor(
        self,
        monitor_id: str,
        name: Optional[str] = None,
        domain: Optional[str] = None,
        record: Optional[MonitorRecord] = None,
        resolver: Optional[str] = None,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Update a DNS monitor by its unique ID. Only the parameters passed change; the monitor's state, its last check and its open alert are kept. Passing `rules` replaces all of them.

        Parameters
        ----------
        monitor_id : str
            Monitor ID.
        name : Optional[str]
            Monitor name. Max length: 128 chars.
        domain : Optional[str]
            Domain to query, such as `example.com`.
        record : Optional[MonitorRecord]
            Record type to query: `A`, `AAAA`, `CNAME`, `MX`, `TXT` or `NS`.
        resolver : Optional[str]
            Resolver to query, as an IP address with an optional port, such as `1.1.1.1` or `[2606:4700:4700::1111]:53`. Pass an empty string to use the server's DNS resolver.
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `answer` (the first record returned, compared lowercased without the trailing dot), `answers` (number of records returned), `latency` (milliseconds the check took). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. `answer` takes `equal` and `notEqual` only. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires when the resolver returns no answers. Replaces the current rules; an empty list restores the defaults.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Whether the monitor is checked.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Pass an empty string to go back to the `notify` roles.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/dns/{monitorId}'
        api_params = {}
        if monitor_id is None or monitor_id == '':
            raise AppwriteException('Missing required parameter: "monitor_id"')
        api_path = api_path.replace('{monitorId}', self._encode_path(monitor_id))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        if record is not None:
            api_params['record'] = self._normalize_value(record)
        if resolver is not None:
            api_params['resolver'] = self._normalize_value(resolver)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def create_http_monitor(
        self,
        monitor_id: str,
        name: str,
        url: str,
        method: Optional[MonitorMethod] = None,
        headers: Optional[Dict[str, Any]] = None,
        body: Optional[str] = None,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Create an HTTP monitor. It requests a URL on its own interval, following redirects, and opens an alert when the request fails or when its rules match the response, by default a status outside 2xx or the certificate of an HTTPS URL about to expire. The response body is discarded as it arrives. Each alert fires the `monitors.[monitorId].alerts.[alertId].create` event when it opens and `.update` when a check passes again, for project webhooks, functions and realtime, and notifies the organization's members by email and in the console.

        Parameters
        ----------
        monitor_id : str
            Monitor ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Monitor name. Max length: 128 chars.
        url : str
            URL to request, with an `http` or `https` scheme.
        method : Optional[MonitorMethod]
            HTTP method to request the URL with: `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE` or `OPTIONS`. Defaults to `GET`.
        headers : Optional[Dict[str, Any]]
            HTTP headers to send, as an object of header names and values. Each name must be a valid HTTP header name.
        body : Optional[str]
            Request body to send. Max length: 16384 chars.
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `statusCode` (HTTP status), `latency` (milliseconds the check took), `certificateDays` (whole days until the certificate expires), `certificateLifetime` (percent of the certificate's lifetime left). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires on a status code outside 200 to 299, or on a certificate with fewer than 14 days and less than 25% of its lifetime left.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Defaults to 60, or to the shortest interval your plan allows when that is longer. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Set to false to create the monitor without checking it.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Defaults to owners; pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Leave empty to notify the `notify` roles once.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/http'
        api_params = {}
        if monitor_id is None:
            raise AppwriteException('Missing required parameter: "monitor_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')
        api_params['monitorId'] = self._normalize_value(monitor_id)
        api_params['name'] = self._normalize_value(name)
        api_params['url'] = self._normalize_value(url)
        if method is not None:
            api_params['method'] = self._normalize_value(method)
        if headers is not None:
            api_params['headers'] = self._normalize_value(headers)
        if body is not None:
            api_params['body'] = self._normalize_value(body)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def update_http_monitor(
        self,
        monitor_id: str,
        name: Optional[str] = None,
        url: Optional[str] = None,
        method: Optional[MonitorMethod] = None,
        headers: Optional[Dict[str, Any]] = None,
        body: Optional[str] = None,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Update an HTTP monitor by its unique ID. Only the parameters passed change; the monitor's state, its last check and its open alert are kept. Passing `rules` replaces all of them.

        Parameters
        ----------
        monitor_id : str
            Monitor ID.
        name : Optional[str]
            Monitor name. Max length: 128 chars.
        url : Optional[str]
            URL to request, with an `http` or `https` scheme.
        method : Optional[MonitorMethod]
            HTTP method to request the URL with: `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE` or `OPTIONS`.
        headers : Optional[Dict[str, Any]]
            HTTP headers to send, as an object of header names and values. Each name must be a valid HTTP header name.
        body : Optional[str]
            Request body to send. Max length: 16384 chars.
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `statusCode` (HTTP status), `latency` (milliseconds the check took), `certificateDays` (whole days until the certificate expires), `certificateLifetime` (percent of the certificate's lifetime left). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires on a status code outside 200 to 299, or on a certificate with fewer than 14 days and less than 25% of its lifetime left. Replaces the current rules; an empty list restores the defaults.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Whether the monitor is checked.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Pass an empty string to go back to the `notify` roles.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/http/{monitorId}'
        api_params = {}
        if monitor_id is None or monitor_id == '':
            raise AppwriteException('Missing required parameter: "monitor_id"')
        api_path = api_path.replace('{monitorId}', self._encode_path(monitor_id))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if url is not None:
            api_params['url'] = self._normalize_value(url)
        if method is not None:
            api_params['method'] = self._normalize_value(method)
        if headers is not None:
            api_params['headers'] = self._normalize_value(headers)
        if body is not None:
            api_params['body'] = self._normalize_value(body)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def create_smtp_monitor(
        self,
        monitor_id: str,
        name: str,
        host: str,
        port: float,
        tls_mode: Optional[MonitorTlsMode] = None,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Create an SMTP monitor. It reads a mail server's greeting, sends `EHLO` and, as its TLS mode asks, upgrades with `STARTTLS` or speaks TLS from the start, on its own interval. It opens an alert when the server cannot be reached, refuses the session or fails the TLS handshake, or when its rules match. It never authenticates or sends mail. Each alert fires the `monitors.[monitorId].alerts.[alertId].create` event when it opens and `.update` when a check passes again, for project webhooks, functions and realtime, and notifies the organization's members by email and in the console.

        Parameters
        ----------
        monitor_id : str
            Monitor ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Monitor name. Max length: 128 chars.
        host : str
            Hostname or IP address of the mail server.
        port : float
            Port to connect to, such as 25, 465 or 587.
        tls_mode : Optional[MonitorTlsMode]
            TLS mode: `auto` (`implicit` on port 465, `starttls` on 587 and `none` otherwise), `none`, `starttls` (upgrade after the greeting, and fail when the server does not offer it) or `implicit` (TLS from the first byte). Defaults to `auto`.
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `code` (SMTP reply code), `latency` (milliseconds the check took), `certificateDays` (whole days until the certificate expires), `certificateLifetime` (percent of the certificate's lifetime left). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires on transport failures only.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Defaults to 60, or to the shortest interval your plan allows when that is longer. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Set to false to create the monitor without checking it.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Defaults to owners; pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Leave empty to notify the `notify` roles once.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/smtp'
        api_params = {}
        if monitor_id is None:
            raise AppwriteException('Missing required parameter: "monitor_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if host is None:
            raise AppwriteException('Missing required parameter: "host"')
        if port is None:
            raise AppwriteException('Missing required parameter: "port"')
        api_params['monitorId'] = self._normalize_value(monitor_id)
        api_params['name'] = self._normalize_value(name)
        api_params['host'] = self._normalize_value(host)
        api_params['port'] = self._normalize_value(port)
        if tls_mode is not None:
            api_params['tlsMode'] = self._normalize_value(tls_mode)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def update_smtp_monitor(
        self,
        monitor_id: str,
        name: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[float] = None,
        tls_mode: Optional[MonitorTlsMode] = None,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Update an SMTP monitor by its unique ID. Only the parameters passed change; the monitor's state, its last check and its open alert are kept. Passing `rules` replaces all of them.

        Parameters
        ----------
        monitor_id : str
            Monitor ID.
        name : Optional[str]
            Monitor name. Max length: 128 chars.
        host : Optional[str]
            Hostname or IP address of the mail server.
        port : Optional[float]
            Port to connect to, such as 25, 465 or 587.
        tls_mode : Optional[MonitorTlsMode]
            TLS mode: `auto` (`implicit` on port 465, `starttls` on 587 and `none` otherwise), `none`, `starttls` (upgrade after the greeting, and fail when the server does not offer it) or `implicit` (TLS from the first byte).
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `code` (SMTP reply code), `latency` (milliseconds the check took), `certificateDays` (whole days until the certificate expires), `certificateLifetime` (percent of the certificate's lifetime left). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires on transport failures only. Replaces the current rules; an empty list removes them.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Whether the monitor is checked.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Pass an empty string to go back to the `notify` roles.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/smtp/{monitorId}'
        api_params = {}
        if monitor_id is None or monitor_id == '':
            raise AppwriteException('Missing required parameter: "monitor_id"')
        api_path = api_path.replace('{monitorId}', self._encode_path(monitor_id))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if host is not None:
            api_params['host'] = self._normalize_value(host)
        if port is not None:
            api_params['port'] = self._normalize_value(port)
        if tls_mode is not None:
            api_params['tlsMode'] = self._normalize_value(tls_mode)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def create_tcp_monitor(
        self,
        monitor_id: str,
        name: str,
        host: str,
        port: float,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Create a TCP monitor. It opens a connection to a host and port on its own interval and closes it at once, and opens an alert when the connection cannot be made, or when its rules match. Each alert fires the `monitors.[monitorId].alerts.[alertId].create` event when it opens and `.update` when a check passes again, for project webhooks, functions and realtime, and notifies the organization's members by email and in the console.

        Parameters
        ----------
        monitor_id : str
            Monitor ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Monitor name. Max length: 128 chars.
        host : str
            Hostname or IP address to connect to.
        port : float
            Port to connect to.
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `latency` (milliseconds the check took). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires on transport failures only.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Defaults to 60, or to the shortest interval your plan allows when that is longer. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Set to false to create the monitor without checking it.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Defaults to owners; pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Leave empty to notify the `notify` roles once.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/tcp'
        api_params = {}
        if monitor_id is None:
            raise AppwriteException('Missing required parameter: "monitor_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if host is None:
            raise AppwriteException('Missing required parameter: "host"')
        if port is None:
            raise AppwriteException('Missing required parameter: "port"')
        api_params['monitorId'] = self._normalize_value(monitor_id)
        api_params['name'] = self._normalize_value(name)
        api_params['host'] = self._normalize_value(host)
        api_params['port'] = self._normalize_value(port)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def update_tcp_monitor(
        self,
        monitor_id: str,
        name: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[float] = None,
        rules: Optional[List[str]] = None,
        interval: Optional[float] = None,
        timeout: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Update a TCP monitor by its unique ID. Only the parameters passed change; the monitor's state, its last check and its open alert are kept. Passing `rules` replaces all of them.

        Parameters
        ----------
        monitor_id : str
            Monitor ID.
        name : Optional[str]
            Monitor name. Max length: 128 chars.
        host : Optional[str]
            Hostname or IP address to connect to.
        port : Optional[float]
            Port to connect to.
        rules : Optional[List[str]]
            Rules that describe the failing state, as query strings generated with the Query class. The monitor fires when they match. Transport failures, such as timeouts, DNS failures, refused connections and denied targets, always fire. Variables: `latency` (milliseconds the check took). Operators: `equal`, `notEqual`, `lessThan`, `lessThanEqual`, `greaterThan`, `greaterThanEqual`, `between`, `notBetween`. Combine rules with `or` and `and`; top-level rules must all match. Without rules it fires on transport failures only. Replaces the current rules; an empty list removes them.
        interval : Optional[float]
            Seconds between two checks, between 1 and 2592000. The scheduler runs on a one second tick, so one second is the shortest interval. Reads back raised to your plan's minimum interval when the plan no longer allows it.
        timeout : Optional[float]
            Seconds a check may take before it fails, between 1 and 60, and no longer than the interval.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Whether the monitor is checked.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Pass an empty string to go back to the `notify` roles.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/tcp/{monitorId}'
        api_params = {}
        if monitor_id is None or monitor_id == '':
            raise AppwriteException('Missing required parameter: "monitor_id"')
        api_path = api_path.replace('{monitorId}', self._encode_path(monitor_id))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if host is not None:
            api_params['host'] = self._normalize_value(host)
        if port is not None:
            api_params['port'] = self._normalize_value(port)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def create_usage_monitor(
        self,
        monitor_id: str,
        name: str,
        rules: List[str],
        window: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Create a usage monitor. It reads a usage metric of the project, or of one of its databases, buckets, functions or sites, on a schedule, and opens an alert when all its rules hold. Each alert fires the `monitors.[monitorId].alerts.[alertId].create` event when it opens and `.update` when usage recovers, for project webhooks, functions and realtime, and notifies the confirmed members of the `notify` roles by email and in the console, or the steps of the escalation set by `escalationId`.

        Parameters
        ----------
        monitor_id : str
            Monitor ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Monitor name. Max length: 128 chars.
        rules : List[str]
            Rules that must all hold for the monitor to fire, as query strings generated with the Query class: one comparing a usage metric, named as the usage endpoints name it (such as `network.outbound` or `databases.operations.reads`), with a threshold in the metric's unit (bytes for storage and bandwidth, MB-seconds for GB-hours, a count otherwise), and optionally `equal` rules on `resourceType` and `resourceId` to watch one database, bucket, function or site instead of the whole project.
        window : Optional[float]
            Seconds a counter metric is summed over, between 60 and 2592000. Gauges compare their latest value.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Set to false to create the monitor without evaluating it.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Defaults to owners; pass an empty list to rely on the alert events alone.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Leave empty to notify the `notify` roles once.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/usage'
        api_params = {}
        if monitor_id is None:
            raise AppwriteException('Missing required parameter: "monitor_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if rules is None:
            raise AppwriteException('Missing required parameter: "rules"')
        api_params['monitorId'] = self._normalize_value(monitor_id)
        api_params['name'] = self._normalize_value(name)
        api_params['rules'] = self._normalize_value(rules)
        if window is not None:
            api_params['window'] = self._normalize_value(window)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def update_usage_monitor(
        self,
        monitor_id: str,
        name: Optional[str] = None,
        rules: Optional[List[str]] = None,
        window: Optional[float] = None,
        cooldown: Optional[float] = None,
        enabled: Optional[bool] = None,
        notify: Optional[List[str]] = None,
        severity: Optional[MonitorSeverity] = None,
        escalation_id: Optional[str] = None,
    ) -> Monitor:
        """
        Update a usage monitor by its unique ID. Only the parameters passed change; the monitor's state and its open alert are kept. Passing `rules` replaces all of them.

        Parameters
        ----------
        monitor_id : str
            Monitor ID.
        name : Optional[str]
            Monitor name. Max length: 128 chars.
        rules : Optional[List[str]]
            Rules that must all hold for the monitor to fire, as query strings generated with the Query class: one comparing a usage metric, named as the usage endpoints name it (such as `network.outbound` or `databases.operations.reads`), with a threshold in the metric's unit (bytes for storage and bandwidth, MB-seconds for GB-hours, a count otherwise), and optionally `equal` rules on `resourceType` and `resourceId` to watch one database, bucket, function or site instead of the whole project. Replaces the current rules.
        window : Optional[float]
            Seconds a counter metric is summed over, between 60 and 2592000. Gauges compare their latest value.
        cooldown : Optional[float]
            Minimum seconds between two team notifications of this monitor firing, between 300 and 2592000. Events fire on every change between firing and resolved regardless.
        enabled : Optional[bool]
            Whether the monitor is evaluated.
        notify : Optional[List[str]]
            Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Each must be an organization role, such as `owner` or `developer`. Pass an empty list to rely on the alert events alone; pass null or omit to keep the current roles.
        severity : Optional[MonitorSeverity]
            How urgent the monitor's alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it, such as a push that rings through silent mode. Omit to keep the current one.
        escalation_id : Optional[str]
            ID of an escalation of the organization that notifies the team of this monitor's alerts step by step, until a member acknowledges the alert or it resolves. When set, `notify` is not used. Pass an empty string to go back to the `notify` roles; pass null or omit to keep the current one.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/usage/{monitorId}'
        api_params = {}
        if monitor_id is None or monitor_id == '':
            raise AppwriteException('Missing required parameter: "monitor_id"')
        api_path = api_path.replace('{monitorId}', self._encode_path(monitor_id))
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)
        if window is not None:
            api_params['window'] = self._normalize_value(window)
        if cooldown is not None:
            api_params['cooldown'] = self._normalize_value(cooldown)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if notify is not None:
            api_params['notify'] = self._normalize_value(notify)
        if severity is not None:
            api_params['severity'] = self._normalize_value(severity)
        if escalation_id is not None:
            api_params['escalationId'] = self._normalize_value(escalation_id)

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

        return self._parse_response(response, model=Monitor)

    def get(
        self,
        monitor_id: str,
    ) -> Monitor:
        """
        Get a monitor by its unique ID, with its state as of its last evaluation.

        Parameters
        ----------
        monitor_id : str
            Monitor ID.
        Returns
        -------
        Monitor
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/{monitorId}'
        api_params = {}
        if monitor_id is None or monitor_id == '':
            raise AppwriteException('Missing required parameter: "monitor_id"')
        api_path = api_path.replace('{monitorId}', self._encode_path(monitor_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Monitor)

    def delete(
        self,
        monitor_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a monitor by its unique ID. It stops being evaluated; an alert it is firing is resolved and kept with the rest of its alert history.

        Parameters
        ----------
        monitor_id : str
            Monitor ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/monitors/{monitorId}'
        api_params = {}
        if monitor_id is None or monitor_id == '':
            raise AppwriteException('Missing required parameter: "monitor_id"')
        api_path = api_path.replace('{monitorId}', self._encode_path(monitor_id))

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
