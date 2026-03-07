from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .function import Function

class FunctionList(AppwriteModel):
    """
    Functions List

    Attributes
    ----------
    total : float
        Total number of functions that matched your query.
    functions : List[Function]
        List of functions.
    """
    total: float = Field(..., alias='total')
    functions: List[Function] = Field(..., alias='functions')
