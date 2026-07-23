```python
from appwrite.client import Client
from appwrite.services.apps import Apps

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

apps = Apps(client)

result = apps.delete_key(
    app_id = '<APP_ID>',
    key_id = '<KEY_ID>'
)
```
