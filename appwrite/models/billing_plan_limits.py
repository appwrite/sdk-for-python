from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BillingPlanLimits(AppwriteModel):
    """
    PlanLimits

    Attributes
    ----------
    credits : Optional[float]
        Credits limit per billing cycle
    dailycredits : Optional[float]
        Daily credits limit (if applicable)
    """
    credits: Optional[float] = Field(default=None, alias='credits')
    dailycredits: Optional[float] = Field(default=None, alias='dailyCredits')
