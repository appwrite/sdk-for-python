```python
from appwrite.client import Client
from appwrite.services.documents_db import DocumentsDB
from appwrite.models import Collection
from appwrite.permission import Permission
from appwrite.role import Role

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

documents_db = DocumentsDB(client)

result: Collection = documents_db.create_collection(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    name = '<NAME>',
    permissions = [Permission.read(Role.any())], # optional
    document_security = False, # optional
    enabled = False, # optional
    attributes = [], # optional
    indexes = [] # optional
)

print(result.model_dump())
```
