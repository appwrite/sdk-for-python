from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.proxy_rule_deployment_resource_type import ProxyRuleDeploymentResourceType
from ..enums.proxy_rule_status import ProxyRuleStatus

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
        Type of deployment. Possible values are &quot;function&quot;, &quot;site&quot;. Used if rule&#039;s type is &quot;deployment&quot;.
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
    deploymentresourcetype: Optional[ProxyRuleDeploymentResourceType] = Field(default=None, alias='deploymentResourceType')
    deploymentresourceid: str = Field(..., alias='deploymentResourceId')
    deploymentvcsproviderbranch: str = Field(..., alias='deploymentVcsProviderBranch')
    status: ProxyRuleStatus = Field(..., alias='status')
    logs: str = Field(..., alias='logs')
    renewat: str = Field(..., alias='renewAt')
