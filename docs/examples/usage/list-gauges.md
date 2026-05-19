```python
from appwrite.client import Client
from appwrite.services.usage import Usage
from appwrite.models import UsageGaugeList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

usage = Usage(client)

result: UsageGaugeList = usage.list_gauges(
    queries = [], # optional
    total = False # optional
)

print(result.model_dump())
```
