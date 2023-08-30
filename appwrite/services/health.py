from ..service import Service
from ..exception import AppwriteException

class Health(Service):

    def __init__(self, client):
        super(Health, self).__init__(client)

    def get(self):
        """Get HTTP"""

        
        api_path = '/health'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_antivirus(self):
        """Get Antivirus"""

        
        api_path = '/health/anti-virus'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_cache(self):
        """Get Cache"""

        
        api_path = '/health/cache'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_db(self):
        """Get DB"""

        
        api_path = '/health/db'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_pub_sub(self):
        """Get PubSub"""

        
        api_path = '/health/pubsub'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_queue(self):
        """Get Queue"""

        
        api_path = '/health/queue'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_certificates(self):
        """Get Certificates Queue"""

        
        api_path = '/health/queue/certificates'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_functions(self):
        """Get Functions Queue"""

        
        api_path = '/health/queue/functions'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_logs(self):
        """Get Logs Queue"""

        
        api_path = '/health/queue/logs'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_webhooks(self):
        """Get Webhooks Queue"""

        
        api_path = '/health/queue/webhooks'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_storage_local(self):
        """Get Local Storage"""

        
        api_path = '/health/storage/local'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)

    def get_time(self):
        """Get Time"""

        
        api_path = '/health/time'
        params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, params)
