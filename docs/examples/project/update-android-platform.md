```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import PlatformAndroid

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: PlatformAndroid = project.update_android_platform(
    platform_id = '<PLATFORM_ID>',
    name = '<NAME>',
    application_id = '<APPLICATION_ID>'
)

print(result.model_dump())
```
