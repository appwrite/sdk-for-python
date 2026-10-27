```python
from appwrite.client import Client
from appwrite.services.migrations import Migrations
from appwrite.models import MigrationReport
from appwrite.enums.n_host_migration_resource import NHostMigrationResource

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

migrations = Migrations(client)

result: MigrationReport = migrations.get_n_host_report(
    resources = [NHostMigrationResource.USER],
    subdomain = '<SUBDOMAIN>',
    region = '<REGION>',
    admin_secret = '<ADMIN_SECRET>',
    database = '<DATABASE>',
    username = '<USERNAME>',
    password = 'password',
    port = 5432 # optional
)

print(result.model_dump())
```
