from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .waf_rule_bypass import WafRuleBypass
from .waf_rule_deny import WafRuleDeny
from .waf_rule_challenge import WafRuleChallenge
from .waf_rule_rate_limit import WafRuleRateLimit
from .waf_rule_redirect import WafRuleRedirect


class WafRuleList(AppwriteModel):
    """
    WAF rule list

    Attributes
    ----------
    total : float
        Total number of rules that matched your query.
    rules : List[Union[WafRuleBypass, WafRuleDeny, WafRuleChallenge, WafRuleRateLimit, WafRuleRedirect]]
        List of rules.
    """

    total: float = Field(..., alias='total')
    rules: List[
        Union[
            WafRuleBypass,
            WafRuleDeny,
            WafRuleChallenge,
            WafRuleRateLimit,
            WafRuleRedirect,
        ]
    ] = Field(..., alias='rules')

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
