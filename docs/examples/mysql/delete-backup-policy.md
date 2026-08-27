```python
from appwrite.client import Client
from appwrite.services.mysql import Mysql

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

mysql = Mysql(client)

result = mysql.delete_backup_policy(
    database_id = '<DATABASE_ID>',
    policy_id = '<POLICY_ID>'
)
```
