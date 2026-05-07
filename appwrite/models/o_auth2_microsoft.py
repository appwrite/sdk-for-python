from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Microsoft(AppwriteModel):
    """
    OAuth2Microsoft

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    applicationid : str
        Microsoft OAuth2 application ID.
    applicationsecret : str
        Microsoft OAuth2 application secret.
    tenant : str
        Microsoft Entra ID tenant identifier. Use &#039;common&#039;, &#039;organizations&#039;, &#039;consumers&#039; or a specific tenant ID.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    applicationid: str = Field(..., alias='applicationId')
    applicationsecret: str = Field(..., alias='applicationSecret')
    tenant: str = Field(..., alias='tenant')
