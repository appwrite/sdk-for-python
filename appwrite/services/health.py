from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException
from ..enums.name import Name;

class Health(Service):

    def __init__(self, client) -> None:
        super(Health, self).__init__(client)

    def get(self) -> Dict[str, Any]:
        """
        Check the Appwrite HTTP server is up and responsive.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_antivirus(self) -> Dict[str, Any]:
        """
        Check the Appwrite Antivirus server is up and connection is successful.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/anti-virus'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_cache(self) -> Dict[str, Any]:
        """
        Check the Appwrite in-memory cache servers are up and connection is successful.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/cache'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_certificate(self, domain: str = None) -> Dict[str, Any]:
        """
        Get the SSL certificate for a domain

        Parameters
        ----------
        domain : str
            string
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/certificate'
        api_params = {}

        api_params['domain'] = domain

        return self.client.call('get', api_path, {
        }, api_params)

    def get_db(self) -> Dict[str, Any]:
        """
        Check the Appwrite database servers are up and connection is successful.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/db'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_pub_sub(self) -> Dict[str, Any]:
        """
        Check the Appwrite pub-sub servers are up and connection is successful.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/pubsub'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_builds(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of builds that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/builds'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_certificates(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/certificates'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_databases(self, name: str = None, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of database changes that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        name : str
            Queue name for which to check the queue size
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/databases'
        api_params = {}

        api_params['name'] = name
        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_deletes(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of background destructive changes that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/deletes'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_failed_jobs(self, name: Name, threshold: float = None) -> Dict[str, Any]:
        """
        Returns the amount of failed jobs in a given queue.
        

        Parameters
        ----------
        name : Name
            The name of the queue
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/failed/{name}'
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', name)

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_functions(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of function executions that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/functions'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_logs(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/logs'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_mails(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of mails that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/mails'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_messaging(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of messages that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/messaging'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_migrations(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of migrations that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/migrations'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_stats_resources(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of metrics that are waiting to be processed in the Appwrite stats resources queue.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/stats-resources'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_usage(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of metrics that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/stats-usage'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_queue_webhooks(self, threshold: float = None) -> Dict[str, Any]:
        """
        Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : float
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/webhooks'
        api_params = {}

        api_params['threshold'] = threshold

        return self.client.call('get', api_path, {
        }, api_params)

    def get_storage(self) -> Dict[str, Any]:
        """
        Check the Appwrite storage device is up and connection is successful.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/storage'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_storage_local(self) -> Dict[str, Any]:
        """
        Check the Appwrite local storage device is up and connection is successful.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/storage/local'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get_time(self) -> Dict[str, Any]:
        """
        Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/time'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)
