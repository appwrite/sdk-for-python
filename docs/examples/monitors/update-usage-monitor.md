```python
from appwrite.client import Client
from appwrite.services.monitors import Monitors
from appwrite.models import Monitor
from appwrite.enums.monitor_severity import MonitorSeverity
from appwrite.query import Query

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

monitors = Monitors(client)

result: Monitor = monitors.update_usage_monitor(
    monitor_id = '<MONITOR_ID>',
    name = '<NAME>', # optional
    rules = [
        Query.greater_than('network.outbound', 5000000000)
    ], # optional
    window = 3600, # optional
    cooldown = 1800, # optional
    enabled = True, # optional
    notify = ["owner"], # optional
    severity = MonitorSeverity.INFO, # optional
    escalation_id = '<ESCALATION_ID>' # optional
)

print(result.model_dump())
```
