```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Environment
from appwrite.enums.environment_resource import EnvironmentResource

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: Environment = project.create_environment(
    environment_id = '<ENVIRONMENT_ID>',
    name = '<NAME>',
    resources = [EnvironmentResource.DATABASE, EnvironmentResource.TABLE, EnvironmentResource.COLUMN, EnvironmentResource.INDEX, EnvironmentResource.BUCKET, EnvironmentResource.TEAM, EnvironmentResource.FUNCTION, EnvironmentResource.ENVIRONMENT_VARIABLE] # optional
)

print(result.model_dump())
```
