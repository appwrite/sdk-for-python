from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DatabaseStatusConnections(AppwriteModel):
    """
    Connections

    Attributes
    ----------
    current : float
        Current number of active connections.
    max : float
        Maximum allowed connections.
    """
    current: float = Field(..., alias='current')
    max: float = Field(..., alias='max')
