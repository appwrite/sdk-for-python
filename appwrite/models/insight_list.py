from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .insight import Insight

class InsightList(AppwriteModel):
    """
    Insights List

    Attributes
    ----------
    total : float
        Total number of insights that matched your query.
    insights : List[Insight]
        List of insights.
    """
    total: float = Field(..., alias='total')
    insights: List[Insight] = Field(..., alias='insights')
