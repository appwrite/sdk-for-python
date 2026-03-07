from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Provider(AppwriteModel):
    """
    Provider

    Attributes
    ----------
    id : str
        Provider ID.
    createdat : str
        Provider creation time in ISO 8601 format.
    updatedat : str
        Provider update date in ISO 8601 format.
    name : str
        The name for the provider instance.
    provider : str
        The name of the provider service.
    enabled : bool
        Is provider enabled?
    type : str
        Type of provider.
    credentials : Dict[str, Any]
        Provider credentials.
    options : Optional[Dict[str, Any]]
        Provider options.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    provider: str = Field(..., alias='provider')
    enabled: bool = Field(..., alias='enabled')
    type: str = Field(..., alias='type')
    credentials: Dict[str, Any] = Field(..., alias='credentials')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
