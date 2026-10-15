from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'name' not in data:
            data['name'] = ''
        if 'type' not in data:
            data['type'] = ''
        return data
