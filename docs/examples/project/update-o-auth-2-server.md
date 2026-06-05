```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Project as ProjectModel

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: ProjectModel = project.update_o_auth2_server(
    enabled = False,
    authorization_url = 'https://example.com',
    scopes = [], # optional
    access_token_duration = 60, # optional
    refresh_token_duration = 60, # optional
    public_access_token_duration = 60, # optional
    public_refresh_token_duration = 60, # optional
    confidential_pkce = False # optional
)

print(result.model_dump())
```
