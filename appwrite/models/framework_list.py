from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .framework import Framework

class FrameworkList(AppwriteModel):
    """
    Frameworks List

    Attributes
    ----------
    total : float
        Total number of frameworks that matched your query.
    frameworks : List[Framework]
        List of frameworks.
    """
    total: float = Field(..., alias='total')
    frameworks: List[Framework] = Field(..., alias='frameworks')
