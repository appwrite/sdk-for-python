```python
from appwrite.client import Client
from appwrite.services.organization import Organization
from appwrite.models import Escalation

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

organization = Organization(client)

result: Escalation = organization.create_escalation(
    escalation_id = '<ESCALATION_ID>',
    name = '<NAME>',
    steps = [
	    {
	        "delay": 0,
	        "roles": [
	            "owner"
	        ]
	    },
	    {
	        "delay": 900,
	        "roles": [
	            "developer"
	        ],
	        "userIds": [
	            "<USER_ID>"
	        ]
	    }
	],
    repeat = 1 # optional
)

print(result.model_dump())
```
