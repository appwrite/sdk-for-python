```python
import asyncio

from appwrite.client import Client
from appwrite.services.sites import Sites
from appwrite.models import SpecificationList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    sites = Sites(client)

    result: SpecificationList = await sites.list_specifications(
        type = 'runtimes', # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
