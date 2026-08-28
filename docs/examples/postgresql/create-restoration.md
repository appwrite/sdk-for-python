```python
from appwrite.client import Client
from appwrite.services.postgresql import Postgresql
from appwrite.models import DedicatedDatabaseRestoration

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

postgresql = Postgresql(client)

result: DedicatedDatabaseRestoration = postgresql.create_restoration(
    database_id = '<DATABASE_ID>',
    type = 'backup', # optional
    backup_id = '<BACKUP_ID>', # optional
    target_database_id = '<TARGET_DATABASE_ID>', # optional
    target_time = '2020-10-15T06:38:00.000+00:00' # optional
)

print(result.model_dump())
```
