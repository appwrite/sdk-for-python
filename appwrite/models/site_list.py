from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'sites' not in data:
            data['sites'] = []
        return data
