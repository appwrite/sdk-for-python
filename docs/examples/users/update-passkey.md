```python
from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.models import Passkey

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

users = Users(client)

result: Passkey = users.update_passkey(
    user_id = '<USER_ID>',
    passkey_id = '<PASSKEY_ID>',
    name = '<NAME>'
)

print(result.model_dump())
```
