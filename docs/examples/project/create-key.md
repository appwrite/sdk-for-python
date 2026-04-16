```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Key
from appwrite.enums import Scopes

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: Key = project.create_key(
    key_id = '<KEY_ID>',
    name = '<NAME>',
    scopes = [Scopes.SESSIONS_WRITE],
    expire = '2020-10-15T06:38:00.000+00:00' # optional
)

print(result.model_dump())
```
