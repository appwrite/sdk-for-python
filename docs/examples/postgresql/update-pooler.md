```python
from appwrite.client import Client
from appwrite.services.postgresql import Postgresql
from appwrite.models import DedicatedDatabasePooler

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

postgresql = Postgresql(client)

result: DedicatedDatabasePooler = postgresql.update_pooler(
    database_id = '<DATABASE_ID>',
    mode = 'transaction', # optional
    max_connections = 10, # optional
    default_pool_size = 1, # optional
    read_write_splitting = False, # optional
    pooler_cpu_request = '<POOLER_CPU_REQUEST>', # optional
    pooler_cpu_limit = '<POOLER_CPU_LIMIT>', # optional
    pooler_memory_request = '<POOLER_MEMORY_REQUEST>', # optional
    pooler_memory_limit = '<POOLER_MEMORY_LIMIT>' # optional
)

print(result.model_dump())
```
