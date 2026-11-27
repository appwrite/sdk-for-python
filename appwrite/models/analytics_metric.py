from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class AnalyticsMetric(AppwriteModel):
    """
    AnalyticsMetric

    Attributes
    ----------
    value : Optional[str]
        Dimension value this row covers. Null when no dimension was requested, empty when the dimension could not be derived for those events.
    date : Optional[str]
        Start of the time bucket this row covers, in ISO 8601. Null when no interval was requested.
    visitors : float
        Unique visitors in the requested range.
    sessions : float
        Unique sessions in the requested range.
    pageviews : Optional[float]
        Total page and screen view events (events named &quot;pageview&quot; or &quot;screen_view&quot;) in the requested range. The flat aggregate and the time series compute it; null on breakdown rows.
    events : float
        Total events in the requested range.
    users : Optional[float]
        Unique identified users in the requested range. Anonymous events are not counted. Null on entry and exit page breakdown rows.
    visits : Optional[float]
        Total sessions with activity in the requested range. Only the flat aggregate computes it; null on breakdown and time-series rows.
    bouncerate : Optional[float]
        Share of bounced visits, as a percentage; a visit is a bounce unless it records two or more page or screen views, at least one interaction, or ten seconds or more of activity. An interaction is any event that is neither a view nor automatic measurement such as &quot;app_foregrounded&quot;, &quot;engagement_time&quot; or &quot;scroll_depth&quot;. Only the flat aggregate computes it; null on breakdown and time-series rows.
    visitduration : Optional[float]
        Average session length in seconds, measured first event to last event. Single-event sessions count as 0. Only the flat aggregate computes it; null on breakdown and time-series rows.
    viewspervisit : Optional[float]
        Average pageviews per session (pageviews divided by visits). Only the flat aggregate computes it; null on breakdown and time-series rows.
    scrolldepth : Optional[float]
        Average scroll depth across events, as a percentage. Only the flat aggregate computes it; null on breakdown and time-series rows.
    engagementtime : Optional[float]
        Average engaged time per session in seconds, counting only foreground time. Sessions that reported no engagement are excluded. Only the flat aggregate computes it; null on breakdown and time-series rows.
    """

    value: Optional[str] = Field(default=None, alias='value')
    date: Optional[str] = Field(default=None, alias='date')
    visitors: float = Field(..., alias='visitors')
    sessions: float = Field(..., alias='sessions')
    pageviews: Optional[float] = Field(default=None, alias='pageviews')
    events: float = Field(..., alias='events')
    users: Optional[float] = Field(default=None, alias='users')
    visits: Optional[float] = Field(default=None, alias='visits')
    bouncerate: Optional[float] = Field(default=None, alias='bounceRate')
    visitduration: Optional[float] = Field(default=None, alias='visitDuration')
    viewspervisit: Optional[float] = Field(default=None, alias='viewsPerVisit')
    scrolldepth: Optional[float] = Field(default=None, alias='scrollDepth')
    engagementtime: Optional[float] = Field(default=None, alias='engagementTime')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'visitors' not in data:
            data['visitors'] = 0
        if 'sessions' not in data:
            data['sessions'] = 0
        if 'events' not in data:
            data['events'] = 0
        return data
