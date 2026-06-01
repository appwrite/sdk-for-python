```python
from appwrite.client import Client
from appwrite.services.organization import Organization

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

organization = Organization(client)

result = organization.delete_project(
    project_id = '<PROJECT_ID>'
)
```
