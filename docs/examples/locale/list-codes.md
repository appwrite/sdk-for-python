```python
from appwrite.client import Client
from appwrite.services.locale import Locale
from appwrite.models import LocaleCodeList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

locale = Locale(client)

result: LocaleCodeList = locale.list_codes()

print(result.model_dump())
```
