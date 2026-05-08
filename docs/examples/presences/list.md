```python
from appwrite.client import Client
from appwrite.services.presences import Presences
from appwrite.models import PresenceList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

presences = Presences(client)

result: PresenceList = presences.list(
    queries = [], # optional
    total = False, # optional
    ttl = 0 # optional
)

print(result.model_dump())
```
