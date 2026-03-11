```python
from appwrite.client import Client
from appwrite.services.sites import Sites
from appwrite.models import Variable

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

sites = Sites(client)

result: Variable = sites.get_variable(
    site_id = '<SITE_ID>',
    variable_id = '<VARIABLE_ID>'
)

print(result.model_dump())
```
