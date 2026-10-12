from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .postgres_extension import PostgresExtension


class DedicatedDatabaseExtensions(AppwriteModel):
    """
    Extensions

    Attributes
    ----------
    installed : List[Any]
        List of installed extensions.
    available : List[Any]
        List of available extensions that can be installed.
    metadata : List[PostgresExtension]
        Curated metadata (display name, description, category) for each available extension.
    """

    installed: List[Any] = Field(..., alias='installed')
    available: List[Any] = Field(..., alias='available')
    metadata: List[PostgresExtension] = Field(..., alias='metadata')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'installed' not in data:
            data['installed'] = []
        if 'available' not in data:
            data['available'] = []
        return data
