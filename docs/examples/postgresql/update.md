```python
from appwrite.client import Client
from appwrite.services.postgresql import Postgresql
from appwrite.models import DedicatedDatabase

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

postgresql = Postgresql(client)

result: DedicatedDatabase = postgresql.update(
    database_id = '<DATABASE_ID>',
    name = '<NAME>', # optional
    status = 'ready', # optional
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
    storage_autoscaling_max_gb = 0, # optional
    metrics_trace_sample_rate = None, # optional
    metrics_slow_query_log_threshold_ms = 0, # optional
    sql_api_enabled = False, # optional
    sql_api_allowed_statements = [], # optional
    sql_api_max_rows = 1, # optional
    sql_api_max_bytes = 1024, # optional
    sql_api_timeout_seconds = 1 # optional
)

print(result.model_dump())
```
