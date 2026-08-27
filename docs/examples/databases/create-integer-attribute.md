```python
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import AttributeInteger

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result: AttributeInteger = databases.create_integer_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = '<KEY>',
    required = False,
    min = 0, # optional
    max = 100, # optional
    default = 10, # optional
    array = False # optional
)

print(result.model_dump())
```
