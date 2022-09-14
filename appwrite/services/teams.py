from ..service import Service
from ..exception import AppwriteException

class Teams(Service):

    def __init__(self, client):
        super(Teams, self).__init__(client)

    def list(self, queries = None, search = None):
        """List Teams"""

        
        path = '/teams'
        params = {}

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create(self, team_id, name, roles = None):
        """Create Team"""

        
        path = '/teams'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        params['teamId'] = team_id
        params['name'] = name
        params['roles'] = roles

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get(self, team_id):
        """Get Team"""

        
        path = '/teams/{teamId}'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        path = path.replace('{teamId}', team_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update(self, team_id, name):
        """Update Team"""

        
        path = '/teams/{teamId}'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        path = path.replace('{teamId}', team_id)

        params['name'] = name

        return self.client.call('put', path, {
            'content-type': 'application/json',
        }, params)

    def delete(self, team_id):
        """Delete Team"""

        
        path = '/teams/{teamId}'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        path = path.replace('{teamId}', team_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def list_memberships(self, team_id, queries = None, search = None):
        """List Team Memberships"""

        
        path = '/teams/{teamId}/memberships'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        path = path.replace('{teamId}', team_id)

        params['queries'] = queries
        params['search'] = search

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def create_membership(self, team_id, email, roles, url, name = None):
        """Create Team Membership"""

        
        path = '/teams/{teamId}/memberships'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')

        if url is None:
            raise AppwriteException('Missing required parameter: "url"')

        path = path.replace('{teamId}', team_id)

        params['email'] = email
        params['roles'] = roles
        params['url'] = url
        params['name'] = name

        return self.client.call('post', path, {
            'content-type': 'application/json',
        }, params)

    def get_membership(self, team_id, membership_id):
        """Get Team Membership"""

        
        path = '/teams/{teamId}/memberships/{membershipId}'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        path = path.replace('{teamId}', team_id)
        path = path.replace('{membershipId}', membership_id)


        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def update_membership_roles(self, team_id, membership_id, roles):
        """Update Membership Roles"""

        
        path = '/teams/{teamId}/memberships/{membershipId}'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')

        path = path.replace('{teamId}', team_id)
        path = path.replace('{membershipId}', membership_id)

        params['roles'] = roles

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)

    def delete_membership(self, team_id, membership_id):
        """Delete Team Membership"""

        
        path = '/teams/{teamId}/memberships/{membershipId}'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        path = path.replace('{teamId}', team_id)
        path = path.replace('{membershipId}', membership_id)


        return self.client.call('delete', path, {
            'content-type': 'application/json',
        }, params)

    def update_membership_status(self, team_id, membership_id, user_id, secret):
        """Update Team Membership Status"""

        
        path = '/teams/{teamId}/memberships/{membershipId}/status'
        params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        path = path.replace('{teamId}', team_id)
        path = path.replace('{membershipId}', membership_id)

        params['userId'] = user_id
        params['secret'] = secret

        return self.client.call('patch', path, {
            'content-type': 'application/json',
        }, params)
