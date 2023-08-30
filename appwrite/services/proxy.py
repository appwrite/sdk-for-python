from ..service import Service
from ..exception import AppwriteException

class Proxy(Service):

    def __init__(self, client):
        super(Proxy, self).__init__(client)

    def list_rules(self, queries = None, search = None):
        """List Rules"""

        
        api_path = '/proxy/rules'
        params = {}

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def create_rule(self, domain, resource_type, resource_id = None):
        """Create Rule"""

        
        api_path = '/proxy/rules'
        params = {}
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')

        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')


        params['domain'] = domain
        params['resourceType'] = resource_type
        params['resourceId'] = resource_id

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_rule(self, rule_id):
        """Get Rule"""

        
        api_path = '/proxy/rules/{ruleId}'
        params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')

        path = path.replace('{ruleId}', rule_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def delete_rule(self, rule_id):
        """Delete Rule"""

        
        api_path = '/proxy/rules/{ruleId}'
        params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')

        path = path.replace('{ruleId}', rule_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, params)

    def update_rule_verification(self, rule_id):
        """Update Rule Verification Status"""

        
        api_path = '/proxy/rules/{ruleId}/verification'
        params = {}
        if rule_id is None:
            raise AppwriteException('Missing required parameter: "rule_id"')

        path = path.replace('{ruleId}', rule_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, params)
