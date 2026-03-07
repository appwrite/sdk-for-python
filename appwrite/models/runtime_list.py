from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .runtime import Runtime

class RuntimeList(AppwriteModel):
    """
    Runtimes List

    Attributes
    ----------
    total : float
        Total number of runtimes that matched your query.
    runtimes : List[Runtime]
        List of runtimes.
    """
    total: float = Field(..., alias='total')
    runtimes: List[Runtime] = Field(..., alias='runtimes')
