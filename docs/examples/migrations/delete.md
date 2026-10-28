```python
from appwrite.client import Client
from appwrite.services.migrations import Migrations

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

migrations = Migrations(client)

result = migrations.delete(
    migration_id = '<MIGRATION_ID>'
)
```
