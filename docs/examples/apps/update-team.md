```python
from appwrite.client import Client
from appwrite.services.apps import Apps
from appwrite.models import App

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

apps = Apps(client)

result: App = apps.update_team(
    app_id = '<APP_ID>',
    team_id = '<TEAM_ID>'
)

print(result.model_dump())
```
