from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .oauth2_organization import Oauth2Organization

class Oauth2OrganizationList(AppwriteModel):
    """
    OAuth2 accessible organizations list

    Attributes
    ----------
    total : float
        Total number of organizations that matched your query.
    organizations : List[Oauth2Organization]
        List of organizations.
    """
    total: float = Field(..., alias='total')
    organizations: List[Oauth2Organization] = Field(..., alias='organizations')
