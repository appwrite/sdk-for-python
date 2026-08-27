```python
from appwrite.client import Client
from appwrite.services.mysql import Mysql
from appwrite.models import DedicatedDatabase

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

mysql = Mysql(client)

result: DedicatedDatabase = mysql.create_branch(
    database_id = '<DATABASE_ID>',
    branch_id = '<BRANCH_ID>', # optional
    ttl = 300 # optional
)

print(result.model_dump())
```
