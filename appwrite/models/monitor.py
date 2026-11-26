from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.monitor_type import MonitorType
from ..enums.monitor_resource_type import MonitorResourceType
from ..enums.monitor_severity import MonitorSeverity
from ..enums.monitor_status import MonitorStatus
from ..enums.monitor_method import MonitorMethod
from ..enums.monitor_record import MonitorRecord
from ..enums.monitor_tls_mode import MonitorTlsMode
from ..enums.monitor_result import MonitorResult


class Monitor(AppwriteModel):
    """
    Monitor

    Attributes
    ----------
    id : str
        Monitor ID.
    createdat : str
        Monitor creation date in ISO 8601 format.
    updatedat : str
        Monitor update date in ISO 8601 format.
    name : str
        Monitor name.
    projectid : str
        Project ID.
    rules : List[Any]
        Rules that must all hold for the monitor to fire, as query strings. A usage monitor has one comparing a metric with a threshold, optionally scoped with `equal(&#039;resourceType&#039;)` and `equal(&#039;resourceId&#039;)`. A probe monitor fires when its rules match the check, over these variables: `http` `statusCode`, `latency`, `certificateDays` and `certificateLifetime`; `dns` `answer`, `answers` and `latency`; `tcp` `latency`; `smtp` `code`, `latency`, `certificateDays` and `certificateLifetime`. A failed connection fires whatever the rules.
    type : MonitorType
        What the monitor checks: `usage` compares a usage metric with a threshold; `http`, `dns`, `tcp` and `smtp` probe a target on their own interval.
    resourcetype : MonitorResourceType
        Type of the resource the monitor watches, from its rules: the project, or one database, bucket, function or site.
    resourceid : str
        ID of the resource the monitor watches, from its rules. The project ID for a project-wide monitor.
    window : float
        Seconds a counter metric is summed over, and a growth metric is measured across. Gauges compare their latest value. Usage is read a short lag behind the evaluation (`_APP_ALERTS_USAGE_LAG`, 120 seconds by default) so events still being written are counted by the next evaluation.
    cooldown : float
        Minimum seconds between two team notifications of this monitor firing. Events fire on every change regardless.
    enabled : bool
        Whether the monitor is evaluated.
    notify : List[Any]
        Organization roles whose confirmed members get an email and a console notification when the monitor fires and resolves. Empty when the alert events are the only delivery. Not used while `escalationId` is set.
    escalationid : str
        ID of the organization&#039;s escalation that notifies the team of this monitor&#039;s alerts, step by step until one is acknowledged. When set, `notify` is not used. Empty to notify the `notify` roles once.
    severity : MonitorSeverity
        How urgent the monitor&#039;s alerts are: `info`, `warning`, `error` or `critical`. Critical alerts may be delivered with higher urgency by the notification channels that support it.
    status : MonitorStatus
        Whether the monitor is firing, as of its last evaluation.
    value : Optional[float]
        Metric value at the last evaluation. Null before the first evaluation, and when the last evaluation (`evaluatedAt`) found no usage recorded to read: without data a monitor is not compared, so it keeps its status and open alert.
    evaluatedat : Optional[str]
        Last evaluation date in ISO 8601 format.
    alertid : str
        ID of the alert the monitor is firing for. Empty while it is not firing.
    triggeredat : Optional[str]
        Date the monitor last announced an alert, in ISO 8601 format.
    interval : float
        Probe monitors: seconds between two checks, read back raised to the plan&#039;s minimum. 0 for usage monitors, which are evaluated on the server&#039;s interval.
    timeout : float
        Probe monitors: seconds a check may take before it fails.
    url : str
        HTTP monitors: URL requested.
    method : Optional[MonitorMethod]
        HTTP monitors: method the URL is requested with. Null for other types.
    headers : Optional[Dict[str, Any]]
        HTTP monitors: headers sent, as an object of header names and values.
    body : str
        HTTP monitors: request body sent.
    domain : str
        DNS monitors: domain queried.
    record : Optional[MonitorRecord]
        DNS monitors: record type queried. Null for other types.
    resolver : str
        DNS monitors: resolver queried. Empty for the server&#039;s DNS resolver.
    host : str
        TCP and SMTP monitors: hostname or IP address connected to.
    port : float
        TCP and SMTP monitors: port connected to.
    tlsmode : Optional[MonitorTlsMode]
        SMTP monitors: how the connection is secured. `auto` picks implicit TLS on port 465, STARTTLS on 587 and none otherwise. Null for other types.
    result : Optional[MonitorResult]
        Probe monitors: what the last check found. `ok` passes; anything else opened the monitor&#039;s alert. Null before the first check.
    latency : Optional[float]
        Probe monitors: milliseconds the last check took.
    code : Optional[float]
        Probe monitors: last status code an HTTP target answered with, reply code an SMTP server sent, or response code a DNS resolver returned.
    certificateexpiresat : Optional[str]
        Probe monitors: expiry date of the TLS certificate the last check saw, in ISO 8601 format. Null without TLS.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    projectid: str = Field(..., alias='projectId')
    rules: List[Any] = Field(..., alias='rules')
    type: MonitorType = Field(..., alias='type')
    resourcetype: MonitorResourceType = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    window: float = Field(..., alias='window')
    cooldown: float = Field(..., alias='cooldown')
    enabled: bool = Field(..., alias='enabled')
    notify: List[Any] = Field(..., alias='notify')
    escalationid: str = Field(..., alias='escalationId')
    severity: MonitorSeverity = Field(..., alias='severity')
    status: MonitorStatus = Field(..., alias='status')
    value: Optional[float] = Field(default=None, alias='value')
    evaluatedat: Optional[str] = Field(default=None, alias='evaluatedAt')
    alertid: str = Field(..., alias='alertId')
    triggeredat: Optional[str] = Field(default=None, alias='triggeredAt')
    interval: float = Field(..., alias='interval')
    timeout: float = Field(..., alias='timeout')
    url: str = Field(..., alias='url')
    method: Optional[MonitorMethod] = Field(default=None, alias='method')
    headers: Optional[Dict[str, Any]] = Field(default=None, alias='headers')
    body: str = Field(..., alias='body')
    domain: str = Field(..., alias='domain')
    record: Optional[MonitorRecord] = Field(default=None, alias='record')
    resolver: str = Field(..., alias='resolver')
    host: str = Field(..., alias='host')
    port: float = Field(..., alias='port')
    tlsmode: Optional[MonitorTlsMode] = Field(default=None, alias='tlsMode')
    result: Optional[MonitorResult] = Field(default=None, alias='result')
    latency: Optional[float] = Field(default=None, alias='latency')
    code: Optional[float] = Field(default=None, alias='code')
    certificateexpiresat: Optional[str] = Field(default=None, alias='certificateExpiresAt')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'rules' not in data:
            data['rules'] = []
        if 'type' not in data:
            data['type'] = 'usage'
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = 'project'
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'window' not in data:
            data['window'] = 3600
        if 'cooldown' not in data:
            data['cooldown'] = 3600
        if 'enabled' not in data:
            data['enabled'] = True
        if 'notify' not in data:
            data['notify'] = ['owner']
        if 'escalationId' not in data and 'escalationid' not in data:
            data['escalationId'] = ''
        if 'severity' not in data:
            data['severity'] = 'warning'
        if 'status' not in data:
            data['status'] = 'ok'
        if 'alertId' not in data and 'alertid' not in data:
            data['alertId'] = ''
        if 'interval' not in data:
            data['interval'] = 0
        if 'timeout' not in data:
            data['timeout'] = 0
        if 'url' not in data:
            data['url'] = ''
        if 'body' not in data:
            data['body'] = ''
        if 'domain' not in data:
            data['domain'] = ''
        if 'resolver' not in data:
            data['resolver'] = ''
        if 'host' not in data:
            data['host'] = ''
        if 'port' not in data:
            data['port'] = 0
        return data
