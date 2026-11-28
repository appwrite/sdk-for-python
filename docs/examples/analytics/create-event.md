```python
from appwrite.client import Client
from appwrite.services.analytics import Analytics

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

analytics = Analytics(client)

result = analytics.create_event(
    property_id = '<PROPERTY_ID>',
    name = '<NAME>',
    url = 'https://example.com',
    domain = '<DOMAIN>', # optional
    referrer = '<REFERRER>', # optional
    screen_width = None, # optional
    session_hash = '<SESSION_HASH>', # optional
    scroll_depth = 0, # optional
    engagement_time = 0, # optional
    props = [], # optional
    user_id = '<USER_ID>', # optional
    ip = '<IP>', # optional
    user_agent = '<USER_AGENT>', # optional
    interactive = False # optional
)
```
