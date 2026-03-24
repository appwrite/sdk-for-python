```python
from appwrite.client import Client
from appwrite.services.documents_db import DocumentsDB
from appwrite.models import Document

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

documents_db = DocumentsDB(client)

result: Document = documents_db.increment_document_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    document_id = '<DOCUMENT_ID>',
    attribute = '',
    value = None, # optional
    max = None, # optional
    transaction_id = '<TRANSACTION_ID>' # optional
)

print(result.model_dump())
```
