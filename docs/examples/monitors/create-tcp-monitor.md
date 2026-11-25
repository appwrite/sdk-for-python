```python
from appwrite.client import Client
from appwrite.services.monitors import Monitors
from appwrite.models import Monitor
from appwrite.enums.monitor_severity import MonitorSeverity

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

monitors = Monitors(client)

result: Monitor = monitors.create_tcp_monitor(
    monitor_id = '<MONITOR_ID>',
    name = '<NAME>',
    host = 'example.com',
    port = 443,
    rules = ["{\"method\":\"greaterThan\", \"attribute\":\"latency\", \"values\":[2000]}"], # optional
    interval = 1, # optional
    timeout = 1, # optional
    cooldown = 300, # optional
    enabled = False, # optional
    notify = [], # optional
    severity = MonitorSeverity.INFO, # optional
    escalation_id = '<ESCALATION_ID>' # optional
)

print(result.model_dump())
```
