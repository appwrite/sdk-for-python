from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Headers(AppwriteModel):
    """
    Headers

    Attributes
    ----------
    name : str
        Header name.
    value : str
        Header value.
    """
    name: str = Field(..., alias='name')
    value: str = Field(..., alias='value')
