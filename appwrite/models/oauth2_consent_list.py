from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .oauth2_consent import Oauth2Consent

class Oauth2ConsentList(AppwriteModel):
    """
    OAuth2 consents list

    Attributes
    ----------
    total : float
        Total number of consents that matched your query.
    consents : List[Oauth2Consent]
        List of consents.
    """
    total: float = Field(..., alias='total')
    consents: List[Oauth2Consent] = Field(..., alias='consents')
