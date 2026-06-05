from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.proxy_rule_list import ProxyRuleList
from ..models.proxy_rule import ProxyRule
from ..enums.status_code import StatusCode
from ..enums.proxy_resource_type import ProxyResourceType

class Proxy(Service):

    def __init__(self, client) -> None:
        super(Proxy, self).__init__(client)

    def list_rules(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> ProxyRuleList:
        """
        Get a list of all the proxy rules. You can use the query params to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: domain, type, trigger, deploymentResourceType, deploymentResourceId, deploymentId, deploymentVcsProviderBranch
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ProxyRuleList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
        }, api_params)

        return self._parse_response(response, model=ProxyRuleList)


    def create_api_rule(
        self,
        domain: str
    ) -> ProxyRule:
        """
        Create a new proxy rule for serving Appwrite's API on custom domain.
        
        Rule ID is automatically generated as MD5 hash of a rule domain for performance purposes.

        Parameters
        ----------
        domain : str
            Domain name.
        
        Returns
        -------
        ProxyRule
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules/api'
        api_params = {}
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')


        api_params['domain'] = self._normalize_value(domain)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProxyRule)


    def create_function_rule(
        self,
        domain: str,
        function_id: str,
        branch: Optional[str] = None
    ) -> ProxyRule:
        """
        Create a new proxy rule for executing Appwrite Function on custom domain.
        
        Rule ID is automatically generated as MD5 hash of a rule domain for performance purposes.

        Parameters
        ----------
        domain : str
            Domain name.
        function_id : str
            ID of function to be executed.
        branch : Optional[str]
            Name of VCS branch to deploy changes automatically
        
        Returns
        -------
        ProxyRule
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules/function'
        api_params = {}
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')

        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')


        api_params['domain'] = self._normalize_value(domain)
        api_params['functionId'] = self._normalize_value(function_id)
        if branch is not None:
            api_params['branch'] = self._normalize_value(branch)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProxyRule)


    def create_redirect_rule(
        self,
        domain: str,
        url: str,
        status_code: StatusCode,
        resource_id: str,
        resource_type: ProxyResourceType
    ) -> ProxyRule:
        """
        Create a new proxy rule for to redirect from custom domain to another domain.
        
        Rule ID is automatically generated as MD5 hash of a rule domain for performance purposes.

        Parameters
        ----------
        domain : str
            Domain name.
        url : str
            Target URL of redirection
        status_code : StatusCode
            Status code of redirection
        resource_id : str
            ID of parent resource.
        resource_type : ProxyResourceType
            Type of parent resource.
        
        Returns
        -------
        ProxyRule
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules/redirect'
        api_params = {}
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')

        if url is None:
            raise AppwriteException('Missing required parameter: "url"')

        if status_code is None:
            raise AppwriteException('Missing required parameter: "status_code"')

        if resource_id is None:
            raise AppwriteException('Missing required parameter: "resource_id"')

        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')


        api_params['domain'] = self._normalize_value(domain)
        api_params['url'] = self._normalize_value(url)
        api_params['statusCode'] = self._normalize_value(status_code)
        api_params['resourceId'] = self._normalize_value(resource_id)
        api_params['resourceType'] = self._normalize_value(resource_type)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProxyRule)


    def create_site_rule(
        self,
        domain: str,
        site_id: str,
        branch: Optional[str] = None
    ) -> ProxyRule:
        """
        Create a new proxy rule for serving Appwrite Site on custom domain.
        
        Rule ID is automatically generated as MD5 hash of a rule domain for performance purposes.

        Parameters
        ----------
        domain : str
            Domain name.
        site_id : str
            ID of site to be executed.
        branch : Optional[str]
            Name of VCS branch to deploy changes automatically
        
        Returns
        -------
        ProxyRule
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules/site'
        api_params = {}
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')

        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')


        api_params['domain'] = self._normalize_value(domain)
        api_params['siteId'] = self._normalize_value(site_id)
        if branch is not None:
            api_params['branch'] = self._normalize_value(branch)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProxyRule)


    def get_rule(
        self,
        rule_id: str
    ) -> ProxyRule:
        """
        Get a proxy rule by its unique ID.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        
        Returns
        -------
        ProxyRule
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules/{ruleId}'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')

        api_path = api_path.replace('{ruleId}', str(self._normalize_value(rule_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
        }, api_params)

        return self._parse_response(response, model=ProxyRule)


    def delete_rule(
        self,
        rule_id: str
    ) -> Dict[str, Any]:
        """
        Delete a proxy rule by its unique ID.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules/{ruleId}'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')

        api_path = api_path.replace('{ruleId}', str(self._normalize_value(rule_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_rule_status(
        self,
        rule_id: str
    ) -> ProxyRule:
        """
        If not succeeded yet, retry verification process of a proxy rule domain. This endpoint triggers domain verification by checking DNS records. If verification is successful, a TLS certificate will be automatically provisioned for the domain asynchronously in the background.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        
        Returns
        -------
        ProxyRule
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/proxy/rules/{ruleId}/status'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')

        api_path = api_path.replace('{ruleId}', str(self._normalize_value(rule_id)))


        response = self.client.call('patch', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ProxyRule)

