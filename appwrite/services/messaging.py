from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.message_list import MessageList;
from ..models.message import Message;
from ..enums.message_priority import MessagePriority;
from ..models.log_list import LogList;
from ..models.target_list import TargetList;
from ..models.provider_list import ProviderList;
from ..models.provider import Provider;
from ..enums.smtp_encryption import SmtpEncryption;
from ..models.topic_list import TopicList;
from ..models.topic import Topic;
from ..models.subscriber_list import SubscriberList;
from ..models.subscriber import Subscriber;

class Messaging(Service):

    def __init__(self, client) -> None:
        super(Messaging, self).__init__(client)

    def list_messages(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None    ) -> MessageList:
        """
        Get a list of all messages from the current Appwrite project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: scheduledAt, deliveredAt, deliveredTotal, status, description, providerType
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        MessageList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MessageList)


    def create_email(
        self,
        message_id: str,
        subject: str,
        content: str,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None,
        targets: Optional[List[str]] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        attachments: Optional[List[str]] = None,
        draft: Optional[bool] = None,
        html: Optional[bool] = None,
        scheduled_at: Optional[str] = None    ) -> Message:
        """
        Create a new email message.

        Parameters
        ----------
        message_id : str
            Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        subject : str
            Email Subject.
        content : str
            Email Content.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        targets : Optional[List[str]]
            List of Targets IDs.
        cc : Optional[List[str]]
            Array of target IDs to be added as CC.
        bcc : Optional[List[str]]
            Array of target IDs to be added as BCC.
        attachments : Optional[List[str]]
            Array of compound ID strings of bucket IDs and file IDs to be attached to the email. They should be formatted as <BUCKET_ID>:<FILE_ID>.
        draft : Optional[bool]
            Is message a draft
        html : Optional[bool]
            Is content of type HTML
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        
        Returns
        -------
        Message            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/email'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        if subject is None:
            raise AppwriteException('Missing required parameter: "subject"')

        if content is None:
            raise AppwriteException('Missing required parameter: "content"')


        api_params['messageId'] = self._normalize_value(message_id)
        api_params['subject'] = self._normalize_value(subject)
        api_params['content'] = self._normalize_value(content)
        if topics is not None:
            api_params['topics'] = self._normalize_value(topics)
        if users is not None:
            api_params['users'] = self._normalize_value(users)
        if targets is not None:
            api_params['targets'] = self._normalize_value(targets)
        if cc is not None:
            api_params['cc'] = self._normalize_value(cc)
        if bcc is not None:
            api_params['bcc'] = self._normalize_value(bcc)
        if attachments is not None:
            api_params['attachments'] = self._normalize_value(attachments)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        if html is not None:
            api_params['html'] = self._normalize_value(html)
        api_params['scheduledAt'] = self._normalize_value(scheduled_at)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def update_email(
        self,
        message_id: str,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None,
        targets: Optional[List[str]] = None,
        subject: Optional[str] = None,
        content: Optional[str] = None,
        draft: Optional[bool] = None,
        html: Optional[bool] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        scheduled_at: Optional[str] = None,
        attachments: Optional[List[str]] = None    ) -> Message:
        """
        Update an email message by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        targets : Optional[List[str]]
            List of Targets IDs.
        subject : Optional[str]
            Email Subject.
        content : Optional[str]
            Email Content.
        draft : Optional[bool]
            Is message a draft
        html : Optional[bool]
            Is content of type HTML
        cc : Optional[List[str]]
            Array of target IDs to be added as CC.
        bcc : Optional[List[str]]
            Array of target IDs to be added as BCC.
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        attachments : Optional[List[str]]
            Array of compound ID strings of bucket IDs and file IDs to be attached to the email. They should be formatted as <BUCKET_ID>:<FILE_ID>.
        
        Returns
        -------
        Message            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/email/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        api_params['topics'] = self._normalize_value(topics)
        api_params['users'] = self._normalize_value(users)
        api_params['targets'] = self._normalize_value(targets)
        api_params['subject'] = self._normalize_value(subject)
        api_params['content'] = self._normalize_value(content)
        api_params['draft'] = self._normalize_value(draft)
        api_params['html'] = self._normalize_value(html)
        api_params['cc'] = self._normalize_value(cc)
        api_params['bcc'] = self._normalize_value(bcc)
        api_params['scheduledAt'] = self._normalize_value(scheduled_at)
        api_params['attachments'] = self._normalize_value(attachments)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def create_push(
        self,
        message_id: str,
        title: Optional[str] = None,
        body: Optional[str] = None,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None,
        targets: Optional[List[str]] = None,
        data: Optional[Dict[str, Any]] = None,
        action: Optional[str] = None,
        image: Optional[str] = None,
        icon: Optional[str] = None,
        sound: Optional[str] = None,
        color: Optional[str] = None,
        tag: Optional[str] = None,
        badge: Optional[float] = None,
        draft: Optional[bool] = None,
        scheduled_at: Optional[str] = None,
        content_available: Optional[bool] = None,
        critical: Optional[bool] = None,
        priority: Optional[MessagePriority] = None    ) -> Message:
        """
        Create a new push notification.

        Parameters
        ----------
        message_id : str
            Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        title : Optional[str]
            Title for push notification.
        body : Optional[str]
            Body for push notification.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        targets : Optional[List[str]]
            List of Targets IDs.
        data : Optional[Dict[str, Any]]
            Additional key-value pair data for push notification.
        action : Optional[str]
            Action for push notification.
        image : Optional[str]
            Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage. It should be formatted as <BUCKET_ID>:<FILE_ID>.
        icon : Optional[str]
            Icon for push notification. Available only for Android and Web Platform.
        sound : Optional[str]
            Sound for push notification. Available only for Android and iOS Platform.
        color : Optional[str]
            Color for push notification. Available only for Android Platform.
        tag : Optional[str]
            Tag for push notification. Available only for Android Platform.
        badge : Optional[float]
            Badge for push notification. Available only for iOS Platform.
        draft : Optional[bool]
            Is message a draft
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        content_available : Optional[bool]
            If set to true, the notification will be delivered in the background. Available only for iOS Platform.
        critical : Optional[bool]
            If set to true, the notification will be marked as critical. This requires the app to have the critical notification entitlement. Available only for iOS Platform.
        priority : Optional[MessagePriority]
            Set the notification priority. "normal" will consider device state and may not deliver notifications immediately. "high" will always attempt to immediately deliver the notification.
        
        Returns
        -------
        Message            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/push'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')


        api_params['messageId'] = self._normalize_value(message_id)
        if title is not None:
            api_params['title'] = self._normalize_value(title)
        if body is not None:
            api_params['body'] = self._normalize_value(body)
        if topics is not None:
            api_params['topics'] = self._normalize_value(topics)
        if users is not None:
            api_params['users'] = self._normalize_value(users)
        if targets is not None:
            api_params['targets'] = self._normalize_value(targets)
        api_params['data'] = self._normalize_value(data)
        if action is not None:
            api_params['action'] = self._normalize_value(action)
        if image is not None:
            api_params['image'] = self._normalize_value(image)
        if icon is not None:
            api_params['icon'] = self._normalize_value(icon)
        if sound is not None:
            api_params['sound'] = self._normalize_value(sound)
        if color is not None:
            api_params['color'] = self._normalize_value(color)
        if tag is not None:
            api_params['tag'] = self._normalize_value(tag)
        if badge is not None:
            api_params['badge'] = self._normalize_value(badge)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        api_params['scheduledAt'] = self._normalize_value(scheduled_at)
        if content_available is not None:
            api_params['contentAvailable'] = self._normalize_value(content_available)
        if critical is not None:
            api_params['critical'] = self._normalize_value(critical)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def update_push(
        self,
        message_id: str,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None,
        targets: Optional[List[str]] = None,
        title: Optional[str] = None,
        body: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        action: Optional[str] = None,
        image: Optional[str] = None,
        icon: Optional[str] = None,
        sound: Optional[str] = None,
        color: Optional[str] = None,
        tag: Optional[str] = None,
        badge: Optional[float] = None,
        draft: Optional[bool] = None,
        scheduled_at: Optional[str] = None,
        content_available: Optional[bool] = None,
        critical: Optional[bool] = None,
        priority: Optional[MessagePriority] = None    ) -> Message:
        """
        Update a push notification by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        targets : Optional[List[str]]
            List of Targets IDs.
        title : Optional[str]
            Title for push notification.
        body : Optional[str]
            Body for push notification.
        data : Optional[Dict[str, Any]]
            Additional Data for push notification.
        action : Optional[str]
            Action for push notification.
        image : Optional[str]
            Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage. It should be formatted as <BUCKET_ID>:<FILE_ID>.
        icon : Optional[str]
            Icon for push notification. Available only for Android and Web platforms.
        sound : Optional[str]
            Sound for push notification. Available only for Android and iOS platforms.
        color : Optional[str]
            Color for push notification. Available only for Android platforms.
        tag : Optional[str]
            Tag for push notification. Available only for Android platforms.
        badge : Optional[float]
            Badge for push notification. Available only for iOS platforms.
        draft : Optional[bool]
            Is message a draft
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        content_available : Optional[bool]
            If set to true, the notification will be delivered in the background. Available only for iOS Platform.
        critical : Optional[bool]
            If set to true, the notification will be marked as critical. This requires the app to have the critical notification entitlement. Available only for iOS Platform.
        priority : Optional[MessagePriority]
            Set the notification priority. "normal" will consider device battery state and may send notifications later. "high" will always attempt to immediately deliver the notification.
        
        Returns
        -------
        Message            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/push/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        api_params['topics'] = self._normalize_value(topics)
        api_params['users'] = self._normalize_value(users)
        api_params['targets'] = self._normalize_value(targets)
        api_params['title'] = self._normalize_value(title)
        api_params['body'] = self._normalize_value(body)
        api_params['data'] = self._normalize_value(data)
        api_params['action'] = self._normalize_value(action)
        api_params['image'] = self._normalize_value(image)
        api_params['icon'] = self._normalize_value(icon)
        api_params['sound'] = self._normalize_value(sound)
        api_params['color'] = self._normalize_value(color)
        api_params['tag'] = self._normalize_value(tag)
        api_params['badge'] = self._normalize_value(badge)
        api_params['draft'] = self._normalize_value(draft)
        api_params['scheduledAt'] = self._normalize_value(scheduled_at)
        api_params['contentAvailable'] = self._normalize_value(content_available)
        api_params['critical'] = self._normalize_value(critical)
        api_params['priority'] = self._normalize_value(priority)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def create_sms(
        self,
        message_id: str,
        content: str,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None,
        targets: Optional[List[str]] = None,
        draft: Optional[bool] = None,
        scheduled_at: Optional[str] = None    ) -> Message:
        """
        Create a new SMS message.

        Parameters
        ----------
        message_id : str
            Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        content : str
            SMS Content.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        targets : Optional[List[str]]
            List of Targets IDs.
        draft : Optional[bool]
            Is message a draft
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        
        Returns
        -------
        Message            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/sms'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        if content is None:
            raise AppwriteException('Missing required parameter: "content"')


        api_params['messageId'] = self._normalize_value(message_id)
        api_params['content'] = self._normalize_value(content)
        if topics is not None:
            api_params['topics'] = self._normalize_value(topics)
        if users is not None:
            api_params['users'] = self._normalize_value(users)
        if targets is not None:
            api_params['targets'] = self._normalize_value(targets)
        if draft is not None:
            api_params['draft'] = self._normalize_value(draft)
        api_params['scheduledAt'] = self._normalize_value(scheduled_at)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def update_sms(
        self,
        message_id: str,
        topics: Optional[List[str]] = None,
        users: Optional[List[str]] = None,
        targets: Optional[List[str]] = None,
        content: Optional[str] = None,
        draft: Optional[bool] = None,
        scheduled_at: Optional[str] = None    ) -> Message:
        """
        Update an SMS message by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        topics : Optional[List[str]]
            List of Topic IDs.
        users : Optional[List[str]]
            List of User IDs.
        targets : Optional[List[str]]
            List of Targets IDs.
        content : Optional[str]
            Email Content.
        draft : Optional[bool]
            Is message a draft
        scheduled_at : Optional[str]
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        
        Returns
        -------
        Message            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/sms/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        api_params['topics'] = self._normalize_value(topics)
        api_params['users'] = self._normalize_value(users)
        api_params['targets'] = self._normalize_value(targets)
        api_params['content'] = self._normalize_value(content)
        api_params['draft'] = self._normalize_value(draft)
        api_params['scheduledAt'] = self._normalize_value(scheduled_at)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Message)


    def get_message(
        self,
        message_id: str    ) -> Message:
        """
        Get a message by its unique ID.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        
        Returns
        -------
        Message            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Message)


    def delete(
        self,
        message_id: str    ) -> Dict[str, Any]:
        """
        Delete a message. If the message is not a draft or scheduled, but has been sent, this will not recall the message.

        Parameters
        ----------
        message_id : str
            Message ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_message_logs(
        self,
        message_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None    ) -> LogList:
        """
        Get the message activity logs listed by its unique ID.

        Parameters
        ----------
        message_id : str
            Message ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/{messageId}/logs'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def list_targets(
        self,
        message_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None    ) -> TargetList:
        """
        Get a list of the targets associated with a message.

        Parameters
        ----------
        message_id : str
            Message ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, providerId, identifier, providerType
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        TargetList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/{messageId}/targets'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', str(self._normalize_value(message_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=TargetList)


    def list_providers(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None    ) -> ProviderList:
        """
        Get a list of all providers from the current Appwrite project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ProviderList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ProviderList)


    def create_apns_provider(
        self,
        provider_id: str,
        name: str,
        auth_key: Optional[str] = None,
        auth_key_id: Optional[str] = None,
        team_id: Optional[str] = None,
        bundle_id: Optional[str] = None,
        sandbox: Optional[bool] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Apple Push Notification service provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        auth_key : Optional[str]
            APNS authentication key.
        auth_key_id : Optional[str]
            APNS authentication key ID.
        team_id : Optional[str]
            APNS team ID.
        bundle_id : Optional[str]
            APNS bundle ID.
        sandbox : Optional[bool]
            Use APNS sandbox environment.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/apns'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if auth_key is not None:
            api_params['authKey'] = self._normalize_value(auth_key)
        if auth_key_id is not None:
            api_params['authKeyId'] = self._normalize_value(auth_key_id)
        if team_id is not None:
            api_params['teamId'] = self._normalize_value(team_id)
        if bundle_id is not None:
            api_params['bundleId'] = self._normalize_value(bundle_id)
        if sandbox is not None:
            api_params['sandbox'] = self._normalize_value(sandbox)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_apns_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        auth_key: Optional[str] = None,
        auth_key_id: Optional[str] = None,
        team_id: Optional[str] = None,
        bundle_id: Optional[str] = None,
        sandbox: Optional[bool] = None    ) -> Provider:
        """
        Update a Apple Push Notification service provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        auth_key : Optional[str]
            APNS authentication key.
        auth_key_id : Optional[str]
            APNS authentication key ID.
        team_id : Optional[str]
            APNS team ID.
        bundle_id : Optional[str]
            APNS bundle ID.
        sandbox : Optional[bool]
            Use APNS sandbox environment.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/apns/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if auth_key is not None:
            api_params['authKey'] = self._normalize_value(auth_key)
        if auth_key_id is not None:
            api_params['authKeyId'] = self._normalize_value(auth_key_id)
        if team_id is not None:
            api_params['teamId'] = self._normalize_value(team_id)
        if bundle_id is not None:
            api_params['bundleId'] = self._normalize_value(bundle_id)
        api_params['sandbox'] = self._normalize_value(sandbox)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_fcm_provider(
        self,
        provider_id: str,
        name: str,
        service_account_json: Optional[Dict[str, Any]] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Firebase Cloud Messaging provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        service_account_json : Optional[Dict[str, Any]]
            FCM service account JSON.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/fcm'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        api_params['serviceAccountJSON'] = self._normalize_value(service_account_json)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_fcm_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        service_account_json: Optional[Dict[str, Any]] = None    ) -> Provider:
        """
        Update a Firebase Cloud Messaging provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        service_account_json : Optional[Dict[str, Any]]
            FCM service account JSON.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/fcm/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        api_params['serviceAccountJSON'] = self._normalize_value(service_account_json)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_mailgun_provider(
        self,
        provider_id: str,
        name: str,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        is_eu_region: Optional[bool] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Mailgun provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        api_key : Optional[str]
            Mailgun API Key.
        domain : Optional[str]
            Mailgun Domain.
        is_eu_region : Optional[bool]
            Set as EU region.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name. Reply to name must have reply to email as well.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email. Reply to email must have reply to name as well.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/mailgun'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        api_params['isEuRegion'] = self._normalize_value(is_eu_region)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_mailgun_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        api_key: Optional[str] = None,
        domain: Optional[str] = None,
        is_eu_region: Optional[bool] = None,
        enabled: Optional[bool] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None    ) -> Provider:
        """
        Update a Mailgun provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        api_key : Optional[str]
            Mailgun API Key.
        domain : Optional[str]
            Mailgun Domain.
        is_eu_region : Optional[bool]
            Set as EU region.
        enabled : Optional[bool]
            Set as enabled.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/mailgun/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if domain is not None:
            api_params['domain'] = self._normalize_value(domain)
        api_params['isEuRegion'] = self._normalize_value(is_eu_region)
        api_params['enabled'] = self._normalize_value(enabled)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_msg91_provider(
        self,
        provider_id: str,
        name: str,
        template_id: Optional[str] = None,
        sender_id: Optional[str] = None,
        auth_key: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new MSG91 provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        template_id : Optional[str]
            Msg91 template ID
        sender_id : Optional[str]
            Msg91 sender ID.
        auth_key : Optional[str]
            Msg91 auth key.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/msg91'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if template_id is not None:
            api_params['templateId'] = self._normalize_value(template_id)
        if sender_id is not None:
            api_params['senderId'] = self._normalize_value(sender_id)
        if auth_key is not None:
            api_params['authKey'] = self._normalize_value(auth_key)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_msg91_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        template_id: Optional[str] = None,
        sender_id: Optional[str] = None,
        auth_key: Optional[str] = None    ) -> Provider:
        """
        Update a MSG91 provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        template_id : Optional[str]
            Msg91 template ID.
        sender_id : Optional[str]
            Msg91 sender ID.
        auth_key : Optional[str]
            Msg91 auth key.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/msg91/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if template_id is not None:
            api_params['templateId'] = self._normalize_value(template_id)
        if sender_id is not None:
            api_params['senderId'] = self._normalize_value(sender_id)
        if auth_key is not None:
            api_params['authKey'] = self._normalize_value(auth_key)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_resend_provider(
        self,
        provider_id: str,
        name: str,
        api_key: Optional[str] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Resend provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        api_key : Optional[str]
            Resend API key.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/resend'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_resend_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        api_key: Optional[str] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None    ) -> Provider:
        """
        Update a Resend provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        api_key : Optional[str]
            Resend API key.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the Reply To field for the mail. Default value is Sender Name.
        reply_to_email : Optional[str]
            Email set in the Reply To field for the mail. Default value is Sender Email.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/resend/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_sendgrid_provider(
        self,
        provider_id: str,
        name: str,
        api_key: Optional[str] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Sendgrid provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        api_key : Optional[str]
            Sendgrid API key.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/sendgrid'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_sendgrid_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        api_key: Optional[str] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None    ) -> Provider:
        """
        Update a Sendgrid provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        api_key : Optional[str]
            Sendgrid API key.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the Reply To field for the mail. Default value is Sender Name.
        reply_to_email : Optional[str]
            Email set in the Reply To field for the mail. Default value is Sender Email.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/sendgrid/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_smtp_provider(
        self,
        provider_id: str,
        name: str,
        host: str,
        port: Optional[float] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        encryption: Optional[SmtpEncryption] = None,
        auto_tls: Optional[bool] = None,
        mailer: Optional[str] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new SMTP provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        host : str
            SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465"`. Hosts will be tried in order.
        port : Optional[float]
            The default SMTP server port.
        username : Optional[str]
            Authentication username.
        password : Optional[str]
            Authentication password.
        encryption : Optional[SmtpEncryption]
            Encryption type. Can be omitted, 'ssl', or 'tls'
        auto_tls : Optional[bool]
            Enable SMTP AutoTLS feature.
        mailer : Optional[str]
            The value to use for the X-Mailer header.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the reply to field for the mail. Default value is sender name.
        reply_to_email : Optional[str]
            Email set in the reply to field for the mail. Default value is sender email.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/smtp'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if host is None:
            raise AppwriteException('Missing required parameter: "host"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        api_params['host'] = self._normalize_value(host)
        if port is not None:
            api_params['port'] = self._normalize_value(port)
        if username is not None:
            api_params['username'] = self._normalize_value(username)
        if password is not None:
            api_params['password'] = self._normalize_value(password)
        if encryption is not None:
            api_params['encryption'] = self._normalize_value(encryption)
        if auto_tls is not None:
            api_params['autoTLS'] = self._normalize_value(auto_tls)
        if mailer is not None:
            api_params['mailer'] = self._normalize_value(mailer)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_smtp_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[float] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        encryption: Optional[SmtpEncryption] = None,
        auto_tls: Optional[bool] = None,
        mailer: Optional[str] = None,
        from_name: Optional[str] = None,
        from_email: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        reply_to_email: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Update a SMTP provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        host : Optional[str]
            SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465"`. Hosts will be tried in order.
        port : Optional[float]
            SMTP port.
        username : Optional[str]
            Authentication username.
        password : Optional[str]
            Authentication password.
        encryption : Optional[SmtpEncryption]
            Encryption type. Can be 'ssl' or 'tls'
        auto_tls : Optional[bool]
            Enable SMTP AutoTLS feature.
        mailer : Optional[str]
            The value to use for the X-Mailer header.
        from_name : Optional[str]
            Sender Name.
        from_email : Optional[str]
            Sender email address.
        reply_to_name : Optional[str]
            Name set in the Reply To field for the mail. Default value is Sender Name.
        reply_to_email : Optional[str]
            Email set in the Reply To field for the mail. Default value is Sender Email.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/smtp/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if host is not None:
            api_params['host'] = self._normalize_value(host)
        api_params['port'] = self._normalize_value(port)
        if username is not None:
            api_params['username'] = self._normalize_value(username)
        if password is not None:
            api_params['password'] = self._normalize_value(password)
        if encryption is not None:
            api_params['encryption'] = self._normalize_value(encryption)
        api_params['autoTLS'] = self._normalize_value(auto_tls)
        if mailer is not None:
            api_params['mailer'] = self._normalize_value(mailer)
        if from_name is not None:
            api_params['fromName'] = self._normalize_value(from_name)
        if from_email is not None:
            api_params['fromEmail'] = self._normalize_value(from_email)
        if reply_to_name is not None:
            api_params['replyToName'] = self._normalize_value(reply_to_name)
        if reply_to_email is not None:
            api_params['replyToEmail'] = self._normalize_value(reply_to_email)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_telesign_provider(
        self,
        provider_id: str,
        name: str,
        xfrom: Optional[str] = None,
        customer_id: Optional[str] = None,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Telesign provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        customer_id : Optional[str]
            Telesign customer ID.
        api_key : Optional[str]
            Telesign API key.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/telesign'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if customer_id is not None:
            api_params['customerId'] = self._normalize_value(customer_id)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_telesign_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        customer_id: Optional[str] = None,
        api_key: Optional[str] = None,
        xfrom: Optional[str] = None    ) -> Provider:
        """
        Update a Telesign provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        customer_id : Optional[str]
            Telesign customer ID.
        api_key : Optional[str]
            Telesign API key.
        xfrom : Optional[str]
            Sender number.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/telesign/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if customer_id is not None:
            api_params['customerId'] = self._normalize_value(customer_id)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_textmagic_provider(
        self,
        provider_id: str,
        name: str,
        xfrom: Optional[str] = None,
        username: Optional[str] = None,
        api_key: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Textmagic provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        username : Optional[str]
            Textmagic username.
        api_key : Optional[str]
            Textmagic apiKey.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/textmagic'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if username is not None:
            api_params['username'] = self._normalize_value(username)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_textmagic_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        username: Optional[str] = None,
        api_key: Optional[str] = None,
        xfrom: Optional[str] = None    ) -> Provider:
        """
        Update a Textmagic provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        username : Optional[str]
            Textmagic username.
        api_key : Optional[str]
            Textmagic apiKey.
        xfrom : Optional[str]
            Sender number.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/textmagic/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if username is not None:
            api_params['username'] = self._normalize_value(username)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_twilio_provider(
        self,
        provider_id: str,
        name: str,
        xfrom: Optional[str] = None,
        account_sid: Optional[str] = None,
        auth_token: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Twilio provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        account_sid : Optional[str]
            Twilio account secret ID.
        auth_token : Optional[str]
            Twilio authentication token.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/twilio'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if account_sid is not None:
            api_params['accountSid'] = self._normalize_value(account_sid)
        if auth_token is not None:
            api_params['authToken'] = self._normalize_value(auth_token)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_twilio_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        account_sid: Optional[str] = None,
        auth_token: Optional[str] = None,
        xfrom: Optional[str] = None    ) -> Provider:
        """
        Update a Twilio provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        account_sid : Optional[str]
            Twilio account secret ID.
        auth_token : Optional[str]
            Twilio authentication token.
        xfrom : Optional[str]
            Sender number.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/twilio/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if account_sid is not None:
            api_params['accountSid'] = self._normalize_value(account_sid)
        if auth_token is not None:
            api_params['authToken'] = self._normalize_value(auth_token)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def create_vonage_provider(
        self,
        provider_id: str,
        name: str,
        xfrom: Optional[str] = None,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        enabled: Optional[bool] = None    ) -> Provider:
        """
        Create a new Vonage provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : Optional[str]
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        api_key : Optional[str]
            Vonage API key.
        api_secret : Optional[str]
            Vonage API secret.
        enabled : Optional[bool]
            Set as enabled.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/vonage'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['providerId'] = self._normalize_value(provider_id)
        api_params['name'] = self._normalize_value(name)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if api_secret is not None:
            api_params['apiSecret'] = self._normalize_value(api_secret)
        api_params['enabled'] = self._normalize_value(enabled)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def update_vonage_provider(
        self,
        provider_id: str,
        name: Optional[str] = None,
        enabled: Optional[bool] = None,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        xfrom: Optional[str] = None    ) -> Provider:
        """
        Update a Vonage provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : Optional[str]
            Provider name.
        enabled : Optional[bool]
            Set as enabled.
        api_key : Optional[str]
            Vonage API key.
        api_secret : Optional[str]
            Vonage API secret.
        xfrom : Optional[str]
            Sender number.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/vonage/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['enabled'] = self._normalize_value(enabled)
        if api_key is not None:
            api_params['apiKey'] = self._normalize_value(api_key)
        if api_secret is not None:
            api_params['apiSecret'] = self._normalize_value(api_secret)
        if xfrom is not None:
            api_params['from'] = self._normalize_value(xfrom)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Provider)


    def get_provider(
        self,
        provider_id: str    ) -> Provider:
        """
        Get a provider by its unique ID.
        

        Parameters
        ----------
        provider_id : str
            Provider ID.
        
        Returns
        -------
        Provider            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Provider)


    def delete_provider(
        self,
        provider_id: str    ) -> Dict[str, Any]:
        """
        Delete a provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_provider_logs(
        self,
        provider_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None    ) -> LogList:
        """
        Get the provider activity logs listed by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/{providerId}/logs'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', str(self._normalize_value(provider_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def list_subscriber_logs(
        self,
        subscriber_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None    ) -> LogList:
        """
        Get the subscriber activity logs listed by its unique ID.

        Parameters
        ----------
        subscriber_id : str
            Subscriber ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/subscribers/{subscriberId}/logs'
        api_params = {}
        if subscriber_id is None:
            raise AppwriteException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{subscriberId}', str(self._normalize_value(subscriber_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def list_topics(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None    ) -> TopicList:
        """
        Get a list of all topics from the current Appwrite project.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, description, emailTotal, smsTotal, pushTotal
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        TopicList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=TopicList)


    def create_topic(
        self,
        topic_id: str,
        name: str,
        subscribe: Optional[List[str]] = None    ) -> Topic:
        """
        Create a new topic.

        Parameters
        ----------
        topic_id : str
            Topic ID. Choose a custom Topic ID or a new Topic ID.
        name : str
            Topic Name.
        subscribe : Optional[List[str]]
            An array of role strings with subscribe permission. By default all users are granted with any subscribe permission. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        
        Returns
        -------
        Topic            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['topicId'] = self._normalize_value(topic_id)
        api_params['name'] = self._normalize_value(name)
        if subscribe is not None:
            api_params['subscribe'] = self._normalize_value(subscribe)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Topic)


    def get_topic(
        self,
        topic_id: str    ) -> Topic:
        """
        Get a topic by its unique ID.
        

        Parameters
        ----------
        topic_id : str
            Topic ID.
        
        Returns
        -------
        Topic            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Topic)


    def update_topic(
        self,
        topic_id: str,
        name: Optional[str] = None,
        subscribe: Optional[List[str]] = None    ) -> Topic:
        """
        Update a topic by its unique ID.
        

        Parameters
        ----------
        topic_id : str
            Topic ID.
        name : Optional[str]
            Topic Name.
        subscribe : Optional[List[str]]
            An array of role strings with subscribe permission. By default all users are granted with any subscribe permission. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        
        Returns
        -------
        Topic            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['subscribe'] = self._normalize_value(subscribe)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Topic)


    def delete_topic(
        self,
        topic_id: str    ) -> Dict[str, Any]:
        """
        Delete a topic by its unique ID.

        Parameters
        ----------
        topic_id : str
            Topic ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_topic_logs(
        self,
        topic_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None    ) -> LogList:
        """
        Get the topic activity logs listed by its unique ID.

        Parameters
        ----------
        topic_id : str
            Topic ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        LogList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}/logs'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=LogList)


    def list_subscribers(
        self,
        topic_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None    ) -> SubscriberList:
        """
        Get a list of all subscribers from the current Appwrite project.

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID subscribed to.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: targetId, topicId, userId, providerType
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        SubscriberList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}/subscribers'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=SubscriberList)


    def create_subscriber(
        self,
        topic_id: str,
        subscriber_id: str,
        target_id: str    ) -> Subscriber:
        """
        Create a new subscriber.

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID to subscribe to.
        subscriber_id : str
            Subscriber ID. Choose a custom Subscriber ID or a new Subscriber ID.
        target_id : str
            Target ID. The target ID to link to the specified Topic ID.
        
        Returns
        -------
        Subscriber            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}/subscribers'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        if subscriber_id is None:
            raise AppwriteException('Missing required parameter: "subscriber_id"')

        if target_id is None:
            raise AppwriteException('Missing required parameter: "target_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))

        api_params['subscriberId'] = self._normalize_value(subscriber_id)
        api_params['targetId'] = self._normalize_value(target_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Subscriber)


    def get_subscriber(
        self,
        topic_id: str,
        subscriber_id: str    ) -> Subscriber:
        """
        Get a subscriber by its unique ID.
        

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID subscribed to.
        subscriber_id : str
            Subscriber ID.
        
        Returns
        -------
        Subscriber            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}/subscribers/{subscriberId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        if subscriber_id is None:
            raise AppwriteException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))
        api_path = api_path.replace('{subscriberId}', str(self._normalize_value(subscriber_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Subscriber)


    def delete_subscriber(
        self,
        topic_id: str,
        subscriber_id: str    ) -> Dict[str, Any]:
        """
        Delete a subscriber by its unique ID.

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID subscribed to.
        subscriber_id : str
            Subscriber ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}/subscribers/{subscriberId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        if subscriber_id is None:
            raise AppwriteException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{topicId}', str(self._normalize_value(topic_id)))
        api_path = api_path.replace('{subscriberId}', str(self._normalize_value(subscriber_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

