```python
from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB
from appwrite.models import DocumentList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

vectors_db = VectorsDB(client)

result: DocumentList = vectors_db.list_documents(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    queries = [], # optional
    transaction_id = '<TRANSACTION_ID>', # optional
    total = False, # optional
    ttl = 0 # optional
)

print(result.model_dump())
```
