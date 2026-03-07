from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .variable import Variable

class VariableList(AppwriteModel):
    """
    Variables List

    Attributes
    ----------
    total : float
        Total number of variables that matched your query.
    variables : List[Variable]
        List of variables.
    """
    total: float = Field(..., alias='total')
    variables: List[Variable] = Field(..., alias='variables')
