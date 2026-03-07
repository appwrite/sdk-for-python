```python
from appwrite.client import Client
from appwrite.services.backups import Backups
from appwrite.models import BackupArchive
from appwrite.enums import BackupServices

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

backups = Backups(client)

result: BackupArchive = backups.create_archive(
    services = [BackupServices.DATABASES],
    resource_id = '<RESOURCE_ID>' # optional
)

print(result.model_dump())
```
