```python
from appwrite.client import Client
from appwrite.services.organization import Organization
from appwrite.models import Key
from appwrite.enums.project_key_scopes import ProjectKeyScopes

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

organization = Organization(client)

result: Key = organization.update_project_key(
    project_id = '<PROJECT_ID>',
    key_id = '<KEY_ID>',
    name = '<NAME>',
    scopes = [ProjectKeyScopes.USERS_READ],
    expire = '2020-10-15T06:38:00.000+00:00' # optional
)

print(result.model_dump())
```
