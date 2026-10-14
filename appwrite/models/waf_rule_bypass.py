from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.waf_rule_action import WafRuleAction


class WafRuleBypass(AppwriteModel):
    """
    WafRuleBypass

    Attributes
    ----------
    id : str
        Rule ID.
    createdat : str
        WAF rule creation time in ISO 8601 format.
    updatedat : str
        WAF rule last update time in ISO 8601 format.
    name : str
        Human friendly rule name.
    description : str
        Optional description for the rule.
    teamid : str
        Team ID.
    projectid : str
        Project ID.
    resourcetype : str
        Resource type the rule is scoped to.
    resourceid : str
        Resource identifier. Empty for API-wide rules.
    action : WafRuleAction
        Action performed when the rule matches.
    priority : float
        Evaluation priority. Lower values execute earlier.
    enabled : bool
        Whether the rule is active.
    conditions : List[Any]
        List of conditions evaluated for this rule.
    config : Dict[str, Any]
        Action specific configuration.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    description: str = Field(..., alias='description')
    teamid: str = Field(..., alias='teamId')
    projectid: str = Field(..., alias='projectId')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    action: WafRuleAction = Field(..., alias='action')
    priority: float = Field(..., alias='priority')
    enabled: bool = Field(..., alias='enabled')
    conditions: List[Any] = Field(..., alias='conditions')
    config: Dict[str, Any] = Field(..., alias='config')
