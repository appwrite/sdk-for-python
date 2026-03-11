```python
from appwrite.client import Client
from appwrite.services.tokens import Tokens
from appwrite.models import ResourceToken

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

tokens = Tokens(client)

result: ResourceToken = tokens.get(
    token_id = '<TOKEN_ID>'
)

print(result.model_dump())
```
