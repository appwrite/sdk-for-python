from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .file import File


class FileList(AppwriteModel):
    """
    Files List

    Attributes
    ----------
    total : float
        Total number of files that matched your query.
    files : List[File]
        List of files.
    """

    total: float = Field(..., alias='total')
    files: List[File] = Field(..., alias='files')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
