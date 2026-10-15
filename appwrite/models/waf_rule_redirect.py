from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.waf_rule_action import WafRuleAction


class WafRuleRedirect(AppwriteModel):
    """
    WafRuleRedirect

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
    location : str
        Target location for the redirect.
    statuscode : float
        HTTP status code used for the redirect.
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
    location: str = Field(..., alias='location')
    statuscode: float = Field(..., alias='statusCode')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = 'api'
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'priority' not in data:
            data['priority'] = 0
        if 'enabled' not in data:
            data['enabled'] = True
        if 'conditions' not in data:
            data['conditions'] = []
        if 'config' not in data:
            data['config'] = {}
        if 'location' not in data:
            data['location'] = '/'
        if 'statusCode' not in data and 'statuscode' not in data:
            data['statusCode'] = 302
        return data
