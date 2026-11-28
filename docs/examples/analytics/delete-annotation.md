```python
from appwrite.client import Client
from appwrite.services.analytics import Analytics

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

analytics = Analytics(client)

result = analytics.delete_annotation(
    property_id = '<PROPERTY_ID>',
    annotation_id = '<ANNOTATION_ID>'
)
```
