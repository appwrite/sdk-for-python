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
        """Get antivirus"""

        
        api_path = '/health/anti-virus'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_cache(self):
        """Get cache"""

        
        api_path = '/health/cache'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_certificate(self, domain = None):
        """Get the SSL certificate for a domain"""

        
        api_path = '/health/certificate'
        api_params = {}

        api_params['domain'] = domain

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
        """Get pubsub"""

        
        api_path = '/health/pubsub'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue(self):
        """Get queue"""

        
        api_path = '/health/queue'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_builds(self, threshold = None):
        """Get builds queue"""

        
        api_path = '/health/queue/builds'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_certificates(self, threshold = None):
        """Get certificates queue"""

        
        api_path = '/health/queue/certificates'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_databases(self, name = None, threshold = None):
        """Get databases queue"""

        
        api_path = '/health/queue/databases'
        api_params = {}

        api_params['name'] = name
        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_deletes(self, threshold = None):
        """Get deletes queue"""

        
        api_path = '/health/queue/deletes'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_failed_jobs(self, name, threshold = None):
        """Get number of failed queue jobs"""

        
        api_path = '/health/queue/failed/{name}'
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', name)

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_functions(self, threshold = None):
        """Get functions queue"""

        
        api_path = '/health/queue/functions'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_logs(self, threshold = None):
        """Get logs queue"""

        
        api_path = '/health/queue/logs'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_mails(self, threshold = None):
        """Get mails queue"""

        
        api_path = '/health/queue/mails'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_messaging(self, threshold = None):
        """Get messaging queue"""

        
        api_path = '/health/queue/messaging'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_migrations(self, threshold = None):
        """Get migrations queue"""

        
        api_path = '/health/queue/migrations'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_usage(self, threshold = None):
        """Get usage queue"""

        
        api_path = '/health/queue/usage'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_usage_dump(self, threshold = None):
        """Get usage dump queue"""

        
        api_path = '/health/queue/usage-dump'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_queue_webhooks(self, threshold = None):
        """Get webhooks queue"""

        
        api_path = '/health/queue/webhooks'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_storage(self):
        """Get storage"""

        
        api_path = '/health/storage'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_storage_local(self):
        """Get local storage"""

        
        api_path = '/health/storage/local'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_time(self):
        """Get time"""

        
        api_path = '/health/time'
        api_params = {}

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)
