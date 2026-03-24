```python
from appwrite.client import Client
from appwrite.services.documents_db import DocumentsDB
from appwrite.models import Index
from appwrite.enums import DocumentsDBIndexType
from appwrite.enums import OrderBy

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

documents_db = DocumentsDB(client)

result: Index = documents_db.create_index(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = '',
    type = DocumentsDBIndexType.KEY,
    attributes = [],
    orders = [OrderBy.ASC], # optional
    lengths = [] # optional
)

print(result.model_dump())
```
