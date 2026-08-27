```python
from appwrite.client import Client
from appwrite.services.mongo import Mongo
from appwrite.models import DedicatedDatabaseBackupList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

mongo = Mongo(client)

result: DedicatedDatabaseBackupList = mongo.list_backups(
    database_id = '<DATABASE_ID>',
    queries = [] # optional
)

print(result.model_dump())
```
