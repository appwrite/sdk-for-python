```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Project as ProjectModel
from appwrite.enums import Secure

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: ProjectModel = project.update_smtp(
    host = '', # optional
    port = None, # optional
    username = '<USERNAME>', # optional
    password = '<PASSWORD>', # optional
    sender_email = 'email@example.com', # optional
    sender_name = '<SENDER_NAME>', # optional
    reply_to_email = 'email@example.com', # optional
    reply_to_name = '<REPLY_TO_NAME>', # optional
    secure = Secure.TLS, # optional
    enabled = False # optional
)

print(result.model_dump())
```
