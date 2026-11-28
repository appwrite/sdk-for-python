```python
from appwrite.client import Client
from appwrite.services.analytics import Analytics
from appwrite.models import AnalyticsProperty
from appwrite.enums.analytics_property_type import AnalyticsPropertyType

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

analytics = Analytics(client)

result: AnalyticsProperty = analytics.create_property(
    property_id = '<PROPERTY_ID>',
    name = '<NAME>',
    domain = '<DOMAIN>', # optional
    enabled = False, # optional
    allowed_origins = [], # optional
    identify_users = False, # optional
    type = AnalyticsPropertyType.WEB # optional
)

print(result.model_dump())
```
