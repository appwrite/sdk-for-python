from ..service import Service
from ..exception import AppwriteException

class Graphql(Service):

    def __init__(self, client):
        super(Graphql, self).__init__(client)

    def query(self, query):
        """GraphQL Endpoint"""

        
        path = '/graphql'
        params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        params['query'] = query

        return self.client.call('post', path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, params)

    def mutation(self, query):
        """GraphQL Endpoint"""

        
        path = '/graphql/mutation'
        params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')


        params['query'] = query

        return self.client.call('post', path, {
            'x-sdk-graphql': 'true',
            'content-type': 'application/json',
        }, params)
