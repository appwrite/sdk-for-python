```python
from appwrite.client import Client
from appwrite.services.webhooks import Webhooks
from appwrite.models import Webhook

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

webhooks = Webhooks(client)

result: Webhook = webhooks.update(
    webhook_id = '<WEBHOOK_ID>',
    name = '<NAME>',
    url = '',
    events = [],
    enabled = False, # optional
    security = False, # optional
    http_user = '<HTTP_USER>', # optional
    http_pass = '<HTTP_PASS>' # optional
)

print(result.model_dump())
```
