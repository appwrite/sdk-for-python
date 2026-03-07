from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class AlgoPhpass(AppwriteModel):
    """
    AlgoPHPass

    Attributes
    ----------
    type : str
        Algo type.
    """
    type: str = Field(..., alias='type')
