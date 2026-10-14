```python
from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.models import Session
from appwrite.enums.id_token_provider import IdTokenProvider

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

account = Account(client)

result: Session = account.create_id_token_session(
    provider = IdTokenProvider.APPLE,
    id_token = '<ID_TOKEN>',
    nonce = '<NONCE>', # optional
    access_token = '<ACCESS_TOKEN>', # optional
    access_token_expiry = 0, # optional
    name = '<NAME>' # optional
)

print(result.model_dump())
```
