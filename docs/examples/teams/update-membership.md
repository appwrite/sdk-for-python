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

    result: Membership = await teams.update_membership(
        team_id = '<TEAM_ID>',
        membership_id = '<MEMBERSHIP_ID>',
        roles = ["editor"]
    )

    print(result.model_dump())


asyncio.run(main())
```
