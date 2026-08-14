```python
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.models import DatabaseMigrationList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tables_db = TablesDB(client)

result: DatabaseMigrationList = tables_db.list_migrations(
    database_id = '<DATABASE_ID>'
)

print(result.model_dump())
```
