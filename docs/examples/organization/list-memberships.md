```python
from appwrite.client import Client
from appwrite.services.organization import Organization
from appwrite.models import MembershipList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

organization = Organization(client)

result: MembershipList = organization.list_memberships(
    queries = [], # optional
    search = '<SEARCH>', # optional
    total = False # optional
)

print(result.model_dump())
```
