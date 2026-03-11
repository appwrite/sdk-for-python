```python
from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.models import User

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

account = Account(client)

result: User = account.update_name(
    name = '<NAME>'
)

print(result.model_dump())
```
