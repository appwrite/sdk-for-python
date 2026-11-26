```python
from appwrite.client import Client
from appwrite.services.alerts import Alerts
from appwrite.models import AlertList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

alerts = Alerts(client)

result: AlertList = alerts.list(
    queries = [], # optional
    total = False # optional
)

print(result.model_dump())
```
