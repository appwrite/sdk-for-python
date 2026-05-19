from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
