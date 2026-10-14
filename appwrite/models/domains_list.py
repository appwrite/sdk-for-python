from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .domain import Domain


class DomainsList(AppwriteModel):
    """
    Domains list

    Attributes
    ----------
    total : float
        Total number of domains that matched your query.
    domains : List[Domain]
        List of domains.
    """

    total: float = Field(..., alias='total')
    domains: List[Domain] = Field(..., alias='domains')
