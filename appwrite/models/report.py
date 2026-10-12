from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .insight import Insight


class Report(AppwriteModel):
    """
    Report

    Attributes
    ----------
    id : str
        Report ID.
    createdat : str
        Report creation date in ISO 8601 format.
    updatedat : str
        Report update date in ISO 8601 format.
    appid : str
        ID of the third-party app that submitted the report.
    type : str
        Analyzer that produced this report. e.g. lighthouse, audit, databaseAnalyzer.
    title : str
        Short, human-readable title for the report.
    summary : str
        Markdown summary describing the report.
    targettype : str
        Plural noun describing what the report analyzes, e.g. databases, sites, urls.
    target : str
        Free-form target identifier (URL for lighthouse, resource ID for db).
    categories : List[Any]
        Categories covered by the report, e.g. performance, accessibility.
    insights : List[Insight]
        Insights nested under this report.
    analyzedat : Optional[str]
        Time the report was analyzed in ISO 8601 format.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    appid: str = Field(..., alias='appId')
    type: str = Field(..., alias='type')
    title: str = Field(..., alias='title')
    summary: str = Field(..., alias='summary')
    targettype: str = Field(..., alias='targetType')
    target: str = Field(..., alias='target')
    categories: List[Any] = Field(..., alias='categories')
    insights: List[Insight] = Field(..., alias='insights')
    analyzedat: Optional[str] = Field(default=None, alias='analyzedAt')

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
        if 'appId' not in data and 'appid' not in data:
            data['appId'] = ''
        if 'type' not in data:
            data['type'] = ''
        if 'title' not in data:
            data['title'] = ''
        if 'summary' not in data:
            data['summary'] = ''
        if 'targetType' not in data and 'targettype' not in data:
            data['targetType'] = ''
        if 'target' not in data:
            data['target'] = ''
        if 'categories' not in data:
            data['categories'] = []
        return data
