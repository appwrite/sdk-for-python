```python
from appwrite.client import Client
from appwrite.services.apps import Apps
from appwrite.models import AppSecret

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

apps = Apps(client)

result: AppSecret = apps.get_secret(
    app_id = '<APP_ID>',
    secret_id = '<SECRET_ID>'
)

print(result.model_dump())
```
