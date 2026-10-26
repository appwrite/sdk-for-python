```python
import asyncio

from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Notion


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    project = Project(client)

    result: OAuth2Notion = await project.update_o_auth2_notion(
        oauth_client_id = '<OAUTH_CLIENT_ID>', # optional
        oauth_client_secret = '<OAUTH_CLIENT_SECRET>', # optional
        enabled = False # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
