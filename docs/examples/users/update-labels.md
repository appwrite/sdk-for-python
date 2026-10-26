```python
import asyncio

from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.models import User


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    users = Users(client)

    result: User = await users.update_labels(
        user_id = '<USER_ID>',
        labels = ["subscriber"]
    )

    print(result.model_dump())


asyncio.run(main())
```
