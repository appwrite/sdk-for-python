from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .proxy_rule import ProxyRule

class ProxyRuleList(AppwriteModel):
    """
    Rule List

    Attributes
    ----------
    total : float
        Total number of rules that matched your query.
    rules : List[ProxyRule]
        List of rules.
    """
    total: float = Field(..., alias='total')
    rules: List[ProxyRule] = Field(..., alias='rules')
