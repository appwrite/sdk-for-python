```python
import asyncio

from appwrite.client import Client
from appwrite.services.tables_db import TablesDB


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_session('') # The user session to authenticate with

    tables_db = TablesDB(client)

    result = await tables_db.delete_row(
        database_id = '<DATABASE_ID>',
        table_id = '<TABLE_ID>',
        row_id = '<ROW_ID>',
        transaction_id = '<TRANSACTION_ID>' # optional
    )


asyncio.run(main())
```
