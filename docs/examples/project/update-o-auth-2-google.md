```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import OAuth2Google
from appwrite.enums.project_o_auth2_google_prompt import ProjectOAuth2GooglePrompt

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: OAuth2Google = project.update_o_auth2_google(
    client_id = '<CLIENT_ID>', # optional
    client_secret = '<CLIENT_SECRET>', # optional
    prompt = [ProjectOAuth2GooglePrompt.NONE], # optional
    native_client_ids = [], # optional
    enabled = False, # optional
    native_enabled = False # optional
)

print(result.model_dump())
```
