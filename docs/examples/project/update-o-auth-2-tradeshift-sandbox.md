```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Tradeshift

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: OAuth2Tradeshift = project.update_o_auth2_tradeshift_sandbox(
    oauth2_client_id = '<OAUTH2_CLIENT_ID>', # optional
    oauth2_client_secret = '<OAUTH2_CLIENT_SECRET>', # optional
    enabled = False # optional
)

print(result.model_dump())
```
