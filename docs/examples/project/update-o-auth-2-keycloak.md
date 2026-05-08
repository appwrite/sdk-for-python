```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Keycloak

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: OAuth2Keycloak = project.update_o_auth2_keycloak(
    client_id = '<CLIENT_ID>', # optional
    client_secret = '<CLIENT_SECRET>', # optional
    endpoint = '<ENDPOINT>', # optional
    realm_name = '<REALM_NAME>', # optional
    enabled = False # optional
)

print(result.model_dump())
```
