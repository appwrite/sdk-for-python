```python
import asyncio

from appwrite.client import Client
from appwrite.services.oauth2 import Oauth2


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    oauth2 = Oauth2(client)

    result = await oauth2.revoke(
        token = '<TOKEN>',
        token_type_hint = 'access_token', # optional
        client_id = '<CLIENT_ID>', # optional
        client_secret = '<CLIENT_SECRET>' # optional
    )


asyncio.run(main())
```
