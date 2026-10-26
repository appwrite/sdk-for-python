```python
import asyncio

from appwrite.client import Client
from appwrite.services.domains import Domains
from appwrite.models import DomainsList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    domains = Domains(client)

    result: DomainsList = await domains.list(
        queries = [], # optional
        search = '<SEARCH>', # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
