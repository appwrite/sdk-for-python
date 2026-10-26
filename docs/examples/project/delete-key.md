```python
import asyncio

from appwrite.client import Client
from appwrite.services.project import Project


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    project = Project(client)

    result = await project.delete_key(
        key_id = '<KEY_ID>'
    )


asyncio.run(main())
```
