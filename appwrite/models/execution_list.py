from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .execution import Execution

class ExecutionList(AppwriteModel):
    """
    Executions List

    Attributes
    ----------
    total : float
        Total number of executions that matched your query.
    executions : List[Execution]
        List of executions.
    """
    total: float = Field(..., alias='total')
    executions: List[Execution] = Field(..., alias='executions')
