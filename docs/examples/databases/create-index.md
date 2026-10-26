```python
import asyncio

from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import Index
from appwrite.enums.databases_index_type import DatabasesIndexType
from appwrite.enums.order_by import OrderBy


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    databases = Databases(client)

    result: Index = await databases.create_index(
        database_id = '<DATABASE_ID>',
        collection_id = '<COLLECTION_ID>',
        key = '<KEY>',
        type = DatabasesIndexType.KEY,
        attributes = ["username"],
        orders = [OrderBy.ASC], # optional
        lengths = [], # optional
        description = '<DESCRIPTION>' # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
