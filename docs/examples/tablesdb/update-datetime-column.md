```python
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.models import ColumnDatetime

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tables_db = TablesDB(client)

result: ColumnDatetime = tables_db.update_datetime_column(
    database_id = '<DATABASE_ID>',
    table_id = '<TABLE_ID>',
    key = '',
    required = False,
    default = '2020-10-15T06:38:00.000+00:00',
    new_key = '' # optional
)

print(result.model_dump())
```
