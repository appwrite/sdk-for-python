from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Program(AppwriteModel):
    """
    Program

    Attributes
    ----------
    id : str
        Program ID
    title : str
        Program title
    description : str
        Program description
    tag : str
        Program tag for highlighting on console
    icon : str
        Program icon for highlighting on console
    url : str
        URL for more information on this program
    active : bool
        Whether this program is active
    external : bool
        Whether this program is external
    billingplanid : str
        Billing plan ID that this is program is associated with.
    """
    id: str = Field(..., alias='$id')
    title: str = Field(..., alias='title')
    description: str = Field(..., alias='description')
    tag: str = Field(..., alias='tag')
    icon: str = Field(..., alias='icon')
    url: str = Field(..., alias='url')
    active: bool = Field(..., alias='active')
    external: bool = Field(..., alias='external')
    billingplanid: str = Field(..., alias='billingPlanId')
