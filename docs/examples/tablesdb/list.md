```python
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.models import DatabaseList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tables_db = TablesDB(client)

result: DatabaseList = tables_db.list(
    queries = [], # optional
    search = '<SEARCH>', # optional
    total = False # optional
)

print(result.model_dump())
```
