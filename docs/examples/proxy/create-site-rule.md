```python
from appwrite.client import Client
from appwrite.services.proxy import Proxy
from appwrite.models import ProxyRule

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

proxy = Proxy(client)

result: ProxyRule = proxy.create_site_rule(
    domain = '',
    site_id = '<SITE_ID>',
    branch = '<BRANCH>' # optional
)

print(result.model_dump())
```
