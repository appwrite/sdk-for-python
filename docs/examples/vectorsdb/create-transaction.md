```python
from appwrite.client import Client
from appwrite.services.vectors_db import VectorsDB
from appwrite.models import Transaction

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

vectors_db = VectorsDB(client)

result: Transaction = vectors_db.create_transaction(
    ttl = 60 # optional
)

print(result.model_dump())
```
