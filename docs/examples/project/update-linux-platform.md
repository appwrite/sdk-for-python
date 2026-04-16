```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import PlatformLinux

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: PlatformLinux = project.update_linux_platform(
    platform_id = '<PLATFORM_ID>',
    name = '<NAME>',
    package_name = '<PACKAGE_NAME>'
)

print(result.model_dump())
```
