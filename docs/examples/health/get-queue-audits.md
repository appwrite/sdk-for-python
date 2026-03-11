```python
from appwrite.client import Client
from appwrite.services.health import Health
from appwrite.models import HealthQueue

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

health = Health(client)

result: HealthQueue = health.get_queue_audits(
    threshold = None # optional
)

print(result.model_dump())
```
