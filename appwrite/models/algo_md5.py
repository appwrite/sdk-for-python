from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class AlgoMd5(AppwriteModel):
    """
    AlgoMD5

    Attributes
    ----------
    type : str
        Algo type.
    """
    type: str = Field(..., alias='type')
