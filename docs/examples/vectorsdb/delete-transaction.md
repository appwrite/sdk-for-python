```python
import asyncio

from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    vectors_db = VectorsDB(client)

    result = await vectors_db.delete_transaction(
        transaction_id = '<TRANSACTION_ID>'
    )


asyncio.run(main())
```
