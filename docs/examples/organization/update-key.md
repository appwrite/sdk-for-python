```python
from appwrite.client import Client
from appwrite.services.organization import Organization
from appwrite.models import Key
from appwrite.enums import OrganizationKeyScopes

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

organization = Organization(client)

result: Key = organization.update_key(
    key_id = '<KEY_ID>',
    name = '<NAME>',
    scopes = [OrganizationKeyScopes.PROJECTS_READ],
    expire = '2020-10-15T06:38:00.000+00:00' # optional
)

print(result.model_dump())
```
