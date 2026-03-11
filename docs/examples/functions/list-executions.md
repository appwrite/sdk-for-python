```python
from appwrite.client import Client
from appwrite.services.functions import Functions
from appwrite.models import ExecutionList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

functions = Functions(client)

result: ExecutionList = functions.list_executions(
    function_id = '<FUNCTION_ID>',
    queries = [], # optional
    total = False # optional
)

print(result.model_dump())
```
