```python
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.models import TransactionList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = Databases(client)

result: TransactionList = databases.list_transactions(
    queries = [] # optional
)

print(result.model_dump())
```
