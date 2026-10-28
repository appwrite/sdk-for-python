```python
from appwrite.client import Client
from appwrite.services.migrations import Migrations
from appwrite.models import Migration
from appwrite.enums.appwrite_migration_resource import AppwriteMigrationResource
from appwrite.enums.on_duplicate import OnDuplicate

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

migrations = Migrations(client)

result: Migration = migrations.create_appwrite_migration(
    resources = [AppwriteMigrationResource.USER],
    endpoint = 'https://example.com',
    project_id = '<PROJECT_ID>',
    api_key = '<API_KEY>',
    on_duplicate = OnDuplicate.FAIL # optional
)

print(result.model_dump())
```
