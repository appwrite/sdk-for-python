from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .provider import Provider

class ProviderList(AppwriteModel):
    """
    Provider list

    Attributes
    ----------
    total : float
        Total number of providers that matched your query.
    providers : List[Provider]
        List of providers.
    """
    total: float = Field(..., alias='total')
    providers: List[Provider] = Field(..., alias='providers')
