from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'title' not in data:
            data['title'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'tag' not in data:
            data['tag'] = ''
        if 'icon' not in data:
            data['icon'] = ''
        if 'url' not in data:
            data['url'] = ''
        if 'active' not in data:
            data['active'] = True
        if 'external' not in data:
            data['external'] = True
        if 'billingPlanId' not in data and 'billingplanid' not in data:
            data['billingPlanId'] = ''
        return data
