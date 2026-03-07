from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Country(AppwriteModel):
    """
    Country

    Attributes
    ----------
    name : str
        Country name.
    code : str
        Country two-character ISO 3166-1 alpha code.
    """
    name: str = Field(..., alias='name')
    code: str = Field(..., alias='code')
