```python
import asyncio

from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    vectors_db = VectorsDB(client)

    result = await vectors_db.delete_document(
        database_id = '<DATABASE_ID>',
        collection_id = '<COLLECTION_ID>',
        document_id = '<DOCUMENT_ID>',
        transaction_id = '<TRANSACTION_ID>' # optional
    )


asyncio.run(main())
```
