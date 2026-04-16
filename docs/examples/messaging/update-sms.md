```python
from appwrite.client import Client
from appwrite.services.messaging import Messaging
from appwrite.models import Message

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

messaging = Messaging(client)

result: Message = messaging.update_sms(
    message_id = '<MESSAGE_ID>',
    topics = [], # optional
    users = [], # optional
    targets = [], # optional
    content = '<CONTENT>', # optional
    draft = False, # optional
    scheduled_at = '2020-10-15T06:38:00.000+00:00' # optional
)

print(result.model_dump())
```
