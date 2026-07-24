```python
from appwrite.client import Client
from appwrite.services.organization import Organization
from appwrite.models import AppInstallation

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

organization = Organization(client)

result: AppInstallation = organization.create_installation(
    app_id = '<APP_ID>',
    authorization_details = '<AUTHORIZATION_DETAILS>' # optional
)

print(result.model_dump())
```
