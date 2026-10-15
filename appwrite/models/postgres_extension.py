from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PostgresExtension(AppwriteModel):
    """
    Postgres extension

    Attributes
    ----------
    key : str
        Extension key used with CREATE EXTENSION.
    name : str
        Human-readable extension name.
    description : str
        Short description of what the extension provides.
    category : str
        Category the extension belongs to.
    """

    key: str = Field(..., alias='key')
    name: str = Field(..., alias='name')
    description: str = Field(..., alias='description')
    category: str = Field(..., alias='category')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'key' not in data:
            data['key'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'category' not in data:
            data['category'] = ''
        return data
