```python
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import AttributeText

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result: AttributeText = databases.update_text_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = '',
    required = False,
    default = '<DEFAULT>',
    new_key = '' # optional
)

print(result.model_dump())
```
