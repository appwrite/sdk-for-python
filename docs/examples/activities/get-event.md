```python
from appwrite.client import Client
from appwrite.services.activities import Activities

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

activities = Activities(client)

result = activities.get_event(
    event_id = '<EVENT_ID>'
)
```
