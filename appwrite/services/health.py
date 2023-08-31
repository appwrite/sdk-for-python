from ..service import Service
from ..exception import AppwriteException

class Health(Service):

    def __init__(self, client):
        super(Health, self).__init__(client)

    def get(self):
        """Get HTTP"""

        
        api_path = '/health'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_antivirus(self):
        """Get Antivirus"""

        
        api_path = '/health/anti-virus'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_cache(self):
        """Get Cache"""

        
        api_path = '/health/cache'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_db(self):
        """Get DB"""

        
        api_path = '/health/db'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_pub_sub(self):
        """Get PubSub"""

        
        api_path = '/health/pubsub'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue(self):
        """Get Queue"""

        
        api_path = '/health/queue'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_certificates(self):
        """Get Certificates Queue"""

        
        api_path = '/health/queue/certificates'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_functions(self):
        """Get Functions Queue"""

        
        api_path = '/health/queue/functions'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_logs(self):
        """Get Logs Queue"""

        
        api_path = '/health/queue/logs'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_webhooks(self):
        """Get Webhooks Queue"""

        
        api_path = '/health/queue/webhooks'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_storage_local(self):
        """Get Local Storage"""

        
        api_path = '/health/storage/local'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_time(self):
        """Get Time"""

        
        api_path = '/health/time'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)
