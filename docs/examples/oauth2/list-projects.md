```python
from appwrite.client import Client
from appwrite.services.oauth2 import Oauth2
from appwrite.models import Oauth2ProjectList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_session('') # The user session to authenticate with
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

oauth2 = Oauth2(client)

result: Oauth2ProjectList = oauth2.list_projects(
    limit = 1, # optional
    offset = 0, # optional
    search = '<SEARCH>' # optional
)

print(result.model_dump())
```
