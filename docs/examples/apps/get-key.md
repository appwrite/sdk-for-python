```python
from appwrite.client import Client
from appwrite.services.apps import Apps
from appwrite.models import AppKey

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

apps = Apps(client)

result: AppKey = apps.get_key(
    app_id = '<APP_ID>',
    key_id = '<KEY_ID>'
)

print(result.model_dump())
```
