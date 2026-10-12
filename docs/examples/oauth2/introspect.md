```python
from appwrite.client import Client
from appwrite.services.oauth2 import Oauth2
from appwrite.models import Oauth2Introspection

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

oauth2 = Oauth2(client)

result: Oauth2Introspection = oauth2.introspect(
    token = '<TOKEN>',
    token_type_hint = 'access_token', # optional
    client_id = '<CLIENT_ID>', # optional
    client_secret = '<CLIENT_SECRET>' # optional
)

print(result.model_dump())
```
