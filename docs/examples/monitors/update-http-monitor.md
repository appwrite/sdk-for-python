```python
from appwrite.client import Client
from appwrite.services.monitors import Monitors
from appwrite.models import Monitor
from appwrite.enums.monitor_method import MonitorMethod
from appwrite.enums.monitor_severity import MonitorSeverity
from appwrite.query import Query

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

monitors = Monitors(client)

result: Monitor = monitors.update_http_monitor(
    monitor_id = '<MONITOR_ID>',
    name = '<NAME>', # optional
    url = 'https://api.example.com/health', # optional
    method = MonitorMethod.GET, # optional
    headers = {
        "Authorization": "Bearer <TOKEN>"
    }, # optional
    body = '<BODY>', # optional
    rules = [
        Query.or_queries([
            Query.not_between('statusCode', 200, 299),
            Query.greater_than('latency', 2000)
        ])
    ], # optional
    interval = 60, # optional
    timeout = 10, # optional
    cooldown = 300, # optional
    enabled = True, # optional
    notify = ["owner"], # optional
    severity = MonitorSeverity.INFO, # optional
    escalation_id = '<ESCALATION_ID>' # optional
)

print(result.model_dump())
```
