from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'baa' not in data:
            data['baa'] = False
        if 'premiumGeoDB' not in data and 'premiumgeodb' not in data:
            data['premiumGeoDB'] = False
        if 'premiumGeoDBOrg' not in data and 'premiumgeodborg' not in data:
            data['premiumGeoDBOrg'] = False
        return data
