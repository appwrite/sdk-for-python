from ..service import Service
from ..exception import AppwriteException

class Health(Service):

    def __init__(self, client):
        super(Health, self).__init__(client)

    def get(self):
        """Get HTTP"""

        
        path = '/health'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_antivirus(self):
        """Get Antivirus"""

        
        path = '/health/anti-virus'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_cache(self):
        """Get Cache"""

        
        path = '/health/cache'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_db(self):
        """Get DB"""

        
        path = '/health/db'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_certificates(self):
        """Get Certificates Queue"""

        
        path = '/health/queue/certificates'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_functions(self):
        """Get Functions Queue"""

        
        path = '/health/queue/functions'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_logs(self):
        """Get Logs Queue"""

        
        path = '/health/queue/logs'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_queue_webhooks(self):
        """Get Webhooks Queue"""

        
        path = '/health/queue/webhooks'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_storage_local(self):
        """Get Local Storage"""

        
        path = '/health/storage/local'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)

    def get_time(self):
        """Get Time"""

        
        path = '/health/time'
        params = {}

        return self.client.call('get', path, {
            'content-type': 'application/json',
        }, params)
