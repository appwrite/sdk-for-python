from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DedicatedDatabaseExecutionColumn(AppwriteModel):
    """
    ExecutionColumn

    Attributes
    ----------
    name : str
        Column name as returned by the database.
    type : str
        Engine-specific column type (e.g. int4, text, timestamptz).
    """

    name: str = Field(..., alias='name')
    type: str = Field(..., alias='type')
