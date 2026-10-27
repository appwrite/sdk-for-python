```python
from appwrite.client import Client
from appwrite.services.migrations import Migrations
from appwrite.models import MigrationReport
from appwrite.enums.firebase_migration_resource import FirebaseMigrationResource

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

migrations = Migrations(client)

result: MigrationReport = migrations.get_firebase_report(
    resources = [FirebaseMigrationResource.USER],
    service_account = '<SERVICE_ACCOUNT>'
)

print(result.model_dump())
```
