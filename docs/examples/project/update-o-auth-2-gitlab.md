```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Gitlab

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: OAuth2Gitlab = project.update_o_auth2_gitlab(
    application_id = '<APPLICATION_ID>', # optional
    secret = '<SECRET>', # optional
    endpoint = 'https://example.com', # optional
    enabled = False # optional
)

print(result.model_dump())
```
