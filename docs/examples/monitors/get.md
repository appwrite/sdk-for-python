```python
from appwrite.client import Client
from appwrite.services.monitors import Monitors
from appwrite.models import Monitor

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

monitors = Monitors(client)

result: Monitor = monitors.get(
    monitor_id = '<MONITOR_ID>'
)

print(result.model_dump())
```
