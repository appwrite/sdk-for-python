```python
from appwrite.client import Client
from appwrite.services.documents_db import DocumentsDB
from appwrite.models import DocumentList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

documents_db = DocumentsDB(client)

result: DocumentList = documents_db.create_documents(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    documents = []
)

print(result.model_dump())
```
