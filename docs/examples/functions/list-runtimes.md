```python
import asyncio

from appwrite.client import Client
from appwrite.services.functions import Functions
from appwrite.models import RuntimeList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    functions = Functions(client)

    result: RuntimeList = await functions.list_runtimes(
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
