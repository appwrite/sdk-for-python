from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException
from ..enums.message_priority import MessagePriority;
from ..enums.smtp_encryption import SmtpEncryption;

class Messaging(Service):

    def __init__(self, client) -> None:
        super(Messaging, self).__init__(client)

    def list_messages(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all messages from the current Appwrite project.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: scheduledAt, deliveredAt, deliveredTotal, status, description, providerType
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create_email(self, message_id: str, subject: str, content: str, topics: List[str] = None, users: List[str] = None, targets: List[str] = None, cc: List[str] = None, bcc: List[str] = None, attachments: List[str] = None, draft: bool = None, html: bool = None, scheduled_at: str = None) -> Dict[str, Any]:
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
        topics : List[str]
            List of Topic IDs.
        users : List[str]
            List of User IDs.
        targets : List[str]
            List of Targets IDs.
        cc : List[str]
            Array of target IDs to be added as CC.
        bcc : List[str]
            Array of target IDs to be added as BCC.
        attachments : List[str]
            Array of compound ID strings of bucket IDs and file IDs to be attached to the email. They should be formatted as <BUCKET_ID>:<FILE_ID>.
        draft : bool
            Is message a draft
        html : bool
            Is content of type HTML
        scheduled_at : str
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['messageId'] = message_id
        api_params['subject'] = subject
        api_params['content'] = content
        api_params['topics'] = topics
        api_params['users'] = users
        api_params['targets'] = targets
        api_params['cc'] = cc
        api_params['bcc'] = bcc
        api_params['attachments'] = attachments
        api_params['draft'] = draft
        api_params['html'] = html
        api_params['scheduledAt'] = scheduled_at

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_email(self, message_id: str, topics: List[str] = None, users: List[str] = None, targets: List[str] = None, subject: str = None, content: str = None, draft: bool = None, html: bool = None, cc: List[str] = None, bcc: List[str] = None, scheduled_at: str = None, attachments: List[str] = None) -> Dict[str, Any]:
        """
        Update an email message by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        topics : List[str]
            List of Topic IDs.
        users : List[str]
            List of User IDs.
        targets : List[str]
            List of Targets IDs.
        subject : str
            Email Subject.
        content : str
            Email Content.
        draft : bool
            Is message a draft
        html : bool
            Is content of type HTML
        cc : List[str]
            Array of target IDs to be added as CC.
        bcc : List[str]
            Array of target IDs to be added as BCC.
        scheduled_at : str
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        attachments : List[str]
            Array of compound ID strings of bucket IDs and file IDs to be attached to the email. They should be formatted as <BUCKET_ID>:<FILE_ID>.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/email/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)

        api_params['topics'] = topics
        api_params['users'] = users
        api_params['targets'] = targets
        api_params['subject'] = subject
        api_params['content'] = content
        api_params['draft'] = draft
        api_params['html'] = html
        api_params['cc'] = cc
        api_params['bcc'] = bcc
        api_params['scheduledAt'] = scheduled_at
        api_params['attachments'] = attachments

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_push(self, message_id: str, title: str = None, body: str = None, topics: List[str] = None, users: List[str] = None, targets: List[str] = None, data: dict = None, action: str = None, image: str = None, icon: str = None, sound: str = None, color: str = None, tag: str = None, badge: float = None, draft: bool = None, scheduled_at: str = None, content_available: bool = None, critical: bool = None, priority: MessagePriority = None) -> Dict[str, Any]:
        """
        Create a new push notification.

        Parameters
        ----------
        message_id : str
            Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        title : str
            Title for push notification.
        body : str
            Body for push notification.
        topics : List[str]
            List of Topic IDs.
        users : List[str]
            List of User IDs.
        targets : List[str]
            List of Targets IDs.
        data : dict
            Additional key-value pair data for push notification.
        action : str
            Action for push notification.
        image : str
            Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage. It should be formatted as <BUCKET_ID>:<FILE_ID>.
        icon : str
            Icon for push notification. Available only for Android and Web Platform.
        sound : str
            Sound for push notification. Available only for Android and iOS Platform.
        color : str
            Color for push notification. Available only for Android Platform.
        tag : str
            Tag for push notification. Available only for Android Platform.
        badge : float
            Badge for push notification. Available only for iOS Platform.
        draft : bool
            Is message a draft
        scheduled_at : str
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        content_available : bool
            If set to true, the notification will be delivered in the background. Available only for iOS Platform.
        critical : bool
            If set to true, the notification will be marked as critical. This requires the app to have the critical notification entitlement. Available only for iOS Platform.
        priority : MessagePriority
            Set the notification priority. "normal" will consider device state and may not deliver notifications immediately. "high" will always attempt to immediately deliver the notification.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/push'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')


        api_params['messageId'] = message_id
        api_params['title'] = title
        api_params['body'] = body
        api_params['topics'] = topics
        api_params['users'] = users
        api_params['targets'] = targets
        api_params['data'] = data
        api_params['action'] = action
        api_params['image'] = image
        api_params['icon'] = icon
        api_params['sound'] = sound
        api_params['color'] = color
        api_params['tag'] = tag
        api_params['badge'] = badge
        api_params['draft'] = draft
        api_params['scheduledAt'] = scheduled_at
        api_params['contentAvailable'] = content_available
        api_params['critical'] = critical
        api_params['priority'] = priority

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_push(self, message_id: str, topics: List[str] = None, users: List[str] = None, targets: List[str] = None, title: str = None, body: str = None, data: dict = None, action: str = None, image: str = None, icon: str = None, sound: str = None, color: str = None, tag: str = None, badge: float = None, draft: bool = None, scheduled_at: str = None, content_available: bool = None, critical: bool = None, priority: MessagePriority = None) -> Dict[str, Any]:
        """
        Update a push notification by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        topics : List[str]
            List of Topic IDs.
        users : List[str]
            List of User IDs.
        targets : List[str]
            List of Targets IDs.
        title : str
            Title for push notification.
        body : str
            Body for push notification.
        data : dict
            Additional Data for push notification.
        action : str
            Action for push notification.
        image : str
            Image for push notification. Must be a compound bucket ID to file ID of a jpeg, png, or bmp image in Appwrite Storage. It should be formatted as <BUCKET_ID>:<FILE_ID>.
        icon : str
            Icon for push notification. Available only for Android and Web platforms.
        sound : str
            Sound for push notification. Available only for Android and iOS platforms.
        color : str
            Color for push notification. Available only for Android platforms.
        tag : str
            Tag for push notification. Available only for Android platforms.
        badge : float
            Badge for push notification. Available only for iOS platforms.
        draft : bool
            Is message a draft
        scheduled_at : str
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        content_available : bool
            If set to true, the notification will be delivered in the background. Available only for iOS Platform.
        critical : bool
            If set to true, the notification will be marked as critical. This requires the app to have the critical notification entitlement. Available only for iOS Platform.
        priority : MessagePriority
            Set the notification priority. "normal" will consider device battery state and may send notifications later. "high" will always attempt to immediately deliver the notification.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/push/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)

        api_params['topics'] = topics
        api_params['users'] = users
        api_params['targets'] = targets
        api_params['title'] = title
        api_params['body'] = body
        api_params['data'] = data
        api_params['action'] = action
        api_params['image'] = image
        api_params['icon'] = icon
        api_params['sound'] = sound
        api_params['color'] = color
        api_params['tag'] = tag
        api_params['badge'] = badge
        api_params['draft'] = draft
        api_params['scheduledAt'] = scheduled_at
        api_params['contentAvailable'] = content_available
        api_params['critical'] = critical
        api_params['priority'] = priority

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_sms(self, message_id: str, content: str, topics: List[str] = None, users: List[str] = None, targets: List[str] = None, draft: bool = None, scheduled_at: str = None) -> Dict[str, Any]:
        """
        Create a new SMS message.

        Parameters
        ----------
        message_id : str
            Message ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        content : str
            SMS Content.
        topics : List[str]
            List of Topic IDs.
        users : List[str]
            List of User IDs.
        targets : List[str]
            List of Targets IDs.
        draft : bool
            Is message a draft
        scheduled_at : str
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['messageId'] = message_id
        api_params['content'] = content
        api_params['topics'] = topics
        api_params['users'] = users
        api_params['targets'] = targets
        api_params['draft'] = draft
        api_params['scheduledAt'] = scheduled_at

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_sms(self, message_id: str, topics: List[str] = None, users: List[str] = None, targets: List[str] = None, content: str = None, draft: bool = None, scheduled_at: str = None) -> Dict[str, Any]:
        """
        Update an SMS message by its unique ID. This endpoint only works on messages that are in draft status. Messages that are already processing, sent, or failed cannot be updated.
        

        Parameters
        ----------
        message_id : str
            Message ID.
        topics : List[str]
            List of Topic IDs.
        users : List[str]
            List of User IDs.
        targets : List[str]
            List of Targets IDs.
        content : str
            Email Content.
        draft : bool
            Is message a draft
        scheduled_at : str
            Scheduled delivery time for message in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/sms/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)

        api_params['topics'] = topics
        api_params['users'] = users
        api_params['targets'] = targets
        api_params['content'] = content
        api_params['draft'] = draft
        api_params['scheduledAt'] = scheduled_at

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_message(self, message_id: str) -> Dict[str, Any]:
        """
        Get a message by its unique ID.
        

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

        api_path = api_path.replace('{messageId}', message_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete(self, message_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{messageId}', message_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_message_logs(self, message_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get the message activity logs listed by its unique ID.

        Parameters
        ----------
        message_id : str
            Message ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/{messageId}/logs'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def list_targets(self, message_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get a list of the targets associated with a message.

        Parameters
        ----------
        message_id : str
            Message ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, providerId, identifier, providerType
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/messages/{messageId}/targets'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def list_providers(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all providers from the current Appwrite project.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create_apns_provider(self, provider_id: str, name: str, auth_key: str = None, auth_key_id: str = None, team_id: str = None, bundle_id: str = None, sandbox: bool = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Apple Push Notification service provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        auth_key : str
            APNS authentication key.
        auth_key_id : str
            APNS authentication key ID.
        team_id : str
            APNS team ID.
        bundle_id : str
            APNS bundle ID.
        sandbox : bool
            Use APNS sandbox environment.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['authKey'] = auth_key
        api_params['authKeyId'] = auth_key_id
        api_params['teamId'] = team_id
        api_params['bundleId'] = bundle_id
        api_params['sandbox'] = sandbox
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_apns_provider(self, provider_id: str, name: str = None, enabled: bool = None, auth_key: str = None, auth_key_id: str = None, team_id: str = None, bundle_id: str = None, sandbox: bool = None) -> Dict[str, Any]:
        """
        Update a Apple Push Notification service provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        auth_key : str
            APNS authentication key.
        auth_key_id : str
            APNS authentication key ID.
        team_id : str
            APNS team ID.
        bundle_id : str
            APNS bundle ID.
        sandbox : bool
            Use APNS sandbox environment.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/apns/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['authKey'] = auth_key
        api_params['authKeyId'] = auth_key_id
        api_params['teamId'] = team_id
        api_params['bundleId'] = bundle_id
        api_params['sandbox'] = sandbox

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_fcm_provider(self, provider_id: str, name: str, service_account_json: dict = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Firebase Cloud Messaging provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        service_account_json : dict
            FCM service account JSON.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['serviceAccountJSON'] = service_account_json
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_fcm_provider(self, provider_id: str, name: str = None, enabled: bool = None, service_account_json: dict = None) -> Dict[str, Any]:
        """
        Update a Firebase Cloud Messaging provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        service_account_json : dict
            FCM service account JSON.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/fcm/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['serviceAccountJSON'] = service_account_json

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_mailgun_provider(self, provider_id: str, name: str, api_key: str = None, domain: str = None, is_eu_region: bool = None, from_name: str = None, from_email: str = None, reply_to_name: str = None, reply_to_email: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Mailgun provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        api_key : str
            Mailgun API Key.
        domain : str
            Mailgun Domain.
        is_eu_region : bool
            Set as EU region.
        from_name : str
            Sender Name.
        from_email : str
            Sender email address.
        reply_to_name : str
            Name set in the reply to field for the mail. Default value is sender name. Reply to name must have reply to email as well.
        reply_to_email : str
            Email set in the reply to field for the mail. Default value is sender email. Reply to email must have reply to name as well.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['apiKey'] = api_key
        api_params['domain'] = domain
        api_params['isEuRegion'] = is_eu_region
        api_params['fromName'] = from_name
        api_params['fromEmail'] = from_email
        api_params['replyToName'] = reply_to_name
        api_params['replyToEmail'] = reply_to_email
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_mailgun_provider(self, provider_id: str, name: str = None, api_key: str = None, domain: str = None, is_eu_region: bool = None, enabled: bool = None, from_name: str = None, from_email: str = None, reply_to_name: str = None, reply_to_email: str = None) -> Dict[str, Any]:
        """
        Update a Mailgun provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        api_key : str
            Mailgun API Key.
        domain : str
            Mailgun Domain.
        is_eu_region : bool
            Set as EU region.
        enabled : bool
            Set as enabled.
        from_name : str
            Sender Name.
        from_email : str
            Sender email address.
        reply_to_name : str
            Name set in the reply to field for the mail. Default value is sender name.
        reply_to_email : str
            Email set in the reply to field for the mail. Default value is sender email.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/mailgun/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['apiKey'] = api_key
        api_params['domain'] = domain
        api_params['isEuRegion'] = is_eu_region
        api_params['enabled'] = enabled
        api_params['fromName'] = from_name
        api_params['fromEmail'] = from_email
        api_params['replyToName'] = reply_to_name
        api_params['replyToEmail'] = reply_to_email

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_msg91_provider(self, provider_id: str, name: str, template_id: str = None, sender_id: str = None, auth_key: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new MSG91 provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        template_id : str
            Msg91 template ID
        sender_id : str
            Msg91 sender ID.
        auth_key : str
            Msg91 auth key.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['templateId'] = template_id
        api_params['senderId'] = sender_id
        api_params['authKey'] = auth_key
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_msg91_provider(self, provider_id: str, name: str = None, enabled: bool = None, template_id: str = None, sender_id: str = None, auth_key: str = None) -> Dict[str, Any]:
        """
        Update a MSG91 provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        template_id : str
            Msg91 template ID.
        sender_id : str
            Msg91 sender ID.
        auth_key : str
            Msg91 auth key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/msg91/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['templateId'] = template_id
        api_params['senderId'] = sender_id
        api_params['authKey'] = auth_key

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_sendgrid_provider(self, provider_id: str, name: str, api_key: str = None, from_name: str = None, from_email: str = None, reply_to_name: str = None, reply_to_email: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Sendgrid provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        api_key : str
            Sendgrid API key.
        from_name : str
            Sender Name.
        from_email : str
            Sender email address.
        reply_to_name : str
            Name set in the reply to field for the mail. Default value is sender name.
        reply_to_email : str
            Email set in the reply to field for the mail. Default value is sender email.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['apiKey'] = api_key
        api_params['fromName'] = from_name
        api_params['fromEmail'] = from_email
        api_params['replyToName'] = reply_to_name
        api_params['replyToEmail'] = reply_to_email
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_sendgrid_provider(self, provider_id: str, name: str = None, enabled: bool = None, api_key: str = None, from_name: str = None, from_email: str = None, reply_to_name: str = None, reply_to_email: str = None) -> Dict[str, Any]:
        """
        Update a Sendgrid provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        api_key : str
            Sendgrid API key.
        from_name : str
            Sender Name.
        from_email : str
            Sender email address.
        reply_to_name : str
            Name set in the Reply To field for the mail. Default value is Sender Name.
        reply_to_email : str
            Email set in the Reply To field for the mail. Default value is Sender Email.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/sendgrid/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['apiKey'] = api_key
        api_params['fromName'] = from_name
        api_params['fromEmail'] = from_email
        api_params['replyToName'] = reply_to_name
        api_params['replyToEmail'] = reply_to_email

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_smtp_provider(self, provider_id: str, name: str, host: str, port: float = None, username: str = None, password: str = None, encryption: SmtpEncryption = None, auto_tls: bool = None, mailer: str = None, from_name: str = None, from_email: str = None, reply_to_name: str = None, reply_to_email: str = None, enabled: bool = None) -> Dict[str, Any]:
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
        port : float
            The default SMTP server port.
        username : str
            Authentication username.
        password : str
            Authentication password.
        encryption : SmtpEncryption
            Encryption type. Can be omitted, 'ssl', or 'tls'
        auto_tls : bool
            Enable SMTP AutoTLS feature.
        mailer : str
            The value to use for the X-Mailer header.
        from_name : str
            Sender Name.
        from_email : str
            Sender email address.
        reply_to_name : str
            Name set in the reply to field for the mail. Default value is sender name.
        reply_to_email : str
            Email set in the reply to field for the mail. Default value is sender email.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['host'] = host
        api_params['port'] = port
        api_params['username'] = username
        api_params['password'] = password
        api_params['encryption'] = encryption
        api_params['autoTLS'] = auto_tls
        api_params['mailer'] = mailer
        api_params['fromName'] = from_name
        api_params['fromEmail'] = from_email
        api_params['replyToName'] = reply_to_name
        api_params['replyToEmail'] = reply_to_email
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_smtp_provider(self, provider_id: str, name: str = None, host: str = None, port: float = None, username: str = None, password: str = None, encryption: SmtpEncryption = None, auto_tls: bool = None, mailer: str = None, from_name: str = None, from_email: str = None, reply_to_name: str = None, reply_to_email: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Update a SMTP provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        host : str
            SMTP hosts. Either a single hostname or multiple semicolon-delimited hostnames. You can also specify a different port for each host such as `smtp1.example.com:25;smtp2.example.com`. You can also specify encryption type, for example: `tls://smtp1.example.com:587;ssl://smtp2.example.com:465"`. Hosts will be tried in order.
        port : float
            SMTP port.
        username : str
            Authentication username.
        password : str
            Authentication password.
        encryption : SmtpEncryption
            Encryption type. Can be 'ssl' or 'tls'
        auto_tls : bool
            Enable SMTP AutoTLS feature.
        mailer : str
            The value to use for the X-Mailer header.
        from_name : str
            Sender Name.
        from_email : str
            Sender email address.
        reply_to_name : str
            Name set in the Reply To field for the mail. Default value is Sender Name.
        reply_to_email : str
            Email set in the Reply To field for the mail. Default value is Sender Email.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/smtp/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['host'] = host
        api_params['port'] = port
        api_params['username'] = username
        api_params['password'] = password
        api_params['encryption'] = encryption
        api_params['autoTLS'] = auto_tls
        api_params['mailer'] = mailer
        api_params['fromName'] = from_name
        api_params['fromEmail'] = from_email
        api_params['replyToName'] = reply_to_name
        api_params['replyToEmail'] = reply_to_email
        api_params['enabled'] = enabled

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_telesign_provider(self, provider_id: str, name: str, xfrom: str = None, customer_id: str = None, api_key: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Telesign provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : str
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        customer_id : str
            Telesign customer ID.
        api_key : str
            Telesign API key.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['from'] = xfrom
        api_params['customerId'] = customer_id
        api_params['apiKey'] = api_key
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_telesign_provider(self, provider_id: str, name: str = None, enabled: bool = None, customer_id: str = None, api_key: str = None, xfrom: str = None) -> Dict[str, Any]:
        """
        Update a Telesign provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        customer_id : str
            Telesign customer ID.
        api_key : str
            Telesign API key.
        xfrom : str
            Sender number.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/telesign/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['customerId'] = customer_id
        api_params['apiKey'] = api_key
        api_params['from'] = xfrom

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_textmagic_provider(self, provider_id: str, name: str, xfrom: str = None, username: str = None, api_key: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Textmagic provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : str
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        username : str
            Textmagic username.
        api_key : str
            Textmagic apiKey.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['from'] = xfrom
        api_params['username'] = username
        api_params['apiKey'] = api_key
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_textmagic_provider(self, provider_id: str, name: str = None, enabled: bool = None, username: str = None, api_key: str = None, xfrom: str = None) -> Dict[str, Any]:
        """
        Update a Textmagic provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        username : str
            Textmagic username.
        api_key : str
            Textmagic apiKey.
        xfrom : str
            Sender number.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/textmagic/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['username'] = username
        api_params['apiKey'] = api_key
        api_params['from'] = xfrom

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_twilio_provider(self, provider_id: str, name: str, xfrom: str = None, account_sid: str = None, auth_token: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Twilio provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : str
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        account_sid : str
            Twilio account secret ID.
        auth_token : str
            Twilio authentication token.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['from'] = xfrom
        api_params['accountSid'] = account_sid
        api_params['authToken'] = auth_token
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_twilio_provider(self, provider_id: str, name: str = None, enabled: bool = None, account_sid: str = None, auth_token: str = None, xfrom: str = None) -> Dict[str, Any]:
        """
        Update a Twilio provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        account_sid : str
            Twilio account secret ID.
        auth_token : str
            Twilio authentication token.
        xfrom : str
            Sender number.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/twilio/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['accountSid'] = account_sid
        api_params['authToken'] = auth_token
        api_params['from'] = xfrom

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_vonage_provider(self, provider_id: str, name: str, xfrom: str = None, api_key: str = None, api_secret: str = None, enabled: bool = None) -> Dict[str, Any]:
        """
        Create a new Vonage provider.

        Parameters
        ----------
        provider_id : str
            Provider ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Provider name.
        xfrom : str
            Sender Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        api_key : str
            Vonage API key.
        api_secret : str
            Vonage API secret.
        enabled : bool
            Set as enabled.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['providerId'] = provider_id
        api_params['name'] = name
        api_params['from'] = xfrom
        api_params['apiKey'] = api_key
        api_params['apiSecret'] = api_secret
        api_params['enabled'] = enabled

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_vonage_provider(self, provider_id: str, name: str = None, enabled: bool = None, api_key: str = None, api_secret: str = None, xfrom: str = None) -> Dict[str, Any]:
        """
        Update a Vonage provider by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        name : str
            Provider name.
        enabled : bool
            Set as enabled.
        api_key : str
            Vonage API key.
        api_secret : str
            Vonage API secret.
        xfrom : str
            Sender number.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/vonage/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['name'] = name
        api_params['enabled'] = enabled
        api_params['apiKey'] = api_key
        api_params['apiSecret'] = api_secret
        api_params['from'] = xfrom

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_provider(self, provider_id: str) -> Dict[str, Any]:
        """
        Get a provider by its unique ID.
        

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

        api_path = api_path.replace('{providerId}', provider_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_provider(self, provider_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{providerId}', provider_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_provider_logs(self, provider_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get the provider activity logs listed by its unique ID.

        Parameters
        ----------
        provider_id : str
            Provider ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/providers/{providerId}/logs'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def list_subscriber_logs(self, subscriber_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get the subscriber activity logs listed by its unique ID.

        Parameters
        ----------
        subscriber_id : str
            Subscriber ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/subscribers/{subscriberId}/logs'
        api_params = {}
        if subscriber_id is None:
            raise AppwriteException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{subscriberId}', subscriber_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def list_topics(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all topics from the current Appwrite project.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, description, emailTotal, smsTotal, pushTotal
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create_topic(self, topic_id: str, name: str, subscribe: List[str] = None) -> Dict[str, Any]:
        """
        Create a new topic.

        Parameters
        ----------
        topic_id : str
            Topic ID. Choose a custom Topic ID or a new Topic ID.
        name : str
            Topic Name.
        subscribe : List[str]
            An array of role strings with subscribe permission. By default all users are granted with any subscribe permission. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
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


        api_params['topicId'] = topic_id
        api_params['name'] = name
        api_params['subscribe'] = subscribe

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_topic(self, topic_id: str) -> Dict[str, Any]:
        """
        Get a topic by its unique ID.
        

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

        api_path = api_path.replace('{topicId}', topic_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_topic(self, topic_id: str, name: str = None, subscribe: List[str] = None) -> Dict[str, Any]:
        """
        Update a topic by its unique ID.
        

        Parameters
        ----------
        topic_id : str
            Topic ID.
        name : str
            Topic Name.
        subscribe : List[str]
            An array of role strings with subscribe permission. By default all users are granted with any subscribe permission. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        
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

        api_path = api_path.replace('{topicId}', topic_id)

        api_params['name'] = name
        api_params['subscribe'] = subscribe

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_topic(self, topic_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{topicId}', topic_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_topic_logs(self, topic_id: str, queries: List[str] = None) -> Dict[str, Any]:
        """
        Get the topic activity logs listed by its unique ID.

        Parameters
        ----------
        topic_id : str
            Topic ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Only supported methods are limit and offset
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}/logs'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', topic_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
        }, api_params)

    def list_subscribers(self, topic_id: str, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all subscribers from the current Appwrite project.

        Parameters
        ----------
        topic_id : str
            Topic ID. The topic ID subscribed to.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, provider, type, enabled
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/messaging/topics/{topicId}/subscribers'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', topic_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create_subscriber(self, topic_id: str, subscriber_id: str, target_id: str) -> Dict[str, Any]:
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
        Dict[str, Any]
            API response as a dictionary
        
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

        api_path = api_path.replace('{topicId}', topic_id)

        api_params['subscriberId'] = subscriber_id
        api_params['targetId'] = target_id

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_subscriber(self, topic_id: str, subscriber_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{topicId}', topic_id)
        api_path = api_path.replace('{subscriberId}', subscriber_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_subscriber(self, topic_id: str, subscriber_id: str) -> Dict[str, Any]:
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

        api_path = api_path.replace('{topicId}', topic_id)
        api_path = api_path.replace('{subscriberId}', subscriber_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)
