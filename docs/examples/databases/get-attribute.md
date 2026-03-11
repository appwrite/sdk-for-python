```python
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import AttributeBoolean
from appwrite.models import AttributeInteger
from appwrite.models import AttributeFloat
from appwrite.models import AttributeEmail
from appwrite.models import AttributeEnum
from appwrite.models import AttributeUrl
from appwrite.models import AttributeIp
from appwrite.models import AttributeDatetime
from appwrite.models import AttributeRelationship
from appwrite.models import AttributeString
from typing import Union

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result: Union[AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributeString] = databases.get_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = ''
)

print(result.model_dump())
```
