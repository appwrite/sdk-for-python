```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Zoho
from appwrite.enums.project_o_auth2_zoho_prompt import ProjectOAuth2ZohoPrompt

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: OAuth2Zoho = project.update_o_auth2_zoho(
    client_id = '<CLIENT_ID>', # optional
    client_secret = '<CLIENT_SECRET>', # optional
    prompt = [ProjectOAuth2ZohoPrompt.CONSENT], # optional
    enabled = False # optional
)

print(result.model_dump())
```
