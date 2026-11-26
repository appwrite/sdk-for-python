```python
from appwrite.client import Client
from appwrite.services.monitors import Monitors

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

monitors = Monitors(client)

result = monitors.delete(
    monitor_id = '<MONITOR_ID>'
)
```
