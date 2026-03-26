```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Variable

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: Variable = project.create_variable(
    variable_id = '<VARIABLE_ID>',
    key = '<KEY>',
    value = '<VALUE>',
    secret = False # optional
)

print(result.model_dump())
```
