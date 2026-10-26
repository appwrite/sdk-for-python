```python
import asyncio

from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import AttributeRelationship
from appwrite.enums.relation_mutate import RelationMutate


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    databases = Databases(client)

    result: AttributeRelationship = await databases.update_relationship_attribute(
        database_id = '<DATABASE_ID>',
        collection_id = '<COLLECTION_ID>',
        key = '<KEY>',
        on_delete = RelationMutate.CASCADE, # optional
        new_key = '<NEW_KEY>', # optional
        description = '<DESCRIPTION>' # optional
    )

    print(result.model_dump())


asyncio.run(main())
```
