```python
from appwrite.client import Client
from appwrite.services.oauth2 import Oauth2

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_session('') # The user session to authenticate with
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

oauth2 = Oauth2(client)

result = oauth2.revoke(
    token = '<TOKEN>',
    token_type_hint = 'access_token', # optional
    client_id = '<CLIENT_ID>', # optional
    client_secret = '<CLIENT_SECRET>' # optional
)
```
