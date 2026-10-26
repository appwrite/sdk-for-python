```python
import asyncio

from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.models import FileList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    storage = Storage(client)

    result: FileList = await storage.list_files(
        bucket_id = '<BUCKET_ID>',
        queries = [], # optional
        search = '<SEARCH>', # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
