```python
from appwrite.client import Client
from appwrite.services.apps import Apps
from appwrite.models import AppInstallationList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

apps = Apps(client)

result: AppInstallationList = apps.list_installations(
    app_id = '<APP_ID>',
    queries = [], # optional
    total = False # optional
)

print(result.model_dump())
```
