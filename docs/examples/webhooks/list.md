```python
import asyncio

from appwrite.client import Client
from appwrite.services.webhooks import Webhooks
from appwrite.models import WebhookList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    webhooks = Webhooks(client)

    result: WebhookList = await webhooks.list(
        queries = [], # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
