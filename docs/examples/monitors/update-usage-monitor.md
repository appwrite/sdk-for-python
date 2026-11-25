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

result: Monitor = monitors.update_usage_monitor(
    monitor_id = '<MONITOR_ID>',
    name = '<NAME>', # optional
    rules = ["{\"method\":\"greaterThan\", \"attribute\":\"network.outbound\", \"values\":[5000000000]}"], # optional
    window = 60, # optional
    cooldown = 300, # optional
    enabled = False, # optional
    notify = ["owner"], # optional
    severity = MonitorSeverity.INFO, # optional
    escalation_id = '<ESCALATION_ID>' # optional
)

print(result.model_dump())
```
