```python
import asyncio

from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import CollectionList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    databases = Databases(client)

    result: CollectionList = await databases.list_collections(
        database_id = '<DATABASE_ID>',
        queries = [], # optional
        search = '<SEARCH>', # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
