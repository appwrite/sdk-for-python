```python
import asyncio

from appwrite.client import Client
from appwrite.services.avatars import Avatars
from appwrite.input_file import InputFile
from appwrite.models import Account


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    avatars = Avatars(client)

    result: Account = await avatars.update_photo(
        file = InputFile.from_path('file.png')
    )

    print(result.model_dump())


asyncio.run(main())
```
