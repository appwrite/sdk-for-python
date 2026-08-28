```python
from appwrite.client import Client
from appwrite.services.mysql import Mysql
from appwrite.models import DedicatedDatabaseRestorationList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

mysql = Mysql(client)

result: DedicatedDatabaseRestorationList = mysql.list_restorations(
    database_id = '<DATABASE_ID>',
    status = 'pending', # optional
    type = 'backup', # optional
    limit = 1, # optional
    offset = 0 # optional
)

print(result.model_dump())
```
