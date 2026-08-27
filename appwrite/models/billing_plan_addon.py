from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .billing_plan_addon_details import BillingPlanAddonDetails


class BillingPlanAddon(AppwriteModel):
    """
    Addon

    Attributes
    ----------
    seats : Optional[BillingPlanAddonDetails]
        Addon seats
    projects : Optional[BillingPlanAddonDetails]
        Addon projects
    """

    seats: Optional[BillingPlanAddonDetails] = Field(default=None, alias='seats')
    projects: Optional[BillingPlanAddonDetails] = Field(default=None, alias='projects')
