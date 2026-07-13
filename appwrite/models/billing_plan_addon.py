from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .billing_plan_addon_details import BillingPlanAddonDetails

class BillingPlanAddon(AppwriteModel):
    """
    Addon

    Attributes
    ----------
    seats : BillingPlanAddonDetails
        Addon seats
    projects : BillingPlanAddonDetails
        Addon projects
    """
    seats: BillingPlanAddonDetails = Field(..., alias='seats')
    projects: BillingPlanAddonDetails = Field(..., alias='projects')
