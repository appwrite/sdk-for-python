from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .site import Site

class SiteList(AppwriteModel):
    """
    Sites List

    Attributes
    ----------
    total : float
        Total number of sites that matched your query.
    sites : List[Site]
        List of sites.
    """
    total: float = Field(..., alias='total')
    sites: List[Site] = Field(..., alias='sites')
