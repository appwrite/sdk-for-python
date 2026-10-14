from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'domain' not in data:
            data['domain'] = ''
        if 'type' not in data:
            data['type'] = ''
        if 'reference' not in data:
            data['reference'] = ''
        if 'status' not in data:
            data['status'] = ''
        return data
