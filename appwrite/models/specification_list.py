from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .specification import Specification

class SpecificationList(AppwriteModel):
    """
    Specifications List

    Attributes
    ----------
    total : float
        Total number of specifications that matched your query.
    specifications : List[Specification]
        List of specifications.
    """
    total: float = Field(..., alias='total')
    specifications: List[Specification] = Field(..., alias='specifications')
