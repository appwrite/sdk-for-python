```python
from appwrite.client import Client
from appwrite.services.mysql import Mysql
from appwrite.models import DedicatedDatabase

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

mysql = Mysql(client)

result: DedicatedDatabase = mysql.create(
    database_id = '<DATABASE_ID>',
    name = '<NAME>',
    version = '17', # optional
    specification = '<SPECIFICATION>', # optional
    replicas = 0, # optional
    sync_mode = 'async', # optional
    network_idle_timeout_seconds = 60, # optional
    network_ip_allowlist = [], # optional
    idle_timeout_minutes = 5, # optional
    pitr = False, # optional
    pitr_retention_days = 1, # optional
    storage_autoscaling = False, # optional
    storage_autoscaling_threshold_percent = 50, # optional
    storage_autoscaling_max_gb = 0 # optional
)

print(result.model_dump())
```
