from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .resource_token import ResourceToken

class ResourceTokenList(AppwriteModel):
    """
    Resource Tokens List

    Attributes
    ----------
    total : float
        Total number of tokens that matched your query.
    tokens : List[ResourceToken]
        List of tokens.
    """
    total: float = Field(..., alias='total')
    tokens: List[ResourceToken] = Field(..., alias='tokens')
