```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import PlatformWeb
from appwrite.models import PlatformApple
from appwrite.models import PlatformAndroid
from appwrite.models import PlatformWindows
from appwrite.models import PlatformLinux
from typing import Union

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: Union[PlatformWeb, PlatformApple, PlatformAndroid, PlatformWindows, PlatformLinux] = project.get_platform(
    platform_id = '<PLATFORM_ID>'
)

print(result.model_dump())
```
