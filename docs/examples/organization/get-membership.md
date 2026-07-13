```python
from appwrite.client import Client
from appwrite.services.organization import Organization
from appwrite.models import Membership

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

organization = Organization(client)

result: Membership = organization.get_membership(
    membership_id = '<MEMBERSHIP_ID>'
)

print(result.model_dump())
```
