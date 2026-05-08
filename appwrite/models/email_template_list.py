from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
