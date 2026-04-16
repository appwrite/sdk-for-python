```python
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import AttributeDatetime

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result: AttributeDatetime = databases.create_datetime_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = '',
    required = False,
    default = '2020-10-15T06:38:00.000+00:00', # optional
    array = False # optional
)

print(result.model_dump())
```
