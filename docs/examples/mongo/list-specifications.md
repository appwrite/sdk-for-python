```python
import asyncio

from appwrite.client import Client
from appwrite.services.mongo import Mongo
from appwrite.models import DedicatedDatabaseSpecificationList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    mongo = Mongo(client)

    result: DedicatedDatabaseSpecificationList = await mongo.list_specifications()

    print(result.model_dump())


asyncio.run(main())
```
