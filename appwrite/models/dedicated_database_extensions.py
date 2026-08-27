from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
