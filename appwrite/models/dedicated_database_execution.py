from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_execution_column import DedicatedDatabaseExecutionColumn


class DedicatedDatabaseExecution(AppwriteModel):
    """
    Execution

    Attributes
    ----------
    rows : List[Any]
        Result rows as a list of column-name =&gt; value maps. Empty for non-returning statements.
    rowcount : float
        Number of rows returned (for SELECT) or affected (for INSERT/UPDATE/DELETE).
    columns : List[DedicatedDatabaseExecutionColumn]
        Column metadata in result-set order.
    durationms : float
        Server-side execution time in milliseconds.
    truncated : bool
        True when the configured row or byte cap was hit and the result was truncated.
    bytes : float
        Serialised payload size in bytes.
    """

    rows: List[Any] = Field(..., alias='rows')
    rowcount: float = Field(..., alias='rowCount')
    columns: List[DedicatedDatabaseExecutionColumn] = Field(..., alias='columns')
    durationms: float = Field(..., alias='durationMs')
    truncated: bool = Field(..., alias='truncated')
    bytes: float = Field(..., alias='bytes')
