from ..service import Service
from typing import List
from ..exception import AppwriteException

class Graphql(Service):

    def __init__(self, client):
        super(Graphql, self).__init__(client)

    def query(self, query: dict):
        """GraphQL endpoint"""

        api_path = '/graphql'
        api_params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        api_params['query'] = query

        return self.client.call('post', api_path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, api_params)

    def mutation(self, query: dict):
        """GraphQL endpoint"""

        api_path = '/graphql/mutation'
        api_params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        api_params['query'] = query

        return self.client.call('post', api_path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, api_params)
