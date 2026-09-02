```python
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.models import DatabaseMigration

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tables_db = TablesDB(client)

result: DatabaseMigration = tables_db.create_cutover(
    database_id = '<DATABASE_ID>',
    migration_id = '<MIGRATION_ID>'
)

print(result.model_dump())
```
