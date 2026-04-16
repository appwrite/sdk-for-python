from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MockNumber(AppwriteModel):
    """
    Mock Number

    Attributes
    ----------
    phone : str
        Mock phone number for testing phone authentication. Useful for testing phone authentication without sending an SMS.
    otp : str
        Mock OTP for the number. 
    """
    phone: str = Field(..., alias='phone')
    otp: str = Field(..., alias='otp')
