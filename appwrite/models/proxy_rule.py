from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.proxy_rule_deployment_resource_type import ProxyRuleDeploymentResourceType
from ..enums.proxy_rule_status import ProxyRuleStatus
from ..enums.proxy_rule_protocol import ProxyRuleProtocol


class ProxyRule(AppwriteModel):
    """
    Rule

    Attributes
    ----------
    id : str
        Rule ID.
    createdat : str
        Rule creation date in ISO 8601 format.
    updatedat : str
        Rule update date in ISO 8601 format.
    domain : str
        Domain name.
    type : str
        Action definition for the rule. Possible values are &quot;api&quot;, &quot;deployment&quot;, or &quot;redirect&quot;
    trigger : str
        Defines how the rule was created. Possible values are &quot;manual&quot; or &quot;deployment&quot;
    redirecturl : str
        URL to redirect to. Used if type is &quot;redirect&quot;
    redirectstatuscode : float
        Status code to apply during redirect. Used if type is &quot;redirect&quot;
    deploymentid : str
        ID of deployment. Used if type is &quot;deployment&quot;
    deploymentresourcetype : Optional[ProxyRuleDeploymentResourceType]
        Type of deployment resource: function, site, or dedicatedDatabase.
    deploymentresourceid : str
        ID of deployment&#039;s resource (site or function ID). Used if type is &quot;deployment&quot;
    deploymentvcsproviderbranch : str
        Name of Git branch that updates rule. Used if type is &quot;deployment&quot;
    status : ProxyRuleStatus
        Domain verification status. Possible values are &quot;unverified&quot;, &quot;verifying&quot;, &quot;verified&quot;
    logs : str
        Logs from rule verification or certificate generation. Certificate generation logs are prioritized if both are available.
    renewat : str
        Certificate auto-renewal date in ISO 8601 format.
    protocol : ProxyRuleProtocol
        Ingress protocol for the rule.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    domain: str = Field(..., alias='domain')
    type: str = Field(..., alias='type')
    trigger: str = Field(..., alias='trigger')
    redirecturl: str = Field(..., alias='redirectUrl')
    redirectstatuscode: float = Field(..., alias='redirectStatusCode')
    deploymentid: str = Field(..., alias='deploymentId')
    deploymentresourcetype: Optional[ProxyRuleDeploymentResourceType] = Field(
        default=None,
        alias='deploymentResourceType',
    )
    deploymentresourceid: str = Field(..., alias='deploymentResourceId')
    deploymentvcsproviderbranch: str = Field(..., alias='deploymentVcsProviderBranch')
    status: ProxyRuleStatus = Field(..., alias='status')
    logs: str = Field(..., alias='logs')
    renewat: str = Field(..., alias='renewAt')
    protocol: ProxyRuleProtocol = Field(..., alias='protocol')

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
        if 'domain' not in data:
            data['domain'] = ''
        if 'type' not in data:
            data['type'] = ''
        if 'trigger' not in data:
            data['trigger'] = ''
        if 'redirectUrl' not in data and 'redirecturl' not in data:
            data['redirectUrl'] = ''
        if 'redirectStatusCode' not in data and 'redirectstatuscode' not in data:
            data['redirectStatusCode'] = 301
        if 'deploymentId' not in data and 'deploymentid' not in data:
            data['deploymentId'] = ''
        if 'deploymentResourceId' not in data and 'deploymentresourceid' not in data:
            data['deploymentResourceId'] = ''
        if 'deploymentVcsProviderBranch' not in data and 'deploymentvcsproviderbranch' not in data:
            data['deploymentVcsProviderBranch'] = ''
        if 'status' not in data:
            data['status'] = 'unverified'
        if 'logs' not in data:
            data['logs'] = ''
        if 'protocol' not in data:
            data['protocol'] = 'http'
        return data
