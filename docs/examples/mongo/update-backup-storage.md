```python
from appwrite.client import Client
from appwrite.services.mongo import Mongo
from appwrite.models import DedicatedDatabaseBackupStorage

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

mongo = Mongo(client)

result: DedicatedDatabaseBackupStorage = mongo.update_backup_storage(
    database_id = '<DATABASE_ID>',
    provider = 's3',
    bucket = '<BUCKET>',
    access_key = '<ACCESS_KEY>',
    secret_key = '<SECRET_KEY>',
    region = '<REGION>', # optional
    prefix = '<PREFIX>', # optional
    endpoint = '<ENDPOINT>' # optional
)

print(result.model_dump())
```
