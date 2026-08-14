from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_operation import DedicatedDatabaseOperation

class DedicatedDatabaseOperationList(AppwriteModel):
    """
    OperationList

    Attributes
    ----------
    total : float
        Total number of operations.
    operations : List[DedicatedDatabaseOperation]
        List of operations.
    """
    total: float = Field(..., alias='total')
    operations: List[DedicatedDatabaseOperation] = Field(..., alias='operations')
