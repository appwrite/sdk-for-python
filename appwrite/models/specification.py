from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Specification(AppwriteModel):
    """
    Specification

    Attributes
    ----------
    memory : float
        Memory size in MB.
    cpus : float
        Number of CPUs.
    enabled : bool
        Is size enabled.
    slug : str
        Size slug.
    """
    memory: float = Field(..., alias='memory')
    cpus: float = Field(..., alias='cpus')
    enabled: bool = Field(..., alias='enabled')
    slug: str = Field(..., alias='slug')
