```python
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.models import Row

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

tables_db = TablesDB(client)

result: Row = tables_db.get_row(
    database_id = '<DATABASE_ID>',
    table_id = '<TABLE_ID>',
    row_id = '<ROW_ID>',
    queries = [], # optional
    transaction_id = '<TRANSACTION_ID>' # optional
)

print(result.model_dump())
```
