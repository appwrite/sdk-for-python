```python
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import AttributeFloat

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result: AttributeFloat = databases.update_float_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = '<KEY>',
    required = False,
    default = 10.5,
    min = 0, # optional
    max = 100, # optional
    new_key = '<NEW_KEY>' # optional
)

print(result.model_dump())
```
