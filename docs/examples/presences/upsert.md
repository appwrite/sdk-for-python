```python
from appwrite.client import Client
from appwrite.services.presences import Presences
from appwrite.models import Presence
from appwrite.permission import Permission
from appwrite.role import Role

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

presences = Presences(client)

result: Presence = presences.upsert(
    presence_id = '<PRESENCE_ID>',
    user_id = '<USER_ID>',
    status = '<STATUS>',
    permissions = [Permission.read(Role.any())], # optional
    expires_at = '2020-10-15T06:38:00.000+00:00', # optional
    metadata = {} # optional
)

print(result.model_dump())
```
