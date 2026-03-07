from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Continent(AppwriteModel):
    """
    Continent

    Attributes
    ----------
    name : str
        Continent name.
    code : str
        Continent two letter code.
    """
    name: str = Field(..., alias='name')
    code: str = Field(..., alias='code')
