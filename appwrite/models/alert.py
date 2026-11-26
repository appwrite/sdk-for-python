from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.alert_status import AlertStatus
from ..enums.monitor_severity import MonitorSeverity
from ..enums.alert_metric import AlertMetric
from ..enums.alert_comparator import AlertComparator
from ..enums.monitor_type import MonitorType
from ..enums.monitor_resource_type import MonitorResourceType
from ..enums.monitor_result import MonitorResult


class Alert(AppwriteModel):
    """
    Alert

    Attributes
    ----------
    id : str
        Alert ID.
    createdat : str
        Date the alert started firing, in ISO 8601 format.
    updatedat : str
        Alert update date in ISO 8601 format.
    monitorid : str
        ID of the monitor that raised the alert.
    projectid : str
        ID of the project the alert is about. Empty for an alert of the whole organization.
    name : str
        Name of the monitor when the alert fired.
    status : AlertStatus
        Whether the alert is still firing or has resolved.
    resolvedat : Optional[str]
        Date the alert resolved, in ISO 8601 format. Empty while it fires.
    acknowledgedat : Optional[str]
        Date a member acknowledged the alert, in ISO 8601 format. Empty while nobody has.
    acknowledgedby : str
        ID of the user who acknowledged the alert. Empty while nobody has, or when it was acknowledged with an API key.
    acknowledgedbyname : str
        Name of the user who acknowledged the alert, when they did.
    escalationid : str
        ID of the escalation notifying the team of this alert. Empty when the monitor notified its `notify` roles instead.
    escalationstep : float
        Index of the escalation&#039;s next step to notify, counting from 0. Equal to the number of steps once the last round has gone out.
    escalationround : float
        How many times the escalation&#039;s steps have been repeated for this alert.
    escalatesat : Optional[str]
        When the next step is notified, in ISO 8601 format. Null when nothing is due: the alert was acknowledged or resolved, or every step has gone out.
    rules : List[Any]
        The monitor&#039;s rules when the alert fired, as query strings.
    severity : MonitorSeverity
        The monitor&#039;s severity when the alert fired: `info`, `warning`, `error` or `critical`.
    metric : Optional[AlertMetric]
        Metric the alert fired on. Null for a probe monitor&#039;s alert.
    comparator : Optional[AlertComparator]
        How the metric was compared with the threshold. Null for a probe monitor&#039;s alert.
    threshold : float
        Threshold the metric crossed, in the metric&#039;s unit.
    value : float
        Latest reading while the alert fired: the metric&#039;s value for a usage monitor, and for a probe monitor its `latency`.
    peak : float
        Reading furthest past the threshold while the alert fired.
    type : MonitorType
        Type of the monitor that raised the alert.
    resourcetype : MonitorResourceType
        Type of the resource the alert fired on: the project, or one database, bucket, function or site.
    resourceid : str
        ID of the resource the alert fired on. The project ID for a project-wide monitor.
    notifications : float
        How many times the alert was announced as firing: once when it fired, and again after each cooldown while it kept firing.
    latency : Optional[float]
        Probe monitors: response time in milliseconds of the latest check recorded on the alert.
    result : Optional[MonitorResult]
        What the failing check of a probe monitor found when the alert opened, such as `connect_refused`. Null for a usage monitor&#039;s alert.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    monitorid: str = Field(..., alias='monitorId')
    projectid: str = Field(..., alias='projectId')
    name: str = Field(..., alias='name')
    status: AlertStatus = Field(..., alias='status')
    resolvedat: Optional[str] = Field(default=None, alias='resolvedAt')
    acknowledgedat: Optional[str] = Field(default=None, alias='acknowledgedAt')
    acknowledgedby: str = Field(..., alias='acknowledgedBy')
    acknowledgedbyname: str = Field(..., alias='acknowledgedByName')
    escalationid: str = Field(..., alias='escalationId')
    escalationstep: float = Field(..., alias='escalationStep')
    escalationround: float = Field(..., alias='escalationRound')
    escalatesat: Optional[str] = Field(default=None, alias='escalatesAt')
    rules: List[Any] = Field(..., alias='rules')
    severity: MonitorSeverity = Field(..., alias='severity')
    metric: Optional[AlertMetric] = Field(default=None, alias='metric')
    comparator: Optional[AlertComparator] = Field(default=None, alias='comparator')
    threshold: float = Field(..., alias='threshold')
    value: float = Field(..., alias='value')
    peak: float = Field(..., alias='peak')
    type: MonitorType = Field(..., alias='type')
    resourcetype: MonitorResourceType = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    notifications: float = Field(..., alias='notifications')
    latency: Optional[float] = Field(default=None, alias='latency')
    result: Optional[MonitorResult] = Field(default=None, alias='result')

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
        if 'monitorId' not in data and 'monitorid' not in data:
            data['monitorId'] = ''
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'status' not in data:
            data['status'] = 'firing'
        if 'acknowledgedBy' not in data and 'acknowledgedby' not in data:
            data['acknowledgedBy'] = ''
        if 'acknowledgedByName' not in data and 'acknowledgedbyname' not in data:
            data['acknowledgedByName'] = ''
        if 'escalationId' not in data and 'escalationid' not in data:
            data['escalationId'] = ''
        if 'escalationStep' not in data and 'escalationstep' not in data:
            data['escalationStep'] = 0
        if 'escalationRound' not in data and 'escalationround' not in data:
            data['escalationRound'] = 0
        if 'rules' not in data:
            data['rules'] = []
        if 'severity' not in data:
            data['severity'] = 'warning'
        if 'threshold' not in data:
            data['threshold'] = 0
        if 'value' not in data:
            data['value'] = 0
        if 'peak' not in data:
            data['peak'] = 0
        if 'type' not in data:
            data['type'] = 'usage'
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = 'project'
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'notifications' not in data:
            data['notifications'] = 0
        return data
