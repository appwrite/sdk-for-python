```python
import asyncio

from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB
from appwrite.models import VectorsdbCollection


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    vectors_db = VectorsDB(client)

    result: VectorsdbCollection = await vectors_db.get_collection(
        database_id = '<DATABASE_ID>',
        collection_id = '<COLLECTION_ID>'
    )

    print(result.model_dump())


asyncio.run(main())
```
