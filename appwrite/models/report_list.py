from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .report import Report

class ReportList(AppwriteModel):
    """
    Reports List

    Attributes
    ----------
    total : float
        Total number of reports that matched your query.
    reports : List[Report]
        List of reports.
    """
    total: float = Field(..., alias='total')
    reports: List[Report] = Field(..., alias='reports')
