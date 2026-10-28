from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.waf_rule_list import WafRuleList
from ..models.waf_rule_bypass import WafRuleBypass
from ..models.waf_rule_challenge import WafRuleChallenge
from ..models.waf_rule_deny import WafRuleDeny
from ..models.waf_rule_rate_limit import WafRuleRateLimit
from ..models.waf_rule_redirect import WafRuleRedirect


class Waf(Service):

    def __init__(self, client) -> None:
        super(Waf, self).__init__(client)

    def list_rules(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None,
    ) -> WafRuleList:
        """
        List WAF rules for the current project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long.
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        WafRuleList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleList)

    def create_bypass_rule(
        self,
        rule_id: str,
        resource_type: str,
        name: str,
        resource_id: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleBypass:
        """
        Create a bypass WAF rule. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID. Choose a custom ID or pass `ID.unique()` to generate a unique one.
        resource_type : str
            Resource type the rule applies to.
        name : str
            Rule name.
        resource_id : Optional[str]
            Resource identifier. Leave empty for the API resource type.
        description : Optional[str]
            Optional description for the rule.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to create the rule in a disabled state.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleBypass
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/bypass'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')
        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_params['ruleId'] = self._normalize_value(rule_id)
        api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleBypass)

    def update_bypass_rule(
        self,
        rule_id: str,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleBypass:
        """
        Update a bypass WAF rule. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        resource_type : Optional[str]
            Resource type the rule applies to.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        name : Optional[str]
            Rule name.
        description : Optional[str]
            Optional description for the rule.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to disable the rule.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleBypass
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/bypass/{ruleId}'
        api_params = {}
        if rule_id is None or rule_id == '':
            raise AppwriteException('Missing required parameter: "rule_id"')
        api_path = api_path.replace('{ruleId}', self._encode_path(rule_id))
        if resource_type is not None:
            api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleBypass)

    def create_challenge_rule(
        self,
        rule_id: str,
        resource_type: str,
        name: str,
        resource_id: Optional[str] = None,
        description: Optional[str] = None,
        challenge_type: Optional[str] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
        difficulty: Optional[float] = None,
        ttl: Optional[float] = None,
    ) -> WafRuleChallenge:
        """
        Create a challenge WAF rule. Use `difficulty` (1 easiest to 5 hardest) to tune the client-side proof-of-work cost, and `ttl` to control how long, in seconds, a visitor stays cleared after passing the challenge before being challenged again. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID. Choose a custom ID or pass `ID.unique()` to generate a unique one.
        resource_type : str
            Resource type the rule applies to.
        name : str
            Rule name.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        description : Optional[str]
            Optional description for the rule.
        challenge_type : Optional[str]
            Challenge type enforced by the rule.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to create the rule in a disabled state.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        difficulty : Optional[float]
            Challenge difficulty from 1 (easiest) to 5 (hardest). Higher values demand more client-side proof-of-work.
        ttl : Optional[float]
            How long, in seconds, a visitor stays cleared after passing the challenge before being challenged again.
        Returns
        -------
        WafRuleChallenge
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/challenge'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')
        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_params['ruleId'] = self._normalize_value(rule_id)
        api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if challenge_type is not None:
            api_params['challengeType'] = self._normalize_value(challenge_type)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)
        if difficulty is not None:
            api_params['difficulty'] = self._normalize_value(difficulty)
        if ttl is not None:
            api_params['ttl'] = self._normalize_value(ttl)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleChallenge)

    def update_challenge_rule(
        self,
        rule_id: str,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        challenge_type: Optional[str] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
        difficulty: Optional[float] = None,
        ttl: Optional[float] = None,
    ) -> WafRuleChallenge:
        """
        Update a challenge WAF rule. Use `difficulty` (1 easiest to 5 hardest) to tune the client-side proof-of-work cost, and `ttl` to control how long, in seconds, a visitor stays cleared after passing the challenge before being challenged again. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        resource_type : Optional[str]
            Resource type the rule applies to.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        name : Optional[str]
            Rule name.
        description : Optional[str]
            Optional description for the rule.
        challenge_type : Optional[str]
            Challenge type enforced by the rule.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to disable the rule.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        difficulty : Optional[float]
            Challenge difficulty from 1 (easiest) to 5 (hardest). Higher values demand more client-side proof-of-work.
        ttl : Optional[float]
            How long, in seconds, a visitor stays cleared after passing the challenge before being challenged again.
        Returns
        -------
        WafRuleChallenge
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/challenge/{ruleId}'
        api_params = {}
        if rule_id is None or rule_id == '':
            raise AppwriteException('Missing required parameter: "rule_id"')
        api_path = api_path.replace('{ruleId}', self._encode_path(rule_id))
        if resource_type is not None:
            api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if challenge_type is not None:
            api_params['challengeType'] = self._normalize_value(challenge_type)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)
        if difficulty is not None:
            api_params['difficulty'] = self._normalize_value(difficulty)
        if ttl is not None:
            api_params['ttl'] = self._normalize_value(ttl)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleChallenge)

    def create_deny_rule(
        self,
        rule_id: str,
        resource_type: str,
        name: str,
        resource_id: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleDeny:
        """
        Create a deny WAF rule. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon. `sessionAge` and `mfaAge` hold the seconds since the request's session was created and since its last MFA challenge. Both are null for requests without a session, such as guests and API keys, while a request authenticated with the `x-appwrite-jwt` header carries the age of the session its token is bound to; on `functions` rules the session comes from the `x-appwrite-user-jwt` header, and `mfaAge` is null when the session never completed MFA. A deny matching on `mfaAge` returns `user_challenge_required` and one matching on `sessionAge` returns `user_reauthentication_required`, both with status 401, so the user can sign in again and retry. To also deny requests without a session, combine `isNull` and `greaterThan` in an `or` condition.

        Parameters
        ----------
        rule_id : str
            Rule ID. Choose a custom ID or pass `ID.unique()` to generate a unique one.
        resource_type : str
            Resource type the rule applies to.
        name : str
            Rule name.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        description : Optional[str]
            Optional description for the rule.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to create the rule in a disabled state.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleDeny
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/deny'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')
        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        api_params['ruleId'] = self._normalize_value(rule_id)
        api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleDeny)

    def update_deny_rule(
        self,
        rule_id: str,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleDeny:
        """
        Update a deny WAF rule. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon. `sessionAge` and `mfaAge` hold the seconds since the request's session was created and since its last MFA challenge. Both are null for requests without a session, such as guests and API keys, while a request authenticated with the `x-appwrite-jwt` header carries the age of the session its token is bound to; on `functions` rules the session comes from the `x-appwrite-user-jwt` header, and `mfaAge` is null when the session never completed MFA. A deny matching on `mfaAge` returns `user_challenge_required` and one matching on `sessionAge` returns `user_reauthentication_required`, both with status 401, so the user can sign in again and retry. To also deny requests without a session, combine `isNull` and `greaterThan` in an `or` condition.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        resource_type : Optional[str]
            Resource type the rule applies to.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        name : Optional[str]
            Rule name.
        description : Optional[str]
            Optional description for the rule.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to disable the rule.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleDeny
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/deny/{ruleId}'
        api_params = {}
        if rule_id is None or rule_id == '':
            raise AppwriteException('Missing required parameter: "rule_id"')
        api_path = api_path.replace('{ruleId}', self._encode_path(rule_id))
        if resource_type is not None:
            api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleDeny)

    def create_rate_limit_rule(
        self,
        rule_id: str,
        resource_type: str,
        name: str,
        limit: float,
        interval: float,
        resource_id: Optional[str] = None,
        description: Optional[str] = None,
        key: Optional[str] = None,
        strategy: Optional[str] = None,
        max_bucket_size: Optional[float] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleRateLimit:
        """
        Create a rate limit WAF rule. Use `key` to choose the counter: `ip` limits per client IP, while `userId` limits per authenticated user (requests without an authenticated user skip `userId` rules). Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID. Choose a custom ID or pass `ID.unique()` to generate a unique one.
        resource_type : str
            Resource type the rule applies to.
        name : str
            Rule name.
        limit : float
            Maximum number of matching requests allowed in the configured interval.
        interval : float
            Interval in seconds used for rate limiting.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        description : Optional[str]
            Optional description for the rule.
        key : Optional[str]
            Rate limit key. Use `ip` to limit per client IP or `userId` to limit per authenticated user. Requests without an authenticated user skip `userId` rules.
        strategy : Optional[str]
            Rate limit strategy. `fixedWindow` counts requests in discrete intervals, `slidingWindow` weights the previous interval for smoother limiting, and `tokenBucket` refills allowance continuously to permit short bursts.
        max_bucket_size : Optional[float]
            Maximum number of tokens the bucket can hold for the `tokenBucket` strategy, controlling how large a burst is allowed. The sustained refill rate is `limit / interval`. Defaults to `limit` when omitted. Ignored by other strategies.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to create the rule in a disabled state.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleRateLimit
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/rate-limit'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')
        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if limit is None:
            raise AppwriteException('Missing required parameter: "limit"')
        if interval is None:
            raise AppwriteException('Missing required parameter: "interval"')
        api_params['ruleId'] = self._normalize_value(rule_id)
        api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        api_params['limit'] = self._normalize_value(limit)
        api_params['interval'] = self._normalize_value(interval)
        if key is not None:
            api_params['key'] = self._normalize_value(key)
        if strategy is not None:
            api_params['strategy'] = self._normalize_value(strategy)
        if max_bucket_size is not None:
            api_params['maxBucketSize'] = self._normalize_value(max_bucket_size)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleRateLimit)

    def update_rate_limit_rule(
        self,
        rule_id: str,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        limit: Optional[float] = None,
        interval: Optional[float] = None,
        key: Optional[str] = None,
        max_bucket_size: Optional[float] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleRateLimit:
        """
        Update a rate limit WAF rule. Use `key` to choose the counter: `ip` limits per client IP, while `userId` limits per authenticated user (requests without an authenticated user skip `userId` rules). Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        resource_type : Optional[str]
            Resource type the rule applies to.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        name : Optional[str]
            Rule name.
        description : Optional[str]
            Optional description for the rule.
        limit : Optional[float]
            Maximum number of matching requests allowed in the configured interval.
        interval : Optional[float]
            Interval in seconds used for rate limiting.
        key : Optional[str]
            Rate limit key. Use `ip` to limit per client IP or `userId` to limit per authenticated user. Requests without an authenticated user skip `userId` rules.
        max_bucket_size : Optional[float]
            Maximum number of tokens the bucket can hold for the `tokenBucket` strategy, controlling how large a burst is allowed. The sustained refill rate is `limit / interval`. Ignored by other strategies. The strategy itself cannot be changed after creation.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to disable the rule.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleRateLimit
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/rate-limit/{ruleId}'
        api_params = {}
        if rule_id is None or rule_id == '':
            raise AppwriteException('Missing required parameter: "rule_id"')
        api_path = api_path.replace('{ruleId}', self._encode_path(rule_id))
        if resource_type is not None:
            api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if interval is not None:
            api_params['interval'] = self._normalize_value(interval)
        if key is not None:
            api_params['key'] = self._normalize_value(key)
        if max_bucket_size is not None:
            api_params['maxBucketSize'] = self._normalize_value(max_bucket_size)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleRateLimit)

    def create_redirect_rule(
        self,
        rule_id: str,
        resource_type: str,
        name: str,
        location: str,
        status_code: float,
        resource_id: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleRedirect:
        """
        Create a redirect WAF rule. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID. Choose a custom ID or pass `ID.unique()` to generate a unique one.
        resource_type : str
            Resource type the rule applies to.
        name : str
            Rule name.
        location : str
            Location used for redirect responses.
        status_code : float
            Integer status code used for redirect responses.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        description : Optional[str]
            Optional description for the rule.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to create the rule in a disabled state.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleRedirect
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/redirect'
        api_params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')
        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if location is None:
            raise AppwriteException('Missing required parameter: "location"')
        if status_code is None:
            raise AppwriteException('Missing required parameter: "status_code"')
        api_params['ruleId'] = self._normalize_value(rule_id)
        api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        api_params['location'] = self._normalize_value(location)
        api_params['statusCode'] = self._normalize_value(status_code)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleRedirect)

    def update_redirect_rule(
        self,
        rule_id: str,
        resource_type: Optional[str] = None,
        resource_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        location: Optional[str] = None,
        status_code: Optional[float] = None,
        priority: Optional[float] = None,
        enabled: Optional[bool] = None,
        conditions: Optional[List[str]] = None,
    ) -> WafRuleRedirect:
        """
        Update a redirect WAF rule. Conditions can match request attributes including `ip` (plain IPs or CIDR blocks like `10.0.0.0/8`), `method`, `path`, `host`, `country`, `continent`, `headers.<name>`, `query.<key>`, `queryKeys`, `accept`, `acceptLanguage`, `cookie`, `userAgent`, `os`, `osVersion`, `browser`, and `browserVersion`. Conditions on `city` and `state` require the premium Geo DB addon.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        resource_type : Optional[str]
            Resource type the rule applies to.
        resource_id : Optional[str]
            Resource identifier. Required for functions and sites.
        name : Optional[str]
            Rule name.
        description : Optional[str]
            Optional description for the rule.
        location : Optional[str]
            Location used for redirect responses.
        status_code : Optional[float]
            Integer status code used for redirect responses.
        priority : Optional[float]
            Evaluation priority. Lower numbers run earlier.
        enabled : Optional[bool]
            Set to false to disable the rule.
        conditions : Optional[List[str]]
            Array of condition strings generated using the WAF Condition builder. Maximum of 100 conditions are allowed, each 4096 characters long.
        Returns
        -------
        WafRuleRedirect
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/redirect/{ruleId}'
        api_params = {}
        if rule_id is None or rule_id == '':
            raise AppwriteException('Missing required parameter: "rule_id"')
        api_path = api_path.replace('{ruleId}', self._encode_path(rule_id))
        if resource_type is not None:
            api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if description is not None:
            api_params['description'] = self._normalize_value(description)
        if location is not None:
            api_params['location'] = self._normalize_value(location)
        if status_code is not None:
            api_params['statusCode'] = self._normalize_value(status_code)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if conditions is not None:
            api_params['conditions'] = self._normalize_value(conditions)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=WafRuleRedirect)

    def get_rule(
        self,
        rule_id: str,
    ) -> Union[
        WafRuleBypass,
        WafRuleDeny,
        WafRuleChallenge,
        WafRuleRateLimit,
        WafRuleRedirect,
    ]:
        """
        Get a WAF rule by its ID.

        Parameters
        ----------
        rule_id : str
            Rule ID.
        Returns
        -------
        Union[WafRuleBypass, WafRuleDeny, WafRuleChallenge, WafRuleRateLimit, WafRuleRedirect]
            API response as one of the typed response models

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/waf/rules/{ruleId}'
        api_params = {}
        if rule_id is None or rule_id == '':
            raise AppwriteException('Missing required parameter: "rule_id"')
        api_path = api_path.replace('{ruleId}', self._encode_path(rule_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )
        if not isinstance(response, dict):
            raise AppwriteException('Expected object response when hydrating a response model')

        if response.get('action') == 'bypass':
            return self._parse_response(response, model=WafRuleBypass)

        if response.get('action') == 'deny':
            return self._parse_response(response, model=WafRuleDeny)

        if response.get('action') == 'challenge':
            return self._parse_response(response, model=WafRuleChallenge)

        if response.get('action') == 'rateLimit':
            return self._parse_response(response, model=WafRuleRateLimit)

        if response.get('action') == 'redirect':
            return self._parse_response(response, model=WafRuleRedirect)

        raise AppwriteException('Unable to match response to any known model')

    def delete_rule(
        self,
        rule_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a WAF rule.

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

        api_path = '/waf/rules/{ruleId}'
        api_params = {}
        if rule_id is None or rule_id == '':
            raise AppwriteException('Missing required parameter: "rule_id"')
        api_path = api_path.replace('{ruleId}', self._encode_path(rule_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response
