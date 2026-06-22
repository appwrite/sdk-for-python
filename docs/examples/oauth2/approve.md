```python
from appwrite.client import Client
from appwrite.services.oauth2 import Oauth2
from appwrite.models import Oauth2Approve

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_session('') # The user session to authenticate with
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

oauth2 = Oauth2(client)

result: Oauth2Approve = oauth2.approve(
    grant_id = '<GRANT_ID>',
    authorization_details = '<AUTHORIZATION_DETAILS>' # optional
)

print(result.model_dump())
```
