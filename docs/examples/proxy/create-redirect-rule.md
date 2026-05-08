```python
from appwrite.client import Client
from appwrite.services.proxy import Proxy
from appwrite.models import ProxyRule
from appwrite.enums import StatusCode
from appwrite.enums import ProxyResourceType

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

proxy = Proxy(client)

result: ProxyRule = proxy.create_redirect_rule(
    domain = '',
    url = 'https://example.com',
    status_code = StatusCode.MOVED_PERMANENTLY_301,
    resource_id = '<RESOURCE_ID>',
    resource_type = ProxyResourceType.SITE
)

print(result.model_dump())
```
