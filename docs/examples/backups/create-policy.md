```python
from appwrite.client import Client
from appwrite.services.backups import Backups
from appwrite.enums import BackupServices

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

backups = Backups(client)

result = backups.create_policy(
    policy_id = '<POLICY_ID>',
    services = [BackupServices.DATABASES],
    retention = 1,
    schedule = '',
    name = '<NAME>', # optional
    resource_id = '<RESOURCE_ID>', # optional
    enabled = False # optional
)
```
