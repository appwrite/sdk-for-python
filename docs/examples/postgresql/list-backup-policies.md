```python
from appwrite.client import Client
from appwrite.services.postgresql import Postgresql
from appwrite.models import BackupPolicyList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

postgresql = Postgresql(client)

result: BackupPolicyList = postgresql.list_backup_policies(
    database_id = '<DATABASE_ID>',
    queries = [] # optional
)

print(result.model_dump())
```
