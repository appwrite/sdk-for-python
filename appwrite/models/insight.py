from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .insight_cta import InsightCTA


class Insight(AppwriteModel):
    """
    Insight

    Attributes
    ----------
    id : str
        Insight ID.
    createdat : str
        Insight creation date in ISO 8601 format.
    updatedat : str
        Insight update date in ISO 8601 format.
    reportid : str
        Parent report ID. Insights always belong to a report.
    type : str
        Insight type. One of databaseIndex (legacy), tablesDBIndex, documentsDBIndex, vectorsDBIndex, databasePerformance, sitePerformance, siteAccessibility, siteSeo, functionPerformance. The index types are engine-specific so each CTA can pair the right service+method (databases.createIndex, tablesDB.createIndex, documentsDB.createIndex, or vectorsDB.createIndex).
    severity : str
        Insight severity. One of info, warning, critical.
    status : str
        Insight status. One of active, dismissed.
    resourcetype : str
        Type of the resource the insight is about. Plural noun, e.g. databases, sites, functions.
    resourceid : str
        ID of the resource the insight is about.
    parentresourcetype : str
        Plural noun for the parent resource that contains the insight&#039;s resource, e.g. an insight about a column index on a table → resourceType=indexes, parentResourceType=tables. Empty when the resource has no parent.
    parentresourceid : str
        ID of the parent resource. Empty when the resource has no parent.
    title : str
        Insight title.
    summary : str
        Short markdown summary describing the insight.
    ctas : List[InsightCTA]
        List of call-to-action buttons attached to this insight.
    analyzedat : Optional[str]
        Time the insight was analyzed in ISO 8601 format.
    dismissedat : Optional[str]
        Time the insight was dismissed in ISO 8601 format. Empty when not dismissed.
    dismissedby : Optional[str]
        User ID that dismissed the insight. Empty when not dismissed.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    reportid: str = Field(..., alias='reportId')
    type: str = Field(..., alias='type')
    severity: str = Field(..., alias='severity')
    status: str = Field(..., alias='status')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    parentresourcetype: str = Field(..., alias='parentResourceType')
    parentresourceid: str = Field(..., alias='parentResourceId')
    title: str = Field(..., alias='title')
    summary: str = Field(..., alias='summary')
    ctas: List[InsightCTA] = Field(..., alias='ctas')
    analyzedat: Optional[str] = Field(default=None, alias='analyzedAt')
    dismissedat: Optional[str] = Field(default=None, alias='dismissedAt')
    dismissedby: Optional[str] = Field(default=None, alias='dismissedBy')

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
        if 'reportId' not in data and 'reportid' not in data:
            data['reportId'] = ''
        if 'type' not in data:
            data['type'] = ''
        if 'severity' not in data:
            data['severity'] = 'info'
        if 'status' not in data:
            data['status'] = 'active'
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = ''
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'parentResourceType' not in data and 'parentresourcetype' not in data:
            data['parentResourceType'] = ''
        if 'parentResourceId' not in data and 'parentresourceid' not in data:
            data['parentResourceId'] = ''
        if 'title' not in data:
            data['title'] = ''
        if 'summary' not in data:
            data['summary'] = ''
        if 'ctas' not in data:
            data['ctas'] = []
        return data
