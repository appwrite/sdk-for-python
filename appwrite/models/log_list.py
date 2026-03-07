from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .log import Log

class LogList(AppwriteModel):
    """
    Logs List

    Attributes
    ----------
    total : float
        Total number of logs that matched your query.
    logs : List[Log]
        List of logs.
    """
    total: float = Field(..., alias='total')
    logs: List[Log] = Field(..., alias='logs')
