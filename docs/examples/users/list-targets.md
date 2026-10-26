```python
import asyncio

from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.models import TargetList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    users = Users(client)

    result: TargetList = await users.list_targets(
        user_id = '<USER_ID>',
        queries = [], # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
