```python
from appwrite.client import Client
from appwrite.services.messaging import Messaging
from appwrite.models import Provider

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

messaging = Messaging(client)

result: Provider = messaging.update_vonage_provider(
    provider_id = '<PROVIDER_ID>',
    name = '<NAME>', # optional
    enabled = False, # optional
    api_key = '<API_KEY>', # optional
    api_secret = '<API_SECRET>', # optional
    from = '<FROM>' # optional
)

print(result.model_dump())
```
