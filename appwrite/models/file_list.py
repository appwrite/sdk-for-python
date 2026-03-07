from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
