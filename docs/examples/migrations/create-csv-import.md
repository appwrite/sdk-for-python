```python
from appwrite.client import Client
from appwrite.services.migrations import Migrations
from appwrite.models import Migration
from appwrite.enums.on_duplicate import OnDuplicate

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

migrations = Migrations(client)

result: Migration = migrations.create_csv_import(
    bucket_id = '<BUCKET_ID>',
    file_id = '<FILE_ID>',
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    internal_file = False, # optional
    on_duplicate = OnDuplicate.FAIL # optional
)

print(result.model_dump())
```
