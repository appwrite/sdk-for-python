from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2DeviceAuthorization(AppwriteModel):
    """
    OAuth2 Device Authorization

    Attributes
    ----------
    device_code : str
        Device verification code used by the client to poll the token endpoint.
    user_code : str
        Short code the end user enters on the verification page.
    verification_uri : str
        URL where the end user enters the user code.
    verification_uri_complete : str
        Verification URL with the user code prefilled as a query parameter.
    expires_in : float
        Lifetime of the device code and user code in seconds.
    interval : float
        Minimum polling interval for the token endpoint in seconds.
    """
    device_code: str = Field(..., alias='device_code')
    user_code: str = Field(..., alias='user_code')
    verification_uri: str = Field(..., alias='verification_uri')
    verification_uri_complete: str = Field(..., alias='verification_uri_complete')
    expires_in: float = Field(..., alias='expires_in')
    interval: float = Field(..., alias='interval')
