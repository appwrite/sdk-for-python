```python
from appwrite.client import Client
from appwrite.services.waf import Waf

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

waf = Waf(client)

result = waf.delete_rule(
    rule_id = '<RULE_ID>'
)
```
