from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.analytics_property_type import AnalyticsPropertyType


class AnalyticsProperty(AppwriteModel):
    """
    AnalyticsProperty

    Attributes
    ----------
    id : str
        Analytics property ID.
    createdat : str
        Property creation date in ISO 8601 format.
    updatedat : str
        Property update date in ISO 8601 format.
    name : str
        Human-readable name of the tracked website or application.
    domain : str
        Primary domain being tracked (e.g. example.com). May be empty for mobile and agent properties.
    enabled : bool
        Whether tracking is currently active.
    allowedorigins : List[Any]
        List of origins allowed to send tracking events. Use [&quot;*&quot;] to allow all. Managed by Appwrite for a property linked to a site, following the site&#039;s production domains.
    type : AnalyticsPropertyType
        Kind of product this property tracks. Decides which dashboard panels apply.
    identifyusers : bool
        Whether events sent from a signed-in client session record that user&#039;s ID.
    accessedat : str
        Most recent event date in ISO 8601 format. This attribute is only updated again after 24 hours.
    firstaccessedat : str
        First event date in ISO 8601 format. Empty until the property receives its first event.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    domain: str = Field(..., alias='domain')
    enabled: bool = Field(..., alias='enabled')
    allowedorigins: List[Any] = Field(..., alias='allowedOrigins')
    type: AnalyticsPropertyType = Field(..., alias='type')
    identifyusers: bool = Field(..., alias='identifyUsers')
    accessedat: str = Field(..., alias='accessedAt')
    firstaccessedat: str = Field(..., alias='firstAccessedAt')

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
        if 'name' not in data:
            data['name'] = ''
        if 'domain' not in data:
            data['domain'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'allowedOrigins' not in data and 'allowedorigins' not in data:
            data['allowedOrigins'] = ['*']
        if 'type' not in data:
            data['type'] = 'web'
        if 'identifyUsers' not in data and 'identifyusers' not in data:
            data['identifyUsers'] = False
        if 'accessedAt' not in data and 'accessedat' not in data:
            data['accessedAt'] = ''
        if 'firstAccessedAt' not in data and 'firstaccessedat' not in data:
            data['firstAccessedAt'] = ''
        return data
