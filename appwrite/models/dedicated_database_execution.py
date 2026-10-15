from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'rows' not in data:
            data['rows'] = []
        if 'rowCount' not in data and 'rowcount' not in data:
            data['rowCount'] = 0
        if 'columns' not in data:
            data['columns'] = []
        if 'durationMs' not in data and 'durationms' not in data:
            data['durationMs'] = 0
        if 'truncated' not in data:
            data['truncated'] = False
        if 'bytes' not in data:
            data['bytes'] = 0
        return data
