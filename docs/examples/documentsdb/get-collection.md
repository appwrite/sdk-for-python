```python
from appwrite.client import Client
from appwrite.services.documents_db import DocumentsDB
from appwrite.models import Collection

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

documents_db = DocumentsDB(client)

result: Collection = documents_db.get_collection(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>'
)

print(result.model_dump())
```
