from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class HealthQueue(AppwriteModel):
    """
    Health Queue

    Attributes
    ----------
    size : float
        Amount of actions in the queue.
    """
    size: float = Field(..., alias='size')
