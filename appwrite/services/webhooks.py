from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.webhook_list import WebhookList;
from ..models.webhook import Webhook;

class Webhooks(Service):

    def __init__(self, client) -> None:
        super(Webhooks, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> WebhookList:
        """
        Get a list of all webhooks belonging to the project. You can use the query params to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, url, authUsername, tls, events, enabled, logs, attempts
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        WebhookList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/webhooks'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=WebhookList)


    def create(
        self,
        webhook_id: str,
        url: str,
        name: str,
        events: List[str],
        enabled: Optional[bool] = None,
        tls: Optional[bool] = None,
        auth_username: Optional[str] = None,
        auth_password: Optional[str] = None,
        secret: Optional[str] = None
    ) -> Webhook:
        """
        Create a new webhook. Use this endpoint to configure a URL that will receive events from Appwrite when specific events occur.

        Parameters
        ----------
        webhook_id : str
            Webhook ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        url : str
            Webhook URL.
        name : str
            Webhook name. Max length: 128 chars.
        events : List[str]
            Events list. Maximum of 100 events are allowed.
        enabled : Optional[bool]
            Enable or disable a webhook.
        tls : Optional[bool]
            Certificate verification, false for disabled or true for enabled.
        auth_username : Optional[str]
            Webhook HTTP user. Max length: 256 chars.
        auth_password : Optional[str]
            Webhook HTTP password. Max length: 256 chars.
        secret : Optional[str]
            Webhook secret key. If not provided, a new key will be generated automatically. Key must be at least 8 characters long, and at max 256 characters.
        
        Returns
        -------
        Webhook
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/webhooks'
        api_params = {}
        if webhook_id is None:
            raise AppwriteException('Missing required parameter: "webhook_id"')

        if url is None:
            raise AppwriteException('Missing required parameter: "url"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if events is None:
            raise AppwriteException('Missing required parameter: "events"')


        api_params['webhookId'] = self._normalize_value(webhook_id)
        api_params['url'] = self._normalize_value(url)
        api_params['name'] = self._normalize_value(name)
        api_params['events'] = self._normalize_value(events)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if tls is not None:
            api_params['tls'] = self._normalize_value(tls)
        if auth_username is not None:
            api_params['authUsername'] = self._normalize_value(auth_username)
        if auth_password is not None:
            api_params['authPassword'] = self._normalize_value(auth_password)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Webhook)


    def get(
        self,
        webhook_id: str
    ) -> Webhook:
        """
        Get a webhook by its unique ID. This endpoint returns details about a specific webhook configured for a project. 

        Parameters
        ----------
        webhook_id : str
            Webhook ID.
        
        Returns
        -------
        Webhook
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/webhooks/{webhookId}'
        api_params = {}
        if webhook_id is None:
            raise AppwriteException('Missing required parameter: "webhook_id"')

        api_path = api_path.replace('{webhookId}', str(self._normalize_value(webhook_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Webhook)


    def update(
        self,
        webhook_id: str,
        name: str,
        url: str,
        events: List[str],
        enabled: Optional[bool] = None,
        tls: Optional[bool] = None,
        auth_username: Optional[str] = None,
        auth_password: Optional[str] = None
    ) -> Webhook:
        """
        Update a webhook by its unique ID. Use this endpoint to update the URL, events, or status of an existing webhook.

        Parameters
        ----------
        webhook_id : str
            Webhook ID.
        name : str
            Webhook name. Max length: 128 chars.
        url : str
            Webhook URL.
        events : List[str]
            Events list. Maximum of 100 events are allowed.
        enabled : Optional[bool]
            Enable or disable a webhook.
        tls : Optional[bool]
            Certificate verification, false for disabled or true for enabled.
        auth_username : Optional[str]
            Webhook HTTP user. Max length: 256 chars.
        auth_password : Optional[str]
            Webhook HTTP password. Max length: 256 chars.
        
        Returns
        -------
        Webhook
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/webhooks/{webhookId}'
        api_params = {}
        if webhook_id is None:
            raise AppwriteException('Missing required parameter: "webhook_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if url is None:
            raise AppwriteException('Missing required parameter: "url"')

        if events is None:
            raise AppwriteException('Missing required parameter: "events"')

        api_path = api_path.replace('{webhookId}', str(self._normalize_value(webhook_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['url'] = self._normalize_value(url)
        api_params['events'] = self._normalize_value(events)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if tls is not None:
            api_params['tls'] = self._normalize_value(tls)
        if auth_username is not None:
            api_params['authUsername'] = self._normalize_value(auth_username)
        if auth_password is not None:
            api_params['authPassword'] = self._normalize_value(auth_password)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Webhook)


    def delete(
        self,
        webhook_id: str
    ) -> Dict[str, Any]:
        """
        Delete a webhook by its unique ID. Once deleted, the webhook will no longer receive project events. 

        Parameters
        ----------
        webhook_id : str
            Webhook ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/webhooks/{webhookId}'
        api_params = {}
        if webhook_id is None:
            raise AppwriteException('Missing required parameter: "webhook_id"')

        api_path = api_path.replace('{webhookId}', str(self._normalize_value(webhook_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_secret(
        self,
        webhook_id: str,
        secret: Optional[str] = None
    ) -> Webhook:
        """
        Update the webhook signing key. This endpoint can be used to regenerate the signing key used to sign and validate payload deliveries for a specific webhook.

        Parameters
        ----------
        webhook_id : str
            Webhook ID.
        secret : Optional[str]
            Webhook secret key. If not provided, a new key will be generated automatically. Key must be at least 8 characters long, and at max 256 characters.
        
        Returns
        -------
        Webhook
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/webhooks/{webhookId}/secret'
        api_params = {}
        if webhook_id is None:
            raise AppwriteException('Missing required parameter: "webhook_id"')

        api_path = api_path.replace('{webhookId}', str(self._normalize_value(webhook_id)))

        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Webhook)

