from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PolicySessionAlert(AppwriteModel):
    """
    Policy Session Alert

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether session alert policy is enabled.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
