```python
from appwrite.client import Client
from appwrite.services.apps import Apps
from appwrite.models import AppInstallation

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

apps = Apps(client)

result: AppInstallation = apps.get_installation(
    app_id = '<APP_ID>',
    installation_id = '<INSTALLATION_ID>'
)

print(result.model_dump())
```
