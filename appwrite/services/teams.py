from ..service import Service
from typing import List
from ..exception import AppwriteException

class Teams(Service):

    def __init__(self, client):
        super(Teams, self).__init__(client)

    def list(self, queries: List[str] = None, search: str = None):
        """List teams"""

        api_path = '/teams'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create(self, team_id: str, name: str, roles: List[str] = None):
        """Create team"""

        api_path = '/teams'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['teamId'] = team_id
        api_params['name'] = name
        api_params['roles'] = roles

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get(self, team_id: str):
        """Get team"""

        api_path = '/teams/{teamId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_name(self, team_id: str, name: str):
        """Update name"""

        api_path = '/teams/{teamId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['name'] = name

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, team_id: str):
        """Delete team"""

        api_path = '/teams/{teamId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_memberships(self, team_id: str, queries: List[str] = None, search: str = None):
        """List team memberships"""

        api_path = '/teams/{teamId}/memberships'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_membership(self, team_id: str, roles: List[str], email: str = None, user_id: str = None, phone: str = None, url: str = None, name: str = None):
        """Create team membership"""

        api_path = '/teams/{teamId}/memberships'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['email'] = email
        api_params['userId'] = user_id
        api_params['phone'] = phone
        api_params['roles'] = roles
        api_params['url'] = url
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_membership(self, team_id: str, membership_id: str):
        """Get team membership"""

        api_path = '/teams/{teamId}/memberships/{membershipId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_membership(self, team_id: str, membership_id: str, roles: List[str]):
        """Update membership"""

        api_path = '/teams/{teamId}/memberships/{membershipId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)

        api_params['roles'] = roles

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_membership(self, team_id: str, membership_id: str):
        """Delete team membership"""

        api_path = '/teams/{teamId}/memberships/{membershipId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_membership_status(self, team_id: str, membership_id: str, user_id: str, secret: str):
        """Update team membership status"""

        api_path = '/teams/{teamId}/memberships/{membershipId}/status'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)

        api_params['userId'] = user_id
        api_params['secret'] = secret

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_prefs(self, team_id: str):
        """Get team preferences"""

        api_path = '/teams/{teamId}/prefs'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_prefs(self, team_id: str, prefs: dict):
        """Update preferences"""

        api_path = '/teams/{teamId}/prefs'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['prefs'] = prefs

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)
