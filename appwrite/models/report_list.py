from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
