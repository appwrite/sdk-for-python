```python
from appwrite.client import Client
from appwrite.services.presences import Presences

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

presences = Presences(client)

result = presences.delete(
    presence_id = '<PRESENCE_ID>'
)
```
