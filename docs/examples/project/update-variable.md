```python
import asyncio

from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Variable


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    project = Project(client)

    result: Variable = await project.update_variable(
        variable_id = '<VARIABLE_ID>',
        key = '<KEY>', # optional
        value = '<VALUE>', # optional
        secret = False, # optional
        description = '<DESCRIPTION>' # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
