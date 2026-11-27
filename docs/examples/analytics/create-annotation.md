```python
from appwrite.client import Client
from appwrite.services.analytics import Analytics
from appwrite.models import AnalyticsAnnotation

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

analytics = Analytics(client)

result: AnalyticsAnnotation = analytics.create_annotation(
    property_id = '<PROPERTY_ID>',
    annotation_id = '<ANNOTATION_ID>',
    date = '2020-10-15T06:38:00.000+00:00',
    content = '<CONTENT>'
)

print(result.model_dump())
```
