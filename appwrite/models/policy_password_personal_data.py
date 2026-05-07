from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicyPasswordPersonalData(AppwriteModel):
    """
    Policy Password Personal Data

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether password personal data policy is enabled.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
