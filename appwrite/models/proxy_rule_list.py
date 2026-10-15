from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'rules' not in data:
            data['rules'] = []
        return data
