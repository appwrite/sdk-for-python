```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Project as ProjectModel

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: ProjectModel = project.update_membership_privacy_policy(
    user_id = False, # optional
    user_email = False, # optional
    user_phone = False, # optional
    user_name = False, # optional
    user_mfa = False, # optional
    user_accessed_at = False # optional
)

print(result.model_dump())
```
