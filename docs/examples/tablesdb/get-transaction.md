```python
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.models import Transaction

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tables_db = TablesDB(client)

result: Transaction = tables_db.get_transaction(
    transaction_id = '<TRANSACTION_ID>'
)

print(result.model_dump())
```
