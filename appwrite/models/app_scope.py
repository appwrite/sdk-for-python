from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AppScope(AppwriteModel):
    """
    AppScope

    Attributes
    ----------
    value : str
        Scope value as requested by apps.
    description : str
        Human-readable description of what the scope grants.
    type : str
        What the scope grants access to. One of `account`, `project`, or `organization`. Only `project` and `organization` scopes are installable.
    category : str
        Scope category, used to group scopes on consent and installation screens.
    deprecated : bool
        Whether the scope is deprecated. Deprecated scopes can still be requested but should not be offered for new grants.
    """
    value: str = Field(..., alias='value')
    description: str = Field(..., alias='description')
    type: str = Field(..., alias='type')
    category: str = Field(..., alias='category')
    deprecated: bool = Field(..., alias='deprecated')
