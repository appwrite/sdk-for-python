from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.health_status import HealthStatus;
from ..models.health_antivirus import HealthAntivirus;
from ..models.health_status_list import HealthStatusList;
from ..models.health_certificate import HealthCertificate;
from ..models.health_queue import HealthQueue;
from ..enums.name import Name;
from ..models.health_time import HealthTime;

class Health(Service):

    def __init__(self, client) -> None:
        super(Health, self).__init__(client)

    def get(
        self
    ) -> HealthStatus:
        """
        Check the Appwrite HTTP server is up and responsive.

        Returns
        -------
        HealthStatus
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthStatus)


    def get_antivirus(
        self
    ) -> HealthAntivirus:
        """
        Check the Appwrite Antivirus server is up and connection is successful.

        Returns
        -------
        HealthAntivirus
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/anti-virus'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthAntivirus)


    def get_cache(
        self
    ) -> HealthStatusList:
        """
        Check the Appwrite in-memory cache servers are up and connection is successful.

        Returns
        -------
        HealthStatusList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/cache'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthStatusList)


    def get_certificate(
        self,
        domain: Optional[str] = None
    ) -> HealthCertificate:
        """
        Get the SSL certificate for a domain

        Parameters
        ----------
        domain : Optional[str]
            string
        
        Returns
        -------
        HealthCertificate
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/certificate'
        api_params = {}

        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthCertificate)


    def get_console_pausing(
        self,
        threshold: Optional[float] = None,
        inactivity_days: Optional[float] = None
    ) -> HealthStatus:
        """
        Get console pausing health status. Monitors projects approaching the pause threshold to detect potential issues with console access tracking.
        

        Parameters
        ----------
        threshold : Optional[float]
            Percentage threshold of projects approaching pause. When hit (equal or higher), endpoint returns server error. Default value is 10.
        inactivity_days : Optional[float]
            Number of days of inactivity before a project is paused. Should match the plan's projectInactivityDays setting. Default value is 7.
        
        Returns
        -------
        HealthStatus
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/console-pausing'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)
        if inactivity_days is not None:
            api_params['inactivityDays'] = self._normalize_value(inactivity_days)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthStatus)


    def get_db(
        self
    ) -> HealthStatusList:
        """
        Check the Appwrite database servers are up and connection is successful.

        Returns
        -------
        HealthStatusList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/db'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthStatusList)


    def get_pub_sub(
        self
    ) -> HealthStatusList:
        """
        Check the Appwrite pub-sub servers are up and connection is successful.

        Returns
        -------
        HealthStatusList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/pubsub'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthStatusList)


    def get_queue_audits(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of audit logs that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/audits'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_billing_project_aggregation(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get billing project aggregation queue.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/billing-project-aggregation'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_billing_team_aggregation(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get billing team aggregation queue.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/billing-team-aggregation'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_builds(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of builds that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/builds'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_priority_builds(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the priority builds queue size.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 500.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/builds-priority'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_certificates(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/certificates'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_databases(
        self,
        name: Optional[str] = None,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of database changes that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        name : Optional[str]
            Queue name for which to check the queue size
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/databases'
        api_params = {}

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_deletes(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of background destructive changes that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/deletes'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_failed_jobs(
        self,
        name: Name,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Returns the amount of failed jobs in a given queue.
        

        Parameters
        ----------
        name : Name
            The name of the queue
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/failed/{name}'
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_functions(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of function executions that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/functions'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_logs(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/logs'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_mails(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of mails that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/mails'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_messaging(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of messages that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/messaging'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_migrations(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of migrations that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/migrations'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_region_manager(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get region manager queue.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 100.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/region-manager'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_stats_resources(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of metrics that are waiting to be processed in the Appwrite stats resources queue.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/stats-resources'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_usage(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of metrics that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/stats-usage'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_threats(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get threats queue.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 100.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/threats'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_queue_webhooks(
        self,
        threshold: Optional[float] = None
    ) -> HealthQueue:
        """
        Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

        Parameters
        ----------
        threshold : Optional[float]
            Queue size threshold. When hit (equal or higher), endpoint returns server error. Default value is 5000.
        
        Returns
        -------
        HealthQueue
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/queue/webhooks'
        api_params = {}

        if threshold is not None:
            api_params['threshold'] = self._normalize_value(threshold)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthQueue)


    def get_storage(
        self
    ) -> HealthStatus:
        """
        Check the Appwrite storage device is up and connection is successful.

        Returns
        -------
        HealthStatus
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/storage'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthStatus)


    def get_storage_local(
        self
    ) -> HealthStatus:
        """
        Check the Appwrite local storage device is up and connection is successful.

        Returns
        -------
        HealthStatus
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/storage/local'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthStatus)


    def get_time(
        self
    ) -> HealthTime:
        """
        Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

        Returns
        -------
        HealthTime
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/health/time'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=HealthTime)

