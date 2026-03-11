from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AlgoSha(AppwriteModel):
    """
    AlgoSHA

    Attributes
    ----------
    type : str
        Algo type.
    """
    type: str = Field(..., alias='type')
