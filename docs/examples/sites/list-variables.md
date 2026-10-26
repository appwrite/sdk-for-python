```python
import asyncio

from appwrite.client import Client
from appwrite.services.sites import Sites
from appwrite.models import VariableList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    sites = Sites(client)

    result: VariableList = await sites.list_variables(
        site_id = '<SITE_ID>',
        queries = [], # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
