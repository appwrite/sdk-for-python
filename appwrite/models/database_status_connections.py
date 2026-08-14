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
        The engine&#039;s own max_connections. On a pooled database this is the backend limit the pooler multiplexes onto, not the ceiling a client pool may reach — that is networkMaxConnections on the database resource.
    """
    current: float = Field(..., alias='current')
    max: float = Field(..., alias='max')
