from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .email_template import EmailTemplate


class EmailTemplateList(AppwriteModel):
    """
    Email Templates List

    Attributes
    ----------
    total : float
        Total number of templates that matched your query.
    templates : List[EmailTemplate]
        List of templates.
    """

    total: float = Field(..., alias='total')
    templates: List[EmailTemplate] = Field(..., alias='templates')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'templates' not in data:
            data['templates'] = []
        return data
