```python
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import AttributeMediumtext

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result: AttributeMediumtext = databases.create_mediumtext_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = '',
    required = False,
    default = '<DEFAULT>', # optional
    array = False, # optional
    encrypt = False # optional
)

print(result.model_dump())
```
