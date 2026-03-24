```python
from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB
from appwrite.models import DocumentList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

vectors_db = VectorsDB(client)

result: DocumentList = vectors_db.upsert_documents(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    documents = [],
    transaction_id = '<TRANSACTION_ID>' # optional
)

print(result.model_dump())
```
