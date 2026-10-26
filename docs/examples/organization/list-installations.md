```python
import asyncio

from appwrite.client import Client
from appwrite.services.organization import Organization
from appwrite.models import AppInstallationList


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    organization = Organization(client)

    result: AppInstallationList = await organization.list_installations(
        queries = [], # optional
        total = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
