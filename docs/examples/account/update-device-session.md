```python
from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.models import Session

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

account = Account(client)

result: Session = account.update_device_session(
    device_id = '<DEVICE_ID>',
    session_id = '<SESSION_ID>'
)

print(result.model_dump())
```
