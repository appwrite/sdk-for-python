from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MockNumber(AppwriteModel):
    """
    Mock Number

    Attributes
    ----------
    number : str
        Mock phone number for testing phone authentication. Useful for testing phone authentication without sending an SMS.
    otp : str
        Mock OTP for the number. 
    createdat : str
        Attribute creation date in ISO 8601 format.
    updatedat : str
        Attribute update date in ISO 8601 format.
    """
    number: str = Field(..., alias='number')
    otp: str = Field(..., alias='otp')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
