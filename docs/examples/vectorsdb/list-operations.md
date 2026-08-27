```python
from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB
from appwrite.models import DedicatedDatabaseOperationList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

vectors_db = VectorsDB(client)

result: DedicatedDatabaseOperationList = vectors_db.list_operations(
    database_id = '<DATABASE_ID>',
    status = 'queued', # optional
    limit = 1, # optional
    offset = 0 # optional
)

print(result.model_dump())
```
