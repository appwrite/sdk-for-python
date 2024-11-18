from ..service import Service
from ..exception import AppwriteException

class Messaging(Service):

    def __init__(self, client):
        super(Messaging, self).__init__(client)

    def list_messages(self, queries = None, search = None):
        """List messages"""

        
        api_path = '/messaging/messages'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_email(self, message_id, subject, content, topics = None, users = None, targets = None, cc = None, bcc = None, attachments = None, draft = None, html = None, scheduled_at = None):
        """Create email"""

        
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

    def update_email(self, message_id, topics = None, users = None, targets = None, subject = None, content = None, draft = None, html = None, cc = None, bcc = None, scheduled_at = None, attachments = None):
        """Update email"""

        
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

    def create_push(self, message_id, title, body, topics = None, users = None, targets = None, data = None, action = None, image = None, icon = None, sound = None, color = None, tag = None, badge = None, draft = None, scheduled_at = None):
        """Create push notification"""

        
        api_path = '/messaging/messages/push'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        if title is None:
            raise AppwriteException('Missing required parameter: "title"')

        if body is None:
            raise AppwriteException('Missing required parameter: "body"')


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

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_push(self, message_id, topics = None, users = None, targets = None, title = None, body = None, data = None, action = None, image = None, icon = None, sound = None, color = None, tag = None, badge = None, draft = None, scheduled_at = None):
        """Update push notification"""

        
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

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_sms(self, message_id, content, topics = None, users = None, targets = None, draft = None, scheduled_at = None):
        """Create SMS"""

        
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

    def update_sms(self, message_id, topics = None, users = None, targets = None, content = None, draft = None, scheduled_at = None):
        """Update SMS"""

        
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

    def get_message(self, message_id):
        """Get message"""

        
        api_path = '/messaging/messages/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, message_id):
        """Delete message"""

        
        api_path = '/messaging/messages/{messageId}'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_message_logs(self, message_id, queries = None):
        """List message logs"""

        
        api_path = '/messaging/messages/{messageId}/logs'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_targets(self, message_id, queries = None):
        """List message targets"""

        
        api_path = '/messaging/messages/{messageId}/targets'
        api_params = {}
        if message_id is None:
            raise AppwriteException('Missing required parameter: "message_id"')

        api_path = api_path.replace('{messageId}', message_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_providers(self, queries = None, search = None):
        """List providers"""

        
        api_path = '/messaging/providers'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_apns_provider(self, provider_id, name, auth_key = None, auth_key_id = None, team_id = None, bundle_id = None, sandbox = None, enabled = None):
        """Create APNS provider"""

        
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

    def update_apns_provider(self, provider_id, name = None, enabled = None, auth_key = None, auth_key_id = None, team_id = None, bundle_id = None, sandbox = None):
        """Update APNS provider"""

        
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

    def create_fcm_provider(self, provider_id, name, service_account_json = None, enabled = None):
        """Create FCM provider"""

        
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

    def update_fcm_provider(self, provider_id, name = None, enabled = None, service_account_json = None):
        """Update FCM provider"""

        
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

    def create_mailgun_provider(self, provider_id, name, api_key = None, domain = None, is_eu_region = None, from_name = None, from_email = None, reply_to_name = None, reply_to_email = None, enabled = None):
        """Create Mailgun provider"""

        
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

    def update_mailgun_provider(self, provider_id, name = None, api_key = None, domain = None, is_eu_region = None, enabled = None, from_name = None, from_email = None, reply_to_name = None, reply_to_email = None):
        """Update Mailgun provider"""

        
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

    def create_msg91_provider(self, provider_id, name, template_id = None, sender_id = None, auth_key = None, enabled = None):
        """Create Msg91 provider"""

        
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

    def update_msg91_provider(self, provider_id, name = None, enabled = None, template_id = None, sender_id = None, auth_key = None):
        """Update Msg91 provider"""

        
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

    def create_sendgrid_provider(self, provider_id, name, api_key = None, from_name = None, from_email = None, reply_to_name = None, reply_to_email = None, enabled = None):
        """Create Sendgrid provider"""

        
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

    def update_sendgrid_provider(self, provider_id, name = None, enabled = None, api_key = None, from_name = None, from_email = None, reply_to_name = None, reply_to_email = None):
        """Update Sendgrid provider"""

        
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

    def create_smtp_provider(self, provider_id, name, host, port = None, username = None, password = None, encryption = None, auto_tls = None, mailer = None, from_name = None, from_email = None, reply_to_name = None, reply_to_email = None, enabled = None):
        """Create SMTP provider"""

        
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

    def update_smtp_provider(self, provider_id, name = None, host = None, port = None, username = None, password = None, encryption = None, auto_tls = None, mailer = None, from_name = None, from_email = None, reply_to_name = None, reply_to_email = None, enabled = None):
        """Update SMTP provider"""

        
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

    def create_telesign_provider(self, provider_id, name, xfrom = None, customer_id = None, api_key = None, enabled = None):
        """Create Telesign provider"""

        
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

    def update_telesign_provider(self, provider_id, name = None, enabled = None, customer_id = None, api_key = None, xfrom = None):
        """Update Telesign provider"""

        
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

    def create_textmagic_provider(self, provider_id, name, xfrom = None, username = None, api_key = None, enabled = None):
        """Create Textmagic provider"""

        
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

    def update_textmagic_provider(self, provider_id, name = None, enabled = None, username = None, api_key = None, xfrom = None):
        """Update Textmagic provider"""

        
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

    def create_twilio_provider(self, provider_id, name, xfrom = None, account_sid = None, auth_token = None, enabled = None):
        """Create Twilio provider"""

        
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

    def update_twilio_provider(self, provider_id, name = None, enabled = None, account_sid = None, auth_token = None, xfrom = None):
        """Update Twilio provider"""

        
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

    def create_vonage_provider(self, provider_id, name, xfrom = None, api_key = None, api_secret = None, enabled = None):
        """Create Vonage provider"""

        
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

    def update_vonage_provider(self, provider_id, name = None, enabled = None, api_key = None, api_secret = None, xfrom = None):
        """Update Vonage provider"""

        
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

    def get_provider(self, provider_id):
        """Get provider"""

        
        api_path = '/messaging/providers/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_provider(self, provider_id):
        """Delete provider"""

        
        api_path = '/messaging/providers/{providerId}'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_provider_logs(self, provider_id, queries = None):
        """List provider logs"""

        
        api_path = '/messaging/providers/{providerId}/logs'
        api_params = {}
        if provider_id is None:
            raise AppwriteException('Missing required parameter: "provider_id"')

        api_path = api_path.replace('{providerId}', provider_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_subscriber_logs(self, subscriber_id, queries = None):
        """List subscriber logs"""

        
        api_path = '/messaging/subscribers/{subscriberId}/logs'
        api_params = {}
        if subscriber_id is None:
            raise AppwriteException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{subscriberId}', subscriber_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_topics(self, queries = None, search = None):
        """List topics"""

        
        api_path = '/messaging/topics'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_topic(self, topic_id, name, subscribe = None):
        """Create topic"""

        
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

    def get_topic(self, topic_id):
        """Get topic"""

        
        api_path = '/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', topic_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_topic(self, topic_id, name = None, subscribe = None):
        """Update topic"""

        
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

    def delete_topic(self, topic_id):
        """Delete topic"""

        
        api_path = '/messaging/topics/{topicId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', topic_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_topic_logs(self, topic_id, queries = None):
        """List topic logs"""

        
        api_path = '/messaging/topics/{topicId}/logs'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', topic_id)

        api_params['queries'] = queries

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_subscribers(self, topic_id, queries = None, search = None):
        """List subscribers"""

        
        api_path = '/messaging/topics/{topicId}/subscribers'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        api_path = api_path.replace('{topicId}', topic_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_subscriber(self, topic_id, subscriber_id, target_id):
        """Create subscriber"""

        
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

    def get_subscriber(self, topic_id, subscriber_id):
        """Get subscriber"""

        
        api_path = '/messaging/topics/{topicId}/subscribers/{subscriberId}'
        api_params = {}
        if topic_id is None:
            raise AppwriteException('Missing required parameter: "topic_id"')

        if subscriber_id is None:
            raise AppwriteException('Missing required parameter: "subscriber_id"')

        api_path = api_path.replace('{topicId}', topic_id)
        api_path = api_path.replace('{subscriberId}', subscriber_id)


        return self.client.call('get', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_subscriber(self, topic_id, subscriber_id):
        """Delete subscriber"""

        
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
