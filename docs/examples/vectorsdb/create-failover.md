```python
import asyncio

from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB
from appwrite.models import DedicatedDatabase


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    vectors_db = VectorsDB(client)

    result: DedicatedDatabase = await vectors_db.create_failover(
        database_id = '<DATABASE_ID>',
        target_replica_id = '<TARGET_REPLICA_ID>' # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
