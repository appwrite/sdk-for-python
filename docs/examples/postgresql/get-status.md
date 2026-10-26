```python
import asyncio

from appwrite.client import Client
from appwrite.services.postgresql import Postgresql
from appwrite.models import DatabaseStatus


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    postgresql = Postgresql(client)

    result: DatabaseStatus = await postgresql.get_status(
        database_id = '<DATABASE_ID>'
    )

    print(result.model_dump())


asyncio.run(main())
```
