from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BillingPlanSupportedAddons(AppwriteModel):
    """
    BillingPlanSupportedAddons

    Attributes
    ----------
    baa : bool
        Whether the plan supports BAA (Business Associate Agreement) addon
    premiumgeodb : bool
        Whether the plan supports Premium Geo DB addon (project-level)
    premiumgeodborg : bool
        Whether the plan supports Premium Geo DB addon (organization-level)
    """
    baa: bool = Field(..., alias='baa')
    premiumgeodb: bool = Field(..., alias='premiumGeoDB')
    premiumgeodborg: bool = Field(..., alias='premiumGeoDBOrg')
