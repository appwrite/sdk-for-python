```python
from appwrite.client import Client
from appwrite.services.messaging import Messaging
from appwrite.models import Provider

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

messaging = Messaging(client)

result: Provider = messaging.update_ses_provider(
    provider_id = '<PROVIDER_ID>',
    name = '<NAME>', # optional
    enabled = False, # optional
    access_key = '<ACCESS_KEY>', # optional
    secret_key = '<SECRET_KEY>', # optional
    region = '<REGION>', # optional
    from_name = '<FROM_NAME>', # optional
    from_email = 'email@example.com', # optional
    reply_to_name = '<REPLY_TO_NAME>', # optional
    reply_to_email = '<REPLY_TO_EMAIL>' # optional
)

print(result.model_dump())
```
