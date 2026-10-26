```python
import asyncio

from appwrite.client import Client
from appwrite.services.postgresql import Postgresql
from appwrite.models import DedicatedDatabaseBackupList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    postgresql = Postgresql(client)

    result: DedicatedDatabaseBackupList = await postgresql.list_backups(
        database_id = '<DATABASE_ID>',
        queries = [], # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
