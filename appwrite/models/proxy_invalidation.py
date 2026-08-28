from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class ProxyInvalidation(AppwriteModel):
    """
    Invalidation

    Attributes
    ----------
    domain : str
        Domain name.
    type : str
        Invalidation type. Possible values are &quot;tag&quot;, &quot;path&quot;, or &quot;all&quot;.
    reference : str
        Invalidated reference. Depending on type this is a cache tag name, a URL path, or empty when type is all.
    status : str
        Invalidation status.
    """

    domain: str = Field(..., alias='domain')
    type: str = Field(..., alias='type')
    reference: str = Field(..., alias='reference')
    status: str = Field(..., alias='status')
