```python
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB
from appwrite.models import ColumnBoolean
from appwrite.models import ColumnInteger
from appwrite.models import ColumnFloat
from appwrite.models import ColumnEmail
from appwrite.models import ColumnEnum
from appwrite.models import ColumnUrl
from appwrite.models import ColumnIp
from appwrite.models import ColumnDatetime
from appwrite.models import ColumnRelationship
from appwrite.models import ColumnString
from typing import Union

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tables_db = TablesDB(client)

result: Union[ColumnBoolean, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnString] = tables_db.get_column(
    database_id = '<DATABASE_ID>',
    table_id = '<TABLE_ID>',
    key = ''
)

print(result.model_dump())
```
