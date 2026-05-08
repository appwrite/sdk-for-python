from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicyPasswordDictionary(AppwriteModel):
    """
    Policy Password Dictionary

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether password dictionary policy is enabled.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
