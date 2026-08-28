```python
from appwrite.client import Client
from appwrite.services.documents_db import DocumentsDB
from appwrite.models import Transaction

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

documents_db = DocumentsDB(client)

result: Transaction = documents_db.create_transaction(
    ttl = 60 # optional
)

print(result.model_dump())
```
