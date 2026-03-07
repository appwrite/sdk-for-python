from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .continent import Continent

class ContinentList(AppwriteModel):
    """
    Continents List

    Attributes
    ----------
    total : float
        Total number of continents that matched your query.
    continents : List[Continent]
        List of continents.
    """
    total: float = Field(..., alias='total')
    continents: List[Continent] = Field(..., alias='continents')
