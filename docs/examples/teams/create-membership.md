```python
import asyncio

from appwrite.client import Client
from appwrite.services.teams import Teams
from appwrite.models import Membership


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    teams = Teams(client)

    result: Membership = await teams.create_membership(
        team_id = '<TEAM_ID>',
        roles = ["editor"],
        email = 'email@example.com', # optional
        user_id = '<USER_ID>', # optional
        phone = '+12065550100', # optional
        url = 'https://example.com', # optional
        name = '<NAME>', # optional
        membership_id = '<MEMBERSHIP_ID>' # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
