```python
import asyncio

from appwrite.client import Client
from appwrite.services.proxy import Proxy
from appwrite.models import ProxyRuleList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    proxy = Proxy(client)

    result: ProxyRuleList = await proxy.list_rules(
        queries = [], # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
