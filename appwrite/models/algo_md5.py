from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
