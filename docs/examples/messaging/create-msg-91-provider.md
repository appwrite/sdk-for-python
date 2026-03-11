```python
from appwrite.client import Client
from appwrite.services.messaging import Messaging
from appwrite.models import Provider

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

messaging = Messaging(client)

result: Provider = messaging.create_msg91_provider(
    provider_id = '<PROVIDER_ID>',
    name = '<NAME>',
    template_id = '<TEMPLATE_ID>', # optional
    sender_id = '<SENDER_ID>', # optional
    auth_key = '<AUTH_KEY>', # optional
    enabled = False # optional
)

print(result.model_dump())
```
