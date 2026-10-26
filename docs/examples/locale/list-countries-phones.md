```python
import asyncio

from appwrite.client import Client
from appwrite.services.locale import Locale
from appwrite.models import PhoneList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    locale = Locale(client)

    result: PhoneList = await locale.list_countries_phones(
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
